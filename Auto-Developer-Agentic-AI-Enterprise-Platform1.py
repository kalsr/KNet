

# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (ULTIMATE FIX)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import os

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
# 🔥 MANUAL SECRETS LOADER (KEY FIX)
# ----------------------------------------------------------
def load_secrets_file():
    try:
        path = ".streamlit/secrets.toml"
        if os.path.exists(path):
            with open(path, "r") as f:
                for line in f:
                    if "GROQ_API_KEY" in line:
                        return line.split("=")[1].strip().strip('"')
    except Exception as e:
        st.warning(f"Manual secrets load error: {e}")
    return None

# ----------------------------------------------------------
# ✅ ROBUST KEY LOADER (3 LEVELS)
# ----------------------------------------------------------
@st.cache_resource
def init_client():

    api_key = None

    # 1️⃣ Try Streamlit secrets
    try:
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
    except:
        pass

    # 2️⃣ Try manual file read (CRITICAL FIX)
    if not api_key:
        api_key = load_secrets_file()

    # 3️⃣ Try environment variable
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)

client = init_client()

# ----------------------------------------------------------
# DEBUG PANEL
# ----------------------------------------------------------
with st.expander("🔍 Debug: GROQ Key Status", expanded=True):
    try:
        st.write("st.secrets keys:", list(st.secrets.keys()))
    except:
        st.write("st.secrets not accessible")

    st.write("Manual file exists:", os.path.exists(".streamlit/secrets.toml"))
    st.write("Env key exists:", bool(os.getenv("GROQ_API_KEY")))
    st.write("Client initialized:", client is not None)

# ----------------------------------------------------------
# HARD STOP
# ----------------------------------------------------------
if client is None:
    st.error("""
❌ GROQ API Key STILL NOT FOUND

ROOT CAUSE:
Your runtime cannot access secrets.toml

FIX OPTIONS:

1. Make sure file is EXACT path:
   .streamlit/secrets.toml

2. Ensure file is INCLUDED in repo (not ignored)

3. If using Streamlit Cloud:
   → MUST add secrets in App Settings UI

4. If local:
   → Run from project root folder

""")
    st.stop()

# ----------------------------------------------------------
# MODEL
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# UI
# ----------------------------------------------------------
use_cases = ["Cyber Defense Monitoring", "Financial Fraud Detection", "Smart City Monitoring"]

mode = st.selectbox("Select Use Case", use_cases)
task = st.text_area("Enter Task")
run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE
# ----------------------------------------------------------
def run_ai(task):
    try:
        res = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": "You are a senior enterprise AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.6,
            max_tokens=900
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"

# ----------------------------------------------------------
# DATA ENGINE
# ----------------------------------------------------------
def generate_data():
    data = []
    for _ in range(30):
        data.append({
            "Entity": random.choice(["Server", "API", "Firewall"]),
            "Risk Score": random.randint(1,100)
        })
    return pd.DataFrame(data)

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:
    st.subheader("AI Reasoning Output")
    st.write(run_ai(task))

    df = generate_data()
    st.dataframe(df)