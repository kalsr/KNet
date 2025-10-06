

import streamlit as st
import pandas as pd
import numpy as np
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(page_title="Cyber Threat Detection v2", layout="wide")

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] > div {
    padding: 0.5em;
}
div.stButton > button {
    width: 100%;
    height: 120px;
    border-radius: 16px;
    color: white;
    font-weight: bold;
    font-size: 1.1em;
    border: none;
    transition: all 0.25s ease;
    box-shadow: 0 6px 15px rgba(0,0,0,0.25);
}
div.stButton > button:hover {
    transform: scale(1.05);
}
.load-btn {
    background: linear-gradient(145deg, #007bff, #0056b3);
}
.gen-btn {
    background: linear-gradient(145deg, #28a745, #218838);
}
.upload-btn {
    background: linear-gradient(145deg, #ffc107, #e0a800);
    color: black;
}
.reset-btn {
    background: linear-gradient(145deg, #dc3545, #a71d2a);
}
.rec-card {
    background: linear-gradient(145deg, #f8f9fa, #e9ecef);
    padding: 1em;
    border-radius: 12px;
    margin-bottom: 0.8em;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.rec-title {
    font-weight: 600;
    color: #0a3d62;
}
.rec-text {
    color: #212529;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SYNTHETIC DATA GENERATOR
# -------------------------------------------------------
def generate_synthetic_data(n=50):
    src_ips = [f"192.168.{random.randint(0,255)}.{random.randint(0,255)}" for _ in range(n)]
    dst_ips = [f"10.0.{random.randint(0,255)}.{random.randint(0,255)}" for _ in range(n)]
    attack_types = np.random.choice(["Phishing", "DDoS", "Malware", "Brute Force", "SQL Injection"], n)
    severity = np.random.choice(["Low", "Medium", "High", "Critical"], n)
    timestamps = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(n)]
    ports = np.random.randint(20, 9000, n)

    df = pd.DataFrame({
        "Timestamp": timestamps,
        "Source IP": src_ips,
        "Destination IP": dst_ips,
        "Port": ports,
        "Attack Type": attack_types,
        "Severity": severity
    })
    df.to_csv("synthetic_threats.csv", index=False)
    return df

# -------------------------------------------------------
# AI RECOMMENDATION LOGIC
# -------------------------------------------------------
def generate_recommendations(df):
    recs = []

    # 1. Most common attack
    if "Attack Type" in df.columns:
        common_attack = df["Attack Type"].mode()[0]
        recs.append({
            "title": f"Frequent Attack: {common_attack}",
            "text": f"The dataset indicates multiple occurrences of {common_attack} attacks. "
                    f"Implement targeted defensive measures like detection signatures and user awareness training."
        })

    # 2. Severity pattern
    if "Severity" in df.columns:
        if (df["Severity"] == "Critical").sum() > 0:
            recs.append({
                "title": "Critical Threats Detected",
                "text": "Multiple critical alerts were found. Ensure 24/7 SOC monitoring, increase firewall logging, "
                        "and prioritize patching high-risk systems immediately."
            })
        elif (df["Severity"] == "High").sum() > 0:
            recs.append({
                "title": "High Severity Activity",
                "text": "High severity threats indicate possible active exploitation attempts. "
                        "Enhance intrusion detection thresholds and verify access control policies."
            })

    # 3. Common ports targeted
    if "Port" in df.columns:
        common_port = df["Port"].mode()[0]
        recs.append({
            "title": f"Frequent Target Port: {common_port}",
            "text": f"Several events target port {common_port}. Review firewall and IDS rules for this port "
                    f"and consider temporary blocking or throttling if non-essential."
        })

    # 4. Source IP concentration
    src_counts = df["Source IP"].value_counts()
    if len(src_counts) > 0 and src_counts.iloc[0] > 3:
        recs.append({
            "title": f"Suspicious Source Activity: {src_counts.index[0]}",
            "text": f"This IP has triggered more than 3 alerts. "
                    f"Investigate logs and consider blacklisting or sandboxing the source."
        })

    # 5. General security posture
    recs.append({
        "title": "General Recommendations",
        "text": "Conduct a weekly review of threat data. Use SIEM tools for correlation. "
                "Implement automated alert escalation and backup verification routines."
    })

    return recs

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.markdown("<h1 style='text-align:center;color:#0a3d62;'>🛡️ Cyber Threat Detection v2 Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Manage, analyze, and visualize cyber threat data using intelligent tools.</p>", unsafe_allow_html=True)

# -------------------------------------------------------
# BUTTONS
# -------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📁 Load Bundled Data", key="load", use_container_width=True):
        if os.path.exists("sample_threat_data.csv"):
            st.session_state.df = pd.read_csv("sample_threat_data.csv")
            st.success("✅ Bundled data loaded successfully!")
        else:
            st.error("⚠️ sample_threat_data.csv not found.")

with col2:
    if st.button("🧠 Generate Synthetic Data", key="generate", use_container_width=True):
        st.session_state.df = generate_synthetic_data()
        st.success("🧠 Synthetic data generated successfully!")

with col3:
    uploaded = st.file_uploader("📤 Upload CSV Data", type="csv", key="upload")
    if uploaded:
        st.session_state.df = pd.read_csv(uploaded)
        st.success("✅ Uploaded data loaded successfully!")

with col4:
    if st.button("🧹 Reset / Clear All", key="reset", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.toast("All data cleared. App resetting...", icon="⚠️")
        st.rerun()

# -------------------------------------------------------
# DATA SECTION
# -------------------------------------------------------
st.divider()
st.subheader("📂 Data Source Information")

if "df" in st.session_state:
    df = st.session_state.df
    st.write(f"✅ Active dataset loaded with **{len(df)} rows**")

    db_path = os.path.abspath("synthetic_threats.csv") if os.path.exists("synthetic_threats.csv") else "(no synthetic file created yet)"
    st.info(f"Database file location: `{db_path}`")

    st.dataframe(df.head(), use_container_width=True)

    # -------------------------------------------------------
    # VISUALIZATION SECTION
    # -------------------------------------------------------
    st.divider()
    st.subheader("📊 Threat Pattern Visualization")

    colA, colB = st.columns(2)

    with colA:
        fig1, ax1 = plt.subplots()
        df["Attack Type"].value_counts().plot(kind="bar", ax=ax1)
        ax1.set_title("Attack Types Frequency")
        ax1.set_xlabel("Attack Type")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    with colB:
        fig2, ax2 = plt.subplots()
        df["Severity"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=90, ax=ax2)
        ax2.set_ylabel("")
        ax2.set_title("Severity Distribution")
        st.pyplot(fig2)

    # -------------------------------------------------------
    # AI RECOMMENDATION PANEL
    # -------------------------------------------------------
    st.divider()
    st.subheader("🧠 AI Recommendations Panel")

    recommendations = generate_recommendations(df)
    for rec in recommendations:
        st.markdown(f"""
        <div class='rec-card'>
            <div class='rec-title'>{rec["title"]}</div>
            <div class='rec-text'>{rec["text"]}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.warning("⚠️ No dataset loaded. Please use one of the buttons above to begin.")
