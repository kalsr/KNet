# THIS USE-CASE IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.

# python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
from io import StringIO
import json

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="KalsNet Cyber Monitor", layout="wide", page_icon="🛡️")

# -----------------------------
# Sidebar: Refresh & Upload
# -----------------------------
st.sidebar.header("Controls")

refresh_rate = st.sidebar.number_input(
    "Auto-refresh interval (seconds)", min_value=10, max_value=600, value=60, step=10
)
manual_refresh = st.sidebar.button("Manual Refresh")
if manual_refresh:
    st.experimental_rerun()

# Countdown logic
if 'countdown' not in st.session_state:
    st.session_state.countdown = refresh_rate
else:
    st.session_state.countdown -= 1
    if st.session_state.countdown <= 0:
        st.session_state.countdown = refresh_rate
        st.experimental_rerun()

st.sidebar.markdown(f"Next auto-refresh in **{st.session_state.countdown} s**")

st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV, JSON, or TXT file", type=['csv', 'json', 'txt']
)

# -----------------------------
# Generate / Load Data
# -----------------------------
@st.cache_data
def generate_sample_data(n=500):
    np.random.seed(42)
    timestamps = [datetime.now() - timedelta(minutes=i*5) for i in range(n)]
    ip_addresses = [f"192.168.1.{np.random.randint(1,255)}" for _ in range(n)]
    record_types = np.random.choice(
        ["Login", "File Access", "Malware", "Phishing", "Port Scan", "Other"],
        size=n,
        p=[0.3,0.25,0.15,0.1,0.1,0.1]
    )
    values = np.random.normal(loc=50, scale=10, size=n)
    df = pd.DataFrame({
        "timestamp": timestamps,
        "ip": ip_addresses,
        "record_type": record_types,
        "value": values
    })
    return df

if uploaded_file is not None:
    try:
        if uploaded_file.type == "application/json":
            df = pd.read_json(uploaded_file)
        elif uploaded_file.type in ["text/csv", "text/plain"]:
            df = pd.read_csv(uploaded_file)
        else:
            st.error("Unsupported file type, using sample data.")
            df = generate_sample_data()
    except:
        st.error("Error reading file, using sample data.")
        df = generate_sample_data()
else:
    df = generate_sample_data()

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
else:
    df["timestamp"] = pd.to_datetime(datetime.now())

# -----------------------------
# Isolation Forest
# -----------------------------
model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly"] = model.fit_predict(df[["value"]])
df["malicious"] = df["anomaly"].apply(lambda x: "Yes" if x==-1 else "No")

# -----------------------------
# Filters
# -----------------------------
st.sidebar.header("Filters")
ip_search = st.sidebar.text_input("Search by IP:")
record_filter = st.sidebar.multiselect("Filter by Record Type", options=df["record_type"].unique())
malicious_filter = st.sidebar.selectbox("Malicious Only?", ["All", "Yes", "No"])

filtered_data = df.copy()
if ip_search:
    filtered_data = filtered_data[filtered_data["ip"].astype(str).str.contains(ip_search)]
if record_filter:
    filtered_data = filtered_data[filtered_data["record_type"].isin(record_filter)]
if malicious_filter != "All":
    filtered_data = filtered_data[filtered_data["malicious"] == malicious_filter]

# -----------------------------
# Dashboard Layout
# -----------------------------
st.title("KNet Cybersecurity Dashboard - Using Model Context Protocol (MCP)")
st.markdown("Monitor anomalous and malicious events in real-time")

# Metrics cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Events", len(filtered_data))
col2.metric("Malicious Events", len(filtered_data[filtered_data["malicious"]=="Yes"]))
col3.metric("Unique IPs", filtered_data["ip"].nunique())

# Tabs for organized layout
tabs = st.tabs(["Overview", "Charts", "Download Data"])

# -----------------------------
# Overview Tab
# -----------------------------
with tabs[0]:
    st.subheader("Event Data Preview")
    st.dataframe(filtered_data.head(20))

# -----------------------------
# Charts Tab
# -----------------------------
with tabs[1]:
    # Pie chart of malicious breakdown
    st.subheader("Malicious Activity Breakdown")
    malicious_counts = filtered_data[filtered_data["malicious"]=="Yes"]["record_type"].value_counts()
    if not malicious_counts.empty:
        fig1, ax1 = plt.subplots()
        ax1.pie(malicious_counts, labels=malicious_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors)
        ax1.axis('equal')
        st.pyplot(fig1)
    else:
        st.info("No malicious events found.")

    # Trend over time
    st.subheader("📈 Malicious Activity Trend")
    trend = filtered_data[filtered_data["malicious"]=="Yes"].groupby(pd.Grouper(key="timestamp", freq="1H")).size()
    if not trend.empty:
        fig2, ax2 = plt.subplots()
        trend.plot(ax=ax2, marker='o', color='red')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Malicious Events")
        ax2.set_title("Malicious Events Over Time")
        st.pyplot(fig2)
    else:
        st.info("No trend data available.")

    # Top offending IPs
    st.subheader("Top Source IPs")
    top_ips = filtered_data["ip"].value_counts().head(20)
    fig3, ax3 = plt.subplots()
    top_ips.plot(kind='bar', ax=ax3, color='orange')
    ax3.set_ylabel("Event Count")
    st.pyplot(fig3)

# -----------------------------
# Download Tab
# -----------------------------
with tabs[2]:
    st.subheader("⬇️ Download Filtered Data")
    csv_data = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv_data, file_name="cyber_threats.csv", mime="text/csv")
    json_data = filtered_data.to_json(orient='records', date_format='iso').encode('utf-8')
    st.download_button("Download JSON", json_data, file_name="cyber_threats.json", mime="application/json")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("© 2025 KalsNet Consulting — Prototype Cybersecurity Monitor")
