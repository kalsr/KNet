

# ============================================================
# ENTERPRISE FRAUD & SCAM DETECTION PLATFORM (STABLE)
# Designed & Developed by Randy Singh – KNet Consulting
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
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
    padding: 30px;
    border-radius: 16px;
    color: white;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
}
.stTabs [role="tab"] {
    font-size: 24px !important;
    font-weight: 900 !important;
}
.stButton button {
    font-size: 18px;
    font-weight: 800;
    padding: 12px 36px;
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
    d.text((20, 70),
           "URGENT SECURITY ALERT\nVerify your bank account now!",
           fill="black")
    return img

# ---------------- SESSION STATE INIT ----------------
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
        baseline = [generate_sample_text() for _ in range(60)]
        X = np.array([vectorize(t) for t in baseline])
        st.session_state.model.fit(X)
        st.session_state.model_trained = True

def ml_predict(text):
    ensure_model_trained()
    X = np.array([vectorize(text)])
    return "Suspicious" if st.session_state.model.predict(X)[0] == -1 else "Normal"

# ---------------- RESET (FIXED) ----------------
def reset_all():
    st.session_state.clear()
    st.rerun()

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✍ Detection",
    "📷 Screenshot",
    "🎲 Sample Generator",
    "📊 Analytics",
    "📤 Export"
])

# ---------------- TAB 1: DETECTION ----------------
with tab1:
    text = st.text_area("Enter Email / Message")

    if st.button("Analyze Message"):
        if text.strip():
            res, score, conf, risk = rule_score(text)
            ml = ml_predict(text)
            st.session_state.results.loc[len(st.session_state.results)] = (
                "Text", text, score, ml, conf, risk, res
            )
            st.success(f"{res} | Risk: {risk} | Confidence: {conf}% | ML: {ml}")

    st.button("🔴 Reset All Data", on_click=reset_all)

# ---------------- TAB 2: SCREENSHOT ----------------
with tab2:
    img_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])

    if img_file:
        img = Image.open(img_file)
        st.image(img, width=450)
        text = "urgent verify bank"
        res, score, conf, risk = rule_score(text)
        ml = ml_predict(text)
        st.session_state.results.loc[len(st.session_state.results)] = (
            "Screenshot", text, score, ml, conf, risk, res
        )
        st.success(f"{res} | Risk: {risk} | ML: {ml}")

    if st.button("Generate Sample Screenshot"):
        st.image(generate_sample_image())

# ---------------- TAB 3: SAMPLE GENERATOR ----------------
with tab3:
    n = st.slider("Generate Sample Messages", 0, 100, 20)

    samples = []
    for _ in range(n):
        msg = generate_sample_text()
        res, score, conf, risk = rule_score(msg)
        ml = ml_predict(msg)
        samples.append([msg, score, ml, conf, risk, res])

    df_samples = pd.DataFrame(
        samples,
        columns=["Message","RuleScore","ML","Confidence","Risk","Result"]
    )

    st.dataframe(df_samples)

    if st.button("Add Samples to Analytics"):
        for _, r in df_samples.iterrows():
            st.session_state.results.loc[len(st.session_state.results)] = (
                "Sample", r["Message"], r["RuleScore"],
                r["ML"], r["Confidence"], r["Risk"], r["Result"]
            )
        st.success("Samples added to Analytics")

# ---------------- TAB 4: ANALYTICS ----------------
with tab4:
    if st.session_state.results.empty:
        st.info("No analysis results available.")
    else:
        st.dataframe(st.session_state.results)

        fig, ax = plt.subplots()
        st.session_state.results["Result"].value_counts().plot(
            kind="bar", ax=ax, title="Fraud vs Legitimate"
        )
        st.pyplot(fig)

# ---------------- TAB 5: EXPORT ----------------
with tab5:
    if not st.session_state.results.empty:
        csv = st.session_state.results.to_csv(index=False).encode()
        st.download_button("Download CSV", csv, "fraud_results.csv")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        for _, r in st.session_state.results.iterrows():
            pdf.multi_cell(
                0, 8,
                f"{r['Source']} | {r['Result']} | Risk: {r['Risk']} | ML: {r['ML']}\n{r['Content']}\n"
            )
        buffer = io.BytesIO()
        pdf.output(buffer)
        st.download_button("Download PDF", buffer.getvalue(), "fraud_results.pdf")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform")
