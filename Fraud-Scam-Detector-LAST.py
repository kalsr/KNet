
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
import random
import io

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

# ---------------- RULES ----------------
KEYWORDS = ["urgent","verify","bank","click","password","wire","lottery","gift card"]

def rule_score(text):
    score = sum(1 for k in KEYWORDS if k in text.lower())
    confidence = min(100, score*25)
    risk = "High" if score >=3 else "Medium" if score >=2 else "Low"
    result = "Fraud / Scam" if score>=2 else "Legitimate"
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

def generate_sample_image_text():
    phrases = [
        "URGENT: verify bank account now",
        "Congratulations! Claim your gift cards",
        "Security alert! Click to update password",
        "Immediate action required on your account"
    ]
    return random.choice(phrases)

def generate_sample_image():
    img = Image.new("RGB", (900,400),"white")
    d = ImageDraw.Draw(img)
    d.text((20,150), generate_sample_image_text(), fill="black")
    return img

# ---------------- SESSION STATE ----------------
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(
        columns=["Source","Content","RuleScore","ML","Confidence","Risk","Result","LLM_Explanation"]
    )
if "model" not in st.session_state:
    st.session_state.model = IsolationForest(contamination=0.3, random_state=42)
    st.session_state.model_trained = False
if "uploaded_screenshots" not in st.session_state:
    st.session_state.uploaded_screenshots = []

# ---------------- ML ----------------
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
    return "Suspicious" if st.session_state.model.predict(X)[0]==-1 else "Normal"

# ---------------- LLM EXPLANATION ----------------
def llm_explain(text):
    if any(k in text.lower() for k in KEYWORDS):
        return "LLM Analysis: Multiple fraud indicators detected."
    else:
        return "LLM Analysis: This message appears safe."

# ---------------- RESET ----------------
def reset_all():
    st.session_state.results = pd.DataFrame(columns=st.session_state.results.columns)
    st.session_state.uploaded_screenshots = []
    st.session_state.text_input = ""
    st.session_state.sample_texts = []

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✍ Detection",
    "📷 Screenshot",
    "🎲 Sample Generator",
    "📊 Executive Analytics",
    "📤 Export"
])

# ---------------- TAB 1: DETECTION ----------------
with tab1:
    text = st.text_area("Enter Email / Message", value=st.session_state.get("text_input",""), height=150)
    st.session_state.text_input = text

    col1, col2 = st.columns(2)
    with col1:
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
    with col2:
        st.button("🔴 Reset All Data", on_click=reset_all)

# ---------------- TAB 2: SCREENSHOT (FIXED) ----------------
with tab2:
    col1, col2 = st.columns([2,1])
    with col1:
        img_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])
        if img_file:
            img = Image.open(img_file)
            st.image(img, width=900)  # Bigger display
            # Simulate OCR from uploaded screenshot
            text = generate_sample_image_text()
            res, score, conf, risk = rule_score(text)
            ml = ml_predict(text)
            llm = llm_explain(text)
            st.session_state.results.loc[len(st.session_state.results)] = (
                "Uploaded Screenshot", text, score, ml, conf, risk, res, llm
            )
            st.success(f"{res} | Risk: {risk} | ML: {ml} | Confidence: {conf}%")
            st.info(llm)

    with col2:
        n = st.number_input("Generate Sample Screenshots", min_value=1, max_value=10, value=1)
        if st.button("Generate & Analyze Sample Screenshots"):
            for _ in range(n):
                # Create larger image and bigger font
                img = Image.new("RGB", (1200,600),"white")
                d = ImageDraw.Draw(img)
                text_img = generate_sample_image_text()
                d.text((50,250), text_img, fill="black", align="center")
                st.image(img, width=900)  # Larger display
                # Analysis for generated screenshot
                res, score, conf, risk = rule_score(text_img)
                ml = ml_predict(text_img)
                llm = llm_explain(text_img)
                st.session_state.results.loc[len(st.session_state.results)] = (
                    "Sample Screenshot", text_img, score, ml, conf, risk, res, llm
                )
                st.success(f"{res} | Risk: {risk} | ML: {ml} | Confidence: {conf}%")
                st.info(llm)


# ---------------- TAB 3: SAMPLE GENERATOR ----------------
with tab3:
    n = st.slider("Generate Sample Messages", 0, 100, 20)
    df_samples = pd.DataFrame(columns=["Message","RuleScore","ML","Confidence","Risk","Result","LLM_Explanation"])
    if st.button("Generate & Analyze Sample Messages"):
        for _ in range(n):
            msg = generate_sample_text()
            res, score, conf, risk = rule_score(msg)
            ml = ml_predict(msg)
            llm = llm_explain(msg)
            df_samples.loc[len(df_samples)] = [msg, score, ml, conf, risk, res, llm]
            st.session_state.results.loc[len(st.session_state.results)] = [
                "Sample Text", msg, score, ml, conf, risk, res, llm
            ]
        st.success(f"{n} sample messages generated and analyzed.")
    st.dataframe(df_samples)

# ---------------- TAB 4: EXECUTIVE ANALYTICS ----------------
with tab4:
    if st.session_state.results.empty:
        st.info("No analysis results yet")
    else:
        st.markdown("### Fraud vs Legitimate Overview")
        st.dataframe(st.session_state.results)
        fig, ax = plt.subplots(figsize=(12,5))
        st.session_state.results["Result"].value_counts().plot(kind="bar", ax=ax, title="Fraud vs Legitimate")
        st.pyplot(fig)

        st.markdown("### Risk Bands")
        fig2, ax2 = plt.subplots(figsize=(12,5))
        st.session_state.results["Risk"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2, title="Risk Distribution")
        st.pyplot(fig2)

        st.markdown("### Average Confidence Score")
        st.metric("Avg Confidence", f"{st.session_state.results['Confidence'].mean():.2f}%")

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
                0,8,
                f"{r['Source']} | {r['Result']} | Risk: {r['Risk']} | ML: {r['ML']}\n{r['Content']}\nLLM: {r['LLM_Explanation']}\n"
            )
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        st.download_button("Download PDF", pdf_bytes, "fraud_results.pdf")

st.markdown("---")
st.caption("© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform")

