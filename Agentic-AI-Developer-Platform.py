# ==========================================================
# KALSNET (KNet) – ENTERPRISE MULTI-AGENT AI PLATFORM (FIXED)
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
st.set_page_config(page_title="KNet Enterprise AI", layout="wide")

# ----------------------------------------------------------
# HEADER (BLUE)
# ----------------------------------------------------------
st.markdown("""
<h1 style='color:blue; text-align:center; font-weight:bold;'>
Kalsnet (KNet) – Enterprise Multi-Agent AI Platform
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
# 🔐 SAFE GROQ KEY HANDLING (FIXED)
# ----------------------------------------------------------
st.sidebar.title("🔐 GROQ API KEY")

user_key = st.sidebar.text_input("Enter API Key (optional)", type="password")

def clean_key(k):
    if not k:
        return None
    return k.strip().replace("\n", "").replace("\r", "").replace('"', '').replace("'", '')

api_key = None

# 1. USER INPUT KEY (HIGHEST PRIORITY)
if user_key:
    api_key = clean_key(user_key)

# 2. FALLBACK: secrets.toml
if not api_key:
    try:
        api_key = st.secrets.get("GROQ_API_KEY", None)
    except Exception:
        api_key = None

# 3. FINAL CHECK
if not api_key:
    st.error("❌ GROQ API Key not found. Please enter it in sidebar or .streamlit/secrets.toml")
    st.stop()

# INIT CLIENT
client = Groq(api_key=api_key)

st.sidebar.success("✅ Groq API Key Loaded Successfully")

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
    "Identity Access Management",
    "Threat Intelligence Analysis",
    "Network Anomaly Detection",
    "SOC Operations Dashboard",
    "Banking Fraud Analytics",
    "Insurance Fraud Detection",
    "Retail Fraud Detection",
    "IoT Security Monitoring",
    "Stock Market Risk",
    "Crypto Risk Intelligence",
    "Energy Grid Monitoring",
    "Government Security Intelligence",
    "Custom Use Case"
]

st.subheader("🎯 Select Agentic AI Use Case")
selected = st.selectbox("Choose Agent", use_cases)

custom = ""
if selected == "Custom Use Case":
    custom = st.text_input("Enter your custom use case")

mode = custom if custom else selected

task = st.text_area("Enter Task for Agent")
run = st.button("🚀 Run Agent")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": task}],
            max_tokens=600
        )
        return res.choices[0].message.content
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
    else:
        return "Critical"

# ----------------------------------------------------------
# DATA GENERATOR (AGENT BASED)
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(60):
        score = random.randint(1, 100)

        if "Cyber" in mode:
            row = {
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Attack Type": random.choice(["DDoS","Phishing","Malware","SQLi"]),
                "Asset": f"Server-{random.randint(1,50)}",
                "Risk Score": score
            }

        elif "Financial" in mode:
            row = {
                "Transaction ID": random.randint(10000,99999),
                "Amount": random.randint(10,20000),
                "Merchant": random.choice(["Amazon","Apple","Stripe","Walmart"]),
                "Country": random.choice(["US","UK","IN"]),
                "Risk Score": score
            }

        elif "Healthcare" in mode:
            row = {
                "Patient ID": random.randint(1000,9999),
                "Heart Rate": random.randint(60,140),
                "Oxygen": random.randint(85,100),
                "BP": f"{random.randint(110,160)}/{random.randint(70,100)}",
                "Risk Score": score
            }

        else:
            row = {
                "Entity": mode,
                "Metric": random.randint(1,100),
                "Risk Score": score
            }

        data.append(row)

    df = pd.DataFrame(data)
    df["Risk Level"] = df["Risk Score"].apply(risk)
    return df

# ----------------------------------------------------------
# EXPORT HELPERS
# ----------------------------------------------------------
def safe_json(df):
    return json.dumps(df.astype(str).to_dict(orient="records"), indent=2)

def export_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNet Enterprise Report", styles["Title"]),
        Spacer(1, 10),
        Paragraph(text.replace("\n","<br/>"), styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader("🧠 AI Reasoning Output")
    ai_result = run_ai(task)
    st.write(ai_result)

    df = generate_data(mode)

    st.subheader(f"📊 Enterprise Dashboard – {mode}")
    st.dataframe(df, use_container_width=True)

    # RISK SUMMARY (ALWAYS CONSISTENT)
    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk","Medium Risk","High Risk","Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df)

    # BAR CHART
    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    ax.set_title("Risk Distribution")
    st.pyplot(fig)

    # PIE CHART
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # EXPORTS
    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")
    st.download_button("PDF", export_pdf(ai_result), "report.pdf")

# ----------------------------------------------------------
# FOOTER
# ----------------------------------------------------------
st.markdown("---")
st.markdown("""
### 🧠 System Status
- Agentic AI: Active
- Risk Engine: Operational
- Analytics: Real-time
- Data Mode: Synthetic Enterprise Simulation
""")