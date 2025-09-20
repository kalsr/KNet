#Agentic_AI_Framework

import streamlit as st
import pandas as pd
import json
import io
import random
import matplotlib.pyplot as plt
import datetime

# ----------------------
# Page Setup
# ----------------------
st.set_page_config(
    page_title="Agentic-AI Cyber Defense Framework",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------
# Styling
# ----------------------
st.markdown("""
<style>
.stApp h1 {color: #0073e6;}
.stApp h2 {color: #005792;}
.stApp h3 {color: #ff6600;}
.stButton>button {background-color:#0073e6; color:white; border-radius:10px; height:50px; width:100%;}
.stButton>button:hover {background-color:#005bb5; color:white;}
a.agent-link {display:inline-block; margin:5px; padding:8px 15px; background:#0073e6; color:white; text-decoration:none; border-radius:8px;}
a.agent-link:hover {background:#005bb5; color:white;}
</style>
""", unsafe_allow_html=True)

# ----------------------
# Title
# ----------------------
st.title(" Agentic-AI Cyber Defense Framework Designed by Randy Singh KNet Consulting Group.")
st.markdown(
    """
    **Agentic AI** = Autonomous AI systems that plan, decide, and act toward goals.  
    Use the sidebar to select an action: Dashboard, Upload Data, Generate Sample Data, or Demo Agent.
    """
)

# ----------------------
# Initialize Session State
# ----------------------
if "data" not in st.session_state:
    st.session_state["data"] = None

# ----------------------
# Utility Functions
# ----------------------
def generate_sample_data(n=20):
    threats = ["Phishing", "Malware", "Ransomware", "Botnet", "Zero-Day", "Insider Threat"]
    severities = ["Low", "Medium", "High", "Critical"]
    data = []
    for i in range(n):
        data.append({
            "id": i + 1,
            "threat": random.choice(threats),
            "severity": random.choice(severities),
            "source_ip": f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}",
            "status": random.choice(["Detected", "Mitigated", "Escalated"]),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return pd.DataFrame(data)

def convert_df(df, fmt="csv"):
    if fmt == "csv":
        return df.to_csv(index=False).encode("utf-8")
    elif fmt == "json":
        return df.to_json(orient="records", indent=2).encode("utf-8")

def clear_data():
    st.session_state["data"] = None
    st.success(" All data cleared!")

# ----------------------
# Sidebar
# ----------------------
st.sidebar.title(" Framework Controls")
st.sidebar.button(" Clear All Data", on_click=clear_data)

action = st.sidebar.radio(
    "Select Action",
    [" Dashboard", " Upload Data", " Generate Sample Data", " Demo Agent"]
)

# ----------------------
# Upload Data
# ----------------------
if action == " Upload Data":
    uploaded_file = st.file_uploader("Upload JSON, CSV, or TXT", type=["json", "csv", "txt"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                st.session_state["data"] = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".json") or uploaded_file.name.endswith(".txt"):
                st.session_state["data"] = pd.read_json(uploaded_file)
            else:
                st.error("Unsupported file format")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    if st.session_state["data"] is not None:
        st.success(" Data uploaded successfully!")
        st.dataframe(st.session_state["data"])

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(" Download as CSV", convert_df(st.session_state["data"], "csv"), "agentic_ai_data.csv", "text/csv")
        with col2:
            st.download_button(" Download as JSON", convert_df(st.session_state["data"], "json"), "agentic_ai_data.json", "application/json")

# ----------------------
# Generate Sample Data
# ----------------------
elif action == " Generate Sample Data":
    n = st.sidebar.slider("Number of Records", 10, 200, 50, 10)
    st.session_state["data"] = generate_sample_data(n)
    st.success(f" Generated {n} sample records")
    st.dataframe(st.session_state["data"])

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(" Download as CSV", convert_df(st.session_state["data"], "csv"), "sample_data.csv", "text/csv")
    with col2:
        st.download_button(" Download as JSON", convert_df(st.session_state["data"], "json"), "sample_data.json", "application/json")

    st.subheader("Threat Distribution")
    fig, ax = plt.subplots(figsize=(6,6))
    st.session_state["data"]["threat"].value_counts().plot.pie(
        autopct="%1.1f%%", ax=ax, shadow=True, startangle=90, colors=plt.cm.tab20.colors
    )
    ax.set_ylabel("")
    st.pyplot(fig)

# ----------------------
# Dashboard View
# ----------------------
elif action == " Dashboard":
    st.info(" Live Dashboard: Showing current data")
    if st.session_state["data"] is None:
        st.warning("No data available. Generate sample data or upload a file first.")
    else:
        df = st.session_state["data"]
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Severity Breakdown")
            fig, ax = plt.subplots(figsize=(5,5))
            df["severity"].value_counts().plot.pie(
                autopct="%1.1f%%",
                ax=ax,
                colors=["#2ecc71", "#f1c40f", "#e67e22", "#e74c3c"],
                shadow=True,
                startangle=90
            )
            ax.set_ylabel("")
            st.pyplot(fig)

        with col2:
            st.subheader("Threat Status Overview")
            st.bar_chart(df["status"].value_counts())

# ----------------------
# Demo Agent View
# ----------------------
elif action == " Demo Agent":
    st.header(" Agentic AI Demo Agents - Designed by Randy Singh KNet Consulting Group.")

    agents = {
        "Automated Threat Hunting": "Scans logs, detects anomalies, queries threat intel feeds.",
        "Adaptive Incident Response": "Detect intrusions, isolate affected machines, block IPs, alert SOC.",
        "Vulnerability Scanning": "Run vulnerability scans, suggest mitigations, open tickets automatically.",
        "Phishing Email Defense": "Inspect emails, flag phishing, extract IOCs, update blocklists.",
        "Cyber Deception & Honeypots": "Deploy honeypots, monitor attackers, update defenses dynamically."
    }

    agent_choice = st.radio("Select Demo Agent", list(agents.keys()))
    st.info(f" {agents[agent_choice]}")

    num_records = st.sidebar.slider("Number of Events", 5, 50, 15)
    demo_data = generate_sample_data(num_records)
    st.dataframe(demo_data)

    st.subheader("Threat Distribution")
    fig, ax = plt.subplots(figsize=(5,5))
    demo_data["threat"].value_counts().plot.pie(
        autopct="%1.1f%%", ax=ax, shadow=True, startangle=90, colors=plt.cm.Set3.colors
    )
    ax.set_ylabel("")
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(" Download Demo as CSV", convert_df(demo_data, "csv"), f"{agent_choice}_demo.csv", "text/csv")
    with col2:
        st.download_button(" Download Demo as JSON", convert_df(demo_data, "json"), f"{agent_choice}_demo.json", "application/json")

    st.success(f" {agent_choice} simulation complete.")
