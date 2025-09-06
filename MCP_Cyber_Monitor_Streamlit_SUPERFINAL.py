
# Full Fixed Code (`mcp_cyber_monitor_streamlit_SUPERFINAL.py`)
# THIS USE-CASE IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.

# python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from io import StringIO, BytesIO
import json

# ---------------------------------
# App Configuration
# ---------------------------------
st.set_page_config(page_title="KalsNet Cyber Monitor", layout="wide")

# ---------------------------------
# Sidebar: Auto-refresh & Manual Refresh
# ---------------------------------
st.sidebar.header(" Refresh Controls")

refresh_rate = st.sidebar.number_input(
    "Auto-refresh interval (seconds)", min_value=10, max_value=600, value=60, step=10
)

# Auto-refresh component
count = st_autorefresh(interval=refresh_rate * 1000, key="auto_refresh")

# Manual refresh button
if st.sidebar.button("Manual Refresh"):
    count += 1  # triggers page refresh safely

st.sidebar.markdown(f" Next auto-refresh in **{refresh_rate} seconds**")

# ---------------------------------
# Title
# ---------------------------------
st.title("KNet Cybersecurity Threat Monitor - Model Contro Protocol (MCP)")
st.caption("AI-Powered Monitoring Dashboard for Anomaly Detection & Cyber Threat trends.")

# ---------------------------------
# Generate Sample Data
# ---------------------------------
@st.cache_data
def generate_sample_data(n=300):
    np.random.seed(42)
    timestamps = [datetime.now() - timedelta(minutes=i*5) for i in range(n)]
    ip_addresses = [f"192.168.1.{np.random.randint(1,255)}" for _ in range(n)]
    record_types = np.random.choice(
        ["Login", "File Access", "Malware", "Phishing", "Port Scan", "Other"],
        size=n,
        p=[0.3, 0.25, 0.15, 0.1, 0.1, 0.1]
    )
    values = np.random.normal(loc=50, scale=10, size=n)
    df = pd.DataFrame({
        "timestamp": timestamps,
        "ip": ip_addresses,
        "record_type": record_types,
        "value": values
    })
    return df

# ---------------------------------
# File Upload / Sample Data
# ---------------------------------
st.sidebar.header("📂 Upload Your Data")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV, JSON, or TXT file", type=['csv', 'json', 'txt']
)

if uploaded_file is not None:
    try:
        if uploaded_file.type == "application/json":
            df = pd.read_json(uploaded_file)
        elif uploaded_file.type in ["text/csv", "text/plain"]:
            df = pd.read_csv(uploaded_file)  # CSV or TXT
        else:
            st.error("Unsupported file type!")
            df = generate_sample_data(300)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        df = generate_sample_data(300)
else:
    # Use sample data if no upload
    df = generate_sample_data(300)

# Ensure timestamp column exists
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
else:
    df["timestamp"] = pd.to_datetime(datetime.now())

# ---------------------------------
# Anomaly Detection
# ---------------------------------
model = IsolationForest(contamination=0.1, random_state=42)
df["anomaly"] = model.fit_predict(df[["value"]])
df["malicious"] = df["anomaly"].apply(lambda x: "Yes" if x == -1 else "No")

# ---------------------------------
# Sidebar Filters
# ---------------------------------
st.sidebar.header("🔎 Filters")
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

# ---------------------------------
# Dashboard Section
# ---------------------------------
st.subheader("📊 Security Events Overview")
st.dataframe(filtered_data.head(20))

# Pie Chart Breakdown
st.subheader("Malicious Activity Breakdown")
malicious_counts = filtered_data[filtered_data["malicious"]=="Yes"]["record_type"].value_counts()
if not malicious_counts.empty:
    fig1, ax1 = plt.subplots()
    ax1.pie(malicious_counts, labels=malicious_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
else:
    st.info("No malicious events found for selected filters.")

# Time-based Trend
st.subheader("📈 Malicious Activity Trend")
trend = filtered_data[filtered_data["malicious"]=="Yes"].groupby(
    pd.Grouper(key="timestamp", freq="1H")
).size()
if not trend.empty:
    fig2, ax2 = plt.subplots()
    trend.plot(ax=ax2, marker="o")
    ax2.set_title("Malicious Events Over Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Number of Malicious Events")
    st.pyplot(fig2)
else:
    st.info("No malicious trend data available for selected filters.")

# ---------------------------------
# Download options
# ---------------------------------
st.subheader("⬇️ Download Data")
csv = filtered_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download filtered dataset as CSV",
    data=csv,
    file_name="cyber_threats.csv",
    mime="text/csv"
)

json_data = filtered_data.to_json(orient='records', date_format='iso').encode('utf-8')
st.download_button(
    label="Download filtered dataset as JSON",
    data=json_data,
    file_name="cyber_threats.json",
    mime="application/json"
)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")
st.caption("© 2025 KalsNet Consulting — Prototype Cybersecurity Monitor")