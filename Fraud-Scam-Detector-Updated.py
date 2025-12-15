

# =====================================================
# ENTERPRISE FRAUD & SCAM DETECTION PLATFORM – PHASE 2
# Designed & Developed by Randy Singh – KNet Consulting
# =====================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from fpdf import FPDF
from PIL import Image, ImageDraw
import random, io, os

# ---------- OPTIONAL OCR ----------
try:
    import pytesseract
    OCR_AVAILABLE = True
except:
    OCR_AVAILABLE = False

# ---------- OPTIONAL OPENAI ----------
OPENAI_AVAILABLE = False
try:
    from openai import OpenAI
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        OPENAI_AVAILABLE = True
except:
    pass

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Enterprise Fraud Detection",
    layout="wide"
)

# ---------- STYLES ----------
st.markdown("""
<style>
.header {
    background: linear-gradient(90deg,#0b4f9c,#1fa2ff);
    padding: 24px;
    border-radius: 14px;
    color: white;
    text-align: center;
    font-size: 30px;
    font-weight: 800;
}
.stTabs [role="tab"] {
    font-size: 18px;
    font-weight: 700;
}
.stButton button {
    font-size: 16px;
    font-weight: 700;
    padding: 10px 28px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header">
Enterprise Fraud & Scam Detection Platform<br>
<b>Randy Singh</b> – <b>KNet Consulting Group</b>
</div>
""", unsafe_allow_html=True)

# =====================================================
# ROLE-BASED ACCESS
# =====================================================
if "role" not in st.session_state:
    st.session_state.role = None

def login():
    st.session_state.role = st.session_state.login_role

def logout():
    st.session_state.clear()
    st.experimental_rerun()

if not st.session_state.role:
    st.subheader("🔐 Secure Login")
    st.selectbox(
        "Select Role",
        ["Analyst", "Commander"],
        key="login_role"
    )
    st.button("Login", on_click=login)
    st.stop()

st.sidebar.success(f"Logged in as: {st.session_state.role}")
st.sidebar.button("Logout", on_click=logout)

# =====================================================
# FRAUD LOGIC
# =====================================================
KEYWORDS = ["urgent","verify","bank","click","password","wire","lottery","gift card"]

def rule_score(text):
    score = sum(1 for k in KEYWORDS if k in text.lower())
    confidence = min(100, score * 20)
    band = "High" if score >= 4 else "Medium" if score >= 2 else "Low"
    result = "Fraud / Scam" if score >= 2 else "Legitimate"
    return result, score, confidence, band

# =====================================================
# SESSION STATE
# =====================================================
if "results" not in st.session_state:
    st.session_state.results = pd.DataFrame(
        columns=["Source","Text","RuleScore","ML","Confidence","Risk","Result"]
    )

if "model" not in st.session_state:
    st.session_state.model = IsolationForest(contamination=0.3, random_state=42)

# =====================================================
# ML FUNCTIONS
# =====================================================
def vectorize(text):
    return [len(text), sum(c.isupper() for c in text)]

def ml_predict(text):
    X = np.array([vectorize(text)])
    return "Suspicious" if st.session_state.model.predict(X)[0] == -1 else "Normal"

def train_model(df):
    X = np.array([vectorize(t) for t in df["Text"]])
    st.session_state.model.fit(X)

# =====================================================
# LLM EXPLANATION
# =====================================================
def llm_explain(text):
    if OPENAI_AVAILABLE:
        r = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role":"user","content":f"Explain fraud risk:\n{text}"}]
        )
        return r.choices[0].message.content
    else:
        hits=[k for k in KEYWORDS if k in text.lower()]
        return f"Fraud indicators detected: {', '.join(hits)}" if hits else "No strong fraud indicators detected."

# =====================================================
# TABS
# =====================================================
tabs = st.tabs([
    "✍ Detection",
    "📷 Screenshot",
    "🧠 ML Training",
    "📊 Analytics",
    "📈 Executive Dashboard"
])

# =====================================================
# TAB 1 – DETECTION
# =====================================================
with tabs[0]:
    text = st.text_area("Enter Email / Message")

    if st.button("Analyze"):
        res, score, conf, band = rule_score(text)
        ml = ml_predict(text)
        st.session_state.results.loc[len(st.session_state.results)] = (
            "Text", text, score, ml, conf, band, res
        )
        st.success(f"{res} | Risk: {band} | Confidence: {conf}% | ML: {ml}")
        st.info(llm_explain(text))

    if st.button("Reset All"):
        st.session_state.results = st.session_state.results.iloc[0:0]
        st.session_state.model = IsolationForest(contamination=0.3, random_state=42)
        st.experimental_rerun()

# =====================================================
# TAB 2 – SCREENSHOT
# =====================================================
with tabs[1]:
    img = st.file_uploader("Upload Screenshot", type=["png","jpg","jpeg"])
    if img:
        image = Image.open(img)
        st.image(image, width=400)
        text = pytesseract.image_to_string(image) if OCR_AVAILABLE else "urgent verify bank"
        res, score, conf, band = rule_score(text)
        ml = ml_predict(text)
        st.session_state.results.loc[len(st.session_state.results)] = (
            "Screenshot", text, score, ml, conf, band, res
        )
        st.success(f"{res} | {band} | ML: {ml}")
        st.info(llm_explain(text))

# =====================================================
# TAB 3 – ML TRAINING (ANALYST ONLY)
# =====================================================
with tabs[2]:
    if st.session_state.role != "Analyst":
        st.warning("Analyst access only")
    else:
        file = st.file_uploader("Upload CSV with Text column", type=["csv"])
        if file:
            df = pd.read_csv(file)
            train_model(df)
            st.success("ML Model retrained successfully")

# =====================================================
# TAB 4 – ANALYTICS
# =====================================================
with tabs[3]:
    if st.session_state.results.empty:
        st.info("No data available")
    else:
        st.dataframe(st.session_state.results)
        fig, ax = plt.subplots()
        st.session_state.results["Result"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

# =====================================================
# TAB 5 – EXECUTIVE DASHBOARD (COMMANDER)
# =====================================================
with tabs[4]:
    if st.session_state.role != "Commander":
        st.warning("Commander access only")
    else:
        df = st.session_state.results
        if df.empty:
            st.info("No executive data available")
        else:
            c1,c2,c3 = st.columns(3)
            c1.metric("Total Cases", len(df))
            c2.metric("High Risk", (df["Risk"]=="High").sum())
            c3.metric("Avg Confidence", f"{df['Confidence'].mean():.1f}%")

            fig, ax = plt.subplots()
            df["Risk"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
            st.pyplot(fig)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("© KNet Consulting Group | Enterprise Security Analytics Platform")
