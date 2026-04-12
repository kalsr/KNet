# ==========================================================
# KALSNET (KNet) – AGENTIC AI PLATFORM (ENTERPRISE VERSION)
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
# HEADER (PROFESSIONAL)
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; font-weight:bold;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; font-weight:bold;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; font-weight:bold;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# SIDEBAR - API KEY
# ----------------------------------------------------------
st.sidebar.title("🔐 GROQ API Management")

user_key = st.sidebar.text_input("Enter Your GROQ API Key:", type="password")

def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"','').replace("'","")

# Multi-user support
if user_key:
    api_key = clean_key(user_key)
    key_source = "User Key"
else:
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        key_source = "Shared Key"
    except:
        api_key = None

if not api_key:
    st.warning("⚠️ Please enter a GROQ API key to proceed.")
    st.stop()

# ----------------------------------------------------------
# INIT CLIENT
# ----------------------------------------------------------
client = Groq(api_key=api_key)

# ----------------------------------------------------------
# KEY TEST
# ----------------------------------------------------------
st.sidebar.success(f"✅ Key Loaded ({key_source})")

if st.sidebar.button("🧠 Test Connection"):
    try:
        client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=10
        )
        st.sidebar.success("✅ Connection Successful")
    except Exception as e:
        st.sidebar.error("❌ Connection Failed")
        st.sidebar.write(str(e))

# ----------------------------------------------------------
# AGENTIC AI EXPLANATION
# ----------------------------------------------------------
st.markdown("### 🤖 What is an Agentic AI Platform?")
st.info("""
An Agentic AI Platform autonomously performs reasoning, decision-making, analytics, and reporting.

It combines:
- Autonomous AI
- Analytics Engine
- Reporting Engine
""")

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
st.subheader("🤖 Agentic AI Task Input")

task = st.text_area("Enter your task:")
run = st.button("🚀 Run Agentic AI")

# ----------------------------------------------------------
# AI FUNCTION
# ----------------------------------------------------------
def run_agentic_ai(task):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert AI analyst."},
                {"role": "user", "content": task}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception:
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
- GROQ service unavailable  
""")
        st.stop()

    st.success("✅ AI Response Generated")
    st.write(result)

    # ------------------------------------------------------
    # REALISTIC ANALYTICS DASHBOARD (FIXED)
    # ------------------------------------------------------
    st.subheader("📊 Analytics Dashboard (Cyber + Financial + Operational)")

    records = []
    event_types = ["Login Attempt", "File Access", "Malware Alert", "Network Scan", "Data Transfer"]

    for _ in range(30):
        severity = random.randint(1, 100)

        record = {
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            "Destination IP": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
            "Event Type": random.choice(event_types),
            "Data Type": random.choice(["Cyber", "Financial", "Operational"]),
            "Severity Score": severity
        }

        records.append(record)

    def classify_risk(val):
        if val < 25:
            return "Low Risk"
        elif val < 50:
            return "Medium Risk"
        elif val < 75:
            return "High Risk"
        else:
            return "Critical"

    df = pd.DataFrame(records)
    df["Risk Level"] = df["Severity Score"].apply(classify_risk)

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # CONSISTENT RISK SUMMARY
    # ------------------------------------------------------
    risk_order = ["Low Risk", "Medium Risk", "High Risk", "Critical"]

    risk_counts = df["Risk Level"].value_counts().reindex(risk_order, fill_value=0)

    summary_df = pd.DataFrame({
        "Risk Level": risk_counts.index,
        "Count": risk_counts.values
    })

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df, use_container_width=True)

    # ------------------------------------------------------
    # BAR CHART
    # ------------------------------------------------------
    fig1, ax1 = plt.subplots()
    ax1.bar(summary_df["Risk Level"], summary_df["Count"])
    ax1.set_title("Risk Distribution by Category (Low → Critical)")
    ax1.set_xlabel("Risk Category")
    ax1.set_ylabel("Number of Events")
    st.pyplot(fig1)

    # ------------------------------------------------------
    # PIE CHART
    # ------------------------------------------------------
    fig2, ax2 = plt.subplots()
    ax2.pie(summary_df["Count"], labels=summary_df["Risk Level"], autopct="%1.1f%%")
    ax2.set_title("Risk Percentage Breakdown")
    st.pyplot(fig2)

    # ------------------------------------------------------
    # EXPORTS
    # ------------------------------------------------------
    st.download_button("⬇️ Download CSV", df.to_csv(index=False), "knet_data.csv")
    st.download_button("⬇️ Download JSON", json.dumps(df.to_dict(), indent=2), "knet_data.json")

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

    st.download_button("⬇️ Download PDF Report", create_pdf(result), "knet_report.pdf")

# ----------------------------------------------------------
# EXPLANATION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 Analytics & Risk Explanation")

st.markdown("""
This dashboard simulates real enterprise systems using:

- Cyber Logs (security events)
- Financial Transactions
- Operational Metrics

Each record is scored and classified into:
Low, Medium, High, or Critical risk levels.

All charts and summaries are generated from the SAME dataset ensuring consistency.
""")