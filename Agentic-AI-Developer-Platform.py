# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (FIXED + ROBUST)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import datetime
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='color:blue; text-align:center; font-weight:bold;'>
Autonomous AI + Analytics + Reporting Engine
</h3>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='color:blue; text-align:center; font-weight:bold;'>
Developed by Randy Singh
</h4>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# SAFE GROQ KEY LOADER (FIXED)
# ----------------------------------------------------------
def load_groq_key():
    # 1. Streamlit secrets (PRIMARY)
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    # 2. Environment fallback
    return os.getenv("GROQ_API_KEY", None)

api_key = load_groq_key()

if not api_key:
    st.error("❌ GROQ API Key missing. Please add it to .streamlit/secrets.toml")
    st.code('GROQ_API_KEY = "gsk_your_key_here"')
    st.stop()

client = Groq(api_key=api_key)

st.sidebar.success(" Groq API Key Loaded Successfully")

# ----------------------------------------------------------
# UPDATED MODEL (FIXED DEPRECATION ERROR)
# ----------------------------------------------------------
GROQ_MODEL = "llama3-70b-8192"  # valid current model (or llama3-8b-8192)

# ----------------------------------------------------------
# USE CASES (20 + CUSTOM)
# ----------------------------------------------------------
use_cases = [
    "Cyber Defense Monitoring",
    "Financial Fraud Detection",
    "Healthcare Risk Analytics",
    "Supply Chain Risk",
    "Insider Threat Detection",
    "Cloud Security Monitoring",
    "API Security Analytics",
    "Identity & Access Management",
    "Threat Intelligence Analysis",
    "Network Anomaly Detection",
    "SOC Operations Dashboard",
    "Banking Risk Analytics",
    "Insurance Fraud Detection",
    "Retail Fraud Detection",
    "IoT Security Monitoring",
    "Payment Fraud Detection",
    "Critical Infrastructure Protection",
    "Incident Response Automation",
    "Predictive Maintenance",
    "Smart City Monitoring",
    "Custom Use Case"
]

st.subheader(" Select Agentic AI Use Case")
selected_use_case = st.selectbox("Choose Use Case", use_cases)

custom_use_case = ""
if selected_use_case == "Custom Use Case":
    custom_use_case = st.text_input("Enter your custom use case")

mode = custom_use_case if custom_use_case else selected_use_case

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task")
run = st.button(" Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE (FIXED MODEL USAGE)
# ----------------------------------------------------------
def run_ai(task):
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a senior enterprise AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

# ----------------------------------------------------------
# RISK ENGINE
# ----------------------------------------------------------
def risk(score):
    if score < 25:
        return "Low Risk"
    elif score < 50:
        return "Medium Risk"
    elif score < 75:
        return "High Risk"
    return "Critical"

# ----------------------------------------------------------
# REALISTIC DATA GENERATOR (USE CASE AWARE)
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(60):
        score = random.randint(1, 100)

        if "Cyber" in mode:
            data.append({
                "Entity": random.choice(["Firewall", "Endpoint", "Server", "API"]),
                "Event": random.choice(["Login Attempt", "Malware", "DDoS", "Scan"]),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Score": score
            })

        elif "Financial" in mode:
            data.append({
                "Entity": "Transaction",
                "Amount": random.randint(10, 20000),
                "Merchant": random.choice(["Amazon", "Apple", "Stripe"]),
                "Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Entity": "Patient",
                "Heart Rate": random.randint(60,140),
                "BP": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Score": score
            })

        else:
            data.append({
                "Entity": mode,
                "Metric": random.randint(1, 100),
                "Score": score
            })

    df = pd.DataFrame(data)
    df["Risk Level"] = df["Score"].apply(risk)
    return df

# ----------------------------------------------------------
# EXPORT SAFE JSON FIX
# ----------------------------------------------------------
def safe_json(df):
    return json.dumps(df.astype(str).to_dict(orient="records"), indent=2)

# ----------------------------------------------------------
# PDF EXPORT
# ----------------------------------------------------------
def export_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNet Enterprise Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader(" AI Reasoning Output")
    result = run_ai(task)
    st.write(result)

    st.subheader(f" Analytics Dashboard - {mode}")

    df = generate_data(mode)
    st.dataframe(df, use_container_width=True)

    # FIXED CONSISTENT RISK SUMMARY
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader(" Risk Distribution Summary (MATCHED)")
    st.dataframe(summary_df)

    # CHARTS
    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # EXPORTS
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(result), "report.pdf")