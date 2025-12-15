

# ============================================================
# ENTERPRISE FRAUD & SCAM DETECTION PLATFORM
# Designed & Developed by Randy Singh – KNet Consulting
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.exceptions import NotFittedError
from PIL import Image, ImageDraw
from fpdf import FPDF
import random, io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Enterprise Fraud Detection", layout="wide")

# ---------------- STYLES ----------------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#0b4f9c,#1fa2ff);
    padding: 26px;
    border-radius: 14px;
    color: white;
    text-align: center;
    font-size: 30px;
    font-weight: 800;
}
.stTabs [role="tab"] {
    font-size: 22px !important;
    font-weight: 800 !important;
}
.stButton button {
    font-size: 17px;
    font-weight: 700;
    padding: 10px 30px;
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

# ---------------- FRAUD RULES ----------------
KEYWORDS = ["urgent","verify","bank","click","password","wire","lottery","gift card"]

def rule_score(text):
    score = sum(1 for k in KEYWORDS if k in text.lower())
    confidence = min(100, score * 20)
    risk = "High" if score >= 4 else "Medium" if score >= 2 else "Low"
    result = "Fraud / Scam" if score >= 2 else "Legitimate"
    return result, score, confidence, risk

# ---------------- SAMPLE GENERATORS ----------------
def generate_sample_text():
    return random.choice([
        "URGENT: Your bank account is suspended. Verify immediately.",
        "Congratulations! You won a lottery. Send gift cards.",
        "Security alert: Click link to reset password.",
        "Team meeting moved to Friday at 3 PM.",
        "Invoice attached for last month's services."
    ])

def generate_sample_image():
    img = Image.new("RGB", (650, 260), "white")
    d = ImageDraw.Draw(img)
    d.text((20, 60),
            "URGENT SECURITY ALERT\nVerify your bank account now!",
            fill="black")
    return img

# ---------------- SESSION STATE ----------------
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(
        columns=["Source","Content","RuleScore","ML","Confidence","Risk","Result"]
    )

if "model" not in st.session_state:
    st.session_state.model = IsolationForest(contamination=0.3, random_state=42)
    st.session_state.model_trained = False

# ---------------- ML FUNCTIONS ----------------
def vectorize(text):
    return [len(text), sum(c.isupper() for c in text)]

def ensure_model_trained():
    if not st.session_state.model_trained:
        baseline = [generate_sample_text() for _ in range(50)]
        X = np.array([vectorize(t) for t in baseline])
        st.session_state.model.fit(X)
        st.session_state.model_trained = True

def ml_predict(text):
    ensure_model_trained()
    X = np.array([vectorize(text)])
    return "Suspicious" if st.session_state.model.predict(X)[0] == -1 else "Normal"

# ---------------- RESET ----------------
def reset_all():
    st.session_state.results = st.session_state.results.iloc[0:0]
    st.session_state.model = IsolationForest(contamination=0.3, random_state=42)
    st.session_state.model_trained = False
    st.experimental_rerun()

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✍ Detection",
    "📷 Screenshot",
    "🎲 Sample Generator",
    "📊 Analytics",
    "📤 Export"
])

# ---------------- TAB 1 ----------------
with tab1:
    text = st.text_area("Enter Email / Message")

    if st.button("Analyze Message"):
        if text:
            res, score, conf, risk = rule_score(text)
            ml = ml_predict(text)
            st.session_state.results.loc[len(st.session_state.results)] = (
                "Text", text, score, ml, conf, risk, res
            )
            st.success(f"{res} | Risk: {risk} | Confidence: {conf}% | ML: {ml}")

    st.button("Reset All Data", on_click=reset_all)

# ---------------- TAB 2 ----------------
with tab2:
    img_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])
    if img_file:
        img = Image.open(img_file)
        st.image(img, width=420)
        text = "urgent verify bank"
        res, score, conf, risk = rule_score(text)
        ml = ml_predict(text)
        st.session_state.results.loc[len(st.session_state.results)] = (
            "Screenshot", text, score, ml, conf, risk, res
        )
        st.success(f"{res} | {risk} | ML: {ml}")

    if st.button("Generate Sample Screenshot"):
        demo = generate_sample_image()
        st.image(demo)

# ---------------- TAB 3 ----------------
with tab3:
    n = st.slider("Number of Sample Messages", 0, 100, 20)
    samples = [generate_sample_text() for _ in range(n)]
    df = pd.DataFrame(samples, columns=["Message"])
    st.dataframe(df)

# ---------------- TAB 4 ----------------
with tab4:
    if st.session_state.results.empty:
        st.info("No analysis results available.")
    else:
        st.dataframe(st.session_state.results)
        fig, ax = plt.subplots()
        st.session_state.results["Result"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

# ---------------- TAB 5 ----------------
with tab5:
    if st.button("Export CSV"):
        csv = st.session_state.results.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "fraud_results.csv")

    if st.button("Export PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        for _, r in st.session_state.results.iterrows():
            pdf.multi_cell(0, 8,
                f"{r['Source']} | {r['Result']} | Risk: {r['Risk']} | ML: {r['ML']}\n{r['Content']}\n")
        buffer = io.BytesIO()
        pdf.output(buffer)
        st.download_button("Download PDF", buffer.getvalue(), "fraud_results.pdf")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform")
