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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# PROFESSIONAL HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; font-weight:bold;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; font-weight:bold;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; font-weight:bold;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# SIDEBAR - API KEY MANAGEMENT
# ----------------------------------------------------------
st.sidebar.title("🔐 GROQ API Management")

user_key = st.sidebar.text_input("Enter Your GROQ API Key:", type="password")

def clean_key(key):
    return key.strip().replace("\n", "").replace("\r", "").replace('"','').replace("'","")

# Multi-user logic
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
# KEY VALIDATION BUTTON
# ----------------------------------------------------------
st.sidebar.success(f"✅ Key Loaded ({key_source})")

if st.sidebar.button("🧠 Test Connection"):
    try:
        test = client.chat.completions.create(
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
An Agentic AI Platform is an intelligent system where AI autonomously performs reasoning, analysis, and execution.

It combines:
- Autonomous AI (decision-making)
- Analytics Engine (data insights)
- Reporting Engine (exportable outputs)
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
    # REALISTIC ANALYTICS DASHBOARD
    # ------------------------------------------------------
    st.subheader("📊 Analytics Dashboard (Cyber + Financial + Operational)")

    records = []

    # Cyber Logs
    for _ in range(10):
        records.append({"Type": "Cyber Log", "Value": random.randint(1, 100)})

    # Financial Transactions
    for _ in range(10):
        records.append({"Type": "Financial", "Value": random.randint(1, 100)})

    # Operational Metrics
    for _ in range(10):
        records.append({"Type": "Operational", "Value": random.randint(1, 100)})

    # Risk Classification
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
    df["Risk Level"] = df["Value"].apply(classify_risk)

    st.dataframe(df)

    # Risk Summary
    risk_counts = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"], fill_value=0
    )

    summary_df = risk_counts.reset_index()
    summary_df.columns = ["Risk Level", "Count"]

    st.subheader("📈 Risk Distribution Summary")
    st.dataframe(summary_df)

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

    st.download_button("⬇️ Download PDF Report", create_pdf(result), "knet_report.pdf")

# ----------------------------------------------------------
# EXPLANATION SECTION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 Analytics & Risk Explanation")

st.markdown("""
### Analytics Dashboard
This dashboard simulates real enterprise data sources:
- Cyber Logs → security events
- Financial → transaction behavior
- Operational → system metrics

### Risk Distribution
Each event is categorized:
- Low Risk → normal activity
- Medium Risk → slight anomaly
- High Risk → suspicious
- Critical → requires immediate attention

### Charts
- Bar Chart → shows count comparison
- Pie Chart → shows percentage breakdown

These are standard views used in SOC, cyber defense, and enterprise analytics platforms.
""")