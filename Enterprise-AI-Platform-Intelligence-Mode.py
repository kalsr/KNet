

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
# STYLE
# ---------------------------------------------------

st.markdown("""

<style>

.knet-title{
color:#007BFF;
font-size:52px;
font-weight:1000;
text-align:center;
}

.knet-sub{
color:#007BFF;
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

</style>

""",unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
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
# ⭐ MODE EXPLANATIONS (FULL EXECUTIVE VERSION)
# ---------------------------------------------------

mode_details={

"Executive Boardroom Dashboard":

"""
Provides senior leadership enterprise visibility across operational risk posture.

Designed for CIOs, CISOs, Program Executives, and Board Leadership to rapidly understand organizational exposure trends, compliance posture, and operational performance metrics.

Supports decision prioritization, mission assurance, and executive risk governance reporting.
""",

"Federal / DoD AI Security":

"""
Simulates Zero Trust cybersecurity monitoring aligned with RMF authorization workflows and MITRE ATT&CK threat intelligence mapping.

Supports SOC operations, continuous monitoring (ConMon), insider threat detection, and ATO readiness decision analytics.

Designed to demonstrate federal civilian agency and DoD cyber defense operational workflows.
""",

"iPhone Camera AI Vision":

"""
Demonstrates real-time AI visual intelligence processing using camera capture.

Simulates field inspection analytics, facility monitoring, threat recognition, and mobile edge AI operations used in defense and homeland security environments.
""",

"Personal AI Assistant":

"""
Provides contextual AI advisory analytics capable of summarizing enterprise risk posture and assisting users with operational understanding.

Represents executive assistant AI copilots supporting decision awareness and productivity automation.
""",

"Commercial AI Platform":

"""
Enterprise fraud detection and commercial analytics simulation.

Demonstrates behavioral anomaly detection, customer risk modeling, transaction monitoring, and explainable AI scoring.
""",

"Kalsnet Enterprise Integration":

"""
Hybrid cloud integration simulation demonstrating enterprise interoperability between AI analytics, operational systems, and compliance frameworks.

Supports modernization initiatives, cross-agency collaboration, and digital transformation programs.
"""
}

st.markdown(f"""

<div class="mode-box">

<div class="mode-header">

Selected Platform Mode — {module}

</div>

<pre style="white-space:pre-wrap;font-family:inherit">

{mode_details[module]}

</pre>

</div>

""",unsafe_allow_html=True)

# ---------------------------------------------------
# SYNTHETIC FIELD EXPLANATION
# ---------------------------------------------------

st.subheader("Synthetic Data Record Fields Explanation")

st.write("""

Category defines severity prioritization supporting SOC triage workflows and executive escalation visibility.

Agentic Risk Score models AI behavioral probability analysis identifying anomaly exposure or insider threat risk.

Confidence Score represents explainable AI certainty ensuring leadership understands reliability of automated decisions.

MITRE Technique maps activity to adversary behavior taxonomy supporting threat hunting and RMF documentation traceability.

Collectively these fields simulate enterprise explainable AI analytics supporting cyber defense and fraud detection programs.

""")

# ---------------------------------------------------
# DATA DISPLAY
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
# CALCULATION EXPLANATION
# ---------------------------------------------------

st.markdown("""

### Enterprise Risk Calculation Methodology

Average Risk Score:

Arithmetic mean of all Agentic Risk Scores.

Risk Category:

LOW <30  
MEDIUM 30-59  
HIGH 60-79  
CRITICAL 80+

FedRAMP Readiness:

100 − Average Risk Score.

Lower risk equals stronger authorization readiness posture.

""")

# ---------------------------------------------------
# GAUGE
# ---------------------------------------------------

fig=go.Figure(go.Indicator(

mode="gauge+number",
value=avg_risk,
title={'text':"Enterprise Risk Index"},
gauge={'axis':{'range':[0,100]}}

))

st.plotly_chart(fig,use_container_width=True)

# ---------------------------------------------------
# PIE
# ---------------------------------------------------

st.subheader("Risk Category Distribution")

fig1,ax1=plt.subplots()

df["Category"].value_counts().plot.pie(
autopct="%1.1f%%",
ax=ax1
)

ax1.axis("equal")

st.pyplot(fig1)

# ---------------------------------------------------
# HISTOGRAM
# ---------------------------------------------------

st.subheader("Agentic Risk Score Distribution")

fig2,ax2=plt.subplots()

ax2.hist(df["Agentic Risk Score"],bins=10)

st.pyplot(fig2)

# ---------------------------------------------------
# MITRE
# ---------------------------------------------------

if module=="Federal / DoD AI Security":

    st.subheader("MITRE ATTACK Technique Distribution")

    st.bar_chart(df["MITRE Technique"].value_counts())

# ---------------------------------------------------
# CAMERA
# ---------------------------------------------------

if module=="iPhone Camera AI Vision":

    image=st.camera_input("Capture Image")

    if image:

        st.image(image)

        st.success("AI Vision Analysis Complete")

        st.write("Threat Probability Index:",random.randint(1,100))

# ---------------------------------------------------
# EXPORT
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
