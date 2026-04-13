

# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (CONSISTENT FINAL FIX)
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
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ API KEY
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API KEY")

api_key = st.sidebar.text_input("Enter API Key", type="password")

if not api_key:
    st.warning("Enter GROQ API Key to continue")
    st.stop()

client = Groq(api_key=api_key)

st.sidebar.success("API Key Loaded")

# ----------------------------------------------------------
# AGENTIC AI EXPLANATION (FIXED + COMPLETE)
# ----------------------------------------------------------
st.markdown("## 🤖 What is Agentic AI Platform?")

st.info("""
An **Agentic AI Platform** is an intelligent system that can autonomously perform reasoning, decision-making, analytics, and reporting without constant human intervention.

### 🧠 Autonomous AI
This is the reasoning core that understands user input, makes decisions, and generates structured outputs.

### 📊 Analytics Engine
This processes raw data (cyber logs, financial transactions, operational metrics) and converts them into insights and risk scores.

### 📄 Reporting Engine
This converts analytics into human-readable outputs such as tables, dashboards, CSV, JSON, and PDF reports.
""")

# ----------------------------------------------------------
# USE CASE SELECTION
# ----------------------------------------------------------
st.subheader("🎯 Select Use Case")

mode = st.selectbox("Choose Scenario", [
    "Cyber Security Monitoring",
    "Financial Fraud Detection",
    "Supply Chain Monitoring",
    "Healthcare Risk Analytics",
    "Custom Analytics"
])

task = st.text_area("Enter Task")
run = st.button("🚀 Run Agentic AI System")

# ----------------------------------------------------------
# AI FUNCTION
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
        return f"Error: {str(e)}"

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
    else:
        return "Critical"

# ----------------------------------------------------------
# DATA GENERATION (CONSISTENT DESIGN)
# ----------------------------------------------------------
def generate_data(mode):
    records = []

    for _ in range(40):
        score = random.randint(1, 100)

        if mode == "Cyber Security Monitoring":
            records.append({
                "Timestamp": datetime.datetime.now(),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Event Type": random.choice(["Login", "Malware", "Phishing", "Exfiltration"]),
                "Risk Score": score
            })

        elif mode == "Financial Fraud Detection":
            records.append({
                "Account ID": random.randint(1000,9999),
                "Transaction Amount": random.randint(100,10000),
                "Risk Score": score
            })

        elif mode == "Supply Chain Monitoring":
            records.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay Days": random.randint(0,30),
                "Risk Score": score
            })

        elif mode == "Healthcare Risk Analytics":
            records.append({
                "Patient ID": random.randint(10000,99999),
                "Vitals Risk Score": score
            })

        else:
            records.append({
                "Metric Value": score
            })

    return pd.DataFrame(records)

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_ai(task)
    st.success("AI Response Generated")
    st.write(result)

    st.subheader(f"📊 Analytics Dashboard - {mode}")

    df = generate_data(mode)

    # ---------------- FIXED SINGLE RISK COLUMN ----------------
    score_col = [c for c in df.columns if "Score" in c]
    score_col = score_col[0] if score_col else df.columns[-1]

    df["Risk Level"] = df[score_col].apply(risk)

    st.dataframe(df, use_container_width=True)

    # ----------------------------------------------------------
    # CONSISTENT RISK SUMMARY (FIXED)
    # ----------------------------------------------------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary (Matches Dashboard Exactly)")
    st.dataframe(summary_df)

    # ----------------------------------------------------------
    # BAR CHART
    # ----------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    ax1.set_title("Risk Distribution")
    st.pyplot(fig1)

    # ----------------------------------------------------------
    # PIE CHART
    # ----------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    ax2.set_title("Risk Breakdown")
    st.pyplot(fig2)

    # ----------------------------------------------------------
    # EXPORTS
    # ----------------------------------------------------------
    st.download_button("CSV Export", df.to_csv(index=False), "data.csv")
    st.download_button("JSON Export", json.dumps(df.to_dict(), indent=2), "data.json")

    def pdf_export(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        style = getSampleStyleSheet()

        doc.build([
            Paragraph("KNet Agentic AI Report", style["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n","<br/>"), style["BodyText"])
        ])

        buffer.seek(0)
        return buffer

    st.download_button("PDF Export", pdf_export(result), "report.pdf")

# ----------------------------------------------------------
# DASHBOARD EXPLANATION (GUI LEVEL)
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 How the Dashboards Work")

st.markdown("""
### 🧠 Agentic AI System Flow
1. User selects a use case (Cyber, Finance, Healthcare, etc.)
2. System generates structured dataset for that domain
3. Each record is assigned a **Risk Score (1–100)**

### 📊 Analytics Dashboard
- Shows raw dataset
- Includes domain-specific fields (IP, transactions, patients, etc.)
- Adds computed Risk Level column

### 📈 Risk Distribution Summary
- Uses EXACT SAME Risk Level column
- Counts Low, Medium, High, Critical events
- Guarantees consistency with dashboard

### ⚠️ Key Design Rule
✔ ONE dataset  
✔ ONE risk column  
✔ ONE source of truth  

This ensures:
👉 No mismatch  
👉 No duplication  
👉 Enterprise-grade reliability  
""")