

# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (ADVANCED)
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
# GROQ KEY FROM TOML (FIXED)
# ----------------------------------------------------------
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except:
    st.error("❌ GROQ API Key not found in secrets.toml")
    st.stop()

# ----------------------------------------------------------
# USE CASES (15 + CUSTOM)
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
    "Other (Enter Your Own)"
]

st.subheader(" Select Agentic AI Use Case")

selected_use_case = st.selectbox("Choose Use Case", use_cases)

custom_use_case = ""
if selected_use_case == "Other (Enter Your Own)":
    custom_use_case = st.text_input("Enter Custom Use Case")

mode = custom_use_case if custom_use_case else selected_use_case

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
            model="llama3-8b-8192",
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
    records = []
    for _ in range(50):
        score = random.randint(1, 100)

        records.append({
            "Entity": mode,
            "Metric A": random.randint(1,100),
            "Metric B": random.randint(1,100),
            "Risk Score": score
        })

    return pd.DataFrame(records)

# ----------------------------------------------------------
# FIELD EXPLANATION ENGINE
# ----------------------------------------------------------
def explain_fields(df):
    explanations = {}
    for col in df.columns:
        if col == "Risk Score":
            explanations[col] = "Numerical score (1–100) representing severity of event."
        elif col == "Risk Level":
            explanations[col] = "Categorical classification derived from Risk Score."
        else:
            explanations[col] = f"{col} represents key operational data used for analysis."

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
        Paragraph(text.replace("\n","<br/>"), styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_ai(task)
    st.success("AI Response Generated")
    st.write(result)

    st.subheader(f" Enterprise Analytics Dashboard - {mode}")

    df = generate_data(mode)
    df["Risk Level"] = df["Risk Score"].apply(risk)

    st.dataframe(df, use_container_width=True)

    # FIELD EXPLANATIONS
    st.subheader(" Field Explanations")
    field_info = explain_fields(df)
    for k, v in field_info.items():
        st.write(f"**{k}:** {v}")

    # RISK SUMMARY
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
### Why Risk Distribution?
This summarizes all events by severity:
- Low → Normal
- Medium → Suspicious
- High → Serious threat
- Critical → Immediate action required

Counts EXACTLY match dashboard totals.
""")

    # BAR CHART
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    st.markdown(" Bar Chart shows comparison of number of events across risk levels.")

    # PIE CHART
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    st.markdown(" Pie Chart shows percentage distribution of risk categories.")

    # EXPORTS
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(result), "report.pdf")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.markdown("---")
st.subheader(" Agentic AI Explanation")

st.markdown("""
###  Autonomous AI
Makes independent decisions and generates outputs.

###  Analytics Engine
Processes enterprise data into structured insights.

###  Reporting Engine
Generates dashboards, charts, and downloadable reports.

###  Agentic AI
Combines all above components into a self-operating intelligent system.
""")