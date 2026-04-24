# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (FINAL)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# TOML loader
try:
    import tomllib
except:
    import tomli as tomllib

# ----------------------------------------------------------
# CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("""
<h1 style='color:blue; text-align:center; font-weight:bold;'>
Kalsnet (KNet) – Agentic AI Platform
</h1>
<h3 style='color:blue; text-align:center; font-weight:bold;'>
Autonomous AI + Analytics + Reporting Engine
</h3>
<h4 style='color:blue; text-align:center; font-weight:bold;'>
Developed by Randy Singh
</h4>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# 🔐 LOAD API KEY (CLEAN + SAFE)
# ----------------------------------------------------------
def load_api_key():
    key = None

    # 1. Streamlit secrets
    try:
        key = st.secrets.get("GROQ_API_KEY")
    except:
        pass

    # 2. Local TOML
    if not key and os.path.exists(".streamlit/secrets.toml"):
        try:
            with open(".streamlit/secrets.toml", "rb") as f:
                data = tomllib.load(f)
                key = data.get("GROQ_API_KEY")
        except:
            pass

    # 3. Env fallback
    if not key:
        key = os.getenv("GROQ_API_KEY")

    # 🔥 CRITICAL CLEANUP (fixes 401)
    if key:
        key = key.strip().replace('"', '').replace("'", "")

    return key

# ----------------------------------------------------------
# INIT CLIENT
# ----------------------------------------------------------
@st.cache_resource
def init_client():
    key = load_api_key()
    if not key or not key.startswith("gsk_"):
        return None
    return Groq(api_key=key)

client = init_client()

if client is None:
    st.error("❌ Invalid or missing GROQ API key. Verify secrets.toml.")
    st.stop()

# ----------------------------------------------------------
# MODEL (SAFE CHOICE)
# ----------------------------------------------------------
GROQ_MODEL = "llama3-70b-8192"

# ----------------------------------------------------------
# USE CASES (ALL 20)
# ----------------------------------------------------------
use_cases = [
    "Cyber Defense Monitoring","Financial Fraud Detection","Healthcare Risk Analytics",
    "Supply Chain Risk","Insider Threat Detection","Cloud Security Monitoring",
    "API Security Analytics","Identity & Access Management","Threat Intelligence Analysis",
    "Network Anomaly Detection","SOC Operations Dashboard","Banking Risk Analytics",
    "Insurance Fraud Detection","Retail Fraud Detection","IoT Security Monitoring",
    "Payment Fraud Detection","Critical Infrastructure Protection",
    "Incident Response Automation","Predictive Maintenance","Smart City Monitoring",
    "Custom Use Case"
]

st.subheader("Select Agentic AI Use Case")
selected = st.selectbox("Choose Use Case", use_cases)

custom = ""
if selected == "Custom Use Case":
    custom = st.text_input("Enter Custom Use Case")

mode = custom if custom else selected

task = st.text_area("Enter Task for Agent")
run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        r = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are an enterprise AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.5,
            max_tokens=700
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

# ----------------------------------------------------------
# DATA ENGINE
# ----------------------------------------------------------
def risk(score):
    if score < 25: return "Low"
    elif score < 50: return "Medium"
    elif score < 75: return "High"
    return "Critical"

def generate_data(mode):
    rows = []
    for _ in range(60):
        score = random.randint(1,100)
        rows.append({
            "Use Case": mode,
            "Metric": random.randint(1,100),
            "Risk Score": score,
            "Risk Level": risk(score)
        })
    return pd.DataFrame(rows)

# ----------------------------------------------------------
# PDF EXPORT
# ----------------------------------------------------------
def export_pdf(text):
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("KNet AI Report", styles["Title"]),
        Spacer(1,12),
        Paragraph(text.replace("\n","<br/>"), styles["BodyText"])
    ]
    doc.build(story)
    buf.seek(0)
    return buf

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader("AI Reasoning Output")
    result = run_ai(task)
    st.write(result)

    df = generate_data(mode)

    st.subheader("Analytics Dashboard")
    st.dataframe(df, use_container_width=True)

    summary = df["Risk Level"].value_counts()

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        ax.bar(summary.index, summary.values)
        ax.set_title("Risk Distribution")
        st.pyplot(fig)

    with col2:
        fig2, ax2 = plt.subplots()
        ax2.pie(summary.values, labels=summary.index, autopct="%1.1f%%")
        ax2.set_title("Risk Share")
        st.pyplot(fig2)

    # DOWNLOADS
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", json.dumps(df.to_dict(), indent=2), "data.json")
    st.download_button("Download PDF", export_pdf(result), "report.pdf")