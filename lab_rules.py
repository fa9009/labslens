# lab_rules.py
LAB_TESTS = {
    "HbA1c": {
        "full_name": "Glycated Hemoglobin (HbA1c)",
        "ar_name": "السكر التراكمي (HbA1c)",
        "unit": "%",
        "low": 4.0,
        "high": 5.6,
        "borderline_high": 6.4,
        "what_it_is": "Your 3-month average blood sugar level—like a movie of your blood sugar over 90 days rather than a single snapshot.",
        "ar_what_it_is": "متوسط مستوى السكر في دمك خلال آخر 3 أشهر، وليس مجرد قياس لحظي.",
        "normal_msg": "Normal—your 3-month average blood sugar is in the healthy range.",
        "borderline_msg": "Slightly High (Prediabetes range)—blood sugar is a bit above optimal, meaning early prevention can make a big difference.",
        "high_msg": "High—blood sugar has been elevated over recent months and needs medical evaluation.",
        "low_msg": "Low—your average blood sugar is below the typical range.",
        "ar_low_msg": "منخفض — متوسط مستوى السكر في الدم أقل من النطاق المعتاد.",
        "ar_normal_msg": "طبيعي — متوسط السكر التراكمي ضمن النطاق الصحي.",
        "ar_borderline_msg": "مرتفع قليلاً (مرحلة ما قبل السكري) — السكر أعلى بقليل من المعدل المثالي، والوقاية المبكرة تصنع فرقاً واضحاً.",
        "ar_high_msg": "مرتفع — مستوى السكر كان مرتفعاً خلال الأشهر الأخيرة ويحتاج إلى تقييم طبي.",
        "next_steps": {
            "low": "Keep a regular meal schedule with balanced carbs and protein, and note any dizzy or shaky episodes.",
            "normal": "Maintain balanced meals, regular physical activity, and routine wellness checkups.",
            "borderline": "Focus on daily brisk walking, fiber-rich foods, and cutting back on sugary drinks.",
            "high": "Avoid delaying care—start gentle daily movement and balanced meals while scheduling a medical review.",
        },
        "ar_next_steps": {
            "low": "التزم بمواعيد وجبات منتظمة تجمع بين الكربوهيدرات المتوازنة والبروتين، وسجّل أي شعور بالدوخة أو الرجفة.",
            "normal": "حافظ على وجبات متوازنة ونشاط بدني منتظم والفحوصات الدورية.",
            "borderline": "ركّز على المشي السريع يومياً، والأطعمة الغنية بالألياف، وتقليل المشروبات السكرية.",
            "high": "لا تؤجل المراجعة—ابدأ بحركة يومية خفيفة ووجبات متوازنة مع حجز موعد طبي قريب.",
        },
        "when_doctor": {
            "low": "Consult your doctor soon—and seek prompt care if you feel dizzy, faint, shaky, or confused.",
            "normal": "Routine follow-up at your next checkup (or earlier if you have symptoms like unusual thirst or fatigue).",
            "borderline": "Book a routine appointment with your doctor to discuss lifestyle targets and whether to recheck in 3–6 months.",
            "high": "Consult a doctor promptly to confirm a diagnosis, set your personal target, and plan safe next steps.",
        },
        "ar_when_doctor": {
            "low": "راجع طبيبك قريباً—واطلب رعاية عاجلة إذا شعرت بدوخة أو إغماء أو رجفة أو تشوش.",
            "normal": "متابعة روتينية في فحصك القادم (أو أبكر إذا ظهرت أعراض مثل العطش غير المعتاد أو الإرهاق).",
            "borderline": "احجز موعداً روتينياً مع طبيبك لمناقشة الأهداف الغذائية والحركية وهل يلزم إعادة الفحص خلال 3–6 أشهر.",
            "high": "راجع الطبيب قريباً لتأكيد التقييم وتحديد الهدف المناسب لك ووضع خطة متابعة آمنة.",
        },
        "doctor_questions": [
            "What is my personal target HbA1c number?",
            "Which small food or activity changes would help my numbers most?",
        ],
        "ar_doctor_questions": [
            "ما الرقم المستهدف المناسب لحالتي في تحليل السكر التراكمي؟",
            "ما التعديلات الغذائية أو الحركية البسيطة التي ستفيد قراءاتي أكثر؟",
        ],
    },
    "Ferritin": {
        "full_name": "Serum Ferritin (Iron Stores)",
        "ar_name": "مخزون الحديد (Ferritin)",
        "unit": "ng/mL",
        "low": 30.0,
        "high": 300.0,
        "borderline_high": 400.0,
        "what_it_is": "Your body's iron savings account. Even if daily blood iron looks okay, low ferritin means your reserves are running empty.",
        "ar_what_it_is": "مخزون الحديد الاحتياطي في جسمك؛ انخفاضه يسبب التعب وتساقط الشعر حتى قبل ظهور فقر الدم.",
        "normal_msg": "Normal—your stored iron reserves are healthy.",
        "borderline_msg": "Slightly High—can sometimes be mildly elevated temporarily after inflammation or infection.",
        "high_msg": "High—iron stores or inflammatory markers are above the usual range.",
        "low_msg": "Low—your stored iron reserves are running low, which commonly causes fatigue, weakness, or hair shedding.",
        "ar_low_msg": "منخفض — مخزون الحديد في جسمك منخفض، وهذا يرتبط غالباً بالإرهاق أو الضعف أو تساقط الشعر.",
        "ar_normal_msg": "طبيعي — مخزون الحديد في جسمك ضمن المعدل الصحي.",
        "ar_borderline_msg": "مرتفع قليلاً — قد يرتفع ارتفاعاً طفيفاً ومؤقتاً بعد التهاب أو عدوى بسيطة.",
        "ar_high_msg": "مرتفع — مخزون الحديد أو مؤشرات الالتهاب أعلى من النطاق المعتاد.",
        "next_steps": {
            "low": "Include iron-rich foods (lentils, lean meat, spinach) paired with Vitamin C, and avoid taking tea/coffee right with meals.",
            "normal": "Keep up a varied diet with iron and Vitamin C sources.",
            "borderline": "Avoid starting extra iron supplements on your own until a doctor reviews your full iron panel.",
            "high": "Do not take iron supplements unless a doctor specifically instructs you to.",
        },
        "ar_next_steps": {
            "low": "أضف أطعمة غنية بالحديد (كالعدس واللحوم الخفيفة والسبانخ) مع مصدر لفيتامين ج، وتجنب الشاي أو القهوة مباشرة مع الوجبات.",
            "normal": "استمر على نظام غذائي متنوع يحتوي على مصادر الحديد وفيتامين ج.",
            "borderline": "تجنب تناول مكملات الحديد من تلقاء نفسك حتى يراجع الطبيب تحاليل الحديد الكاملة.",
            "high": "لا تتناول مكملات الحديد إلا إذا أوصى الطبيب بذلك صراحةً.",
        },
        "when_doctor": {
            "low": "Consult your doctor to ask about safe iron supplementation, dosage, and when to recheck levels.",
            "normal": "No urgent visit needed unless you feel unusually tired, pale, or short of breath.",
            "borderline": "Schedule a routine doctor visit to check if mild inflammation or another factor explains the slight rise.",
            "high": "Consult a doctor to evaluate why ferritin is elevated—seek prompt care if you have chest or abdominal pain.",
        },
        "ar_when_doctor": {
            "low": "راجع طبيبك للاستفسار عن المكمل الآمن والجرعة المناسبة وموعد إعادة التحليل.",
            "normal": "لا حاجة لزيارة عاجلة إلا إذا شعرت بتعب غير معتاد أو شحوب أو ضيق في التنفس.",
            "borderline": "حدد موعداً روتينياً مع الطبيب لمعرفة إن كان التهاب خفيف أو سبب آخر يفسر هذا الارتفاع البسيط.",
            "high": "راجع الطبيب لتقييم سبب ارتفاع الفيريتين—واطلب رعاية عاجلة عند وجود ألم في الصدر أو البطن.",
        },
        "doctor_questions": [
            "Do I need an iron supplement, and what dose is safe for me?",
            "Should we recheck my ferritin in 8 to 12 weeks?",
        ],
        "ar_doctor_questions": [
            "هل أحتاج إلى مكمل حديد، وما الجرعة الآمنة لي؟",
            "هل يُنصح بإعادة تحليل الفيريتين بعد 8 إلى 12 أسبوعاً؟",
        ],
    },
    "Vitamin D": {
        "full_name": "25-Hydroxy Vitamin D",
        "ar_name": "فيتامين د (Vitamin D)",
        "unit": "ng/mL",
        "low": 30.0,
        "high": 100.0,
        "borderline_high": 120.0,
        "what_it_is": "The 'sunshine vitamin' that keeps bones strong, supports immunity, and helps maintain steady energy and mood.",
        "ar_what_it_is": "فيتامين أساسي لصحة العظام والمناعة ومستوى النشاط اليومي.",
        "normal_msg": "Normal—your Vitamin D level is in the healthy range.",
        "borderline_msg": "Slightly High—often linked to taking high-dose Vitamin D supplements.",
        "high_msg": "High—above the usual range, most commonly from excessive supplementation.",
        "low_msg": "Low—below optimal levels, which can contribute to bone aches, muscle fatigue, or low energy.",
        "ar_low_msg": "منخفض — أقل من المستوى المثالي، وقد يرتبط بآلام العظام أو إرهاق العضلات أو انخفاض النشاط.",
        "ar_normal_msg": "طبيعي — مستوى فيتامين د ضمن النطاق الصحي.",
        "ar_borderline_msg": "مرتفع قليلاً — يرتبط غالباً بتناول مكملات فيتامين د بجرعات مرتفعة.",
        "ar_high_msg": "مرتفع — أعلى من النطاق المعتاد، وغالباً ما يكون بسبب زيادة جرعات المكملات.",
        "next_steps": {
            "low": "Get safe sun exposure and discuss an appropriate supplement regimen with your doctor or pharmacist.",
            "normal": "Maintain healthy habits and stay consistent with any maintenance dose your doctor recommends.",
            "borderline": "Pause high-dose Vitamin D supplements and check your current dose before taking more.",
            "high": "Stop extra Vitamin D supplements right away and check your supplement labels.",
        },
        "ar_next_steps": {
            "low": "احرص على تعرّض آمن للشمس وناقش الجرعة المناسبة مع الطبيب أو الصيدلي.",
            "normal": "حافظ على العادات الصحية واستمر على الجرعة الوقائية إذا أوصى بها الطبيب.",
            "borderline": "أوقف جرعات فيتامين د المرتفعة مؤقتاً وتحقق من جرعتك الحالية قبل أخذ المزيد.",
            "high": "توقف فوراً عن مكملات فيتامين د الإضافية وراجع ملصقات المكملات التي تستخدمها.",
        },
        "when_doctor": {
            "low": "Consult a doctor or pharmacist for the right dose (weekly or daily) rather than guessing high doses.",
            "normal": "Routine follow-up at your regular checkup.",
            "borderline": "Mention your supplement use to your doctor at your next visit so they can advise on maintenance.",
            "high": "Consult a doctor promptly—especially if you have nausea, excessive thirst, frequent urination, or weakness.",
        },
        "ar_when_doctor": {
            "low": "استشر الطبيب أو الصيدلي لتحديد الجرعة المناسبة (أسبوعية أو يومية) بدلاً من اجتهاد الجرعات العالية.",
            "normal": "متابعة روتينية في موعد فحصك المعتاد.",
            "borderline": "أخبر طبيبك بالمكملات التي تتناولها في زيارتك القادمة ليحدد لك الجرعة المناسبة.",
            "high": "راجع الطبيب قريباً—خاصة إذا شعرت بغثيان أو عطش شديد أو كثرة التبول أو ضعف عام.",
        },
        "doctor_questions": [
            "Do I need a weekly loading dose or a daily maintenance dose of Vitamin D?",
            "Should I take it with a meal containing healthy fats for better absorption?",
        ],
        "ar_doctor_questions": [
            "هل أحتاج إلى جرعة أسبوعية تعويضية أم جرعة يومية وقائية من فيتامين د؟",
            "هل يُفضل تناوله مع وجبة تحتوي على دهون صحية لتحسين الامتصاص؟",
        ],
    },
    "TSH": {
        "full_name": "Thyroid-Stimulating Hormone (TSH)",
        "ar_name": "هرمون الغدة الدرقية (TSH)",
        "unit": "mIU/L",
        "low": 0.4,
        "high": 4.2,
        "borderline_high": 5.5,
        "what_it_is": "The signal your brain sends to your thyroid gland (the body's energy thermostat). Counterintuitively, a HIGH TSH means a SLOWER thyroid.",
        "ar_what_it_is": "الهرمون المنظم لعمل الغدة الدرقية المسؤولة عن حرق الطاقة ونشاط الجسم.",
        "normal_msg": "Normal—your thyroid signal is balanced.",
        "borderline_msg": "Slightly High—your thyroid may be working a bit harder than usual (mild/subclinical slowing).",
        "high_msg": "High—suggests an underactive thyroid (hypothyroidism), which can slow energy and metabolism.",
        "low_msg": "Low—suggests an overactive thyroid (hyperthyroidism), which can speed up body processes.",
        "ar_low_msg": "منخفض — قد يشير إلى فرط نشاط الغدة الدرقية مما قد يسرّع بعض وظائف الجسم.",
        "ar_normal_msg": "طبيعي — إشارة الغدة الدرقية متوازنة.",
        "ar_borderline_msg": "مرتفع قليلاً — قد تبذل الغدة الدرقية جهداً أكبر من المعتاد (قصور طفيف أو تحت السريري).",
        "ar_high_msg": "مرتفع — قد يشير إلى كسل أو خمول الغدة الدرقية مما قد يبطئ النشاط والتمثيل الغذائي.",
        "next_steps": {
            "low": "Note any racing heart, anxiety, heat intolerance, or weight changes to share with your doctor.",
            "normal": "Keep up routine health monitoring.",
            "borderline": "Track symptoms like fatigue, feeling cold, or dry skin; doctors often recheck TSH before starting treatment.",
            "high": "Take any prescribed thyroid medication consistently on an empty stomach with water if advised by your doctor.",
        },
        "ar_next_steps": {
            "low": "لاحظ أي تسارع في نبض القلب أو توتر أو عدم تحمّل للحرارة أو تغير في الوزن لمشاركته مع طبيبك.",
            "normal": "استمر في المتابعة الصحية الدورية.",
            "borderline": "راقب أعراضاً مثل الإرهاق أو الإحساس بالبرد أو جفاف الجلد؛ وغالباً ما يعيد الأطباء الفحص قبل بدء العلاج.",
            "high": "التزم بأي دواء موصوف للغدة الدرقية على معدة فارغة مع الماء إذا أوصى الطبيب بذلك.",
        },
        "when_doctor": {
            "low": "Consult a doctor soon—seek urgent care if you have chest pain, severe shortness of breath, or a very fast/irregular heartbeat.",
            "normal": "Routine checkup unless new thyroid-related symptoms appear.",
            "borderline": "Schedule a doctor visit to see if a repeat test or Free T3/Free T4 check is recommended.",
            "high": "Consult a doctor to check Free T4/T3 and decide whether treatment or a repeat test is needed.",
        },
        "ar_when_doctor": {
            "low": "راجع الطبيب قريباً—واطلب رعاية عاجلة عند وجود ألم في الصدر أو ضيق شديد في التنفس أو تسارع/عدم انتظام واضح في النبض.",
            "normal": "متابعة روتينية ما لم تظهر أعراض جديدة مرتبطة بالغدة الدرقية.",
            "borderline": "احجز موعداً مع الطبيب لمعرفة هل يُنصح بإعادة التحليل أو فحص هرموني T4 وT3 الحر.",
            "high": "راجع الطبيب لفحص T4 وT3 الحر وتحديد ما إذا كان يلزم علاج أو إعادة فحص.",
        },
        "doctor_questions": [
            "Should we also check Free T3 and Free T4 to get the full thyroid picture?",
            "Does this level need treatment now or just a repeat test in 6 weeks?",
        ],
        "ar_doctor_questions": [
            "هل يجب أيضاً فحص T3 الحر وT4 الحر للحصول على صورة كاملة للغدة الدرقية؟",
            "هل يحتاج هذا المستوى إلى علاج الآن أم إلى إعادة فحص بعد 6 أسابيع؟",
        ],
    },
    "LDL": {
        "full_name": "LDL Cholesterol ('Lousy' Cholesterol)",
        "ar_name": "الكوليسترول الضار (LDL)",
        "unit": "mg/dL",
        "low": 0.0,
        "high": 100.0,
        "borderline_high": 129.0,
        "what_it_is": "The type of cholesterol that can slowly build up inside blood vessel walls if it stays high for years.",
        "ar_what_it_is": "نوع الكوليسترول الذي قد يترسب في جدران الأوعية الدموية إذا ارتفع لفترات طويلة.",
        "normal_msg": "Normal / Optimal—within the target range for long-term heart health.",
        "borderline_msg": "Slightly High (Near-optimal to borderline)—above 100 mg/dL, where heart-healthy habits help.",
        "high_msg": "High—above the optimal range, increasing long-term cardiovascular risk if left unaddressed.",
        "low_msg": "Low—generally protective for blood vessels.",
        "ar_low_msg": "منخفض — غالباً ما يكون داعماً لصحة الأوعية الدموية.",
        "ar_normal_msg": "طبيعي / مثالي — ضمن النطاق المستهدف لصحة القلب على المدى الطويل.",
        "ar_borderline_msg": "مرتفع قليلاً (قريب من المثالي إلى حدي) — أعلى من 100 mg/dL، وتساعد العادات الصحية للقلب على تحسينه.",
        "ar_high_msg": "مرتفع — أعلى من النطاق المثالي، وقد يزيد من عوامل الخطر القلبية الوعائية إذا لم يُتابع.",
        "next_steps": {
            "low": "Continue heart-healthy nutrition and regular physical activity.",
            "normal": "Keep up balanced meals, regular exercise, and routine lipid checks.",
            "borderline": "Increase soluble fiber (oats, beans, apples) and swap saturated fats for olive oil, nuts, and fish.",
            "high": "Prioritize soluble fiber, regular aerobic exercise, and avoiding smoking while reviewing your overall heart risk.",
        },
        "ar_next_steps": {
            "low": "استمر على التغذية الداعمة لصحة القلب والنشاط البدني المنتظم.",
            "normal": "حافظ على الوجبات المتوازنة والرياضة المنتظمة وفحوصات الدهون الدورية.",
            "borderline": "زد من الألياف القابلة للذوبان (كالشوفان والبقوليات والتفاح) واستبدل الدهون المشبعة بزيت الزيتون والمكسرات والسمك.",
            "high": "ركّز على الألياف القابلة للذوبان والتمارين الهوائية المنتظمة وتجنب التدخين مع مراجعة عوامل الخطر العامة للقلب.",
        },
        "when_doctor": {
            "low": "No urgent action needed unless your doctor notes another health condition.",
            "normal": "Routine screening every few years or as advised for your age and risk factors.",
            "borderline": "Bring this result to your next doctor visit to review your overall heart health and lifestyle plan.",
            "high": "Consult a doctor to review your personal LDL target based on age, blood pressure, blood sugar, and family history.",
        },
        "ar_when_doctor": {
            "low": "لا يتطلب إجراءً عاجلاً ما لم يذكر طبيبك حالة صحية أخرى.",
            "normal": "فحص دوري كل عدة سنوات أو حسب ما يوصي به الطبيب لعمرك وعوامل الخطر لديك.",
            "borderline": "اصطحب هذه النتيجة في زيارتك القادمة للطبيب لمراجعة صحة القلب وخطة نمط الحياة.",
            "high": "راجع الطبيب لتحديد الرقم المستهدف المناسب لك بناءً على العمر وضغط الدم والسكر والتاريخ العائلي.",
        },
        "doctor_questions": [
            "Based on my age and overall health, what is my ideal LDL target?",
            "How much can diet and exercise lower this before considering medication?",
        ],
        "ar_doctor_questions": [
            "بناءً على عمري وصحتي العامة، ما المستوى المثالي للكوليسترول الضار (LDL) بالنسبة لي؟",
            "إلى أي مدى يمكن أن يخفضه الغذاء والرياضة قبل التفكير في العلاج الدوائي؟",
        ],
    },
    "Hemoglobin": {
        "full_name": "Hemoglobin (Hgb)",
        "ar_name": "الهيموغلوبين / قوة الدم (Hemoglobin)",
        "unit": "g/dL",
        "low": 12.0,
        "high": 17.5,
        "borderline_high": 18.5,
        "what_it_is": "The oxygen-carrying protein inside your red blood cells—literally your blood's oxygen delivery trucks.",
        "ar_what_it_is": "البروتين المسؤول عن نقل الأكسجين من الرئتين إلى جميع أعضاء الجسم.",
        "normal_msg": "Normal—healthy oxygen-carrying capacity in your blood.",
        "borderline_msg": "Slightly High—can sometimes appear higher after mild dehydration or recent high-altitude/smoking factors.",
        "high_msg": "High—above the standard range and worth checking with your doctor.",
        "low_msg": "Low—below the standard range (anemia), meaning less oxygen is carried to tissues.",
        "ar_low_msg": "منخفض — أقل من النطاق المعتاد (فقر الدم)، مما يعني وصول كمية أقل من الأكسجين إلى الأنسجة.",
        "ar_normal_msg": "طبيعي — قدرة الدم على نقل الأكسجين ضمن المعدل الصحي.",
        "ar_borderline_msg": "مرتفع قليلاً — قد يظهر أعلى أحياناً بعد جفاف خفيف أو بسبب الارتفاعات أو التدخين.",
        "ar_high_msg": "مرتفع — أعلى من النطاق المعتاد ويستحق المراجعة مع الطبيب.",
        "next_steps": {
            "low": "Avoid heavy physical strain if you feel dizzy or winded, and pair iron/B12/folate-rich foods with a medical check.",
            "normal": "Stay hydrated and keep a balanced, nutrient-rich diet.",
            "borderline": "Stay well-hydrated with water and note if you were dehydrated before the blood draw.",
            "high": "Stay hydrated and avoid unprescribed supplements or smoking while awaiting medical review.",
        },
        "ar_next_steps": {
            "low": "تجنب المجهود البدني الشاق إذا شعرت بدوخة أو نهجان، واجمع بين الأطعمة الغنية بالحديد أو فيتامين B12 أو الفولات مع مراجعة طبية.",
            "normal": "حافظ على شرب الماء بانتظام واتبع نظاماً غذائياً متوازناً غنياً بالعناصر الغذائية.",
            "borderline": "احرص على ترطيب الجسم بالماء ولاحظ إن كنت تعاني من جفاف قبل سحب العينة.",
            "high": "حافظ على شرب الماء وتجنب المكملات غير الموصوفة أو التدخين لحين مراجعة الطبيب.",
        },
        "when_doctor": {
            "low": "Consult a doctor promptly—seek urgent care if you have chest pain, fainting, or shortness of breath at rest.",
            "normal": "Routine follow-up at your next checkup.",
            "borderline": "Schedule a doctor visit to review your full CBC and hydration status.",
            "high": "Consult a doctor to evaluate why hemoglobin is elevated—seek prompt care for severe headaches, vision changes, or chest symptoms.",
        },
        "ar_when_doctor": {
            "low": "راجع الطبيب قريباً—واطلب رعاية عاجلة عند وجود ألم في الصدر أو إغماء أو ضيق في التنفس أثناء الراحة.",
            "normal": "متابعة روتينية في فحصك القادم.",
            "borderline": "احجز موعداً مع الطبيب لمراجعة صورة الدم الكاملة (CBC) وحالة الترطيب.",
            "high": "راجع الطبيب لتقييم سبب ارتفاع الهيموغلوبين—واطلب رعاية عاجلة عند وجود صداع شديد أو تغير في الرؤية أو أعراض في الصدر.",
        },
        "doctor_questions": [
            "Is my low hemoglobin linked to iron, Vitamin B12, or something else?",
            "Are there any dietary changes I should start this week?",
        ],
        "ar_doctor_questions": [
            "هل انخفاض الهيموغلوبين مرتبط بالحديد أو فيتامين B12 أم بسبب آخر؟",
            "ما التعديلات الغذائية التي يُنصح أن أبدأ بها هذا الأسبوع؟",
        ],
    },
}

SAMPLE_PATIENTS = {
    "Custom Entry": None,
    "Case 1: Tired Student (Low Iron & Vit D)": {
        "HbA1c": 4.9,
        "Ferritin": 14.0,
        "Vitamin D": 16.0,
        "TSH": 2.1,
        "LDL": 88.0,
        "Hemoglobin": 11.2,
    },
    "Case 2: Routine Checkup (Borderline Sugar & LDL)": {
        "HbA1c": 5.9,
        "Ferritin": 85.0,
        "Vitamin D": 38.0,
        "TSH": 1.8,
        "LDL": 118.0,
        "Hemoglobin": 13.8,
    },
    "Case 3: High Markers Check": {
        "HbA1c": 6.8,
        "Ferritin": 140.0,
        "Vitamin D": 45.0,
        "TSH": 5.2,
        "LDL": 145.0,
        "Hemoglobin": 14.5,
    },
}

JARGON_DICTIONARY = {
    "Hemolyzed Sample": {
        "en": "Red blood cells broke open slightly before or during lab processing, which can falsely raise certain values like potassium or alter readings.",
        "ar": "تكسر طفيف في خلايا الدم الحمراء قبل أو أثناء معالجة العينة في المختبر، وقد يرفع بعض القيم كالبوتاسيوم بشكل غير حقيقي أو يؤثر على القراءة.",
    },
    "MCV (Mean Corpuscular Volume)": {
        "en": "The average size of your red blood cells—helps doctors see if low blood count leans toward iron deficiency (small cells) or B12/folate issues (larger cells).",
        "ar": "متوسط حجم خلايا الدم الحمراء؛ يساعد الطبيب على معرفة هل انخفاض الهيموغلوبين يميل لنقص الحديد (خلايا أصغر) أم لنقص B12 أو الفولات (خلايا أكبر).",
    },
    "Reference Range / Interval": {
        "en": "The typical range seen in most healthy people—being slightly outside it doesn't automatically mean an emergency, which is why context and symptoms matter.",
        "ar": "النطاق المعتاد لدى أغلب الأصحاء؛ والخروج البسيط عنه لا يعني بالضرورة حالة طارئة، ولهذا تُقرأ النتيجة مع الأعراض والسياق الطبي.",
    },
    "Fasting vs. Non-Fasting": {
        "en": "Whether you went without food/caloric drinks for 8–12 hours beforehand; water is usually fine unless your lab sheet says otherwise.",
        "ar": "هل امتنعت عن الطعام أو المشروبات المحتوية على سعرات لمدة 8–12 ساعة قبل التحليل؛ ويُسمح بالماء غالباً ما لم يُذكر غير ذلك في ورقة المختبر.",
    },
    "Prediabetes Range": {
        "en": "Blood sugar levels higher than normal but not yet in the diabetes range—an early window where lifestyle habits have a strong impact.",
        "ar": "مستوى سكر أعلى من الطبيعي ولكنه لم يصل إلى نطاق السكري؛ وهي مرحلة مبكرة يكون فيها لتعديل نمط الحياة أثر قوي.",
    },
}

STATUS_LABELS = {
    "en": {
        "low": ("LOW (Below Normal)", "🟡"),
        "normal": ("NORMAL", "🟢"),
        "borderline": ("BORDERLINE HIGH", "🟠"),
        "high": ("HIGH (Needs Doctor Review)", "🔴"),
    },
    "ar": {
        "low": ("منخفض (أقل من الطبيعي)", "🟡"),
        "normal": ("طبيعي", "🟢"),
        "borderline": ("مرتفع قليلاً (حدي)", "🟠"),
        "high": ("مرتفع (يحتاج مراجعة الطبيب)", "🔴"),
    },
}


def evaluate_marker(marker_name: str, value: float, lang: str = "en"):
    lang = "ar" if lang == "ar" else "en"
    info = LAB_TESTS[marker_name]

    if value < info["low"]:
        key = "low"
    elif value <= info["high"]:
        key = "normal"
    elif value <= info["borderline_high"]:
        key = "borderline"
    else:
        key = "high"

    status, badge = STATUS_LABELS[lang][key]

    if lang == "ar":
        meaning = info[f"ar_{key}_msg"]
        next_steps = info["ar_next_steps"][key]
        when_doctor = info["ar_when_doctor"][key]
        questions = info["ar_doctor_questions"]
    else:
        meaning = info[f"{key}_msg"]
        next_steps = info["next_steps"][key]
        when_doctor = info["when_doctor"][key]
        questions = info["doctor_questions"]

    return {
        "key": key,
        "status": status,
        "badge": badge,
        "meaning": meaning,
        "next_steps": next_steps,
        "when_doctor": when_doctor,
        "doctor_questions": questions,
    }