

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

st.set_page_config(page_title="KNet Agentic AI Platform", layout="wide")

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------
st.markdown("<h1 style='color:blue; text-align:center; font-weight:bold;'>Kalsnet (KNet) – Agentic AI Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center; font-weight:bold;'>Autonomous AI + Analytics + Reporting Engine</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='color:blue; text-align:center; font-weight:bold;'>Developed by Randy Singh</h4>", unsafe_allow_html=True)

# ----------------------------------------------------------
# API KEY
# ----------------------------------------------------------
st.sidebar.title(" GROQ API Management")

user_key = st.sidebar.text_input("Enter GROQ API Key:", type="password")

# ✅ NEW: Instructions added (as requested)
st.sidebar.markdown("""
**How to Create GROQ API Key:**

Each user can:

1. Go to https://console.groq.com  
2. Sign up (free)  
3. Navigate to API Keys  
4. Click **Create API Key**  
5. Copy the full key (starts with `gsk_...`)  
6. Paste it into this input box  
""")

def clean_key(key):
    return key.strip()

if user_key:
    api_key = clean_key(user_key)
else:
    api_key = st.secrets.get("GROQ_API_KEY", None)

if not api_key:
    st.warning(" Enter API key")
    st.stop()

client = Groq(api_key=api_key)

# ----------------------------------------------------------
# USE CASE SELECTION (NEW)
# ----------------------------------------------------------
st.subheader(" Select Agentic AI Use Case")

use_cases = [
    "Cybersecurity Threat Detection",
    "Financial Fraud Detection",
    "Supply Chain Risk Analysis",
    "Healthcare Risk Prediction",
    "Customer Behavior Analytics",
    "Market Intelligence",
    "Operational Efficiency Monitoring",
    "Insider Threat Detection",
    "Network Anomaly Detection",
    "Cloud Security Monitoring",
    "Compliance Monitoring",
    "Threat Intelligence Analysis",
    "Fraud Transaction Monitoring",
    "Predictive Maintenance",
    "Log Analytics",
    "Other (Custom)"
]

selected_use_case = st.selectbox("Select Use Case:", use_cases)

custom_use_case = ""
if selected_use_case == "Other (Custom)":
    custom_use_case = st.text_input("Enter your custom use case:")

final_use_case = custom_use_case if custom_use_case else selected_use_case

# ----------------------------------------------------------
# TASK INPUT
# ----------------------------------------------------------
st.subheader(" Agentic AI Task Input")
task = st.text_area("Enter your task:")
run = st.button(" Run Agentic AI")

# ----------------------------------------------------------
# AI FUNCTION
# ----------------------------------------------------------
def run_agentic_ai(task):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": task}],
            max_tokens=1024
        )
        return response.choices[0].message.content
    except:
        return None

# ----------------------------------------------------------
# RISK FUNCTION
# ----------------------------------------------------------
def classify_risk(val):
    if val < 25:
        return "Low Risk"
    elif val < 50:
        return "Medium Risk"
    elif val < 75:
        return "High Risk"
    else:
        return "Critical"

# ----------------------------------------------------------
# EXECUTION
# ----------------------------------------------------------
if run:

    result = run_agentic_ai(task)
    if not result:
        st.error("AI execution failed")
        st.stop()

    st.success("AI Response Generated")
    st.write(result)

    st.subheader(f" Analytics Dashboard ({final_use_case})")

    records = []

    # ------------------------------------------------------
    # DYNAMIC DATA GENERATION BASED ON USE CASE
    # ------------------------------------------------------
    for _ in range(30):
        val = random.randint(1, 100)

        if "Cyber" in final_use_case:
            records.append({
                "Timestamp": datetime.datetime.now(),
                "Source IP": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "Event Type": random.choice(["Malware", "Scan", "Login"]),
                "Severity": val
            })

        elif "Financial" in final_use_case or "Fraud" in final_use_case:
            records.append({
                "Account ID": random.randint(1000,9999),
                "Transaction Amount": random.randint(100,5000),
                "Location": random.choice(["US","UK","IN"]),
                "Risk Score": val
            })

        elif "Supply" in final_use_case:
            records.append({
                "Supplier": f"Vendor-{random.randint(1,50)}",
                "Delay Days": random.randint(0,20),
                "Status": random.choice(["On-Time","Delayed"]),
                "Risk Score": val
            })

        else:
            records.append({
                "Record ID": random.randint(1,1000),
                "Metric Value": val
            })

    df = pd.DataFrame(records)

    # Determine correct score column
    score_col = [col for col in df.columns if "Score" in col or "Severity" in col or "Value" in col][0]

    df["Risk Level"] = df[score_col].apply(classify_risk)

    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------
    # CONSISTENT RISK SUMMARY
    # ------------------------------------------------------
    summary_df = df["Risk Level"].value_counts().reindex(
        ["Low Risk", "Medium Risk", "High Risk", "Critical"], fill_value=0
    ).reset_index()

    summary_df.columns = ["Risk Level", "Count"]

    st.subheader(" Risk Distribution Summary")
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
    st.download_button("CSV", df.to_csv(index=False), "data.csv")

    # ✅ FIXED JSON (only change made)
    st.download_button("JSON", json.dumps(df.astype(str).to_dict(), indent=2), "data.json")

    # ✅ NEW: PDF EXPORT
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph("KNet Agentic AI Report", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Use Case: {final_use_case}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    for i, row in df.head(20).iterrows():
        elements.append(Paragraph(str(row.to_dict()), styles["Normal"]))
        elements.append(Spacer(1, 8))

    doc.build(elements)
    buffer.seek(0)

    st.download_button("PDF Report", buffer, "report.pdf")

# ----------------------------------------------------------
# EXPLANATION
# ----------------------------------------------------------
st.markdown("---")
st.subheader("📖 Dashboard Explanation")

st.markdown("""
###  Use Case Selection
User selects a predefined use case or enters a custom one. The system dynamically adapts analytics accordingly.

###  Analytics Dashboard
Data fields change based on selected use case:
- Cyber → IP, events, threats
- Financial → transactions, accounts
- Supply Chain → vendors, delays

###  Risk Distribution
Risk levels are computed from the SAME dataset ensuring:
- Dashboard = Summary = Charts (100% match)

###  Agentic AI
Autonomously interprets task → generates insights → produces analytics.
""")