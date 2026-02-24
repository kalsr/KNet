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
from reportlab.lib.units import inch


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
page_title="KALSNET AI ENTERPRISE PLATFORM",
layout="wide"
)

# ---------------------------------------------------
# BLUE HEADER STYLE
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

.mode-header{
color:#00AEEF;
font-size:34px;
font-weight:900;
padding-top:10px;
}

.mode-box{
background-color:#111827;
padding:18px;
border-radius:10px;
border:1px solid #1F2937;
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
# UPLOAD DATA
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
# MODE DETAILS (UNCHANGED)
# ---------------------------------------------------

mode_details={

"Executive Boardroom Dashboard":
"Executive leadership visibility platform providing enterprise operational intelligence.",

"Federal / DoD AI Security":
"Simulates Zero Trust cybersecurity operations aligned with RMF and MITRE ATT&CK.",

"iPhone Camera AI Vision":
"Demonstrates real-time AI visual intelligence.",

"Personal AI Assistant":
"AI assistant delivering contextual analytics.",

"Commercial AI Platform":
"Enterprise fraud analytics simulation.",

"Kalsnet Enterprise Integration":
"Hybrid cloud enterprise integration simulation."

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
# ⭐ FULL DETAILED SYNTHETIC FIELD EXPLANATION
# ---------------------------------------------------

st.markdown("""

### Synthetic Data Record Fields Explanation — Enterprise AI Risk Modeling

The synthetic dataset represents simulated enterprise operational activity designed to mirror real-world cybersecurity monitoring, fraud detection analytics, federal compliance validation, and executive risk reporting environments. Each selected field demonstrates explainable Artificial Intelligence (XAI) decision-making used across Security Operations Centers (SOC), Federal Risk Management Framework (RMF) processes, and commercial enterprise analytics platforms.

---

**Category — Operational Severity Classification**

The Category field represents organizational severity or priority classification assigned to each activity record. In real environments, analysts triage alerts into operational levels such as Low, Medium, High, or Critical severity.

Why this field is used:

• Enables executive dashboards to quickly visualize enterprise exposure.  
• Supports SOC analyst prioritization workflows.  
• Assists RMF authorization officials in understanding mission impact levels.  
• Simulates incident escalation procedures used in Federal civilian agencies and DoD cyber defense operations.

Without severity classification, organizations cannot effectively prioritize limited response resources.

---

**Agentic Risk Score — AI Behavioral Risk Probability**

The Agentic Risk Score represents an AI-derived probabilistic threat exposure value ranging from 1–100.

Why this field is used:

• Models behavioral anomaly detection used in fraud monitoring and insider threat programs.  
• Represents machine learning outputs combining indicators such as suspicious patterns, anomalies, or known threat signals.  
• Enables Zero Trust decision automation where access or action decisions depend on calculated risk.

Higher scores indicate elevated exposure requiring investigation or mitigation.

Federal and commercial enterprises use similar scoring models for:

• Continuous Authorization Monitoring (ConMon).  
• Insider Threat Detection.  
• Fraud analytics and transaction monitoring.

---

**Confidence Score — Explainable AI Decision Reliability**

The Confidence Score represents the analytical certainty associated with the AI-generated risk decision.

Why this field is used:

• Executive leadership must understand not only risk level but confidence in that assessment.  
• Prevents overreaction to weak signals or underreaction to strong correlations.  
• Supports explainable AI governance requirements increasingly required under Federal AI policy initiatives.

Higher confidence indicates corroborated intelligence sources or stronger supporting data correlations.

This mirrors operational practices used within intelligence analysis and cyber fusion centers.

---

**MITRE Technique — Threat Intelligence Mapping**

This field maps each simulated activity to adversarial tactics defined within the MITRE ATT&CK framework.

Why this field is used:

• Enables standardized cyber threat communication across agencies and contractors.  
• Supports RMF control traceability and threat modeling exercises.  
• Demonstrates mapping between detected activity and known adversary behavior patterns.

Federal cybersecurity teams rely heavily on MITRE ATT&CK taxonomy for:

• Threat hunting.  
• Incident response investigations.  
• ATO and FedRAMP security documentation.

---

Collectively these fields demonstrate enterprise explainable AI analytics combining risk probability, operational severity, analytical confidence, and adversary intelligence mapping — providing executive leadership actionable decision visibility.

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

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Records",len(df))
col2.metric("Average Agentic Risk Score",avg_risk)
col3.metric("Risk Category",risk)
col4.metric("FedRAMP Readiness",fedramp)

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
