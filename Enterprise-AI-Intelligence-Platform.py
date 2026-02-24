# ===============================================
# KALSNET ENTERPRISE AI PLATFORM
# ENTERPRISE MODE INTELLIGENCE VERSION
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


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
page_title="KALSNET AI ENTERPRISE PLATFORM",
layout="wide"
)

# ---------------------------------------------------
# STYLE (FIXED BLUE HEADER + WHITE MODE TEXT)
# ---------------------------------------------------

st.markdown("""

<style>

.knet-title{
color:#007BFF !important;
font-size:52px;
font-weight:1000;
text-align:center;
}

.knet-sub{
color:#007BFF !important;
font-size:22px;
font-weight:900;
text-align:center;
}

.mode-box{
background-color:#111827;
padding:18px;
border-radius:10px;
border:1px solid #1F2937;
margin-bottom:15px;
}

.mode-header{
color:#00AEEF;
font-size:34px;
font-weight:900;
}

.mode-text{
color:white !important;
font-size:16px;
line-height:1.6;
}

</style>

""",unsafe_allow_html=True)


# ---------------------------------------------------
# HEADER (BLUE RESTORED)
# ---------------------------------------------------

st.markdown("""

<h1 class="knet-title">

KALSNET AI VISION ENTERPRISE PLATFORM

</h1>

<h3 class="knet-sub">

Developed by Randy Singh | Kalsnet (KNet) Consulting Group

</h3>

""",unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "df" not in st.session_state:
    st.session_state.df=None


# ---------------------------------------------------
# DATA GENERATOR
# ---------------------------------------------------

def generate_data(records):

    categories=["Low","Medium","High","Critical"]

    mitre=[
"T1059 - Command Execution",
"T1078 - Valid Accounts",
"T1566 - Phishing",
"T1027 - Obfuscated Files",
"T1486 - Data Encryption"
]

    return pd.DataFrame({

"Category":np.random.choice(categories,records),

"Agentic Risk Score":np.random.randint(1,100,records),

"Confidence Score":np.random.randint(50,100,records),

"MITRE Technique":np.random.choice(mitre,records)

})

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("Simulation Controls")

MODULES=[

"Executive Boardroom Dashboard",
"Federal / DoD AI Security",
"iPhone Camera AI Vision",
"Personal AI Assistant",
"Commercial AI Platform",
"Kalsnet Enterprise Integration"

]

module=st.sidebar.selectbox(
"Select Platform Mode",
MODULES
)

volume=st.sidebar.slider(
"Synthetic Data Volume",
0,
200,
50
)

dod_mode=st.sidebar.checkbox(
"Enable Zero Trust / DoD Mode"
)

if st.sidebar.button("Reset & Refresh Data"):

    st.session_state.df=generate_data(volume)

    st.success("Dataset Reset Successfully")


# ---------------------------------------------------
# UPLOAD
# ---------------------------------------------------

uploaded=st.sidebar.file_uploader(
"Upload CSV or JSON",
["csv","json"]
)

if uploaded:

    if uploaded.name.endswith(".csv"):

        st.session_state.df=pd.read_csv(uploaded)

    else:

        st.session_state.df=pd.read_json(uploaded)

    st.success("User Dataset Loaded Successfully")

elif st.session_state.df is None:

    st.session_state.df=generate_data(volume)

df=st.session_state.df


# ---------------------------------------------------
# MODE DETAILS (WHITE READABLE)
# ---------------------------------------------------

mode_details={

"Executive Boardroom Dashboard":

"""
Executive leadership visibility environment designed for CIOs, CISOs, SES leadership, and Board Directors.

Provides enterprise operational awareness across cybersecurity exposure, compliance readiness, and mission performance indicators enabling rapid executive decision making.
""",

"Federal / DoD AI Security":

"""
Simulates Zero Trust cyber defense operations aligned with RMF authorization workflows and MITRE ATT&CK threat intelligence.

Supports SOC monitoring, ConMon compliance, insider threat analytics, and ATO readiness demonstrations used by Federal civilian agencies and DoD missions.
""",

"iPhone Camera AI Vision":

"""
Demonstrates mobile edge AI intelligence using live camera capture.

Supports facility inspections, threat recognition, homeland security field analytics, and operational situational awareness scenarios.
""",

"Personal AI Assistant":

"""
AI copilot providing contextual enterprise advisory analytics supporting executive awareness, risk interpretation, and productivity automation.
""",

"Commercial AI Platform":

"""
Fraud detection and behavioral analytics simulation supporting banking, healthcare, insurance, and enterprise anomaly monitoring operations.
""",

"Kalsnet Enterprise Integration":

"""
Hybrid enterprise integration simulation demonstrating interoperability between AI analytics platforms, cloud environments, and modernization initiatives.
"""
}

st.markdown(f"""

<div class="mode-box">

<div class="mode-header">

Selected Platform Mode — {module}

</div>

<div class="mode-text">

{mode_details[module]}

</div>

</div>

""",unsafe_allow_html=True)


# ---------------------------------------------------
# ⭐ DETAILED SYNTHETIC FIELD EXPLANATION (EXPANDED)
# ---------------------------------------------------

st.subheader("Synthetic Data Record Fields Explanation")

st.write("""

Category represents operational severity classification used within Security Operations Centers (SOC) and executive dashboards.

Organizations require severity categorization to prioritize limited investigative resources and ensure Critical incidents impacting mission operations receive immediate attention.

Agentic Risk Score models AI behavioral probability analytics representing anomaly likelihood or insider threat exposure.

Modern enterprise AI platforms combine behavioral indicators, anomaly detection, and historical intelligence signals into a normalized 1–100 scoring range enabling Zero Trust automated decisions.

Confidence Score represents explainable Artificial Intelligence reliability.

Federal AI governance increasingly requires transparency ensuring leadership understands whether automated recommendations are supported by strong analytical evidence.

MITRE Technique mapping aligns simulated activity with adversary tactics defined within the MITRE ATT&CK framework.

Federal cybersecurity teams rely on MITRE mapping for threat hunting, incident response documentation, RMF control traceability, and FedRAMP authorization evidence packages.

Together these fields demonstrate explainable enterprise AI combining severity prioritization, probabilistic analytics, decision transparency, and threat intelligence mapping.

""")


# ---------------------------------------------------
# DISPLAY DATA
# ---------------------------------------------------

st.subheader("Synthetic / Uploaded Records")

st.dataframe(df,use_container_width=True)


# ---------------------------------------------------
# RISK ENGINE
# ---------------------------------------------------

avg_risk=round(df["Agentic Risk Score"].mean(),2)

risk=("LOW" if avg_risk<30 else
"MEDIUM" if avg_risk<60 else
"HIGH" if avg_risk<80 else
"CRITICAL")

fedramp=round(100-avg_risk,2)

c1,c2,c3,c4=st.columns(4)

c1.metric("Total Records",len(df))
c2.metric("Average Agentic Risk Score",avg_risk)
c3.metric("Risk Category",risk)
c4.metric("FedRAMP Readiness",fedramp)


# ---------------------------------------------------
# EXPORT RESULTS (RESTORED)
# ---------------------------------------------------

st.divider()

st.subheader("Export Results")

csv=df.to_csv(index=False).encode()

st.download_button(
"Download CSV",
csv,
"Enterprise_AI_Report.csv"
)

json=df.to_json(orient="records").encode()

st.download_button(
"Download JSON",
json,
"Enterprise_AI_Report.json"
)

def create_pdf():

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(buffer)

    styles=getSampleStyleSheet()

    story=[]

    story.append(Paragraph("KALSNET Executive Report",styles["Title"]))

    story.append(Spacer(1,12))

    story.append(Paragraph(f"Records : {len(df)}",styles["Normal"]))

    story.append(Paragraph(f"Risk Category : {risk}",styles["Normal"]))

    story.append(Paragraph(f"FedRAMP Readiness : {fedramp}",styles["Normal"]))

    doc.build(story)

    buffer.seek(0)

    return buffer

pdf=create_pdf()

st.download_button(
"Download PDF",
pdf,
"Enterprise_AI_Report.pdf"
)

# ---------------------------------------------------
# SUMMARY
# ---------------------------------------------------

st.divider()

st.subheader("Executive Summary")

st.write(f"""

As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Records Processed : {len(df)}

Average Risk Score : {avg_risk}

Risk Category : {risk}

FedRAMP Readiness Score : {fedramp}

Platform Designed by Randy Singh
Kalsnet (KNet) Consulting Group

""")

st.success("Enterprise AI Platform Running Successfully")
