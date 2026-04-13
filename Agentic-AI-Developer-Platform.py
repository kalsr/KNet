# ==========================================================
# KALSNET (KNet) – FIXED GROQ KEY RESOLUTION VERSION
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
# 🔐 GROQ KEY FIX (ROBUST MULTI-SOURCE LOADER)
# ----------------------------------------------------------
def get_groq_key():
    # 1. Streamlit UI input (MOST RELIABLE)
    if "ui_key" in st.session_state and st.session_state.ui_key:
        return st.session_state.ui_key

    # 2. Environment variable
    env_key = os.getenv("GROQ_API_KEY")
    if env_key:
        return env_key

    # 3. Streamlit secrets (optional fallback)
    try:
        if hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except:
        pass

    return None


st.sidebar.subheader(" Groq API Key (Required)")
st.session_state.ui_key = st.sidebar.text_input(
    "Enter GROQ API Key",
    type="password"
)

api_key = get_groq_key()

if not api_key:
    st.error("❌ GROQ API Key not found. Please enter it in the sidebar.")
    st.stop()

client = Groq(api_key=api_key)

st.sidebar.success(" API Key Loaded Successfully")

# ----------------------------------------------------------
# MODEL (UPDATED)
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# USE CASES (20)
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

custom = ""
if selected_use_case == "Custom Use Case":
    custom = st.text_input("Enter Custom Use Case")

mode = custom if custom else selected_use_case

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task")
run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": task}],
            temperature=0.7,
            max_tokens=800
        )
        return res.choices[0].message.content
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
# DATA GENERATOR (USE CASE DEPENDENT)
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(60):
        score = random.randint(1, 100)

        if "Cyber" in mode:
            data.append({
                "Entity": random.choice(["Firewall", "Server", "Endpoint", "API"]),
                "Event": random.choice(["Login", "Scan", "DDoS", "Malware"]),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Score": score
            })

        elif "Financial" in mode:
            data.append({
                "Transaction ID": random.randint(10000, 99999),
                "Amount": random.randint(50, 20000),
                "Merchant": random.choice(["Amazon", "Apple", "Stripe"]),
                "Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Patient ID": random.randint(1000, 9999),
                "Heart Rate": random.randint(60, 140),
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
# SAFE JSON FIX
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
        Paragraph("KNet Agentic Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader(" AI Output")
    result = run_ai(task)
    st.write(result)

    st.subheader(f" Dashboard - {mode}")

    df = generate_data(mode)
    st.dataframe(df, use_container_width=True)

    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader(" Risk Distribution")
    st.dataframe(summary_df)

    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(result), "report.pdf")
