


# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (FINAL FIX)
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

# ----------------------------------------------------------
# CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER (ALWAYS VISIBLE)
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
# ✅ STABLE GROQ CLIENT (CACHED - NO FAILURES)
# ----------------------------------------------------------
@st.cache_resource
def init_client():
    try:
        api_key = st.secrets["GROQ_API_KEY"]  # STRICTLY from secrets
        return Groq(api_key=api_key)
    except Exception as e:
        return None

client = init_client()

# ----------------------------------------------------------
# 🚨 HARD STOP (NO UI INPUT, STRICT MODE)
# ----------------------------------------------------------
if client is None:
    st.error("""
❌ GROQ API Key NOT found in secrets.

✔ FIX (GitHub / Streamlit Cloud):
1. Create file: .streamlit/secrets.toml
2. Add EXACTLY:

GROQ_API_KEY = "gsk_xxxxxx"

3. Redeploy app (once)

⚠️ No manual entry allowed in this version.
""")
    st.stop()

# ----------------------------------------------------------
# MODEL
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# USE CASES
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

st.subheader("Select Agentic AI Use Case")

selected_use_case = st.selectbox("Choose Use Case", use_cases)

custom_use_case = ""
if selected_use_case == "Custom Use Case":
    custom_use_case = st.text_input("Enter Custom Use Case")

mode = custom_use_case if custom_use_case else selected_use_case

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task for Agent")
run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# ✅ AI ENGINE (CLIENT ALWAYS AVAILABLE)
# ----------------------------------------------------------
def run_ai(task):
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a senior enterprise AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.6,
            max_tokens=900
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
# DATA GENERATION
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(60):
        score = random.randint(1, 100)

        if "Cyber" in mode:
            data.append({
                "Entity": random.choice(["Firewall", "Endpoint", "Server", "API"]),
                "Event Type": random.choice(["Login", "DDoS", "Malware", "Scan"]),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Risk Score": score
            })

        elif "Financial" in mode or "Banking" in mode:
            data.append({
                "Transaction ID": random.randint(10000, 99999),
                "Amount ($)": random.randint(50, 20000),
                "Merchant": random.choice(["Amazon", "Stripe", "Apple"]),
                "Country": random.choice(["US", "UK", "IN"]),
                "Risk Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Patient ID": random.randint(1000, 9999),
                "Heart Rate": random.randint(60, 140),
                "Blood Pressure": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Oxygen Level": random.randint(85,100),
                "Risk Score": score
            })

        elif "Supply Chain" in mode:
            data.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay Days": random.randint(0,40),
                "Region": random.choice(["NA", "EU", "APAC"]),
                "Risk Score": score
            })

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
# EXPORTS
# ----------------------------------------------------------
def safe_json(df):
    return json.dumps(df.astype(str).to_dict(orient="records"), indent=2)

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

    st.subheader("AI Reasoning Output")
    result = run_ai(task)
    st.write(result)

    st.subheader(f"Enterprise Analytics Dashboard - {mode}")

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

    st.subheader("Risk Distribution Summary")
    st.dataframe(summary_df)

    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    st.download_button("CSV Export", df.to_csv(index=False), "data.csv")
    st.download_button("JSON Export", safe_json(df), "data.json")
    st.download_button("PDF Export", export_pdf(result), "report.pdf")