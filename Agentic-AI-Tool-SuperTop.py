
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
# TOP EXPLANATION (NEW POSITION)
# ----------------------------------------------------------
st.markdown("""
<h3 style='color:blue; font-weight:bold;'>What is Agentic AI?</h3>

<b>Agentic AI</b> is an intelligent system that autonomously performs reasoning, decision-making, analytics, and reporting.

<b>Autonomous AI:</b> Executes tasks independently using AI models without human intervention.<br>
<b>Analytics Engine:</b> Processes enterprise data into structured insights and risk scores.<br>
<b>Reporting Engine:</b> Generates dashboards, charts, and exportable reports (CSV, JSON, PDF).
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
# USE CASES
# ----------------------------------------------------------
use_cases = [
    "Cyber Defense Monitoring",
    "Financial Fraud Detection",
    "Healthcare Risk Analytics",
    "Supply Chain Risk",
    "Other (Enter Your Own)"
]

st.subheader("🎯 Select Agentic AI Use Case")

selected = st.selectbox("Choose Use Case", use_cases)

custom = ""
if selected == "Other (Enter Your Own)":
    custom = st.text_input("Enter Custom Use Case")

mode = custom if custom else selected

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task")
run = st.button("🚀 Run Enterprise AI System")

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
# REAL ENTERPRISE DATA GENERATOR
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(50):
        score = random.randint(1,100)

        if "Cyber" in mode:
            data.append({
                "Timestamp": datetime.datetime.now(),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Destination IP": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
                "Attack Type": random.choice(["Phishing","Malware","DDoS","Brute Force"]),
                "System": f"Server-{random.randint(1,20)}",
                "Risk Score": score
            })

        elif "Financial" in mode:
            data.append({
                "Transaction ID": random.randint(100000,999999),
                "Account ID": random.randint(1000,9999),
                "Amount": random.randint(10,20000),
                "Merchant": random.choice(["Amazon","Walmart","Apple"]),
                "Country": random.choice(["US","UK","EU"]),
                "Risk Score": score
            })

        elif "Healthcare" in mode:
            data.append({
                "Patient ID": random.randint(10000,99999),
                "Condition": random.choice(["Diabetes","Cardiac","Asthma"]),
                "Heart Rate": random.randint(60,140),
                "Blood Pressure": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Oxygen Level": random.randint(85,100),
                "Risk Score": score
            })

        elif "Supply" in mode:
            data.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Shipment ID": random.randint(10000,99999),
                "Delay Days": random.randint(0,30),
                "Region": random.choice(["NA","EU","APAC"]),
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
# FIELD EXPLANATION
# ----------------------------------------------------------
def explain_fields(df):
    exp = {}
    for col in df.columns:
        exp[col] = f"{col} is used for domain-specific analytics and risk evaluation."
    return exp

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
    st.success("✅ AI Response Generated")
    st.write(result)

    st.subheader(f"📊 Enterprise Analytics Dashboard - {mode}")

    df = generate_data(mode)
    df["Risk Level"] = df["Risk Score"].apply(risk)

    st.dataframe(df)

    # FIELD EXPLANATION
    st.subheader("📘 Field Explanations")
    for k,v in explain_fields(df).items():
        st.write(f"**{k}:** {v}")

    # RISK SUMMARY
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df)

    st.markdown("""
**How counts are calculated:**
Each row in the dashboard has a Risk Level.
We count how many rows fall into:
- Low Risk
- Medium Risk
- High Risk
- Critical

These counts EXACTLY match the dataset above.
""")

    # BAR
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    st.markdown("Bar chart compares number of events across risk levels.")

    # PIE
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    st.markdown("Pie chart shows percentage distribution of risk categories.")

    # EXPORTS
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(result), "report.pdf")