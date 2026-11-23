import html
import os
import re
import streamlit as st
from lab_rules import JARGON_DICTIONARY, LAB_TESTS, SAMPLE_PATIENTS, evaluate_marker

try:
    from google import genai
    from google.genai import types
except ImportError:
    genai = None
    types = None

CREATOR_NAME = "Farah"
ACTIVE_GEMINI_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
]

HOSPITALS_BY_CITY = {
    "Riyadh": [
        {
            "en_name": "Kingdom Hospital (24h)",
            "ar_name": "مستشفى المملكة (يعمل 24 ساعة)",
            "en_addr": "Al Thoumamah Rd, Ar Rabi, Riyadh",
            "ar_addr": "طريق الثمامة، الربيع، الرياض",
        },
        {
            "en_name": "EMERGENCY - Kingdom Hospital",
            "ar_name": "طوارئ مستشفى المملكة",
            "en_addr": "King Abdulaziz Rd, Ar Rabi, Riyadh",
            "ar_addr": "طريق الملك عبدالعزيز، الربيع، الرياض",
        },
        {
            "en_name": "Dr Sulaiman Alhabib Hospital, Al Sahafah (24h)",
            "ar_name": "مستشفى الدكتور سليمان الحبيب، الصحافة (يعمل 24 ساعة)",
            "en_addr": "Al Yasmeen, Riyadh",
            "ar_addr": "الياسمين، الرياض",
        },
    ],
    "Makkah": [
        {
            "en_name": "Asia Al Aziziyah General Medical Complex (24h)",
            "ar_name": "مجمع شركة آسيا العزيزية الطبي العام (يعمل 24 ساعة)",
            "en_addr": "Al Naseem / Al Aziziyah, Makkah",
            "ar_addr": "النسيم / العزيزية، مكة المكرمة",
        },
        {
            "en_name": "Makkah Medical Center Hospital (24h)",
            "ar_name": "مستشفى مركز مكة الطبي (يعمل 24 ساعة)",
            "en_addr": "Al Madinah Al Munawwarah Rd, Al Taneem, Makkah",
            "ar_addr": "طريق المدينة المنورة، التنعيم، مكة المكرمة",
        },
        {
            "en_name": "Al Baraka Medical Complex (24h)",
            "ar_name": "مجمع البركة الطبي (يعمل 24 ساعة)",
            "en_addr": "Al Mansur, Makkah",
            "ar_addr": "المنصور، مكة المكرمة",
        },
        {
            "en_name": "Al Noor Specialist Hospital (24h)",
            "ar_name": "مستشفى النور التخصصي (يعمل 24 ساعة)",
            "en_addr": "3rd Ring Rd, Al Hijrah, Makkah",
            "ar_addr": "الدائري الثالث، الهجرة، مكة المكرمة",
        },
    ],
    "Jeddah": [
        {
            "en_name": "Andalusia Hospital (24h)",
            "ar_name": "مستشفى أندلسية (يعمل 24 ساعة)",
            "en_addr": "Abdullah Sulaiman St, Al Jamiah, Jeddah",
            "ar_addr": "شارع عبدالله سليمان، الجامعة، جدة",
        },
        {
            "en_name": "International Medical Center (24h)",
            "ar_name": "المركز الطبي الدولي (يعمل 24 ساعة)",
            "en_addr": "Nour Al Huda, Al Ruwais, Jeddah",
            "ar_addr": "نور الهدى، الرويس، جدة",
        },
        {
            "en_name": "Al Zahraa Hospital (24h)",
            "ar_name": "مستشفى الزهراء (يعمل 24 ساعة)",
            "en_addr": "Abdullah Kazim, Al Zahraa, Jeddah",
            "ar_addr": "عبدالله كاظم، الزهراء، جدة",
        },
        {
            "en_name": "Al Salamah Hospital (24h)",
            "ar_name": "مستشفى السلامة (يعمل 24 ساعة)",
            "en_addr": "King Abdulaziz Rd, Al Malek, Jeddah",
            "ar_addr": "طريق الملك عبدالعزيز، الملك، جدة",
        },
    ],
}

st.set_page_config(page_title="LabLens", layout="wide")

lang = st.radio(
    "Language / اللغة",
    options=["en", "ar"],
    format_func=lambda code: "English" if code == "en" else "العربية",
    horizontal=True,
)

is_ar = lang == "ar"
dir_attr = "rtl" if is_ar else "ltr"
align_css = "right" if is_ar else "left"

title_text = (
    f"LabLens — مترجم نتائج التحاليل الطبية (إعداد: {CREATOR_NAME})"
    if is_ar
    else f"LabLens — Lab Result Translator · Built by {CREATOR_NAME}"
)
subtitle_text = (
    "أداة تعليمية لشرح نتائج التحاليل وتوضيح الخطوات التالية ولا تُعد تشخيصاً طبياً."
    if is_ar
    else "Educational lab explainer for understanding results and next steps — not a medical diagnosis."
)

st.title(title_text)
st.caption(subtitle_text)

marker_keys = list(LAB_TESTS.keys())
sample_keys = list(SAMPLE_PATIENTS.keys())

col_controls, col_output = st.columns([1, 1.35], gap="large")

with col_controls:
    st.markdown(
        f"<div dir='{dir_attr}' style='text-align:{align_css};'>",
        unsafe_allow_html=True,
    )
    st.subheader("إدخال البيانات" if is_ar else "1. Select Preset & Value")

    selected_city = st.selectbox(
        "المدينة (للطوارئ وأقرب مستشفى)" if is_ar else "City (for urgent hospital lookup)",
        options=["Riyadh", "Makkah", "Jeddah"],
    )

    preset_label = "حالة تجريبية" if is_ar else "Sample case"
    selected_preset = st.selectbox(preset_label, options=sample_keys)
    preset_values = SAMPLE_PATIENTS[selected_preset]

    marker_label = "التحليل" if is_ar else "Marker"
    selected_marker = st.selectbox(
        marker_label,
        options=marker_keys,
        format_func=lambda k: LAB_TESTS[k]["ar_name"] if is_ar else f"{k} — {LAB_TESTS[k]['full_name']}",
    )

    marker_info = LAB_TESTS[selected_marker]
    default_val = (
        float(preset_values[selected_marker])
        if preset_values is not None and selected_marker in preset_values
        else float(marker_info["high"])
    )

    val_label = f"النتيجة ({marker_info['unit']})" if is_ar else f"Your value ({marker_info['unit']})"
    value = st.number_input(
        val_label,
        value=default_val,
        step=0.1,
        format="%.2f",
        key=f"val_{selected_preset}_{selected_marker}",
    )

    range_text = (
        f"النطاق المرجعي: {marker_info['low']} – {marker_info['high']} {marker_info['unit']} (الحدي حتى {marker_info['borderline_high']})"
        if is_ar
        else f"Reference range: {marker_info['low']} – {marker_info['high']} {marker_info['unit']} (borderline up to {marker_info['borderline_high']})"
    )
    st.caption(range_text)

    st.divider()
    st.subheader("قاموس المصطلحات" if is_ar else "Lab Jargon Decoder")
    jargon_keys = list(JARGON_DICTIONARY.keys())
    picked_jargon = st.selectbox(
        "اختر مصطلحاً" if is_ar else "Choose a term",
        options=jargon_keys,
    )
    jargon_entry = JARGON_DICTIONARY[picked_jargon]
    jargon_desc = jargon_entry["ar"] if is_ar else jargon_entry["en"]
    st.info(f"**{picked_jargon}:** {jargon_desc}")
    st.markdown("</div>", unsafe_allow_html=True)

evaluation = evaluate_marker(selected_marker, float(value), lang=lang)
marker_display_name = marker_info["ar_name"] if is_ar else marker_info["full_name"]
what_it_is_text = marker_info["ar_what_it_is"] if is_ar else marker_info["what_it_is"]

status_colors = {
    "normal": ("#1B7F5A", "#E6F6EE"),
    "low": ("#9A5B00", "#FFF6DC"),
    "borderline": ("#B8470A", "#FFF0E5"),
    "high": ("#B42318", "#FDECEA"),
}
accent_hex, soft_bg = status_colors.get(evaluation["key"], ("#0F766E", "#EEF6F5"))


def format_nearby_hospitals(city: str, current_lang: str) -> str:
    hospitals = HOSPITALS_BY_CITY.get(city, HOSPITALS_BY_CITY["Riyadh"])
    if current_lang == "ar":
        city_ar = {"Riyadh": "الرياض", "Makkah": "مكة المكرمة", "Jeddah": "جدة"}.get(city, city)
        items = "\n".join(f"- **{h['ar_name']}** — {h['ar_addr']}" for h in hospitals)
        return (
            f"**أقرب المستشفيات والطوارئ في {city_ar}:**\n"
            f"{items}\n"
            f"*في الحالات الطارئة الشديدة اتصل فوراً برقم الطوارئ (997 في السعودية).*"
        )
    items = "\n".join(f"- **{h['en_name']}** — {h['en_addr']}" for h in hospitals)
    return (
        f"**Nearby hospitals & emergency care in {city}:**\n"
        f"{items}\n"
        f"*For severe emergencies, call emergency services (997 in Saudi Arabia) immediately.*"
    )


with col_output:
    st.markdown(
        f"""
        <div dir="{dir_attr}" style="text-align:{align_css}; background:{soft_bg}; border:1px solid {accent_hex}33; border-left:6px solid {accent_hex}; border-radius:16px; padding:18px 20px; margin-bottom:14px;">
            <div style="font-size:13px; font-weight:700; color:{accent_hex}; margin-bottom:4px;">
                {evaluation['badge']} {evaluation['status']} · {CREATOR_NAME}
            </div>
            <div style="font-size:28px; font-weight:700; color:#17201C; line-height:1.2;">
                {value:g} <span style="font-size:15px; font-weight:500; color:#4A5651;">{marker_info['unit']}</span>
            </div>
            <div style="font-size:14px; font-weight:600; color:#17201C; margin-top:4px;">
                {marker_display_name}
            </div>
            <p style="margin:8px 0 0; font-size:14px; color:#2C3935;">
                {evaluation['meaning']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div dir='{dir_attr}' style='text-align:{align_css};'>",
        unsafe_allow_html=True,
    )
    st.markdown("**ماذا يعني هذا التحليل؟**" if is_ar else "**What this test measures**")
    st.write(what_it_is_text)

    st.markdown("**الخطوات التالية المقترحة**" if is_ar else "**Suggested next steps**")
    st.write(evaluation["next_steps"])

    st.markdown("**متى تراجع الطبيب؟**" if is_ar else "**When to see a doctor**")
    st.write(evaluation["when_doctor"])

    if evaluation["key"] == "high":
        st.error(format_nearby_hospitals(selected_city, lang))

    st.markdown("**أسئلة يمكنك طرحها على الطبيب**" if is_ar else "**Questions to ask your doctor**")
    for question in evaluation["doctor_questions"]:
        st.markdown(f"- {question}")
    st.markdown("</div>", unsafe_allow_html=True)


def _get_gemini_api_key() -> str | None:
    key = (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or "").strip().strip('"').strip("'")
    if key:
        return key
    try:
        secret_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
        if secret_key:
            return str(secret_key).strip().strip('"').strip("'")
    except Exception:
        pass
    return None


def _detect_reply_language(text: str, fallback_lang: str) -> str:
    if re.search(r"[\u0600-\u06FF]", text):
        return "ar"
    if re.search(r"[A-Za-z]", text):
        return "en"
    return "ar" if fallback_lang == "ar" else "en"


def _simple_md_to_rtl_html(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)
    return escaped.replace("\n", "<br>")


def _render_chat_bubble_content(content: str) -> None:
    if re.search(r"[\u0600-\u06FF]", content) and not re.search(r"[A-Za-z]{4,}", content):
        rtl_html = _simple_md_to_rtl_html(content)
        st.markdown(f"<div dir='rtl' style='text-align:right; line-height:1.7;'>{rtl_html}</div>", unsafe_allow_html=True)
    else:
        st.markdown(content)


def _build_context_bundle(marker_key: str, val: float, eval_data: dict, city: str) -> str:
    markers_summary = []
    for k, info in LAB_TESTS.items():
        markers_summary.append(
            f"- {k} ({info['full_name']} / {info['ar_name']}): unit={info['unit']}, "
            f"low<{info['low']}, normal={info['low']}..{info['high']}, "
            f"borderline={info['high']}..{info['borderline_high']}, high>{info['borderline_high']}."
        )

    jargon_summary = [
        f"- {term}: EN='{d['en']}' | AR='{d['ar']}'"
        for term, d in JARGON_DICTIONARY.items()
    ]

    hospitals = HOSPITALS_BY_CITY.get(city, HOSPITALS_BY_CITY["Riyadh"])
    hosp_summary = [
        f"- {h['en_name']} ({h['ar_name']}) at {h['en_addr']} / {h['ar_addr']}"
        for h in hospitals
    ]

    return (
        f"Active marker: {marker_key} ({LAB_TESTS[marker_key]['full_name']} / {LAB_TESTS[marker_key]['ar_name']})\n"
        f"Active value: {val:g} {LAB_TESTS[marker_key]['unit']}\n"
        f"Current rule evaluation: status={eval_data.get('status')}, key={eval_data.get('key')}, "
        f"meaning={eval_data.get('meaning')}, next_steps={eval_data.get('next_steps')}, "
        f"when_doctor={eval_data.get('when_doctor')}\n"
        f"Selected city: {city}\n"
        f"Available markers:\n" + "\n".join(markers_summary) + "\n"
        f"Jargon terms:\n" + "\n".join(jargon_summary) + "\n"
        f"Nearby hospitals in {city}:\n" + "\n".join(hosp_summary)
    )


def _emergency_local_reply(prompt: str, marker_key: str, val: float, eval_data: dict, reply_lang: str) -> str:
    q_low = prompt.lower()
    info = LAB_TESTS[marker_key]

    if reply_lang == "ar":
        if any(w in q_low for w in ["طبيب", "دكتور", "أسأل", "اسأل"]):
            qs = (eval_data.get("doctor_questions") or [
                "هل تتوافق هذه النتيجة مع أعراضي؟",
                "هل أحتاج إلى إعادة التحليل؟",
            ])[:2]
            return f"**{info['ar_name']}** (`{val:g} {info['unit']}`): " + "، ".join(qs)
        if any(w in q_low for w in ["أفعل", "افعل", "الخطوات", "التالي", "الآن", "الان"]):
            return f"**{info['ar_name']}** (`{val:g} {info['unit']}`): {eval_data.get('next_steps', 'راجع طبيبك لتقييم النتيجة.')}"
        return (
            f"**{info['ar_name']}** (`{val:g} {info['unit']}`, المدى `{info['low']}–{info['high']} {info['unit']}`): "
            f"{info.get('ar_what_it_is', info['full_name'])}"
        )

    if "doctor" in q_low or "ask" in q_low:
        qs = (eval_data.get("doctor_questions") or [
            "Does this fit my symptoms?",
            "Do I need a repeat test?",
        ])[:2]
        return f"**{info['full_name']}** (`{val:g} {info['unit']}`): " + "; ".join(qs)

    if "next" in q_low or "do" in q_low:
        return f"**{info['full_name']}** (`{val:g} {info['unit']}`): {eval_data.get('next_steps', 'Discuss with a clinician.')}"

    return (
        f"**{info['full_name']}** (`{val:g} {info['unit']}`, ref `{info['low']}–{info['high']} {info['unit']}`): "
        f"{info.get('what_it_is', info['full_name'])}"
    )


def build_assistant_reply(
    prompt: str,
    marker_key: str,
    val: float,
    eval_data: dict,
    current_lang: str,
) -> tuple[str, str | None]:
    raw = prompt.strip()
    reply_lang = _detect_reply_language(raw, current_lang)
    api_key = _get_gemini_api_key()

    if genai is None or types is None:
        return (
            _emergency_local_reply(raw, marker_key, val, eval_data, reply_lang),
            "google-genai SDK is not installed in this environment.",
        )

    if not api_key:
        return (
            _emergency_local_reply(raw, marker_key, val, eval_data, reply_lang),
            "GEMINI_API_KEY / GOOGLE_API_KEY is not set.",
        )

    system_instruction = (
        "You are LabLens, a concise bilingual (Arabic and English) health-literacy assistant created by Farah. "
        "Keep answers short and summarized (2–4 short sentences or up to 3 complete bullet points). Never repeat instructions or prompt text. "
        "Never diagnose or prescribe exact drug dosages; encourage consulting a clinician, and mention nearby hospitals or 997 in Saudi Arabia only if urgent/high values or emergencies apply. "
        f"Reply strictly in {'clear, concise Arabic (العربية)' if reply_lang == 'ar' else 'clear, concise English'}.\n\n"
        + _build_context_bundle(marker_key, val, eval_data, selected_city)
    )

    contents = []
    for m in st.session_state.get("chat_messages", [])[-6:]:
        role = "user" if m["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=m["content"])]))
    contents.append(types.Content(role="user", parts=[types.Part.from_text(text=raw)]))

    last_err = "Unknown Gemini error"
    try:
        client = genai.Client(api_key=api_key)
        for model_name in ACTIVE_GEMINI_MODELS:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.4,
                        max_output_tokens=1200,
                    ),
                )
                if response and response.text and response.text.strip():
                    return response.text.strip(), None
                last_err = f"{model_name} returned empty response"
            except Exception as e:
                last_err = f"{model_name}: {type(e).__name__}: {e}"
    except Exception as e:
        last_err = f"{type(e).__name__}: {e}"

    return _emergency_local_reply(raw, marker_key, val, eval_data, reply_lang), last_err


st.divider()
st.subheader("مساعد LabLens الذكي" if is_ar else "LabLens Chat Assistant")
st.caption(
    "اسأل أي سؤال بالعربية أو الإنجليزية حول التحاليل، أو النطاق الطبيعي، أو الخطوات التالية، أو أقرب مستشفى (شرح تعليمي وليس تشخيصاً)."
    if is_ar
    else "Ask any question in English or Arabic about markers, ranges, next steps, or nearby hospitals (educational only, not a diagnosis)."
)

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if st.button("مسح المحادثة" if is_ar else "Clear chat"):
    st.session_state.chat_messages = []
    st.rerun()

quick_prompts = (
    [
        "ما النطاق الطبيعي لهذا التحليل؟",
        "ما الخطوات التالية المقترحة؟",
        "ما الأسئلة التي أسألها للطبيب؟",
        "ما هو Hemolyzed Sample؟",
    ]
    if is_ar
    else [
        "What is the normal range?",
        "What should I do next?",
        "What should I ask my doctor?",
        "What is Hemolyzed Sample?",
    ]
)

q_cols = st.columns(len(quick_prompts))
clicked_quick = None
for idx, qp in enumerate(quick_prompts):
    with q_cols[idx]:
        if st.button(qp, key=f"quick_{lang}_{idx}", use_container_width=True):
            clicked_quick = qp

with st.form(key="chat_form", clear_on_submit=True):
    typed_prompt = st.text_input(
        "اكتب سؤالك هنا..." if is_ar else "Ask a question about your result...",
        placeholder="Type your question and press Send..." if not is_ar else "اكتب سؤالك واضغط إرسال...",
    )
    submitted = st.form_submit_button("إرسال" if is_ar else "Send")

active_prompt = (typed_prompt.strip() if submitted and typed_prompt else None) or clicked_quick

if active_prompt:
    st.session_state.chat_messages.append({"role": "user", "content": active_prompt})
    reply, api_note = build_assistant_reply(active_prompt, selected_marker, float(value), evaluation, lang)
    st.session_state.chat_messages.append({"role": "assistant", "content": reply, "api_note": api_note})

for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        _render_chat_bubble_content(msg["content"])
        if msg.get("api_note"):
            st.caption(f"API status: {msg['api_note']}")

st.divider()
st.caption(f"LabLens · Built by {CREATOR_NAME} · Educational explainer only, not a medical diagnosis.")