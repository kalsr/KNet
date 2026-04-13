

# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (ENHANCED)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Enterprise AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center; font-weight:bold;'>Kalsnet (KNet) – Enterprise Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center; font-weight:bold;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center; font-weight:bold;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# BLUE EXPLANATION (UPDATED)
# ----------------------------------------------------------
st.markdown("""
<h3 style='color:blue; font-weight:bold;'>What is Agentic AI?</h3>

<div style='color:blue; font-weight:bold;'>

Agentic AI is an intelligent system that autonomously performs reasoning, decision-making, analytics, and reporting.<br><br>

Autonomous AI: Executes tasks independently using AI models without human intervention.<br>
Analytics Engine: Processes enterprise data into structured insights and risk scores.<br>
Reporting Engine: Generates dashboards, charts, and exportable reports (CSV, JSON, PDF).

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ KEY
# ----------------------------------------------------------
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except:
    st.error("❌ GROQ API Key not found in secrets.toml")
    st.stop()

# ----------------------------------------------------------
# 20 USE CASES
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
    "Insurance Claim Fraud",
    "Retail Fraud Detection",
    "IoT Security Monitoring",
    "Fraud Detection in Payments",
    "Critical Infrastructure Protection",
    "AI-driven Incident Response",
    "Predictive Maintenance",
    "Smart City Security",
    "Other (Enter Your Own)"
]

st.subheader(" Select Agentic AI Use Case")
selected = st.selectbox("Choose Use Case", use_cases)

custom = ""
if selected == "Other (Enter Your Own)":
    custom = st.text_input("Enter Custom Use Case")

mode = custom if custom else selected

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task")
run = st.button(" Run Enterprise AI System")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": task}],
            max_tokens=600
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)

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
    else:
        return "Critical"

# ----------------------------------------------------------
# DATA GENERATOR (UNCHANGED CORE LOGIC)
# ----------------------------------------------------------
def generate_data(mode):
    data = []
    for _ in range(50):
        score = random.randint(1,100)

        if "Cyber" in mode:
            data.append({
                "Timestamp": datetime.datetime.now(),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Attack Type": random.choice(["Phishing","Malware","DDoS"]),
                "System": f"Server-{random.randint(1,20)}",
                "Risk Score": score
            })

        elif "Financial" in mode:
            data.append({
                "Transaction ID": random.randint(100000,999999),
                "Amount": random.randint(10,20000),
                "Merchant": random.choice(["Amazon","Walmart"]),
                "Country": random.choice(["US","UK"]),
                "Risk Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Patient ID": random.randint(10000,99999),
                "Heart Rate": random.randint(60,140),
                "Oxygen Level": random.randint(85,100),
                "Risk Score": score
            })

        else:
            data.append({
                "Entity": mode,
                "Value": random.randint(1,100),
                "Risk Score": score
            })

    return pd.DataFrame(data)

# ----------------------------------------------------------
# SAFE JSON
# ----------------------------------------------------------
def safe_json(df):
    return json.dumps(df.astype(str).to_dict(orient="records"), indent=2)

# ----------------------------------------------------------
# PDF
# ----------------------------------------------------------
def export_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNet Report", styles["Title"]),
        Spacer(1,12),
        Paragraph(text, styles["BodyText"])
    ])
    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_ai(task)
    st.success(" AI Response Generated")
    st.write(result)

    st.subheader(f" Enterprise Analytics Dashboard - {mode}")

    df = generate_data(mode)
    df["Risk Level"] = df["Risk Score"].apply(risk)

    st.dataframe(df)

    # ------------------------------------------------------
    # SHOW ROWS PER RISK CATEGORY (NEW)
    # ------------------------------------------------------
    st.subheader(" Detailed Risk Breakdown (Rows)")

    for level in ["Low Risk","Medium Risk","High Risk","Critical"]:
        st.markdown(f"### {level}")
        st.dataframe(df[df["Risk Level"] == level])

    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader(" Risk Distribution Summary")
    st.dataframe(summary_df)

    st.markdown("""
Each row in the dashboard is assigned a Risk Level.

The counts above are calculated by:
- Counting ALL rows labeled Low Risk
- Counting ALL rows labeled Medium Risk
- Counting ALL rows labeled High Risk
- Counting ALL rows labeled Critical

The detailed tables above show EXACT rows contributing to each count.
""")

    # ------------------------------------------------------
    # CHARTS
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(result), "report.pdf")