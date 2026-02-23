



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
# EXECUTIVE DARK THEME
# ---------------------------------------------------

st.markdown("""

<style>

body {
background-color:#0E1117;
}

/* Bright Blue Title */

.knet-title{
color:#007BFF;
font-weight:900;
text-align:center;
font-size:48px;
}

.knet-sub{
text-align:center;
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

<h4 class="knet-sub">

Developed by Randy Singh | Kalsnet (KNet) Consulting Group

</h4>

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

# FIXED RESET BUTTON

if st.sidebar.button("🔄 Reset & Refresh Data"):

    st.rerun()


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
# LOAD DATA (UPLOAD OR SYNTHETIC)
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
# DISPLAY DATA
# ---------------------------------------------------

st.subheader("Synthetic / Uploaded Records")

st.dataframe(df,use_container_width=True)

# ---------------------------------------------------
# RISK ENGINE
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
# EXPORT FUNCTIONS
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

    story.append(Spacer(1,0.2*inch))

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

# CSV

csv=df.to_csv(index=False).encode()

st.sidebar.download_button(

"Export CSV",

csv,

"enterprise_results.csv",

"csv"

)

# JSON

json_data=df.to_json(orient="records").encode()

st.sidebar.download_button(

"Export JSON",

json_data,

"enterprise_results.json",

"application/json"

)

# PDF

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
