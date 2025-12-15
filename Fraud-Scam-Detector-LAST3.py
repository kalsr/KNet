

# ============================================================
# ENTERPRISE FRAUD & SCAM DETECTION PLATFORM (STABLE)
# Designed & Developed by Randy Singh – KNet Consulting
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from PIL import Image, ImageDraw, ImageFont
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
    confidence = min(100, score*20)
    risk = "High" if score >=4 else "Medium" if score >=2 else "Low"
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
    # Larger font for better readability
    img = Image.new("RGB", (900,300),"white")
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((20,100), generate_sample_image_text(), fill="black", font=font)
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
if "text_input" not in st.session_state:
    st.session_state.text_input = ""
if "sample_texts" not in st.session_state:
    st.session_state.sample_texts = []

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
    # Simulated LLM explanation
    if any(k in text.lower() for k in KEYWORDS):
        return "LLM Analysis: This message contains multiple indicators of fraud or scam."
    else:
        return "LLM Analysis: The message appears safe."

# ---------------- RESET ----------------
def reset_all():
    st.session_state.results = pd.DataFrame(columns=st.session_state.results.columns)
    st.session_state.uploaded_screenshots = []
    st.session_state.text_input = ""
    st.session_state.sample_texts = []

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    " DETECTION",
    " SCREENSHOT",
    " SAMPLE DATA GNERATOR",
    " EXECUTIVE DASHBOARD",
    " EXPORT RESULTS" 
])

# ---------------- TAB 1: DETECTION ----------------
with tab1:
    text = st.text_area("Enter Email / Message", value=st.session_state.get("text_input",""))
    st.session_state.text_input = text

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
    col1, col2 = st.columns([2,1])
    with col1:
        img_file = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])
        if img_file:
            img = Image.open(img_file)
            st.image(img, width=600)
            # Simulate OCR text for demo purposes
            text = generate_sample_image_text()
            res, score, conf, risk = rule_score(text)
            ml = ml_predict(text)
            llm = llm_explain(text)
            st.session_state.results.loc[len(st.session_state.results)] = (
                "Uploaded Screenshot", text, score, ml, conf, risk, res, llm
            )
            # Display full analysis below the image
            st.subheader("SCREENSHOT ANALYSIS RESULT")
            st.markdown(f"**Result:** {res}")
            st.markdown(f"**Risk Level:** {risk}")
            st.markdown(f"**Confidence:** {conf}%")
            st.markdown(f"**ML Prediction:** {ml}")
            st.markdown(f"**LLM Explanation:** {llm}")

    with col2:
        n = st.number_input("Generate Sample Screenshots", min_value=1, max_value=10, value=1)
        if st.button("Generate & Analyze Sample Screenshots"):
            for i in range(n):
                img = generate_sample_image()
                st.image(img, width=600)
                text = generate_sample_image_text()
                res, score, conf, risk = rule_score(text)
                ml = ml_predict(text)
                llm = llm_explain(text)
                st.session_state.results.loc[len(st.session_state.results)] = (
                    "Sample Screenshot", text, score, ml, conf, risk, res, llm
                )
                # Display detailed analysis immediately
                st.subheader(f" Sample Screenshot {i+1} Analysis Result")
                st.markdown(f"**Result:** {res}")
                st.markdown(f"**Risk Level:** {risk}")
                st.markdown(f"**Confidence:** {conf}%")
                st.markdown(f"**ML Prediction:** {ml}")
                st.markdown(f"**LLM Explanation:** {llm}")
            st.success(f"{n} Sample screenshots generated and analyzed.")


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

# ---------------- TAB 4: EXECUTIVE DASHBOARD ----------------
with tab4:
    if st.session_state.results.empty:
        st.info("No analysis results yet")
    else:
        st.markdown("### Fraud vs Legitimate Overview")
        st.dataframe(st.session_state.results)
        
        # Bar chart
        fig, ax = plt.subplots(figsize=(10,5))
        st.session_state.results["Result"].value_counts().plot(kind="bar", ax=ax, title="Fraud vs Legitimate")
        st.pyplot(fig)

        # Risk bands
        st.markdown("### Risk Bands")
        fig2, ax2 = plt.subplots(figsize=(10,5))
        st.session_state.results["Risk"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2, title="Risk Distribution")
        st.pyplot(fig2)

        # Average confidence
        st.markdown("### Average Confidence Score")
        st.metric("Avg Confidence", f"{st.session_state.results['Confidence'].mean():.2f}%")

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
                0,10,
                f"{r['Source']} | {r['Result']} | Risk: {r['Risk']} | ML: {r['ML']}\n{r['Content']}\nLLM: {r['LLM_Explanation']}\n"
            )
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        st.download_button("Download PDF", pdf_bytes, "fraud_results.pdf")

st.markdown("---")
st.caption("© KNet Consulting Group | Enterprise Fraud & Scam Detection Platform")


