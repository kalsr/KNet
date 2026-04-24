# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (FINAL CLEAN)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import os

# ✅ Proper TOML parser (IMPORTANT FIX)
try:
    import tomllib  # Python 3.11+
except:
    import tomli as tomllib

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
<h3 style='color:blue; text-align:center; font-weight:bold;'>
Autonomous AI + Analytics + Reporting Engine
</h3>
<h4 style='color:blue; text-align:center; font-weight:bold;'>
Developed by Randy Singh
</h4>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# ✅ SAFE SECRETS LOADER (NO STRING PARSING)
# ----------------------------------------------------------
def load_api_key():

    # 1. Try Streamlit secrets
    try:
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except:
        pass

    # 2. Try reading TOML properly
    try:
        if os.path.exists(".streamlit/secrets.toml"):
            with open(".streamlit/secrets.toml", "rb") as f:
                data = tomllib.load(f)
                return data.get("GROQ_API_KEY")
    except:
        pass

    # 3. Fallback env
    return os.getenv("GROQ_API_KEY")

# ----------------------------------------------------------
# INIT CLIENT (CACHED)
# ----------------------------------------------------------
@st.cache_resource
def init_client():
    key = load_api_key()

    if not key:
        return None

    return Groq(api_key=key.strip())

client = init_client()

# ----------------------------------------------------------
# HARD STOP
# ----------------------------------------------------------
if client is None:
    st.error("❌ GROQ API Key not found. Check .streamlit/secrets.toml")
    st.stop()

# ----------------------------------------------------------
# MODEL
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# ✅ FULL 20 USE CASES RESTORED
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
# AI ENGINE
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
# DATA GENERATOR
# ----------------------------------------------------------
def generate_data(mode):
    data = []

    for _ in range(50):
        score = random.randint(1, 100)

        if "Cyber" in mode:
            data.append({
                "Entity": random.choice(["Firewall", "Server", "API"]),
                "Event": random.choice(["Login", "DDoS", "Malware"]),
                "Risk Score": score
            })

        elif "Financial" in mode or "Banking" in mode:
            data.append({
                "Transaction ID": random.randint(1000, 9999),
                "Amount": random.randint(50, 5000),
                "Risk Score": score
            })

        else:
            data.append({
                "Entity": mode,
                "Value": random.randint(1, 100),
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

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader("AI Reasoning Output")
    result = run_ai(task)
    st.write(result)

    df = generate_data(mode)

    st.subheader(f"Enterprise Analytics Dashboard - {mode}")
    st.dataframe(df)

    summary = df["Risk Level"].value_counts()

    st.subheader("Risk Summary")
    st.write(summary)

    fig, ax = plt.subplots()
    ax.bar(summary.index, summary.values)
    st.pyplot(fig)

    st.download_button("CSV", df.to_csv(index=False), "data.csv")
    st.download_button("JSON", safe_json(df), "data.json")