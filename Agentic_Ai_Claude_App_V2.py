

# Agentic_Cyber_Analysis_App_V2.py

import streamlit as st
import pandas as pd
import numpy as np
import os
import io
import time
import matplotlib.pyplot as plt
from anthropic import Anthropic

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Agentic Cyber AI Analysis Hub",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------- STYLES ----------------------
st.markdown("""
    <style>
        div[data-testid="stMetricValue"] {
            font-size: 24px;
            color: #0b6e4f;
        }
        div[data-testid="stButton"] button {
            font-weight: bold;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- ROLE SELECTION ----------------------
st.sidebar.title("🔐 Role Access Control")
role = st.sidebar.radio("Select your role:", ["Admin", "Analyst", "Viewer"])

role_colors = {
    "Admin": "#b30000",
    "Analyst": "#003366",
    "Viewer": "#145A32"
}

st.markdown(f"""
<div style='background-color:{role_colors[role]}; padding:15px; border-radius:12px'>
<h2 style='color:white; text-align:center;'>Agentic Cyber AI Analysis Dashboard — {role} Mode</h2>
</div>
""", unsafe_allow_html=True)

# ---------------------- SESSION STATE ----------------------
if "df" not in st.session_state:
    st.session_state.df = None
if "analysis" not in st.session_state:
    st.session_state.analysis = None

# ---------------------- SAMPLE DATA GENERATOR ----------------------
def generate_sample_data(num_records=50):
    np.random.seed(42)
    severities = ["Low", "Medium", "High"]
    threats = ["Malware", "Phishing", "DoS", "SQL Injection", "Insider Threat"]
    df = pd.DataFrame({
        "Timestamp": pd.date_range(start="2025-01-01", periods=num_records, freq="H"),
        "Source_IP": [f"192.168.1.{i%255}" for i in range(num_records)],
        "Destination_IP": [f"10.0.0.{i%255}" for i in range(num_records)],
        "Threat_Type": np.random.choice(threats, num_records),
        "Severity": np.random.choice(severities, num_records),
        "Confidence_Score": np.random.uniform(0.5, 1.0, num_records).round(2)
    })
    return df

# ---------------------- AGENTIC AI ANALYSIS ----------------------
def analyze_with_agentic_ai(df):
    st.info("Running Agentic AI Analysis...")
    df.columns = [c.strip().lower() for c in df.columns]

    possible_severity = next((c for c in df.columns if "severity" in c), None)
    possible_threat = next((c for c in df.columns if "threat" in c), None)
    possible_ip = next((c for c in df.columns if "ip" in c or "source" in c), None)

    summary = {}

    if possible_severity:
        summary["Severity Counts"] = df[possible_severity].value_counts().to_dict()
    else:
        summary["Severity Counts"] = "No severity column found."

    if possible_threat:
        summary["Threat Types"] = df[possible_threat].value_counts().to_dict()
    else:
        summary["Threat Types"] = "No threat column found."

    if possible_ip:
        summary["Unique IPs"] = df[possible_ip].nunique()

    insights = []
    if isinstance(summary["Severity Counts"], dict):
        high_threats = summary["Severity Counts"].get("High", 0)
        if high_threats > 0:
            insights.append(f"⚠️ {high_threats} High-severity events detected. Immediate containment advised.")
        else:
            insights.append("✅ No High-severity events detected.")
    if possible_ip:
        insights.append(f"🔍 {summary['Unique IPs']} unique IPs observed.")
    if possible_threat:
        insights.append(f"🧠 Top threats: {', '.join(list(summary['Threat Types'])[:5])}.")

    ai_summary = "Agentic AI summary unavailable (API Key missing)."
    if os.getenv("ANTHROPIC_API_KEY"):
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        prompt = f"""
        You are an AI Cyber Analyst. Analyze this summary:
        {summary}
        Provide 3 strategic risk recommendations for the SOC.
        """
        try:
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=400,
                messages=[{"role": "user", "content": prompt}]
            )
            ai_summary = response.content[0].text
        except Exception as e:
            ai_summary = f"AI error: {str(e)}"

    return {"summary": summary, "insights": insights, "ai_summary": ai_summary}

# ---------------------- MAIN FUNCTIONAL UI ----------------------
st.sidebar.header("⚙️ Operations")

if role in ["Admin", "Analyst"]:
    num_records = st.sidebar.slider("Number of Sample Records", 10, 100, 50)
    if st.sidebar.button("🟩 Generate Sample Logs"):
        st.session_state.df = generate_sample_data(num_records)
        st.success(f"Generated {num_records} sample cyber records!")

if role != "Viewer":
    uploaded_file = st.sidebar.file_uploader("📤 Upload Cyber Logs (CSV)", type=["csv"])
    if uploaded_file:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

if st.session_state.df is not None:
    st.dataframe(st.session_state.df.head(), use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    if col1.button("🧠 Agentic AI Analysis", type="primary"):
        st.session_state.analysis = analyze_with_agentic_ai(st.session_state.df)

    if role == "Admin":
        if col2.button("🚨 Auto-Contain (Admin)"):
            st.warning("Auto-containment initiated on High severity threats.")
        if col3.button("🔴 Reset Data"):
            st.session_state.df = None
            st.session_state.analysis = None
            st.experimental_rerun()

    if col4.button("📥 Download Results"):
        if st.session_state.df is not None:
            csv = st.session_state.df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", csv, "analysis_results.csv", "text/csv")

    if st.session_state.analysis:
        st.subheader("🧩 Agentic AI Insights")
        for insight in st.session_state.analysis["insights"]:
            st.write(insight)
        st.write("---")
        st.markdown(st.session_state.analysis["ai_summary"])

        # Simple visualization
        if "Severity Counts" in st.session_state.analysis["summary"] and isinstance(st.session_state.analysis["summary"]["Severity Counts"], dict):
            fig, ax = plt.subplots()
            pd.Series(st.session_state.analysis["summary"]["Severity Counts"]).plot(kind="pie", autopct='%1.1f%%', ax=ax)
            ax.set_ylabel('')
            ax.set_title("Severity Distribution")
            st.pyplot(fig)

else:
    st.info("Upload a file or generate sample data to begin analysis.")

# ---------------------- FOOTER ----------------------
st.markdown("""
---
© 2025 KNet Cyber Intelligence — Powered by Agentic AI
""")
