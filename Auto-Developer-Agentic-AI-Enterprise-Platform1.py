

# ==========================================================
# KALSNET (KNet) – ENTERPRISE AGENTIC AI PLATFORM (FIXED)
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center;'>KNet Agentic AI Platform</h1>", unsafe_allow_html=True)

# ----------------------------------------------------------
# ✅ ROBUST GROQ CLIENT (CACHED + FALLBACK)
# ----------------------------------------------------------
@st.cache_resource
def get_client():
    api_key = None

    # 1. Try Streamlit secrets
    try:
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    # 2. Fallback to environment variable
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    # 3. If still missing → return None
    if not api_key:
        return None

    return Groq(api_key=api_key)


client = get_client()

# ----------------------------------------------------------
# 🚨 HARD STOP + OPTIONAL UI INPUT
# ----------------------------------------------------------
if client is None:
    st.error("GROQ API Key not found.")
    manual_key = st.text_input("Enter GROQ API Key", type="password")

    if manual_key:
        client = Groq(api_key=manual_key)
    else:
        st.stop()

# ----------------------------------------------------------
# MODEL
# ----------------------------------------------------------
GROQ_MODEL = "llama-3.3-70b-versatile"

# ----------------------------------------------------------
# USE CASES
# ----------------------------------------------------------
use_cases = [
    "Cyber Defense Monitoring",
    "Financial Fraud Detection",
    "Healthcare Risk Analytics",
    "Supply Chain Risk",
    "Custom Use Case"
]

mode = st.selectbox("Select Use Case", use_cases)

if mode == "Custom Use Case":
    mode = st.text_input("Enter Custom Use Case")

task = st.text_area("Enter Task")
run = st.button("Run Agentic AI")

# ----------------------------------------------------------
# AI ENGINE (FIXED)
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
# DATA GENERATION
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

        elif "Financial" in mode:
            data.append({
                "Transaction": random.randint(1000, 9999),
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
# EXPORT FUNCTIONS
# ----------------------------------------------------------
def safe_json(df):
    return json.dumps(df.astype(str).to_dict(orient="records"), indent=2)

def export_pdf(text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    doc.build([
        Paragraph("KNet AI Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
    ])

    buffer.seek(0)
    return buffer

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    st.subheader("AI Output")
    result = run_ai(task)
    st.write(result)

    df = generate_data(mode)

    st.subheader("Analytics Data")
    st.dataframe(df)

    summary = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"],
        fill_value=0
    )

    summary_df = pd.DataFrame({
        "Risk Level": summary.index,
        "Count": summary.values
    })

    st.subheader("Risk Summary")
    st.dataframe(summary_df)

    # Charts
    fig, ax = plt.subplots()
    ax.bar(summary_df["Risk Level"], summary_df["Count"])
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    st.pyplot(fig2)

    # Downloads
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", safe_json(df), "data.json")
    st.download_button("Download PDF", export_pdf(result), "report.pdf")