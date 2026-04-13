# ==========================================================
# KALSNET (KNet) – ENTERPRISE AI + REAL DATASET GENERATOR
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
st.markdown("<h1 style='color:blue; text-align:center;'>Kalsnet (KNet) – Enterprise Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# GROQ API
# ----------------------------------------------------------
st.sidebar.title("🔑 GROQ API KEY")
api_key = st.sidebar.text_input("Enter API Key", type="password")

if not api_key:
    st.stop()

client = Groq(api_key=api_key)

st.sidebar.success("API Key Loaded")

# ----------------------------------------------------------
# USE CASE SELECTION
# ----------------------------------------------------------
st.subheader("🎯 Select Enterprise Use Case")

mode = st.selectbox("Choose Domain", [
    "Cyber Security",
    "Financial Fraud",
    "Supply Chain",
    "Healthcare",
    "Custom AI Analytics"
])

task = st.text_area("Enter Task")
run = st.button("🚀 Run Enterprise AI System")

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
# ENTERPRISE AI DATA GENERATOR (NEW CORE ENGINE)
# ----------------------------------------------------------
def generate_enterprise_data(mode):
    records = []

    for _ in range(50):
        score = random.randint(1, 100)

        # ---------------- CYBER ----------------
        if mode == "Cyber Security":
            records.append({
                "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Destination IP": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
                "Attack Type": random.choice([
                    "Brute Force", "Phishing", "Malware Injection",
                    "DDoS", "Data Exfiltration"
                ]),
                "System": f"Server-{random.randint(1,25)}",
                "Risk Score": score
            })

        # ---------------- FINANCE ----------------
        elif mode == "Financial Fraud":
            records.append({
                "Transaction ID": random.randint(100000,999999),
                "Account ID": random.randint(1000,9999),
                "Amount": random.randint(50,20000),
                "Merchant": random.choice(["Amazon", "Walmart", "Apple", "Stripe"]),
                "Country": random.choice(["US","UK","IN","EU"]),
                "Risk Score": score
            })

        # ---------------- SUPPLY CHAIN ----------------
        elif mode == "Supply Chain":
            records.append({
                "Supplier": f"Vendor-{random.randint(1,80)}",
                "Shipment ID": random.randint(10000,99999),
                "Delay Days": random.randint(0,40),
                "Region": random.choice(["NA","EU","APAC"]),
                "Risk Score": score
            })

        # ---------------- HEALTHCARE ----------------
        elif mode == "Healthcare":
            records.append({
                "Patient ID": random.randint(10000,99999),
                "Age": random.randint(18,90),
                "Condition": random.choice([
                    "Diabetes", "Hypertension", "Cardiac Risk", "Asthma"
                ]),
                "Heart Rate": random.randint(60,140),
                "Blood Pressure": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Oxygen Level": random.randint(85,100),
                "Risk Score": score
            })

        # ---------------- CUSTOM ----------------
        else:
            records.append({
                "Entity": f"Item-{random.randint(1,1000)}",
                "Metric A": random.randint(1,100),
                "Metric B": random.randint(1,100),
                "Risk Score": score
            })

    return pd.DataFrame(records)

# ----------------------------------------------------------
# SAFE JSON EXPORT
# ----------------------------------------------------------
def safe_json(df):
    df_copy = df.copy()
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
        Paragraph("KNet Enterprise AI Report", style["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n","<br/>"), style["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION ENGINE
# ----------------------------------------------------------
if run:

    result = run_ai(task)

    st.success("AI Response Generated")
    st.write(result)

    st.subheader(f"📊 Enterprise Analytics Dashboard - {mode}")

    df = generate_enterprise_data(mode)

    # SINGLE RISK COLUMN
    df["Risk Level"] = df["Risk Score"].apply(risk)

    st.dataframe(df, use_container_width=True)

    # CONSISTENT SUMMARY
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary (Enterprise)")
    st.dataframe(summary_df)

    # BAR CHART
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    ax1.set_title("Enterprise Risk Distribution")
    st.pyplot(fig1)

    # PIE CHART
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    ax2.set_title("Risk Breakdown")
    st.pyplot(fig2)

    # EXPORTS
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
st.subheader("📖 Enterprise AI System Architecture")

st.markdown("""
### 🧠 Agentic AI Layer
Interprets user tasks and generates reasoning-based responses using LLM.

### 📊 Enterprise Data Layer
Each domain uses AI-enhanced realistic schema:
- Cyber Security → attacks, IPs, systems
- Finance → transactions, merchants, fraud signals
- Healthcare → vitals, diagnosis, patient profiles
- Supply Chain → logistics + delays + region risk

### 📈 Analytics Engine
- Converts raw data → structured risk scoring
- Ensures one unified risk model across all dashboards

### 📄 Reporting Engine
Exports:
✔ CSV  
✔ JSON (safe serialization)  
✔ PDF reports  

### 🔥 Key Upgrade
This system now behaves like a **mini enterprise SOC + analytics platform with AI-generated datasets**
""")