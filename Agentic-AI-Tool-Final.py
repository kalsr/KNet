# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI + CYBER RANGE SYSTEM
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
st.set_page_config(page_title="KNet Cyber AI Platform", layout="wide")

# ----------------------------------------------------------
# ACCESS CONTROL
# ----------------------------------------------------------
st.sidebar.title("🔐 Security Access")

password = st.sidebar.text_input("Enter System Password:", type="password")

if password != "knet123":
    st.warning("Access Denied")
    st.stop()

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ API
# ----------------------------------------------------------
st.sidebar.markdown("---")
api_key = st.sidebar.text_input("GROQ API Key", type="password")

if not api_key:
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------------------------------------
# MODE SELECTOR (NEW: CYBER RANGE)
# ----------------------------------------------------------
st.subheader("🎯 Select Mode")

mode = st.selectbox("Choose Mode", [
    "Agentic AI Analytics",
    "Cyber Range Simulation (NEW)",
    "Financial Fraud Simulation",
    "Supply Chain Risk",
    "Healthcare Analytics"
])

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
task = st.text_area("Enter Task")
run = st.button("🚀 Execute System")

# ----------------------------------------------------------
# AI FUNCTION
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": task}],
            max_tokens=800
        )
        return res.choices[0].message.content
    except:
        return None

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
# CYBER RANGE ATTACK ENGINE (NEW)
# ----------------------------------------------------------
def cyber_attack_generator():
    attack_types = ["Brute Force", "Malware Injection", "Phishing", "Data Exfiltration", "Insider Threat"]

    return {
        "Timestamp": datetime.datetime.now(),
        "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
        "Target System": f"Server-{random.randint(1,20)}",
        "Attack Type": random.choice(attack_types),
        "Payload Size": random.randint(50, 5000),
        "Severity Score": random.randint(1, 100)
    }

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_ai(task)

    if not result:
        st.error("AI failed")
        st.stop()

    st.success("AI Response")
    st.write(result)

    st.subheader(f"📊 Analytics Dashboard - {mode}")

    records = []

    # ------------------------------------------------------
    # CYBER RANGE MODE (NEW ADVANCED SYSTEM)
    # ------------------------------------------------------
    if mode == "Cyber Range Simulation (NEW)":
        for _ in range(40):
            records.append(cyber_attack_generator())

    # ------------------------------------------------------
    # FINANCIAL
    # ------------------------------------------------------
    elif mode == "Financial Fraud Simulation":
        for _ in range(40):
            records.append({
                "Account": random.randint(1000,9999),
                "Transaction Amount": random.randint(100,10000),
                "Location": random.choice(["US","UK","IN","EU"]),
                "Risk Score": random.randint(1,100)
            })

    # ------------------------------------------------------
    # SUPPLY CHAIN
    # ------------------------------------------------------
    elif mode == "Supply Chain Risk":
        for _ in range(40):
            records.append({
                "Supplier": f"Vendor-{random.randint(1,60)}",
                "Delay Days": random.randint(0,30),
                "Status": random.choice(["On-Time","Delayed","Critical Delay"]),
                "Risk Score": random.randint(1,100)
            })

    # ------------------------------------------------------
    # HEALTHCARE
    # ------------------------------------------------------
    elif mode == "Healthcare Analytics":
        for _ in range(40):
            records.append({
                "Patient ID": random.randint(10000,99999),
                "Condition": random.choice(["Stable","Risk","Critical"]),
                "Vitals Score": random.randint(1,100)
            })

    # ------------------------------------------------------
    # DEFAULT AGENTIC MODE
    # ------------------------------------------------------
    else:
        for _ in range(40):
            records.append({
                "Record": random.randint(1,1000),
                "Metric": random.randint(1,100)
            })

    df = pd.DataFrame(records)

    # detect score column
    score_col = [c for c in df.columns if "Score" in c or "Payload" in c or "Metric" in c][-1]
    df["Risk Level"] = df[score_col].apply(risk)

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # RISK SUMMARY (100% CONSISTENT FIX)
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
    # CHARTS
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    ax1.set_title("Risk Distribution")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("CSV Export", df.to_csv(index=False), "data.csv")
    st.download_button("JSON Export", json.dumps(df.to_dict(), indent=2), "data.json")

    def pdf_export(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        style = getSampleStyleSheet()

        doc.build([
            Paragraph("KNet Cyber AI Report", style["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n","<br/>"), style["BodyText"])
        ])

        buffer.seek(0)
        return buffer

    st.download_button("PDF Export", pdf_export(result), "report.pdf")

# ----------------------------------------------------------
# EXPLANATION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 System Overview")

st.markdown("""
### 🔴 Cyber Range Mode (NEW)
Simulates real-world cyber attacks:
- Brute force
- Malware injection
- Phishing
- Insider threats
- Data exfiltration

### 🛡️ AI Defense Layer
Each event is scored and classified into risk levels:
Low → Medium → High → Critical

### 📊 Analytics Engine
All dashboards are derived from SAME dataset ensuring:
✔ No mismatch  
✔ Real-time consistency  
✔ Enterprise SOC-style analytics  

### 🤖 Agentic AI Layer
Interprets user task, generates reasoning, and produces structured intelligence output.
""")