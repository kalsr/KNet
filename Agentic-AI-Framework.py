# Agentic-AI-Framework
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

st.markdown(
    """
    <style>
    /* Header Styles */
    .stApp h1 {color: #0073e6;}
    .stApp h2 {color: #005792;}
    .stApp h3 {color: #ff6600;}
    .stButton>button {background-color:#0073e6; color:white; border-radius:10px; height:50px; width:100%;}
    .stButton>button:hover {background-color:#005bb5; color:white;}
    </style>
    """, unsafe_allow_html=True
)

# ----------------------
# Title
# ----------------------
st.title("🛡️ Agentic-AI Cyber Defense Framework")
st.markdown(
    """
    **Agentic AI** = Autonomous AI systems that plan, decide, and act toward goals.  
    This framework demonstrates how AI agents can help in **cyber defense**:
    - Automated Threat Hunting  
    - Adaptive Incident Response  
    - Vulnerability Scanning  
    - Phishing Email Defense  
    - Cyber Deception & Honeypots  
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
# Sidebar Navigation
# ----------------------
st.sidebar.title("⚙️ Framework Controls")
choice = st.sidebar.radio(
    "Select Action",
    ["📊 Dashboard", "📂 Upload Data", "🛠 Generate Sample Data", "🤖 Demo Agent"]
)

# ----------------------
# Upload Data
# ----------------------
if choice == "📂 Upload Data":
    uploaded_file = st.file_uploader("Upload JSON, CSV, or TXT", type=["json", "csv", "txt"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json") or uploaded_file.name.endswith(".txt"):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file format")
            df = None

        if df is not None:
            st.success("✅ Data uploaded successfully!")
            st.dataframe(df)

            col1, col2 = st.columns(2)
            with col1:
                st.download_button("⬇️ Download as CSV", convert_df(df, "csv"), "agentic_ai_data.csv", "text/csv")
            with col2:
                st.download_button("⬇️ Download as JSON", convert_df(df, "json"), "agentic_ai_data.json", "application/json")

# ----------------------
# Generate Sample Data
# ----------------------
elif choice == "🛠 Generate Sample Data":
    n = st.sidebar.slider("Number of Records", 10, 200, 50, 10)
    df = generate_sample_data(n)
    st.success(f"✅ Generated {n} sample records")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button("⬇️ Download as CSV", convert_df(df, "csv"), "sample_data.csv", "text/csv")
    with col2:
        st.download_button("⬇️ Download as JSON", convert_df(df, "json"), "sample_data.json", "application/json")

    # Pie chart visualization
    st.subheader("Threat Distribution")
    fig, ax = plt.subplots(figsize=(6,6))
    df["threat"].value_counts().plot.pie(
        autopct="%1.1f%%", ax=ax, shadow=True, startangle=90, colors=plt.cm.tab20.colors
    )
    ax.set_ylabel("")
    st.pyplot(fig)

# ----------------------
# Dashboard View
# ----------------------
elif choice == "📊 Dashboard":
    st.info("📡 Live Dashboard: Showing demo data for Agentic-AI use cases")
    df = generate_sample_data(30)
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
elif choice == "🤖 Demo Agent":
    st.header("🤖 Agentic AI Demo: Automated Threat Hunting")

    # Sample Target IPs
    target_ips = [f"192.168.{random.randint(0,255)}.{random.randint(1,254)}" for _ in range(10)]
    st.subheader("Target Hosts")
    st.write(target_ips)

    st.subheader("Simulated Threat Detection Results")
    threats = ["Phishing", "Malware", "Ransomware", "Botnet", "Zero-Day"]
    results = []
    for ip in target_ips:
        results.append({
            "ip": ip,
            "threat": random.choice(threats),
            "severity": random.choice(["Low", "Medium", "High", "Critical"]),
            "action": random.choice(["Detected", "Blocked", "Alerted SOC"])
        })

    df_agent = pd.DataFrame(results)
    st.dataframe(df_agent)

    # Pie chart for threat distribution
    st.subheader("Threat Distribution (Agentic AI)")
    fig, ax = plt.subplots(figsize=(5,5))
    df_agent["threat"].value_counts().plot.pie(
        autopct="%1.1f%%", ax=ax, shadow=True, startangle=90, colors=plt.cm.Set3.colors
    )
    ax.set_ylabel("")
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button("⬇️ Download Agent Results as CSV", convert_df(df_agent, "csv"), "agentic_agent_results.csv", "text/csv")
    with col2:
        st.download_button("⬇️ Download Agent Results as JSON", convert_df(df_agent, "json"), "agentic_agent_results.json", "application/json")

    st.info("⚡ Demo agent shows autonomous threat detection. Real-world agents connect to logs, APIs (Shodan, VirusTotal), and can act adaptively.")

