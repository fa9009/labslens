
import streamlit as st
from lab_rules import LAB_TESTS, JARGON_DICTIONARY, SAMPLE_PATIENTS, evaluate_marker

st.set_page_config(page_title="LabLens | لاب لينز", page_icon="🔬", layout="wide")

st.title("🔬 LabLens (لاب لينز)")
st.caption("Plain-language blood test & lab terminology translator for patients — educational support, not a medical diagnosis.")
st.markdown("**Created by Farah** — NMKN Academy Hackathon")

st.sidebar.header("Quick Demo & Settings")
st.sidebar.caption("Built by Farah | NMKN Academy Hackathon")
preset_choice = st.sidebar.selectbox("Load Sample Report", list(SAMPLE_PATIENTS.keys()))
show_arabic = st.sidebar.toggle("Show Arabic Explanations (العربية)", value=True)

preset_values = SAMPLE_PATIENTS[preset_choice]

col_input, col_results = st.columns([1, 1.4], gap="large")

user_values = {}

with col_input:
    st.subheader("1. Enter Your Lab Results")
    for test_name, info in LAB_TESTS.items():
        default_val = preset_values[test_name] if preset_values else (info["low"] + info["high"]) / 2
        user_values[test_name] = st.number_input(
            label=f"{test_name} ({info['unit']})",
            min_value=0.0,
            value=float(default_val),
            step=0.1,
            key=f"input_{test_name}"
        )

with col_results:
    st.subheader("2. Plain-Language Translation & Guidance")
    collected_questions = []

    for test_name, val in user_values.items():
        info = LAB_TESTS[test_name]
        result = evaluate_marker(test_name, val)

        with st.container(border=True):
            st.markdown(f"### {result['badge']} {info['full_name']} — **{val} {info['unit']}**")
            if show_arabic:
                st.markdown(f"**{info['ar_name']}**")

            st.markdown(f"**Status:** `{result['status']}`")
            st.caption(f"Typical reference range: {info['low']} – {info['high']} {info['unit']}")

            st.write(f"**What this test is:** {info['what_it_is']}")
            if show_arabic:
                st.write(f"**بالعربي:** {info['ar_what_it_is']}")

            st.write(f"**What your number means:** {result['meaning']}")
            st.write(f"**What should be done:** {result['next_steps']}")
            st.write(f"**When to consult a doctor:** {result['when_doctor']}")

            if result["key"] != "normal":
                collected_questions.extend(info["doctor_questions"])

    st.subheader("3. Questions to Ask Your Doctor")
    if collected_questions:
        for q in dict.fromkeys(collected_questions):
            st.markdown(f"- {q}")
    else:
        st.info("All selected markers are in the normal range. You can still ask your doctor when your next routine checkup should be.")

st.divider()
st.subheader("4. Lab Report Jargon & Terminology Decoder")
selected_term = st.selectbox("Pick a lab term, flag, or note from your report", list(JARGON_DICTIONARY.keys()))
st.success(f"**{selected_term}:** {JARGON_DICTIONARY[selected_term]}")