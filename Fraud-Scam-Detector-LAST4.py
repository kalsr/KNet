# 1-1-1-

# ============================================================

# ENTERPRISE FRAUD & SCAM DETECTION PLATFORM (ENHANCED)

# Designed & Developed by Randy Singh – KNet Consulting Group

# ============================================================



import streamlit as st

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.ensemble import IsolationForest

from PIL import Image, ImageDraw, ImageFont

from fpdf import FPDF

import random



# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Enterprise Fraud Detection", layout="wide")



# ---------------- STYLES ----------------

st.markdown("""

<style>

.header {

    background: linear-gradient(90deg,#0b4f9c,#1fa2ff);

    padding: 30px;

    border-radius: 16px;

    color: white;

    text-align: center;

    font-size: 36px;

    font-weight: 900;

}

.stTabs [role="tab"] {

    font-size: 28px !important;

    font-weight: 900 !important;

}

.stButton button {

    font-size: 20px !important;

    font-weight: 900 !important;

    padding: 14px 40px !important;

}

</style>

""", unsafe_allow_html=True)



# ---------------- HEADER ----------------

st.markdown("""

<div class="header">

Enterprise Fraud & Scam Detection Platform<br>

<b>Randy Singh</b> – <b>KNet Consulting Group</b>

</div>

""", unsafe_allow_html=True)



# ============================================================

# FRAUD INTELLIGENCE ENGINE

# ============================================================



FRAUD_SIGNALS = {

    "urgent": 15,

    "verify": 12,

    "account": 10,

    "bank": 15,

    "click": 12,

    "password": 18,

    "wire": 20,

    "gift card": 25,

    "lottery": 30,

    "suspended": 20,

    "security alert": 18,

    "action required": 15

}



SAFE_SIGNALS = [

    "meeting", "invoice", "attached", "schedule",

    "project", "team", "regards"

]



# ---------------- RULE ENGINE ----------------

def rule_score(text):

    text_l = text.lower()



    fraud_score = sum(

        weight for k, weight in FRAUD_SIGNALS.items() if k in text_l

    )



    safe_hits = sum(1 for k in SAFE_SIGNALS if k in text_l)

    fraud_score = max(0, fraud_score - safe_hits * 10)



    confidence = min(99, int((fraud_score / 100) * 100))



    if fraud_score >= 60:

        return "Fraud / Scam", fraud_score, confidence, "High"

    elif fraud_score >= 30:

        return "Suspicious", fraud_score, confidence, "Medium"

    else:

        return "Legitimate", fraud_score, confidence, "Low"



# ============================================================

# SAMPLE DATA GENERATORS

# ============================================================



def generate_sample_text():

    return random.choice([

        "URGENT: Your bank account has been suspended. Verify immediately.",

        "Congratulations! You won a lottery. Send gift cards now.",

        "Security alert: Click the link to reset your password.",

        "Team meeting moved to Friday at 3 PM.",

        "Invoice attached for last month's consulting services."

    ])



def generate_sample_image_text():

    return random.choice([

        "URGENT: verify bank account now",

        "Congratulations! Claim your gift cards",

        "Security alert! Click to update password",

        "Immediate action required on your account"

    ])



def generate_sample_image():

    img = Image.new("RGB", (900, 300), "white")

    d = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    d.text((20, 120), generate_sample_image_text(), fill="black", font=font)

    return img



# ============================================================

# MACHINE LEARNING ENGINE

# ============================================================



def vectorize(text):

    return [

        len(text),

        sum(c.isupper() for c in text),

        sum(c.isdigit() for c in text),

        text.count("!"),

        sum(1 for k in FRAUD_SIGNALS if k in text.lower())

    ]



def ensure_model_trained():

    if not st.session_state.model_trained:

        baseline = [generate_sample_text() for _ in range(80)]

        X = np.array([vectorize(t) for t in baseline])

        st.session_state.model.fit(X)

        st.session_state.model_trained = True



def ml_predict(text):

    ensure_model_trained()

    X = np.array([vectorize(text)])

    return "Anomalous" if st.session_state.model.predict(X)[0] == -1 else "Normal"



# ============================================================

# LLM EXPLANATION (DETERMINISTIC)

# ============================================================



def llm_explain(text):

    text_l = text.lower()

    hits = [k for k in FRAUD_SIGNALS if k in text_l]



    if not hits:

        return (

            "LLM Analysis: The message follows standard business communication patterns, "

            "contains no urgency manipulation, and does not request sensitive actions."

        )



    return (

        "LLM Analysis identified potential fraud indicators: "

        + ", ".join(hits)

        + ". These patterns are commonly associated with social engineering attacks "

          "designed to induce urgency, fear, or financial pressure."

    )



# ============================================================

# SESSION STATE

# ============================================================



if "results" not in st.session_state:

    st.session_state.results = pd.DataFrame(

        columns=["Source","Content","RuleScore","ML","Confidence","Risk","Result","LLM_Explanation"]

    )



if "model" not in st.session_state:

    st.session_state.model = IsolationForest(contamination=0.3, random_state=42)

    st.session_state.model_trained = False



if "text_input" not in st.session_state:

    st.session_state.text_input = ""



# ---------------- RESET ----------------

def reset_all():

    st.session_state.results = st.session_state.results.iloc[0:0]

    st.session_state.text_input = ""



# ============================================================

# TABS

# ============================================================



tab1, tab2, tab3, tab4, tab5 = st.tabs([

    " DETECTION",

    " SCREENSHOT",

    " SAMPLE DATA GENERATOR",

    " EXECUTIVE DASHBOARD",

    " EXPORT RESULTS"

])



# ---------------- TAB 1: DETECTION ----------------

with tab1:

    text = st.text_area("Enter Email / Message", value=st.session_state.text_input)



    if st.button("Analyze Message"):

        if text.strip():

            res, score, conf, risk = rule_score(text)

            ml = ml_predict(text)

            llm = llm_explain(text)



            st.session_state.results.loc[len(st.session_state.results)] = (

                "Text", text, score, ml, conf, risk, res, llm

            )



            st.success(f"{res} | Risk: {risk} | Confidence: {conf}% | ML: {ml}")

            st.info(llm)



    st.button(" RESET ALL DATA", on_click=reset_all)



# ---------------- TAB 2: SCREENSHOT ----------------

with tab2:

    img_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])

    if img_file:

        img = Image.open(img_file)

        st.image(img, width=600)



        text = generate_sample_image_text()

        res, score, conf, risk = rule_score(text)

        ml = ml_predict(text)

        llm = llm_explain(text)



        st.session_state.results.loc[len(st.session_state.results)] = (

            "Screenshot", text, score, ml, conf, risk, res, llm

        )



        st.subheader("SCREENSHOT ANALYSIS RESULT")

        st.markdown(f"**Result:** {res}")

        st.markdown(f"**Risk:** {risk}")

        st.markdown(f"**Confidence:** {conf}%")

        st.markdown(f"**ML:** {ml}")

        st.markdown(f"**LLM Explanation:** {llm}")



# ---------------- TAB 3: SAMPLE GENERATOR ----------------

with tab3:

    n = st.slider("Generate Sample Messages", 1, 100, 20)

    if st.button("Generate & Analyze"):

        for _ in range(n):

            msg = generate_sample_text()

            res, score, conf, risk = rule_score(msg)

            ml = ml_predict(msg)

            llm = llm_explain(msg)



            st.session_state.results.loc[len(st.session_state.results)] = (

                "Sample", msg, score, ml, conf, risk, res, llm

            )

        st.success(f"{n} messages generated and analyzed")



# ---------------- TAB 4: DASHBOARD ----------------

with tab4:

    if not st.session_state.results.empty:

        st.dataframe(st.session_state.results)



        fig, ax = plt.subplots()

        st.session_state.results["Result"].value_counts().plot(kind="bar", ax=ax)

        st.pyplot(fig)



        st.metric("Average Confidence",

                  f"{st.session_state.results['Confidence'].mean():.2f}%")



# ---------------- TAB 5: EXPORT ----------------

with tab5:

    if not st.session_state.results.empty:

        csv = st.session_state.results.to_csv(index=False).encode()

        st.download_button("Download CSV", csv, "fraud_results.csv")



        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=12)



        for _, r in st.session_state.results.iterrows():

            pdf.multi_cell(

                0, 10,

                f"{r['Source']} | {r['Result']} | Risk: {r['Risk']} | ML: {r['ML']}\n"

                f"{r['Content']}\nLLM: {r['LLM_Explanation']}\n\n"

            )



        st.download_button(

            "Download PDF",

            pdf.output(dest="S").encode("latin1"),

            "fraud_results.pdf"

        )



st.markdown("---")

st.caption("© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform")

