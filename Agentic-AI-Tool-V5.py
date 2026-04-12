

# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (ENTERPRISE VERSION)
# Developed by Randy Singh
# ==========================================================

import streamlit as st
from groq import Groq
import pandas as pd
import json
import matplotlib.pyplot as plt
import io
import random
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# PROFESSIONAL HEADER
# ----------------------------------------------------------
st.markdown(
    "<h1 style='color:blue; font-weight:bold;'>Kalsnet (KNet) – Agentic AI Platform</h1>",
    unsafe_allow_html=True
)
st.markdown("### Developed by Randy Singh | Autonomous AI + Analytics + Reporting Engine")

# ----------------------------------------------------------
# SIDEBAR - KEY MANAGEMENT
# ----------------------------------------------------------
st.sidebar.title("🔐 GROQ API Management")

user_key = st.sidebar.text_input("Enter Your GROQ API Key:", type="password")

def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"','').replace("'","")

# Multi-user mode
if user_key:
    api_key = clean_key(user_key)
    key_source = "User Key"
else:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        key_source = "Shared Secure Key"
    except:
        api_key = None

# ----------------------------------------------------------
# KEY VALIDATION + TEST BUTTON
# ----------------------------------------------------------
if api_key:
    st.sidebar.success(f"✅ Key Loaded ({key_source})")

    if st.sidebar.button("🧠 Test Connection"):
        try:
            client = Groq(api_key=api_key)
            test = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=10
            )
            st.sidebar.success("✅ Connection Successful")
        except Exception as e:
            st.sidebar.error("❌ Connection Failed")
            st.sidebar.write(str(e))
else:
    st.warning("⚠️ Please enter a GROQ API key to proceed.")
    st.stop()

# ----------------------------------------------------------
# INIT CLIENT
# ----------------------------------------------------------
client = Groq(api_key=api_key)

# ----------------------------------------------------------
# AGENTIC AI EXPLANATION
# ----------------------------------------------------------
st.markdown("### 🤖 What is an Agentic AI Platform?")
st.info("""
An **Agentic AI Platform** is an intelligent system where AI acts autonomously to plan, analyze, and generate outcomes based on user input. 
It combines reasoning, decision-making, and execution capabilities.

This platform integrates:
- **Autonomous AI** → Executes tasks independently
- **Analytics Engine** → Generates structured insights
- **Reporting Engine** → Produces downloadable outputs (CSV, JSON, PDF)
""")

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task Input")

task = st.text_area("Enter your task (cyber analysis, report, insights):")

run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# AI EXECUTION FUNCTION
# ----------------------------------------------------------
def run_agentic_ai(task):
    models = ["llama-3.1-8b-instant"]

    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert AI analyst."},
                    {"role": "user", "content": task}
                ],
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content
        except Exception as e:
            return None

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    if not task.strip():
        st.warning("⚠️ Please enter a valid task.")
        st.stop()

    result = run_agentic_ai(task)

    if not result:
        st.error("❌ AI execution failed. Possible reasons:")
        st.markdown("""
- Invalid or expired API key  
- Rate limit exceeded  
- GROQ service temporarily unavailable  
""")
        st.stop()

    st.success("✅ AI Response Generated")
    st.write(result)

    # ------------------------------------------------------
    # DYNAMIC ANALYTICS (FIXED ISSUE)
    # ------------------------------------------------------
    st.subheader("📊 Analytics Dashboard")

    categories = ["Low Risk", "Medium Risk", "High Risk", "Critical"]
    counts = [random.randint(5, 30) for _ in categories]

    df = pd.DataFrame({"Category": categories, "Count": counts})
    st.dataframe(df)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(df["Category"], df["Count"])
    ax1.set_title("Dynamic Risk Distribution")
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(df["Count"], labels=df["Category"], autopct="%1.1f%%")
    ax2.set_title("Risk Percentage Breakdown")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("⬇️ CSV", df.to_csv(index=False), "data.csv")
    st.download_button("⬇️ JSON", json.dumps(df.to_dict(), indent=2), "data.json")

    # PDF
    def create_pdf(text):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()

        content = [
            Paragraph("KNet AI Report", styles["Title"]),
            Spacer(1, 12),
            Paragraph(text.replace("\n", "<br/>"), styles["BodyText"])
        ]

        doc.build(content)
        buffer.seek(0)
        return buffer

    st.download_button("⬇️ PDF", create_pdf(result), "report.pdf")

# ----------------------------------------------------------
# EXPLANATIONS
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 Explanation of Analytics & Charts")

st.markdown("""
### 📊 Analytics Dashboard
Previously, the dashboard showed static data. Now it dynamically simulates real-world outputs by generating varying datasets each run. 
In a production system, this would come from:
- Cyber logs
- Financial transactions
- Operational metrics

### 📈 Risk Distribution (Bar Chart)
This chart compares risk categories numerically. It helps decision-makers quickly identify:
- Which risk level dominates
- Where attention is required

### 🥧 Pie Chart
Shows proportional distribution of risks, useful for executive summaries and briefings.

### 🤖 Agentic AI Engine
The system performs:
- Task interpretation
- Autonomous reasoning
- Output generation
- Structured analytics creation
- Report export

This mimics real enterprise AI systems used in cybersecurity, defense, and analytics platforms.
""")