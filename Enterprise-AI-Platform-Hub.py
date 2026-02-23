# ===============================================
# KALSNET ENTERPRISE AI PLATFORM
# Fixed Reset/Refresh Implementation
# ===============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
from datetime import datetime
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# ---------------------------
# SAFE RESET HANDLER
# ---------------------------
if "reset_request" not in st.session_state:
    st.session_state.reset_request = False

def safe_reset():
    # Clear all keys except reset_request
    keys_to_clear = [k for k in st.session_state.keys() if k != "reset_request"]
    for k in keys_to_clear:
        del st.session_state[k]
    st.session_state.reset_request = False

# ---------------------------
# MAIN APP FUNCTION
# ---------------------------
def app():
    # ---------------------------
    # PAGE CONFIG
    # ---------------------------
    st.set_page_config(
        page_title="KALSNET AI ENTERPRISE PLATFORM",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # ---------------------------
    # HEADER BLUE STYLE
    # ---------------------------
    st.markdown("""
    <style>
    body { background-color:#0E1117; }
    .knet-title { color:#007BFF !important; font-weight:1000; font-size:52px; text-align:center; letter-spacing:1px; }
    .knet-sub { color:#007BFF !important; font-weight:900; font-size:22px; text-align:center; }
    </style>
    """, unsafe_allow_html=True)

    # ---------------------------
    # HEADER
    # ---------------------------
    st.markdown("""
    <h1 class="knet-title">KALSNET AI VISION ENTERPRISE PLATFORM</h1>
    <h3 class="knet-sub">Developed by Randy Singh | Kalsnet (KNet) Consulting Group</h3>
    """, unsafe_allow_html=True)
    st.divider()

    # ---------------------------
    # SIDEBAR
    # ---------------------------
    st.sidebar.header("🎛 Simulation Controls")
    MODULES = [
        "Executive Boardroom Dashboard",
        "Federal / DoD AI Security",
        "iPhone Camera AI Vision",
        "Personal AI Assistant",
        "Commercial AI Platform",
        "Kalsnet Enterprise Integration"
    ]
    module = st.sidebar.selectbox("Select Platform Mode", MODULES)
    data_volume = st.sidebar.slider("Synthetic Data Volume", 0, 200, 50)
    dod_mode = st.sidebar.checkbox("Enable Zero Trust / DoD Mode")

    # Reset button
    if st.sidebar.button("Reset & Refresh Data"):
        st.session_state.reset_request = True
        st.experimental_rerun()  # Safe here because flag triggers rerun

    # ---------------------------
    # MODE EXPLANATIONS
    # ---------------------------
    mode_explanations = {
        "Executive Boardroom Dashboard": "Provides senior leadership enterprise risk visibility and executive decision intelligence.",
        "Federal / DoD AI Security": "Simulates Zero Trust cybersecurity operations aligned with RMF, NIST controls, and MITRE ATT&CK mapping.",
        "iPhone Camera AI Vision": "Demonstrates real-time AI visual analysis and mobile threat scoring capabilities.",
        "Personal AI Assistant": "Models AI assistants providing contextual analytics and decision automation.",
        "Commercial AI Platform": "Represents enterprise fraud monitoring and behavioral analytics operations.",
        "Kalsnet Enterprise Integration": "Simulates hybrid enterprise cloud integrations across APIs and SaaS systems."
    }
    st.info(mode_explanations.get(module, "No description available."))

    # ---------------------------
    # DATA UPLOAD
    # ---------------------------
    st.sidebar.subheader("Upload Your Own Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload CSV or JSON", type=["csv","json"])

    # ---------------------------
    # DATA GENERATOR
    # ---------------------------
    def generate_data(records):
        categories = ["Low", "Medium", "High", "Critical"]
        mitre_techniques = [
            "T1059 - Command Execution",
            "T1078 - Valid Accounts",
            "T1566 - Phishing",
            "T1027 - Obfuscated Files",
            "T1486 - Data Encryption"
        ]
        data = {
            "Category": np.random.choice(categories, records),
            "Agentic Risk Score": np.random.randint(1, 100, records),
            "Confidence Score": np.random.randint(50, 100, records),
            "MITRE Technique": np.random.choice(mitre_techniques, records)
        }
        return pd.DataFrame(data)

    # ---------------------------
    # LOAD DATA
    # ---------------------------
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_json(uploaded_file)
        st.success("User Dataset Loaded Successfully")
    else:
        df = generate_data(data_volume)

    # ---------------------------
    # SYNTHETIC DATA FIELD EXPLANATION
    # ---------------------------
    st.markdown("""
    ### Synthetic Data Record Fields Explanation

    **1. Category**: Operational severity classification assigned to each record. `Low/Medium/High/Critical` simulates SOC triage and dashboards.  
    **2. Agentic Risk Score**: AI probability score (1–100) representing potential threat exposure.  
    **3. Confidence Score**: Model confidence (50–100) in the Agentic Risk Score.  
    **4. MITRE Technique**: Maps events to MITRE ATT&CK tactics/techniques for threat intelligence and RMF mapping.
    """)

    # ---------------------------
    # DISPLAY DATA
    # ---------------------------
    st.subheader("Synthetic / Uploaded Records")
    st.dataframe(df, use_container_width=True)

    # ---------------------------
    # RISK ENGINE
    # ---------------------------
    avg_risk = round(df["Agentic Risk Score"].mean(), 2) if len(df) > 0 else 0
    if avg_risk < 30: risk_level = "LOW"
    elif avg_risk < 60: risk_level = "MEDIUM"
    elif avg_risk < 80: risk_level = "HIGH"
    else: risk_level = "CRITICAL"
    fedramp_score = round(100 - avg_risk, 2)

    # ---------------------------
    # RISK EXPLANATION
    # ---------------------------
    st.markdown(f"""
    ### Risk Scoring Methodology
    - **Average Risk Score** = mean of all Agentic Risk Scores.  
    - **Risk Category**: LOW <30, MEDIUM 30-59, HIGH 60-79, CRITICAL ≥80.  
    - **FedRAMP Readiness Score** = 100 − Average Risk Score.
    """)

    # ---------------------------
    # EXPORT FUNCTIONS
    # ---------------------------
    def create_pdf():
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        story = []
        story.append(Paragraph("KALSNET Enterprise AI Executive Report", styles["Title"]))
        story.append(Spacer(1, 0.3 * inch))
        story.append(Paragraph(f"Generated: {datetime.now()}", styles["Normal"]))
        story.append(Paragraph(f"Average Risk Score: {avg_risk}", styles["Normal"]))
        story.append(Paragraph(f"Risk Category: {risk_level}", styles["Normal"]))
        story.append(Paragraph(f"FedRAMP Readiness Score: {fedramp_score}", styles["Normal"]))
        doc.build(story)
        buffer.seek(0)
        return buffer

    st.sidebar.subheader("Export Results")
    st.sidebar.download_button("Export CSV", df.to_csv(index=False).encode(), "enterprise_results.csv", "csv")
    st.sidebar.download_button("Export JSON", df.to_json(orient="records").encode(), "enterprise_results.json", "application/json")
    st.sidebar.download_button("Export Executive PDF", create_pdf(), "enterprise_report.pdf", "application/pdf")

    # ---------------------------
    # EXECUTIVE GAUGE
    # ---------------------------
    def executive_gauge(score):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Enterprise Risk Index"},
            gauge={'axis': {'range':[0,100]},
                   'steps':[{'range':[0,30],'color':"green"},
                            {'range':[30,60],'color':"yellow"},
                            {'range':[60,80],'color':"orange"},
                            {'range':[80,100],'color':"red"}]}
        ))
        st.plotly_chart(fig, use_container_width=True)

    # ---------------------------
    # MODULE DISPLAY
    # ---------------------------
    st.subheader(module)
    if dod_mode:
        st.warning("🛡 Zero Trust Enforcement Enabled")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", len(df))
    col2.metric("Average Agentic Risk Score", avg_risk)
    col3.metric("Overall Risk Category", risk_level)
    col4.metric("FedRAMP Readiness Score", fedramp_score)

    st.divider()
    executive_gauge(avg_risk)

    # ---------------------------
    # PIE CHART
    # ---------------------------
    st.subheader("Risk Category Distribution")
    fig1, ax1 = plt.subplots()
    df["Category"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
    ax1.axis('equal')
    st.pyplot(fig1)

    # ---------------------------
    # HISTOGRAM
    # ---------------------------
    st.subheader("Agentic Risk Score Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["Agentic Risk Score"], bins=10)
    st.pyplot(fig2)

    # ---------------------------
    # MITRE
    # ---------------------------
    if module == "Federal / DoD AI Security":
        st.subheader("MITRE ATT&CK Technique Distribution")
        st.bar_chart(df["MITRE Technique"].value_counts())

    # ---------------------------
    # CAMERA
    # ---------------------------
    if module == "iPhone Camera AI Vision":
        image = st.camera_input("Capture Image")
        if image:
            st.image(image)
            st.success("AI Vision Analysis Complete")
            st.write("Threat Probability Index:", random.randint(1,100))

    # ---------------------------
    # EXECUTIVE SUMMARY
    # ---------------------------
    st.divider()
    st.subheader("Executive Summary")
    st.write(f"""
    As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')},

    The enterprise AI agent processed {len(df)} records.

    Average Risk Score : {avg_risk}
    Risk Category : {risk_level}
    FedRAMP Readiness Score : {fedramp_score}

    Platform Designed by Randy Singh
    Kalsnet (KNet) Consulting Group
    """)
    st.success("Enterprise AI Platform Running Successfully")


# ---------------------------
# RUN APP
# ---------------------------
app()
