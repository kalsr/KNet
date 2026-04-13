
# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (STABLE FINAL BUILD)
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
    st.warning("Please enter GROQ API Key")
    st.stop()

client = Groq(api_key=api_key)
st.sidebar.success("API Key Loaded")

# ----------------------------------------------------------
# AGENTIC AI EXPLANATION
# ----------------------------------------------------------
st.markdown("## 🤖 What is Agentic AI Platform?")

st.info("""
An Agentic AI Platform is an autonomous system that can reason, analyze data, and generate insights without constant human control.

### 🧠 Autonomous AI
Makes decisions and interprets user input intelligently.

### 📊 Analytics Engine
Processes raw structured data (cyber, finance, healthcare, etc.) into insights.

### 📄 Reporting Engine
Converts analytics into dashboards, CSV, JSON, and PDF reports.
""")

# ----------------------------------------------------------
# USE CASE SELECTION
# ----------------------------------------------------------
st.subheader("🎯 Select Use Case")

mode = st.selectbox("Choose Mode", [
    "Cyber Security",
    "Financial Fraud",
    "Supply Chain",
    "Healthcare",
    "Custom Analytics"
])

task = st.text_area("Enter Task")
run = st.button("🚀 Run AI System")

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
# DATA GENERATOR
# ----------------------------------------------------------
def generate_data(mode):
    records = []

    for _ in range(40):
        score = random.randint(1, 100)

        if mode == "Cyber Security":
            records.append({
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Event Type": random.choice(["Login", "Malware", "Phishing", "Exfiltration"]),
                "Risk Score": score
            })

        elif mode == "Financial Fraud":
            records.append({
                "Account ID": random.randint(1000,9999),
                "Transaction Amount": random.randint(100,10000),
                "Risk Score": score
            })

        elif mode == "Supply Chain":
            records.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay Days": random.randint(0,30),
                "Risk Score": score
            })

        elif mode == "Healthcare":
            records.append({
                "Patient ID": random.randint(10000,99999),
                "Risk Score": score
            })

        else:
            records.append({
                "Metric Value": score
            })

    return pd.DataFrame(records)

# ----------------------------------------------------------
# SAFE JSON EXPORT (FIXED CRASH)
# ----------------------------------------------------------
def safe_json(df):
    df_copy = df.copy()

    # convert everything to string-safe format
    df_copy = df_copy.astype(str)

    return json.dumps(df_copy.to_dict(orient="records"), indent=2)

# ----------------------------------------------------------
# PDF EXPORT
# ----------------------------------------------------------
def export_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    style = getSampleStyleSheet()

    doc.build([
        Paragraph("KNet AI Report", style["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n","<br/>"), style["BodyText"])
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

    st.subheader(f"📊 Analytics Dashboard - {mode}")

    df = generate_data(mode)

    # ------------------------------------------------------
    # RISK SCORE (SINGLE SOURCE)
    # ------------------------------------------------------
    score_col = [c for c in df.columns if "Risk Score" in c]

    if score_col:
        score_col = score_col[0]
        df["Risk Level"] = df[score_col].apply(risk)
    else:
        df["Risk Level"] = df.iloc[:, -1].apply(risk)

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # RISK SUMMARY (CONSISTENT)
    # ------------------------------------------------------
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"], fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("⬇️ CSV Export", df.to_csv(index=False), "data.csv")

    st.download_button(
        "⬇️ JSON Export",
        safe_json(df),
        "data.json",
        mime="application/json"
    )

    st.download_button(
        "⬇️ PDF Export",
        export_pdf(result),
        "report.pdf"
    )

# ----------------------------------------------------------
# FOOTER EXPLANATION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 How System Works")

st.markdown("""
### 🧠 Agentic AI Flow
User input → AI reasoning → response generation

### 📊 Analytics Engine
Same dataset is used for:
- Dashboard table
- Risk summary
- Charts

✔ Ensures 100% consistency

### 📄 Reporting Engine
Exports:
- CSV
- JSON (fixed safe serialization)
- PDF report
""")