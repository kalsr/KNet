

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
# CUSTOM CSS: Fancy Cards + Style
# -------------------------------------------------------
st.markdown("""
<style>
.cards-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-top: 20px;
}
.card {
    width: 220px;
    height: 130px;
    border-radius: 16px;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 1.1em;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    margin: 15px;
    cursor: pointer;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    text-align: center;
    border: none;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
.green { background: linear-gradient(145deg, #28a745, #218838); }
.blue { background: linear-gradient(145deg, #007bff, #0056b3); }
.orange { background: linear-gradient(145deg, #ffc107, #e0a800); color: black; }
.red { background: linear-gradient(145deg, #dc3545, #a71d2a); }
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
# ACTION HANDLER
# -------------------------------------------------------
def trigger_action(action):
    if action == "load":
        if os.path.exists("sample_threat_data.csv"):
            st.session_state.df = pd.read_csv("sample_threat_data.csv")
            st.success("✅ Bundled data loaded successfully!")
        else:
            st.error("⚠️ sample_threat_data.csv not found.")
    elif action == "generate":
        st.session_state.df = generate_synthetic_data()
        st.success("🧠 Synthetic data generated!")
    elif action == "upload":
        uploaded = st.file_uploader("📤 Upload your CSV file", type="csv")
        if uploaded:
            st.session_state.df = pd.read_csv(uploaded)
            st.success("✅ Uploaded data loaded successfully!")
    elif action == "reset":
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.toast("All data cleared. App resetting...", icon="⚠️")
        st.rerun()

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.markdown("<h1 style='text-align:center;color:#0a3d62;'>🛡️ Cyber Threat Detection v2 Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Manage, analyze, and visualize threat data using interactive tools.</p>", unsafe_allow_html=True)

# -------------------------------------------------------
# CARD LAYOUT
# -------------------------------------------------------
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    <div class='cards-container'>
        <form action='?action=load' method='get'>
            <button class='card blue' type='submit'>📁<br>Load Bundled Data</button>
        </form>
        <form action='?action=generate' method='get'>
            <button class='card green' type='submit'>🧠<br>Generate Synthetic Data</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='cards-container'>
        <form action='?action=upload' method='get'>
            <button class='card orange' type='submit'>📤<br>Upload CSV Data</button>
        </form>
        <form action='?action=reset' method='get'>
            <button class='card red' type='submit'>🧹<br>Reset / Clear All</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# ACTION HANDLING
# -------------------------------------------------------
query_params = st.query_params
if "action" in query_params:
    action = query_params["action"][0] if isinstance(query_params["action"], list) else query_params["action"]
    trigger_action(action)
    st.query_params.clear()

# -------------------------------------------------------
# DATA SOURCE SECTION
# -------------------------------------------------------
st.divider()
st.subheader("📂 Data Source Information")

if "df" in st.session_state:
    st.write(f"✅ Active dataset loaded with **{len(st.session_state.df)} rows**")
    db_path = os.path.abspath("synthetic_threats.csv") if os.path.exists("synthetic_threats.csv") else "(no synthetic file created yet)"
    st.info(f"Database file location: `{db_path}`")

    st.dataframe(st.session_state.df.head(), use_container_width=True)

    # -------------------------------------------------------
    # VISUALIZATION SECTION
    # -------------------------------------------------------
    st.divider()
    st.subheader("📊 Threat Pattern Visualization")

    col1, col2 = st.columns(2)
    df = st.session_state.df

    # Attack Type Bar Chart
    with col1:
        fig1, ax1 = plt.subplots()
        df["Attack Type"].value_counts().plot(kind="bar", ax=ax1)
        ax1.set_title("Attack Types Frequency")
        ax1.set_xlabel("Attack Type")
        ax1.set_ylabel("Count")
        st.pyplot(fig1)

    # Severity Pie Chart
    with col2:
        fig2, ax2 = plt.subplots()
        df["Severity"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=90, ax=ax2)
        ax2.set_ylabel("")  # remove label
        ax2.set_title("Severity Distribution")
        st.pyplot(fig2)

else:
    st.warning("⚠️ No dataset loaded. Please use one of the options above to begin.")
