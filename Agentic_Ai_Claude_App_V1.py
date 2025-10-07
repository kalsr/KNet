


# python
# Agentic_Ai_Claude_App_V1.py
# Agentic AI (Claude) Threat Analyzer – developed by Randy Singh, KNet Consulting Group

import streamlit as st
import pandas as pd
import random, json, io, os
import matplotlib.pyplot as plt

# Try importing Anthropic API
try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Agentic AI (Claude) Threat Analyzer", layout="wide")
st.title(" Agentic AI (Claude) Threat Intelligence Dashboard - Designed By Randy Singh")

# -------------------------------
# ANTHROPIC CLIENT INITIALIZATION
# -------------------------------
api_key = os.getenv("ANTHROPIC_API_KEY")
if Anthropic and api_key:
    client = Anthropic(api_key=api_key)
    anthropic_enabled = True
else:
    client = None
    anthropic_enabled = False

# -------------------------------
# FUNCTIONS
# -------------------------------
def generate_sample_data(n=20):
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


def detect_severity_column(df):
    """Try to find a column that represents severity."""
    for col in df.columns:
        if "severity" in col.lower():
            return col
    return None


def analyze_with_agentic_ai(df):
    """Use Anthropic Claude if available; otherwise use rule-based AI."""
    sev_col = detect_severity_column(df)

    if anthropic_enabled:
        prompt = f"""
        You are an AI cyber-threat analyst. Analyze the following threat dataset and summarize:
        1. Common threat patterns
        2. Severity distribution
        3. Recommended mitigations

        Data:
        {df.to_json(orient='records', indent=2)}
        """
        try:
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f" Claude API error: {e}"

    # ---------- FALLBACK (if no Anthropic key) ----------
    summary = " Local AI Summary (No Anthropic key detected)\n\n"
    if sev_col:
        severity_counts = df[sev_col].value_counts()
        summary += "Severity Distribution:\n"
        for s, c in severity_counts.items():
            summary += f"- {s}: {c}\n"
    else:
        summary += "No severity column found; showing only general recommendations.\n"
    summary += "\nRecommendations:\n"
    summary += "• Strengthen email filtering and MFA for phishing.\n"
    summary += "• Patch systems regularly to prevent exploits.\n"
    summary += "• Implement network segmentation and regular audits.\n"
    return summary


def plot_pie_chart(df):
    """Generate a pie chart if a severity column is found."""
    sev_col = detect_severity_column(df)
    if not sev_col:
        st.warning(" No 'Severity' column found for visualization.")
        return
    severity_counts = df[sev_col].value_counts()
    fig, ax = plt.subplots()
    ax.pie(severity_counts, labels=severity_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)


def convert_to_bytes(df, file_format):
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
# UI LAYOUT
# -------------------------------
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    sample_n = st.number_input("Records", min_value=10, max_value=100, step=10, value=20)
with col2:
    btn_generate = st.button(" Generate Sample Data", use_container_width=True)
with col3:
    uploaded_file = st.file_uploader("Upload CSV", type="csv", label_visibility="collapsed")
with col4:
    btn_analyze = st.button(" Run Agentic AI Analysis", use_container_width=True)
with col5:
    btn_download = st.button(" Download Results", use_container_width=True)
with col6:
    btn_reset = st.button(" Reset Data", use_container_width=True)

# Style Buttons
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #218838;
        color: white;
    }
    div.stButton:nth-child(6) > button {
        background-color: #dc3545 !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SESSION STATE
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
    st.success(f" Generated {sample_n} sample records.")

if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file)
    st.success(" Uploaded dataset successfully.")

if btn_analyze:
    if not st.session_state.df.empty:
        with st.spinner("Analyzing threats..."):
            st.session_state.analysis = analyze_with_agentic_ai(st.session_state.df)
        st.success(" Agentic AI analysis complete!")
    else:
        st.warning(" Please generate or upload data first.")

if btn_download:
    if not st.session_state.df.empty:
        csv_bytes = convert_to_bytes(st.session_state.df, "csv")
        json_bytes = convert_to_bytes(st.session_state.df, "json")
        xlsx_bytes = convert_to_bytes(st.session_state.df, "excel")

        st.download_button(" Download CSV", data=csv_bytes, file_name="analysis.csv")
        st.download_button(" Download JSON", data=json_bytes, file_name="analysis.json")
        st.download_button(" Download Excel", data=xlsx_bytes, file_name="analysis.xlsx")
    else:
        st.warning(" No data to download.")

if btn_reset:
    st.session_state.df = pd.DataFrame()
    st.session_state.analysis = ""
    st.success(" All data cleared. Ready to start again!")

# -------------------------------
# DISPLAY OUTPUT
# -------------------------------
if not st.session_state.df.empty:
    st.subheader(" Threat Dataset")
    st.dataframe(st.session_state.df, use_container_width=True)
    plot_pie_chart(st.session_state.df)

if st.session_state.analysis:
    st.subheader(" Agentic AI Analysis Result")
    st.write(st.session_state.analysis)

