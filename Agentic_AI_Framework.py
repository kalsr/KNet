# Agentic_AI_Framework

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
    page_title="Agentic-AI Cyber Defense Framework Designed by Randy Singh From KNet Consulting Group.",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* Header Styles */
    .stApp h1 {color: #0073e6;}
    .stApp h2 {color: #005792;}
    .stApp h3 {color: #ff6600;}
    .stButton>button {background-color:#0073e6; color:white; border-radius:10px; height:50px; width:100%;}
    .stButton>button:hover {background-color:#005bb5; color:white;}
    a.agent-link {display:inline-block; margin:5px; padding:8px 15px; background:#0073e6; color:white; text-decoration:none; border-radius:8px;}
    a.agent-link:hover {background:#005bb5; color:white;}
    </style>
    """, unsafe_allow_html=True
)

# ----------------------
# Title
# ----------------------
st.title(" Agentic-AI Cyber Defense Framework Designed by Randy Singh From KNet Consulting Group.")
st.markdown(
    """
    **Agentic AI** = Autonomous AI systems that plan, decide, and act toward goals.  
    Select a demo agent below to simulate its behavior or generate/upload data.  
    """
)

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

# ----------------------
# Clear Data Button
# ----------------------
if "data" not in st.session_state:
    st.session_state["data"] = None

def clear_data():
    st.session_state["data"] = None
    st.success(" Data cleared!")

st.sidebar.button(" Clear All Data", on_click=clear_data)

# ----------------------
# Sidebar Navigation
# ----------------------
st.sidebar.title(" Framework Controls")
choice = st.sidebar.radio(
    "Select Action",
    [" Dashboard", " Upload Data", " Generate Sample Data", " Demo Agent"]
)

# ----------------------
# Upload Data
# ----------------------
if choice == " Upload Data":
    uploaded_file = st.file_uploader("Upload JSON, CSV, or TXT", type=["json", "csv", "txt"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            st.session_state["data"] = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json") or uploaded_file.name.endswith(".txt"):
            st.session_state["data"] = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file format")

    if st.session_state["data"] is not None:
        st.success("Data uploaded successfully!")
        st.dataframe(st.session_state["data"])

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(" Download as CSV", convert_df(st.session_state["data"], "csv"), "agentic_ai_data.csv", "text/csv")
        with col2:
            st.download_button(" Download as JSON", convert_df(st.session_state["data"], "json"), "agentic_ai_data.json", "application/json")

# ----------------------
# Generate Sample Data
# ----------------------
elif choice == "🛠 Generate Sample Data":
    n = st.sidebar.slider("Number of Records", 10, 200, 50, 10)
    st.session_state["data"] = generate_sample_data(n)
    st.success(f" Generated {n} sample records")
    st.dataframe(st.session_state["data"])

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(" Download as CSV", convert_df(st.session_state["data"], "csv"), "sample_data.csv", "text/csv")
    with col2:
        st.download_button(" Download as JSON", convert_df(st.session_state["data"], "json"), "sample_data.json", "application/json")

    # Pie chart visualization
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
elif choice == "Dashboard":
    st.info("📡 Live Dashboard: Showing demo data for Agentic-AI use cases")
    if st.session_state["data"] is None:
        st.session_state["data"] = generate_sample_data(30)
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
elif choice == "Demo Agent":
    st.header("Agentic AI Demo Agents")

    # List of available demo agents
    agents = {
        "Automated Threat Hunting": "Simulates scanning logs, detecting anomalies, querying threat intel feeds.",
        "Adaptive Incident Response": "Detect intrusions, isolate affected machines, block IPs, alert SOC.",
        "Vulnerability Scanning": "Run vulnerability scans, suggest mitigations, open tickets automatically.",
        "Phishing Email Defense": "Inspect emails, flag phishing, extract IOCs, update blocklists.",
        "Cyber Deception & Honeypots": "Deploy honeypots/decoys, monitor attacker behavior, update defenses dynamically."
    }

    agent_choice = st.radio("Select Demo Agent", list(agents.keys()))
    st.info(f" {agents[agent_choice]}")

    st.subheader(f"Demo: {agent_choice}")

    # Generate random sample data for selected agent
    num_records = st.sidebar.slider("Number of Events", 5, 50, 15)
    demo_data = generate_sample_data(num_records)
    st.dataframe(demo_data)

    # Pie chart for threat distribution
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

