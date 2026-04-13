

# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM
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
# GROQ KEY (STRICTLY FROM SECRETS ONLY)
# ----------------------------------------------------------
try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("❌ GROQ API Key missing in .streamlit/secrets.toml")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------------------------------------
# MODEL (CURRENT VALID)
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# 20 AGENTIC USE CASES
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
    custom_use_case = st.text_input("Enter Custom Use Case")

mode = custom_use_case if custom_use_case else selected_use_case

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task for Agent")
run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a senior enterprise AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.6,
            max_tokens=900
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

# ----------------------------------------------------------
# RISK ENGINE (SINGLE SOURCE OF TRUTH)
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
# USE CASE SPECIFIC DATA ENGINE
# ----------------------------------------------------------
def generate_data(mode):

    data = []

    for _ in range(60):
        score = random.randint(1, 100)

        # ---------------- CYBER ----------------
        if "Cyber" in mode:
            data.append({
                "Entity": random.choice(["Firewall", "Endpoint", "Server", "API"]),
                "Event Type": random.choice(["Login", "DDoS", "Malware", "Scan"]),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Risk Score": score
            })

        # ---------------- FINANCE ----------------
        elif "Financial" in mode or "Banking" in mode:
            data.append({
                "Transaction ID": random.randint(10000, 99999),
                "Amount ($)": random.randint(50, 20000),
                "Merchant": random.choice(["Amazon", "Stripe", "Apple"]),
                "Country": random.choice(["US", "UK", "IN"]),
                "Risk Score": score
            })

        # ---------------- HEALTHCARE ----------------
        elif "Healthcare" in mode:
            data.append({
                "Patient ID": random.randint(1000, 9999),
                "Heart Rate": random.randint(60, 140),
                "Blood Pressure": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Oxygen Level": random.randint(85,100),
                "Risk Score": score
            })

        # ---------------- SUPPLY CHAIN ----------------
        elif "Supply Chain" in mode:
            data.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay Days": random.randint(0,40),
                "Region": random.choice(["NA", "EU", "APAC"]),
                "Risk Score": score
            })

        # ---------------- DEFAULT ----------------
        else:
            data.append({
                "Entity": mode,
                "Metric Value": random.randint(1, 100),
                "Risk Score": score
            })

    df = pd.DataFrame(data)
    df["Risk Level"] = df["Risk Score"].apply(risk)
    return df

# ----------------------------------------------------------
# FIELD EXPLANATIONS ENGINE
# ----------------------------------------------------------
def explain_fields(df):

    explanations = {}

    for col in df.columns:

        if col == "Risk Score":
            explanations[col] = "Numerical value (1–100) derived from anomaly detection or rule-based scoring."
        elif col == "Risk Level":
            explanations[col] = "Categorical classification derived from Risk Score thresholds."
        elif "IP" in col:
            explanations[col] = "Network address used to trace source of activity."
        elif "Transaction" in col:
            explanations[col] = "Unique financial transaction identifier."
        elif "Amount" in col:
            explanations[col] = "Monetary value of transaction used for fraud detection."
        elif "Heart" in col:
            explanations[col] = "Physiological health metric."
        else:
            explanations[col] = "Domain-specific operational field used for analytics."

    return explanations

# ----------------------------------------------------------
# SAFE JSON
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
        Paragraph("KNet Enterprise AI Report", styles["Title"]),
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

    st.subheader(f" Enterprise Analytics Dashboard - {mode}")

    df = generate_data(mode)
    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # FIELD EXPLANATIONS
    # ------------------------------------------------------
    st.subheader(" Field-Level Explanation")
    for k, v in explain_fields(df).items():
        st.write(f"**{k}:** {v}")

    # ------------------------------------------------------
    # RISK SUMMARY (SINGLE SOURCE OF TRUTH)
    # ------------------------------------------------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader(" Risk Distribution Summary")
    st.dataframe(summary_df)

    st.markdown("""
### 📊 How Risk is Calculated
- Risk Score is generated per record (1–100)
- Low: 0–24
- Medium: 25–49
- High: 50–74
- Critical: 75–100
""")

    # ------------------------------------------------------
    # CHARTS
    # ------------------------------------------------------
    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    ax.set_title("Risk Distribution (Bar Chart)")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    ax2.set_title("Risk Distribution (Pie Chart)")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("CSV Export", df.to_csv(index=False), "data.csv")
    st.download_button("JSON Export", safe_json(df), "data.json")
    st.download_button("PDF Export", export_pdf(result), "report.pdf")