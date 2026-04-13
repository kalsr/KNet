# ==========================================================
# KALSNET (KNet) – TRUE AGENTIC AI PLATFORM
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
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center; font-weight:bold;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center; font-weight:bold;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center; font-weight:bold;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# AGENTIC AI EXPLANATION (BLUE)
# ----------------------------------------------------------
st.markdown("""
<div style='color:blue; font-weight:bold;'>

Agentic AI is an intelligent system that autonomously performs reasoning, decision-making, analytics, and task execution.

Autonomous AI: Executes tasks independently using AI models.  
Analytics Engine: Processes enterprise data into insights and risk scores.  
Reporting Engine: Generates dashboards and exports (CSV, JSON, PDF).

</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ KEY
# ----------------------------------------------------------
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except:
    st.error("❌ GROQ API Key missing in secrets.toml")
    st.stop()

# ----------------------------------------------------------
# USE CASES (20 AGENTS)
# ----------------------------------------------------------
use_cases = [
    "Cyber Defense Monitoring","Financial Fraud Detection","Healthcare Risk Analytics",
    "Supply Chain Risk","Insider Threat Detection","Cloud Security Monitoring",
    "API Security Analytics","Identity & Access Management","Threat Intelligence Analysis",
    "Network Anomaly Detection","SOC Operations Dashboard","Banking Risk Analytics",
    "Insurance Claim Fraud","Retail Fraud Detection","IoT Security Monitoring",
    "Fraud Detection in Payments","Critical Infrastructure Protection",
    "AI-driven Incident Response","Predictive Maintenance","Smart City Security",
    "Other (Enter Your Own)"
]

st.subheader(" Select Agent")
selected = st.selectbox("Choose Agentic AI Use Case", use_cases)

custom = ""
if selected == "Other (Enter Your Own)":
    custom = st.text_input("Enter Custom Agent Task")

mode = custom if custom else selected

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area(" Enter Mission / Task for Agent")
run = st.button(" Execute Agent")

# ----------------------------------------------------------
# AI BRAIN
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
# DATA GENERATOR
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(50):
        score = random.randint(1,100)

        if "Cyber" in mode:
            data.append({
                "IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Attack": random.choice(["DDoS","Phishing","Malware"]),
                "Score": score
            })

        elif "Financial" in mode:
            data.append({
                "Transaction": random.randint(10000,99999),
                "Amount": random.randint(10,20000),
                "Merchant": random.choice(["Amazon","Stripe"]),
                "Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Patient": random.randint(1000,9999),
                "Heart Rate": random.randint(60,140),
                "Oxygen": random.randint(85,100),
                "Score": score
            })

        else:
            data.append({
                "Entity": mode,
                "Value": random.randint(1,100),
                "Score": score
            })

    df = pd.DataFrame(data)
    df["Risk Level"] = df["Score"].apply(risk)
    return df

# ----------------------------------------------------------
# AGENT ACTION ENGINE (NEW CORE)
# ----------------------------------------------------------
def run_agent_logic(mode, df):

    if "Cyber" in mode:
        threats = df[df["Risk Level"].isin(["High Risk","Critical"])]
        return f" Detected {len(threats)} potential cyber threats. Blocking suspicious IPs."

    elif "Financial" in mode:
        fraud = df[df["Risk Level"] == "Critical"]
        return f" Flagged {len(fraud)} fraudulent transactions. Initiating review."

    elif "Healthcare" in mode:
        patients = df[df["Risk Level"].isin(["High Risk","Critical"])]
        return f" {len(patients)} high-risk patients detected. Alerting medical staff."

    elif "Supply Chain" in mode:
        delays = df[df["Risk Level"].isin(["High Risk","Critical"])]
        return f" {len(delays)} shipment risks detected. Escalating logistics."

    else:
        return " Agent executed task and analyzed operational data."

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
        Paragraph("KNet AI Report", styles["Title"]),
        Spacer(1,12),
        Paragraph(text, styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader(" AI Reasoning Engine Output")
    ai_result = run_ai(task)
    st.write(ai_result)

    # DATA
    df = generate_data(mode)

    # AGENT ACTION
    st.subheader(" Agent Execution Result")
    action_result = run_agent_logic(mode, df)
    st.success(action_result)

    # DASHBOARD
    st.subheader(f" Analytics Dashboard - {mode}")
    st.dataframe(df)

    # SHOW ROWS BY RISK
    st.subheader(" Risk Breakdown (Rows)")
    for level in ["Low Risk","Medium Risk","High Risk","Critical"]:
        st.markdown(f"### {level}")
        st.dataframe(df[df["Risk Level"] == level])

    # SUMMARY
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader(" Risk Distribution Summary")
    st.dataframe(summary_df)

    # CHARTS
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # EXPORTS
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(ai_result + "\n" + action_result), "report.pdf")