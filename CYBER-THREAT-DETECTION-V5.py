import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Cyber Threat Detection v3", layout="wide")

# ---------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------
st.markdown("""
<style>
h1, h2, h3 {
    color: #0a3d62;
}
div[data-testid="stHorizontalBlock"] > div {
    padding: 0.3em;
}
div.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 12px;
    color: white;
    font-weight: 600;
    border: none;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    transition: all 0.3s ease-in-out;
}
div.stButton > button:hover {
    transform: scale(1.05);
}
.load-btn { background: linear-gradient(135deg, #007bff, #004aad); }
.upload-btn { background: linear-gradient(135deg, #ffc107, #e0a800); color: black; }
.gen-btn { background: linear-gradient(135deg, #28a745, #1c7430); }
.reset-btn { background: linear-gradient(135deg, #dc3545, #a71d2a); }
.rec-card {
    background-color: #f8f9fa;
    border-left: 6px solid #0a3d62;
    padding: 12px 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.rec-title { font-weight: bold; color: #0a3d62; font-size: 1.05em; }
.rec-text { color: #333; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SYNTHETIC DATA GENERATION
# ---------------------------------------------------
def generate_synthetic_data(n=100):
    attacks = ["Phishing", "DDoS", "Malware", "SQL Injection", "Brute Force"]
    severities = ["Low", "Medium", "High", "Critical"]

    data = []
    for i in range(n):
        row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": f"192.168.{random.randint(0,255)}.{random.randint(1,255)}",
            "Destination IP": f"10.0.{random.randint(0,255)}.{random.randint(1,255)}",
            "Port": random.randint(20, 9000),
            "Attack Type": random.choice(attacks),
            "Severity": random.choice(severities)
        }
        data.append(row)
    df = pd.DataFrame(data)
    df.to_csv("synthetic_threats.csv", index=False)
    return df

# ---------------------------------------------------
# AI RECOMMENDATION ENGINE
# ---------------------------------------------------
def generate_recommendations(df):
    recs = []

    if "Attack Type" in df.columns:
        top_attack = df["Attack Type"].mode()[0]
        recs.append({
            "title": f"Most Frequent Attack: {top_attack}",
            "text": f"Detected several {top_attack} events. Strengthen detection rules, user training, and correlation alerts."
        })

    if "Severity" in df.columns:
        high_count = (df["Severity"] == "High").sum()
        crit_count = (df["Severity"] == "Critical").sum()

        if crit_count > 0:
            recs.append({
                "title": "Critical Threats Found",
                "text": "Multiple critical alerts suggest potential compromise. Immediately review firewall, patch systems, and notify SOC."
            })
        elif high_count > 0:
            recs.append({
                "title": "High Severity Threats",
                "text": "High-severity activities detected. Increase IDS sensitivity and confirm system hardening."
            })

    if "Port" in df.columns:
        common_port = df["Port"].mode()[0]
        recs.append({
            "title": f"Frequent Target Port: {common_port}",
            "text": f"Monitor and restrict unnecessary exposure on port {common_port}. Implement rate-limiting if possible."
        })

    src_counts = df["Source IP"].value_counts()
    if len(src_counts) and src_counts.iloc[0] > 5:
        recs.append({
            "title": f"Suspicious Source: {src_counts.index[0]}",
            "text": f"Source triggered {src_counts.iloc[0]} alerts. Consider blacklisting and deeper forensic analysis."
        })

    recs.append({
        "title": "General Defensive Posture",
        "text": "Enable continuous monitoring, automate log review, and conduct weekly SIEM correlation checks."
    })

    return recs

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("<h1 style='text-align:center;'>🛡️ Cyber Threat Detection Dashboard v3</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Detect, analyze, and respond to cyber incidents using data-driven intelligence.</p>", unsafe_allow_html=True)

# ---------------------------------------------------
# BUTTONS
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📂 Load Sample Data", key="load", help="Load bundled CSV data", use_container_width=True):
        if os.path.exists("sample_threat_data.csv"):
            st.session_state.df = pd.read_csv("sample_threat_data.csv")
            st.success("Sample data loaded successfully!")
        else:
            st.warning("sample_threat_data.csv not found. Try generating synthetic data instead.")

with col2:
    uploaded_file = st.file_uploader("Upload Data", type="csv", key="upload")
    if uploaded_file:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.success("Uploaded dataset loaded successfully!")

with col3:
    if st.button("🧠 Generate Synthetic Data", key="gen", use_container_width=True):
        st.session_state.df = generate_synthetic_data()
        st.success("Synthetic dataset created successfully!")

with col4:
    if st.button("🧹 Reset / Clear", key="reset", use_container_width=True):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.experimental_rerun()

# ---------------------------------------------------
# MAIN DATA VIEW
# ---------------------------------------------------
st.divider()
st.subheader("📊 Dataset Overview")

if "df" in st.session_state:
    df = st.session_state.df
    total_rows = len(df)

    limit = st.selectbox("Select number of records to view:", [10, 25, 50, 100, total_rows], index=0)
    st.dataframe(df.head(limit), use_container_width=True)
    st.info(f"Showing {min(limit, total_rows)} of {total_rows} total records")

    # ---------------------------------------------------
    # CHARTS
    # ---------------------------------------------------
    st.divider()
    st.subheader("📈 Threat Analytics")

    c1, c2 = st.columns(2)

    with c1:
        fig1, ax1 = plt.subplots()
        df["Attack Type"].value_counts().plot(kind="bar", ax=ax1, color="#007bff")
        ax1.set_title("Attack Type Frequency")
        ax1.set_xlabel("Attack Type")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    with c2:
        fig2, ax2 = plt.subplots()
        df["Severity"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax2, colors=["#28a745","#ffc107","#dc3545","#6f42c1"])
        ax2.set_ylabel("")
        ax2.set_title("Severity Distribution")
        st.pyplot(fig2)

    # ---------------------------------------------------
    # AI RECOMMENDATION PANEL
    # ---------------------------------------------------
    st.divider()
    st.subheader("🧠 AI Recommendations")

    recs = generate_recommendations(df)
    for rec in recs:
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-title">{rec['title']}</div>
            <div class="rec-text">{rec['text']}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.warning("Please load, upload, or generate data to begin analysis.")
