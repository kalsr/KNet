

# ===============================================
# KALSNET ENTERPRISE AI PLATFORM
# Updated Enterprise Version
# ===============================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import random
from datetime import datetime
import json
import io

# PDF Export
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="KALSNET AI ENTERPRISE PLATFORM",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# EXECUTIVE DARK THEME + BOLD BLUE HEADER
# ---------------------------------------------------

st.markdown("""

<style>

body{
background-color:#0E1117;
}

/* EXECUTIVE HEADER */

.knet-title{

color:#0066FF;
font-weight:1000;
font-size:52px;
text-align:center;
letter-spacing:1px;

}

.knet-sub{

color:#0066FF;
font-weight:900;
font-size:22px;
text-align:center;

}

</style>

""",unsafe_allow_html=True)


# ---------------------------------------------------
# HEADER (UPDATED BOLD BLUE)
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
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("🎛 Simulation Controls")

module = st.sidebar.selectbox(

"Select Platform Mode",

[
"🔥 Executive Boardroom Dashboard",
"🛡 Federal / DoD AI Security",
"📱 iPhone Camera AI Vision",
"👤 Personal AI Assistant",
"💼 Commercial AI Platform",
"☁️ Kalsnet Enterprise Integration"

]

)

data_volume = st.sidebar.slider("Synthetic Data Volume",0,200,50)

dod_mode = st.sidebar.checkbox("Enable Zero Trust / DoD Mode")

if st.sidebar.button("🔄 Reset & Refresh Data"):

    st.rerun()


# ---------------------------------------------------
# MODE EXPLANATION (UNCHANGED)
# ---------------------------------------------------

mode_explanations={

"🔥 Executive Boardroom Dashboard":

"Provides senior leadership enterprise risk visibility and executive decision intelligence.",

"🛡 Federal / DoD AI Security":

"Simulates Zero Trust cybersecurity operations aligned with RMF, NIST controls, and MITRE ATT&CK mapping.",

"📱 iPhone Camera AI Vision":

"Demonstrates real-time AI visual analysis and mobile threat scoring capabilities.",

"👤 Personal AI Assistant":

"Models AI assistants providing contextual analytics and decision automation.",

"💼 Commercial AI Platform":

"Represents enterprise fraud monitoring and behavioral analytics operations.",

"☁️ Kalsnet Enterprise Integration":

"Simulates hybrid enterprise cloud integrations across APIs and SaaS systems."

}

st.info(mode_explanations[module])


# ---------------------------------------------------
# DATA UPLOAD
# ---------------------------------------------------

st.sidebar.subheader("Upload Your Own Dataset")

uploaded_file = st.sidebar.file_uploader(

"Upload CSV or JSON",

type=["csv","json"]

)

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

    data={

"Category":np.random.choice(categories,records),

"Agentic Risk Score":np.random.randint(1,100,records),

"Confidence Score":np.random.randint(50,100,records),

"MITRE Technique":np.random.choice(mitre,records)

}

    return pd.DataFrame(data)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):

        df=pd.read_csv(uploaded_file)

    else:

        df=pd.read_json(uploaded_file)

    st.success("User Dataset Loaded Successfully")

else:

    df=generate_data(data_volume)


# ---------------------------------------------------
# NEW — SYNTHETIC FIELD EXPLANATION
# ---------------------------------------------------

st.markdown("""

### 📊 Synthetic Data Record Field Explanation

The synthetic dataset represents enterprise AI risk modeling scenarios commonly used across cybersecurity operations, fraud analytics, and federal compliance simulations.

**Category**

Represents overall operational severity classification assigned to each event or transaction. Categories simulate analyst triage levels used within SOC environments and executive dashboards.

**Agentic Risk Score**

A simulated AI-derived risk probability score ranging from 1–100 generated from behavioral anomalies, threat indicators, or suspicious activities. Higher values indicate elevated risk requiring mitigation or investigation.

**Confidence Score**

Represents the AI model confidence level associated with each risk decision. Higher confidence scores indicate stronger analytical certainty derived from supporting indicators or corroborating signals.

**MITRE Technique**

Maps simulated activity to recognized MITRE ATT&CK adversarial tactics and techniques used by cybersecurity professionals and federal agencies for threat intelligence tracking and RMF risk assessments.

These selected fields collectively demonstrate real-world enterprise AI analytics involving explainability, compliance readiness, and executive risk visibility.

""")


# ---------------------------------------------------
# DISPLAY DATA
# ---------------------------------------------------

st.subheader("Synthetic / Uploaded Records")

st.dataframe(df,use_container_width=True)


# ---------------------------------------------------
# RISK ENGINE (UNCHANGED)
# ---------------------------------------------------

avg_risk=round(df["Agentic Risk Score"].mean(),2) if len(df)>0 else 0

if avg_risk<30:

    risk_level="LOW"

elif avg_risk<60:

    risk_level="MEDIUM"

elif avg_risk<80:

    risk_level="HIGH"

else:

    risk_level="CRITICAL"

fedramp_score=round(100-avg_risk,2)


# ---------------------------------------------------
# RISK EXPLANATION (UNCHANGED)
# ---------------------------------------------------

st.markdown("""

### 📘 Risk Scoring Methodology

Agentic Risk Score represents averaged AI threat exposure across records.

Risk Categories:

LOW <30  
MEDIUM 30-59  
HIGH 60-79  
CRITICAL ≥80.

FedRAMP Readiness Score = 100 − Average Risk Score.

Higher readiness indicates stronger cybersecurity posture and improved compliance readiness.

""")


# ---------------------------------------------------
# EXPORT FUNCTIONS (UNCHANGED)
# ---------------------------------------------------

def create_pdf():

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(buffer)

    styles=getSampleStyleSheet()

    story=[]

    story.append(Paragraph(

"KALSNET Enterprise AI Executive Report",

styles["Title"]

))

    story.append(Spacer(1,0.3*inch))

    story.append(Paragraph(

f"Generated: {datetime.now()}",

styles["Normal"]

))

    story.append(Paragraph(

f"Average Risk Score: {avg_risk}",

styles["Normal"]

))

    story.append(Paragraph(

f"Risk Category: {risk_level}",

styles["Normal"]

))

    story.append(Paragraph(

f"FedRAMP Readiness Score: {fedramp_score}",

styles["Normal"]

))

    doc.build(story)

    buffer.seek(0)

    return buffer


st.sidebar.subheader("Export Results")

csv=df.to_csv(index=False).encode()

st.sidebar.download_button(

"Export CSV",

csv,

"enterprise_results.csv",

"csv"

)

json_data=df.to_json(orient="records").encode()

st.sidebar.download_button(

"Export JSON",

json_data,

"enterprise_results.json",

"application/json"

)

pdf=create_pdf()

st.sidebar.download_button(

"Export Executive PDF",

pdf,

"enterprise_report.pdf",

"application/pdf"

)

# ---------------------------------------------------
# EXECUTIVE GAUGE
# ---------------------------------------------------

def executive_gauge(score):

    fig=go.Figure(go.Indicator(

mode="gauge+number",

value=score,

title={'text':"Enterprise Risk Index"},

gauge={

'axis':{'range':[0,100]},

'steps':[

{'range':[0,30],'color':"green"},
{'range':[30,60],'color':"yellow"},
{'range':[60,80],'color':"orange"},
{'range':[80,100],'color':"red"}

]

}

))

    st.plotly_chart(fig,use_container_width=True)


# ---------------------------------------------------
# MODULE DISPLAY
# ---------------------------------------------------

st.subheader(module)

if dod_mode:

    st.warning("🛡 Zero Trust Enforcement Enabled")


# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Records",len(df))
col2.metric("Average Agentic Risk Score",avg_risk)
col3.metric("Overall Risk Category",risk_level)
col4.metric("FedRAMP Readiness Score",fedramp_score)

st.divider()

executive_gauge(avg_risk)

# ---------------------------------------------------
# PIE
# ---------------------------------------------------

st.subheader("Risk Category Distribution")

fig1,ax1=plt.subplots()

df["Category"].value_counts().plot.pie(autopct='%1.1f%%',ax=ax1)

ax1.axis('equal')

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

if module=="🛡 Federal / DoD AI Security":

    st.subheader("MITRE ATT&CK Technique Distribution")

    st.bar_chart(df["MITRE Technique"].value_counts())


# ---------------------------------------------------
# CAMERA
# ---------------------------------------------------

if module=="📱 iPhone Camera AI Vision":

    image=st.camera_input("Capture Image")

    if image:

        st.image(image)

        st.success("AI Vision Analysis Complete")

        st.write("Threat Probability Index:",random.randint(1,100))


# ---------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------

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
