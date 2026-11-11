import math
import pickle
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="MediScope | Multiple Disease Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Visual system: calm teal, deep navy, soft neutral canvas.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
    :root{--ink:#172f3d;--muted:#758894;--teal:#087f8c;--line:#e2ebef;--canvas:#f4f8fa}
    html,body,[class*="css"]{font-family:'DM Sans',sans-serif;color:var(--ink)}
    .stApp{background:var(--canvas)} .block-container{max-width:1440px;padding-top:1.8rem;padding-bottom:3rem}
    h1,h2,h3,h4{font-family:'Manrope',sans-serif!important;color:var(--ink)}
    [data-testid="stSidebar"]{background:#102c3b;border-right:1px solid rgba(255,255,255,.06)}
    [data-testid="stSidebar"]>div:first-child{padding-top:1.4rem}
    [data-testid="stSidebar"] *{color:#eaf3f5}
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p{color:#a9c1c9}
    [data-testid="stSidebar"] .stRadio>label{display:none}
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"]{gap:.4rem}
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{border:1px solid transparent;border-radius:12px;padding:.65rem .8rem}
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{background:rgba(255,255,255,.07)}
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){background:rgba(31,177,181,.16);border-color:rgba(93,218,213,.26)}
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p{color:#eaf3f5;font-weight:600}
    .brand{display:flex;align-items:center;gap:.7rem;margin:.1rem 0 2rem}
    .brand-mark{width:42px;height:42px;border-radius:14px;background:linear-gradient(145deg,#18b6b2,#087c8c);display:grid;place-items:center;color:white;font-size:1.3rem}
    .brand-name{font:800 1.1rem Manrope,sans-serif;color:#f5fbfc}.brand-sub{font-size:.7rem;color:#91adb7}
    .side-label{font-size:.65rem;text-transform:uppercase;letter-spacing:.14em;font-weight:700;color:#7f9da8;margin:0 0 .65rem .3rem}
    .side-foot{border-top:1px solid rgba(255,255,255,.1);margin-top:2rem;padding-top:1rem;color:#8ca8b2;font-size:.72rem;line-height:1.6}
    .eyebrow{color:var(--teal);font-size:.68rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
    .hero-title{font:800 clamp(2rem,3vw,2.8rem)/1.12 Manrope,sans-serif;letter-spacing:-.055em;margin:.45rem 0 .6rem;color:var(--ink)}
    .hero-copy{max-width:720px;color:#758894;font-size:.98rem;line-height:1.7}
    .status{display:inline-flex;align-items:center;gap:.45rem;background:#e6f5f3;color:#08737a;border:1px solid #cce9e5;border-radius:99px;padding:.48rem .8rem;font-size:.72rem;font-weight:700}
    .dot{width:7px;height:7px;border-radius:50%;background:#17a79b}
    .banner{background:#eef8f8;border:1px solid #d5e9eb;border-left:4px solid #0a9297;border-radius:12px;padding:.9rem 1rem;color:#486a72;font-size:.82rem;line-height:1.6;margin:1.2rem 0}
    .section-title{font:700 1.08rem Manrope,sans-serif;color:var(--ink);margin:1.35rem 0 .3rem}
    .section-copy{font-size:.84rem;color:#7c8d98;margin-bottom:.95rem}
    .card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:1.2rem;min-height:216px;box-shadow:0 8px 25px rgba(23,54,71,.035)}
    .card-icon{width:46px;height:46px;border-radius:14px;background:#e8f6f5;display:grid;place-items:center;font-size:1.25rem;margin-bottom:.9rem}
    .card-title{font:700 1rem Manrope,sans-serif;color:var(--ink);margin-bottom:.35rem}
    .card-copy{font-size:.81rem;line-height:1.6;color:#7a8b96;min-height:53px}
    .tag{display:inline-block;margin-top:.7rem;background:#f0f5f7;color:#58717e;border-radius:99px;padding:.28rem .6rem;font-size:.68rem;font-weight:700}
    .intro{background:linear-gradient(110deg,#103446,#0b6973);color:#fff;border-radius:18px;padding:1.3rem 1.5rem;margin:.35rem 0 1.15rem;box-shadow:0 12px 28px rgba(10,75,88,.12)}
    .intro-kicker{color:#a4e3df;font-size:.67rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
    .intro-title{font:750 1.35rem Manrope,sans-serif;color:white;margin:.35rem 0 .25rem}
    .intro-copy{color:#c3d9de;font-size:.82rem;margin:0}
    [data-testid="stForm"]{background:#fff;border:1px solid var(--line);border-radius:18px;padding:1.2rem 1.3rem 1.1rem;box-shadow:0 8px 25px rgba(23,54,71,.035)}
    [data-testid="stForm"] label p{color:#425966;font-weight:600;font-size:.8rem}
    [data-testid="stTextInput"] input,[data-testid="stSelectbox"] div[data-baseweb="select"]>div{border-radius:10px!important;border-color:#dce6ea!important;background:#fbfdfe!important}
    .stButton>button,[data-testid="stFormSubmitButton"]>button{border:0;border-radius:11px;padding:.68rem 1rem;color:white;font-weight:700;background:linear-gradient(100deg,#087f8c,#0b9c9b);box-shadow:0 7px 16px rgba(8,127,140,.16)}
    .stButton>button:hover,[data-testid="stFormSubmitButton"]>button:hover{color:white;filter:brightness(1.05);transform:translateY(-1px)}
    .result{border:1px solid #cce9e5;border-radius:16px;padding:1.1rem 1.25rem;background:linear-gradient(110deg,#f0fbf8,#fff);margin-top:1.1rem}
    .result.flagged{border-color:#f1d6b6;background:linear-gradient(110deg,#fff7ed,#fff)}
    .result-kicker{color:#718891;font-size:.66rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
    .result-title{color:#116c66;font:750 1.15rem Manrope,sans-serif;margin:.28rem 0 .35rem}
    .result.flagged .result-title{color:#a45b21}
    .result-copy{color:#647984;font-size:.82rem;line-height:1.65;margin:0}
    .footnote{color:#95a4ac;font-size:.72rem;text-align:center;margin-top:2.3rem}
    @media(max-width:768px){.block-container{padding-top:1rem}.hero-title{font-size:2rem}[data-testid="stForm"]{padding:1rem}}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_models():
    model_dir = Path(__file__).resolve().parent / "saved_models"
    files = {
        "diabetes": "diabetes_model.sav",
        "heart": "heart_disease_model.sav",
        "parkinsons": "parkinsons_model.sav",
    }
    models = {}
    for key, filename in files.items():
        path = model_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Missing model file: {path}")
        with path.open("rb") as model_file:
            models[key] = pickle.load(model_file)
    return models


try:
    MODELS = load_models()
except Exception as exc:
    st.error(f"Could not load the prediction models: {exc}")
    st.info("Confirm that all three .sav files are inside the saved_models folder.")
    st.stop()


def numeric_fields(specs, columns=4):
    """Render required blank numeric text fields in a responsive column grid."""
    values = {}
    cols = st.columns(columns)
    for index, (key, label) in enumerate(specs):
        with cols[index % columns]:
            values[key] = st.text_input(label, key=f"input_{key}", placeholder="Enter numeric value")
    return values


def category_field(label, options, descriptions, key):
    return st.selectbox(
        label,
        options=[None] + options,
        format_func=lambda value: "Select a value" if value is None else f"{value} · {descriptions[value]}",
        key=f"select_{key}",
    )


def parse_features(fields):
    """Validate required fields and return model-ready values in supplied order."""
    output, missing, invalid = [], [], []
    for label, raw_value, field_type in fields:
        if field_type == "category":
            if raw_value is None:
                missing.append(label)
            else:
                output.append(raw_value)
            continue
        raw_text = str(raw_value).strip()
        if not raw_text:
            missing.append(label)
            continue
        try:
            value = float(raw_text)
            if not math.isfinite(value):
                raise ValueError
            output.append(value)
        except (TypeError, ValueError):
            invalid.append(label)
    if missing:
        st.error("Complete all required fields: " + ", ".join(missing[:7]) + (" and more." if len(missing) > 7 else "."))
        return None
    if invalid:
        st.error("Enter a valid finite number for: " + ", ".join(invalid) + ".")
        return None
    return output


def run_prediction(model, values, condition):
    try:
        prediction = int(model.predict([values])[0])
    except Exception as exc:
        st.error(f"The model could not process these values: {exc}")
        return
    if prediction == 1:
        title, state = "Positive classification", "flagged"
        copy = f"The model classified this input as positive for {condition.lower()}. This is a machine-learning screening signal, not a medical diagnosis. Discuss the result with a qualified healthcare professional."
    else:
        title, state = "Negative classification", ""
        copy = f"The model did not classify this input as positive for {condition.lower()}. A negative model output does not rule out a medical condition. Consult a healthcare professional if you have symptoms or concerns."
    st.markdown(
        f'<div class="result {state}"><div class="result-kicker">Model output · {condition}</div><div class="result-title">{title}</div><p class="result-copy">{copy}</p></div>',
        unsafe_allow_html=True,
    )


def page_intro(kicker, title, description):
    st.markdown(
        f'<div class="intro"><div class="intro-kicker">{kicker}</div><div class="intro-title">{title}</div><p class="intro-copy">{description}</p></div>',
        unsafe_allow_html=True,
    )


def medical_notice():
    st.markdown(
        "<div class='banner'><strong>Important:</strong> This is an educational machine-learning demonstration, not a medical device. It must not be used to diagnose, treat, or rule out any condition. Seek professional medical advice for health decisions.</div>",
        unsafe_allow_html=True,
    )


def navigate_to(destination):
    st.session_state["navigation"] = destination


# Sidebar navigation.
with st.sidebar:
    st.markdown(
        '<div class="brand"><div class="brand-mark">✚</div><div><div class="brand-name">MediScope</div><div class="brand-sub">Multiple disease prediction</div></div></div><div class="side-label">Workspace</div>',
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Navigation", ["Overview", "Diabetes", "Heart Disease", "Parkinson's"],
        label_visibility="collapsed", key="navigation",
    )
    st.markdown(
        '<div class="side-foot"><strong style="color:#dcebef">ML Health Lab</strong><br>Three trained classification models<br><br>Educational prototype · Not for diagnosis</div>',
        unsafe_allow_html=True,
    )


if page == "Overview":
    left, right = st.columns([5, 2])
    with left:
        st.markdown('<div class="eyebrow">MACHINE LEARNING HEALTH WORKSPACE</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Understand the signals.<br>Explore the predictions.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-copy">A clean workspace for exploring three machine-learning models trained to classify diabetes, heart disease, and Parkinson\'s-related input patterns.</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div style="display:flex;justify-content:flex-end;padding-top:.5rem"><span class="status"><span class="dot"></span> Models ready</span></div>', unsafe_allow_html=True)
    medical_notice()
    st.markdown('<div class="section-title">Prediction modules</div><div class="section-copy">Choose a module to enter its required features and run the existing trained model.</div>', unsafe_allow_html=True)
    cards = st.columns(3, gap="medium")
    modules = [
        ("🩸", "Diabetes prediction", "Eight health and demographic features, including glucose, BMI, and age.", "8 INPUT FEATURES", "Diabetes"),
        ("❤️", "Heart disease prediction", "Thirteen clinical attributes such as blood pressure, cholesterol, and ECG codes.", "13 INPUT FEATURES", "Heart Disease"),
        ("🎙️", "Parkinson's prediction", "Twenty-two acoustic measurements extracted from voice recordings.", "22 INPUT FEATURES", "Parkinson's"),
    ]
    for col, (icon, title, description, tag, destination) in zip(cards, modules):
        with col:
            st.markdown(f'<div class="card"><div class="card-icon">{icon}</div><div class="card-title">{title}</div><div class="card-copy">{description}</div><span class="tag">{tag}</span></div>', unsafe_allow_html=True)
            st.button(f"Open {destination} →", key=f"open_{destination}", use_container_width=True, on_click=navigate_to, args=(destination,))
    st.markdown('<div class="section-title">How it works</div>', unsafe_allow_html=True)
    steps = st.columns(3)
    for col, number, title, description in zip(
        steps,
        ["01", "02", "03"],
        ["Choose a module", "Enter input features", "Review the output"],
        ["Select one of the three prediction models.", "Provide values in the format expected by the model.", "Review the binary classification and its limitations."],
    ):
        with col:
            st.markdown(f'<div style="border-top:2px solid #cde4e5;padding-top:.8rem"><div style="color:#0a8990;font:800 1.2rem Manrope">{number}</div><div style="font-weight:700;color:#294452;margin:.25rem 0">{title}</div><div style="font-size:.8rem;color:#82929c;line-height:1.55">{description}</div></div>', unsafe_allow_html=True)


elif page == "Diabetes":
    page_intro("MODULE 01 · 8 FEATURES", "Diabetes prediction", "Enter the eight features expected by the existing diabetes classification model.")
    with st.form("diabetes_form"):
        st.markdown("**Health and demographic details**")
        st.caption("Provide values in the measurement units shown.")
        fields = numeric_fields([
            ("pregnancies", "Pregnancies"), ("glucose", "Glucose (mg/dL)"),
            ("blood_pressure", "Blood pressure (mmHg)"), ("skin_thickness", "Skin thickness (mm)"),
            ("insulin", "Insulin (µU/mL)"), ("bmi", "BMI (kg/m²)"),
            ("pedigree", "Diabetes pedigree function"), ("age", "Age (years)"),
        ], columns=4)
        submitted = st.form_submit_button("Run diabetes prediction", use_container_width=True)
    if submitted:
        values = parse_features([
            ("Pregnancies", fields["pregnancies"], "numeric"), ("Glucose", fields["glucose"], "numeric"),
            ("Blood pressure", fields["blood_pressure"], "numeric"), ("Skin thickness", fields["skin_thickness"], "numeric"),
            ("Insulin", fields["insulin"], "numeric"), ("BMI", fields["bmi"], "numeric"),
            ("Diabetes pedigree function", fields["pedigree"], "numeric"), ("Age", fields["age"], "numeric"),
        ])
        if values is not None:
            run_prediction(MODELS["diabetes"], values, "Diabetes")
    medical_notice()


elif page == "Heart Disease":
    page_intro("MODULE 02 · 13 FEATURES", "Heart disease prediction", "Provide clinical attributes in the numeric and category formats used by the model's training data.")
    with st.form("heart_form"):
        st.markdown("**Patient profile and measurements**")
        numeric = numeric_fields([
            ("heart_age", "Age (years)"), ("trestbps", "Resting BP (mmHg)"),
            ("chol", "Cholesterol (mg/dL)"), ("thalach", "Maximum heart rate"),
        ], columns=4)
        cats1 = st.columns(4)
        with cats1[0]: sex = category_field("Sex", [0, 1], {0: "Female", 1: "Male"}, "sex")
        with cats1[1]: cp = category_field("Chest pain type", [0, 1, 2, 3], {0: "Typical angina", 1: "Atypical angina", 2: "Non-anginal pain", 3: "Asymptomatic"}, "cp")
        with cats1[2]: fbs = category_field("Fasting blood sugar >120", [0, 1], {0: "No", 1: "Yes"}, "fbs")
        with cats1[3]: restecg = category_field("Resting ECG", [0, 1, 2], {0: "Normal", 1: "ST-T abnormality", 2: "Possible LV hypertrophy"}, "restecg")
        st.markdown("**Exercise and diagnostic attributes**")
        cats2 = st.columns(5)
        with cats2[0]: exang = category_field("Exercise angina", [0, 1], {0: "No", 1: "Yes"}, "exang")
        with cats2[1]: oldpeak = st.text_input("ST depression (oldpeak)", key="input_oldpeak", placeholder="Enter numeric value")
        with cats2[2]: slope = category_field("ST segment slope", [0, 1, 2], {0: "Upsloping", 1: "Flat", 2: "Downsloping"}, "slope")
        with cats2[3]: ca = st.text_input("Major vessels (ca)", key="input_ca", placeholder="Enter numeric value")
        with cats2[4]: thal = category_field("Thalassemia (thal)", [0, 1, 2], {0: "Normal", 1: "Fixed defect", 2: "Reversible defect"}, "thal")
        submitted = st.form_submit_button("Run heart disease prediction", use_container_width=True)
    if submitted:
        values = parse_features([
            ("Age", numeric["heart_age"], "numeric"), ("Sex", sex, "category"), ("Chest pain type", cp, "category"),
            ("Resting blood pressure", numeric["trestbps"], "numeric"), ("Cholesterol", numeric["chol"], "numeric"),
            ("Fasting blood sugar", fbs, "category"), ("Resting ECG", restecg, "category"),
            ("Maximum heart rate", numeric["thalach"], "numeric"), ("Exercise-induced angina", exang, "category"),
            ("ST depression", oldpeak, "numeric"), ("ST segment slope", slope, "category"),
            ("Major vessels", ca, "numeric"), ("Thalassemia", thal, "category"),
        ])
        if values is not None:
            run_prediction(MODELS["heart"], values, "Heart disease")
    medical_notice()


elif page == "Parkinson's":
    page_intro("MODULE 03 · 22 FEATURES", "Parkinson's prediction", "Enter acoustic measurements extracted from a voice recording. These are model features, not ordinary patient details.")
    st.markdown("<div class='banner'><strong>Before you begin:</strong> The model expects 22 precomputed voice-analysis features. A voice recording cannot be entered directly; the numeric measurements must first be generated by a compatible feature-extraction pipeline.</div>", unsafe_allow_html=True)
    with st.form("parkinsons_form"):
        st.markdown("**Frequency and pitch · Hz**")
        freq = numeric_fields([("fo", "MDVP:Fo (Hz)"), ("fhi", "MDVP:Fhi (Hz)"), ("flo", "MDVP:Flo (Hz)")], columns=3)
        st.markdown("**Jitter measurements**")
        jitter = numeric_fields([
            ("jitter_percent", "MDVP:Jitter (%)"), ("jitter_abs", "MDVP:Jitter (Abs)"),
            ("rap", "MDVP:RAP"), ("ppq", "MDVP:PPQ"), ("ddp", "Jitter:DDP"),
        ], columns=5)
        st.markdown("**Shimmer measurements**")
        shimmer = numeric_fields([
            ("shimmer", "MDVP:Shimmer"), ("shimmer_db", "MDVP:Shimmer (dB)"),
            ("apq3", "Shimmer:APQ3"), ("apq5", "Shimmer:APQ5"),
            ("apq", "MDVP:APQ"), ("dda", "Shimmer:DDA"),
        ], columns=3)
        st.markdown("**Voice quality and nonlinear features**")
        voice = numeric_fields([
            ("nhr", "NHR"), ("hnr", "HNR"), ("rpde", "RPDE"), ("dfa", "DFA"),
            ("spread1", "spread1"), ("spread2", "spread2"), ("d2", "D2"), ("ppe", "PPE"),
        ], columns=4)
        submitted = st.form_submit_button("Run Parkinson's prediction", use_container_width=True)
    if submitted:
        all_fields = {**freq, **jitter, **shimmer, **voice}
        order = ["fo", "fhi", "flo", "jitter_percent", "jitter_abs", "rap", "ppq", "ddp", "shimmer", "shimmer_db", "apq3", "apq5", "apq", "dda", "nhr", "hnr", "rpde", "dfa", "spread1", "spread2", "d2", "ppe"]
        labels = ["MDVP:Fo", "MDVP:Fhi", "MDVP:Flo", "MDVP:Jitter (%)", "MDVP:Jitter (Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer (dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"]
        values = parse_features([(label, all_fields[key], "numeric") for key, label in zip(order, labels)])
        if values is not None:
            run_prediction(MODELS["parkinsons"], values, "Parkinson's disease")
    medical_notice()


st.markdown('<div class="footnote">MediScope · Machine-learning project interface · Educational output, not a substitute for professional medical care.</div>', unsafe_allow_html=True)
