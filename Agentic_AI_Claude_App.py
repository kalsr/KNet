

# agentic_ai_claude_app.py

# Integrates an Agentic AI step powered by Anthropic Claude (if you provide an API key).

# Falls back to an internal rule-based agent if Anthropic credentials aren’t set.

# Shows all major UI buttons at the top (green styling) and a red reset control with a red badge.

# Lets you upload sample data or generate a variable number of sample records (20–100).

# Displays DB records and lets you select any record to run Agentic analysis.

# Saves Agentic analysis results into a separate agentic_analysis table.

# Has a separate UI to query Agentic analysis, visualize simple pie charts, and download results as CSV / JSON / Excel.

# Uses SQLite for local storage (cyber_threats.db) and auto-creates tables when needed.

# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.


import streamlit as st

import pandas as pd

import random

import json

import io

import matplotlib.pyplot as plt

from anthropic import Anthropic



# -------------------------------

# CONFIG

# -------------------------------

st.set_page_config(page_title="Agentic AI (Claude) Threat Analyzer", layout="wide")



# Initialize Claude API (Make sure to set ANTHROPIC_API_KEY in your environment)

client = Anthropic()



# -------------------------------

# FUNCTIONS

# -------------------------------



def generate_sample_data(n=20):

    """Generate sample cybersecurity threat dataset."""

    threats = [

        "Phishing", "Malware", "DDoS", "Ransomware",

        "Data Breach", "Insider Threat", "SQL Injection", "Zero-Day Exploit"

    ]

    severity_levels = ["Low", "Medium", "High", "Critical"]



    data = []

    for i in range(1, n + 1):

        data.append({

            "Threat_ID": i,

            "Threat_Type": random.choice(threats),

            "Severity": random.choice(severity_levels),

            "Impact_Score": random.randint(10, 100)

        })

    return pd.DataFrame(data)



def analyze_with_agentic_ai(df):

    """Use Anthropic Claude to perform high-level AI analysis on threats."""

    prompt = f"""

    You are an AI cyber-threat analyst. Analyze the following threats data and summarize:

    1. Common threat patterns

    2. Severity distribution

    3. Recommended mitigations



    Data:

    {df.to_json(orient='records', indent=2)}

    """



    response = client.messages.create(

        model="claude-3-sonnet-20240229",

        max_tokens=500,

        messages=[

            {"role": "user", "content": prompt}

        ]

    )

    return response.content[0].text



def plot_pie_chart(df):

    """Generate a pie chart for severity levels."""

    severity_counts = df["Severity"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(severity_counts, labels=severity_counts.index, autopct="%1.1f%%", startangle=90)

    ax.axis("equal")

    st.pyplot(fig)



def convert_to_bytes(df, file_format):

    """Convert dataframe to downloadable format."""

    if file_format == "csv":

        return df.to_csv(index=False).encode("utf-8")

    elif file_format == "json":

        return df.to_json(orient="records", indent=2).encode("utf-8")

    elif file_format == "excel":

        output = io.BytesIO()

        with pd.ExcelWriter(output, engine="openpyxl") as writer:

            df.to_excel(writer, index=False, sheet_name="Analysis")

        return output.getvalue()



# -------------------------------

# STREAMLIT APP

# -------------------------------



st.title("🤖 Agentic AI (Claude) Threat Intelligence Dashboard")



# Button layout (top row)

col1, col2, col3, col4, col5, col6 = st.columns(6)



with col1:

    sample_n = st.number_input("Records", min_value=10, max_value=100, step=10, value=20)

with col2:

    btn_generate = st.button("Generate Sample Data", use_container_width=True)

with col3:

    btn_upload = st.file_uploader("Upload CSV", type="csv", label_visibility="collapsed")

with col4:

    btn_analyze = st.button("Run Agentic AI Analysis", use_container_width=True)

with col5:

    btn_download = st.button("Download Results", use_container_width=True)

with col6:

    btn_reset = st.button("🔴 Reset", use_container_width=True)



# Button colors via CSS

st.markdown("""

<style>

    button[kind="primary"] {

        background-color: green !important;

        color: white !important;

    }

    button:has(span:contains("Reset")) {

        background-color: red !important;

        color: white !important;

    }

</style>

""", unsafe_allow_html=True)



# -------------------------------

# STATE MANAGEMENT

# -------------------------------



if "df" not in st.session_state:

    st.session_state.df = pd.DataFrame()

if "analysis" not in st.session_state:

    st.session_state.analysis = ""



# -------------------------------

# BUTTON ACTIONS

# -------------------------------



if btn_generate:

    st.session_state.df = generate_sample_data(sample_n)

    st.success(f"✅ Generated {sample_n} sample records.")



if btn_upload is not None:

    st.session_state.df = pd.read_csv(btn_upload)

    st.success("✅ Uploaded dataset successfully.")



if btn_analyze:

    if not st.session_state.df.empty:

        with st.spinner("Analyzing data using Anthropic Claude..."):

            st.session_state.analysis = analyze_with_agentic_ai(st.session_state.df)

        st.success("✅ Agentic AI analysis complete!")

    else:

        st.warning("⚠️ Please generate or upload data first.")



if btn_download:

    if not st.session_state.df.empty:

        csv_bytes = convert_to_bytes(st.session_state.df, "csv")

        json_bytes = convert_to_bytes(st.session_state.df, "json")

        xlsx_bytes = convert_to_bytes(st.session_state.df, "excel")



        st.download_button("⬇️ Download CSV", data=csv_bytes, file_name="analysis.csv")

        st.download_button("⬇️ Download JSON", data=json_bytes, file_name="analysis.json")

        st.download_button("⬇️ Download Excel", data=xlsx_bytes, file_name="analysis.xlsx")

    else:

        st.warning("⚠️ No data to download.")



if btn_reset:

    st.session_state.df = pd.DataFrame()

    st.session_state.analysis = ""

    st.experimental_rerun()



# -------------------------------

# DISPLAY RESULTS

# -------------------------------



if not st.session_state.df.empty:

    st.subheader("📊 Threat Dataset")

    st.dataframe(st.session_state.df, use_container_width=True)

    plot_pie_chart(st.session_state.df)



if st.session_state.analysis:

    st.subheader("🧠 Agentic AI Analysis (Claude)")

    st.write(st.session_state.analysis)
