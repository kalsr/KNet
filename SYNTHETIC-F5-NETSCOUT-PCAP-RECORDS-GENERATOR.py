# SYNTHETIC-F5-NETSCOUT-PCAP-RECORDS-GENERATOR
#Features included:
#1. Generate multiple record types: F5, NetScout, PCAP, PCAP Parsed
#2. Filter/search records interactively
#3. Upload/download JSON, CSV, Excel
#4. Clear records feature
#5. **Summary cards** for total records, malicious count, non-malicious count, and per-record type counts
# 6. **Bar chart**: Malicious vs Non-Malicious counts
# 7. **Pie chart**: Malicious vs Non-Malicious distribution
# 8. **Time-series line chart**: Malicious activity over time per record type
# 9. **Pie chart**: Malicious reason breakdown
# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTANTS.

# python
# app.py
# SOC-style Dashboard for F5 / NetScout / PCAP Records

import streamlit as st
import pandas as pd
import json
import random
import io
import matplotlib.pyplot as plt

# ------------------------------
# Utility Functions
# ------------------------------
def generate_record(record_type):
    record = {
        "record_type": record_type,
        "timestamp": random.randint(1609459200, 1672444800),  # 2021–2023
        "source_ip": f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
        "destination_ip": f"10.0.{random.randint(0,255)}.{random.randint(0,255)}",
        "data_volume": round(random.uniform(0.1, 100.0), 2)
    }
    if random.choice([True, False]):
        record["api_status"] = "malicious"
        record["reason"] = random.choice([
            "SQL Injection attempt detected",
            "Cross-Site Scripting (XSS) attack detected",
            "Unauthorized access attempt detected",
            "API abuse detected with high frequency requests"
        ])
    else:
        record["api_status"] = "non-malicious"
        record["reason"] = "Legitimate API usage"
    return record

def convert_df(df, file_format="json"):
    if file_format == "json":
        return df.to_json(orient="records", indent=4).encode("utf-8")
    elif file_format == "csv":
        return df.to_csv(index=False).encode("utf-8")
    elif file_format == "excel":
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Records")
        return buffer.getvalue()

def timestamp_to_date(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["timestamp"], unit="s").dt.date
    return df

# ------------------------------
# Streamlit App Layout
# ------------------------------
st.set_page_config(page_title="SOC Dashboard", layout="wide")
st.title("🛡️ SOC Dashboard: F5 / NetScout / PCAP Records")
st.caption("Generate, analyze, visualize, and download API records (malicious & non-malicious)")

# Initialize session state
if "records" not in st.session_state:
    st.session_state.records = pd.DataFrame()

# Sidebar Options
st.sidebar.header("Options")
record_type = st.sidebar.selectbox("Choose Record Type", ["F5", "NetScout", "PCAP", "PCAP Parsed"])
num_records = st.sidebar.number_input("Number of Records to Generate", 1, 500, 20)
if st.sidebar.button("Generate Records"):
    new_data = [generate_record(record_type) for _ in range(num_records)]
    st.session_state.records = pd.concat([st.session_state.records, pd.DataFrame(new_data)], ignore_index=True)
    st.success(f"Generated {num_records} {record_type} records.")

if st.sidebar.button("Clear Records"):
    st.session_state.records = pd.DataFrame()
    st.warning("All records cleared.")

# Upload Records
uploaded_file = st.sidebar.file_uploader("Upload Records (JSON, CSV, Excel)", type=["json", "csv", "xlsx"])
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".json"):
            data = json.load(uploaded_file)
            st.session_state.records = pd.DataFrame(data)
        elif uploaded_file.name.endswith(".csv"):
            st.session_state.records = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            st.session_state.records = pd.read_excel(uploaded_file)
        st.success("Records uploaded successfully.")
    except Exception as e:
        st.error(f"Error uploading file: {e}")

# Main Dashboard
if not st.session_state.records.empty:
    df = st.session_state.records.copy()

    # Search and Filter
    st.subheader("🔍 Records Table")
    search_term = st.text_input("Search (IP, status, reason, etc.)")
    filter_status = st.selectbox("Filter by Status", ["All", "malicious", "non-malicious"])
    if search_term:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    if filter_status != "All":
        df = df[df["api_status"] == filter_status]
    st.dataframe(df, use_container_width=True)

    # ------------------------------
    # Summary Cards
    # ------------------------------
    st.subheader("📊 Summary")
    total_records = len(df)
    total_malicious = len(df[df["api_status"]=="malicious"])
    total_non_malicious = len(df[df["api_status"]=="non-malicious"])
    record_type_counts = df["record_type"].value_counts()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", total_records)
    col2.metric("Malicious Records", total_malicious)
    col3.metric("Non-Malicious Records", total_non_malicious)

    st.write("**Records per Type:**")
    st.bar_chart(record_type_counts)

    # ------------------------------
    # Charts Section
    # ------------------------------
    st.subheader("📈 Visualizations")

    # 1. Bar chart: Malicious vs Non-Malicious
    counts = df["api_status"].value_counts()
    st.write("Malicious vs Non-Malicious Count:")
    st.bar_chart(counts)

    # 2. Pie chart: Malicious vs Non-Malicious
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=["#ff6b6b","#4ecdc4"], startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

    # 3. Time-based Trend
    st.write("Time-Based Malicious Activity Trend:")
    df_dates = timestamp_to_date(df)
    trend_df = df_dates[df_dates["api_status"]=="malicious"].groupby(["date", "record_type"]).size().unstack(fill_value=0)
    if not trend_df.empty:
        st.line_chart(trend_df)

    # 4. Malicious Reason Breakdown
    st.write("Malicious Reason Breakdown:")
    malicious_reasons = df[df["api_status"]=="malicious"]["reason"].value_counts()
    if not malicious_reasons.empty:
        fig2, ax2 = plt.subplots()
        ax2.pie(malicious_reasons, labels=malicious_reasons.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
        ax2.axis('equal')
        st.pyplot(fig2)
    else:
        st.info("No malicious records to display reason breakdown.")

    # ------------------------------
    # Download Section
    # ------------------------------
    st.subheader("⬇️ Download Records")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button("Download JSON", data=convert_df(df, "json"), file_name="records.json", mime="application/json")
    with col2:
        st.download_button("Download CSV", data=convert_df(df, "csv"), file_name="records.csv", mime="text/csv")
    with col3:
        st.download_button("Download Excel", data=convert_df(df, "excel"), file_name="records.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

else:
    st.info("No records generated yet. Use the sidebar to generate or upload records.")






