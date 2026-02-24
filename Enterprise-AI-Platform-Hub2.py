

# ===============================================
# KALSNET ENTERPRISE AI PLATFORM
# FINAL ENTERPRISE VERSION
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

if "uploaded" not in st.session_state:
    st.session_state.uploaded=None


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

"Agentic Risk Score":
np.random.randint(1,100,records),

"Confidence Score":
np.random.randint(50,100,records),

"MITRE Technique":
np.random.choice(mitre,records)

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


# ---------------------------------------------------
# RESET & REFRESH (FINAL SAFE VERSION)
# ---------------------------------------------------

if st.sidebar.button("Reset & Refresh Data"):

    st.session_state.uploaded=None

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
# MODE EXPLANATION
# ---------------------------------------------------

mode_explanations={

"Executive Boardroom Dashboard":
"Provides senior leadership enterprise risk visibility and executive decision intelligence.",

"Federal / DoD AI Security":
"Simulates Zero Trust cybersecurity operations aligned with RMF, NIST controls, and MITRE ATT&CK mapping.",

"iPhone Camera AI Vision":
"Demonstrates real-time AI visual analysis and mobile threat scoring capabilities.",

"Personal AI Assistant":
"Models AI assistants providing contextual analytics and decision automation.",

"Commercial AI Platform":
"Represents enterprise fraud monitoring and behavioral analytics operations.",

"Kalsnet Enterprise Integration":
"Simulates hybrid enterprise cloud integrations across APIs and SaaS systems."

}

st.info(mode_explanations[module])

# ---------------------------------------------------
# FULL DETAILED SYNTHETIC FIELD EXPLANATION
# ---------------------------------------------------

st.markdown("""

### Synthetic Data Record Fields Explanation

The synthetic dataset represents enterprise operational scenarios across cybersecurity monitoring, fraud analytics, governance risk management, and federal compliance demonstrations. Each field is intentionally selected to reflect real-world AI explainability and executive risk assessment workflows.

**1. Category**

Category represents the operational severity classification assigned to simulated events, transactions, or behavioral activities. Security Operations Centers (SOC), fraud investigation teams, and enterprise governance boards commonly classify incidents using severity tiers such as Low, Medium, High, and Critical.

This enables executive leadership to immediately understand enterprise exposure distribution and prioritize remediation resources. Category grouping also enables dashboards to visualize threat density and operational posture trends.

**2. Agentic Risk Score**

The Agentic Risk Score is an AI-derived probabilistic threat index ranging from 1 to 100. The score simulates outputs generated from behavioral anomaly detection engines, large language model reasoning agents, insider threat analytics, or fraud detection algorithms.

Higher scores indicate increased likelihood of malicious activity or operational risk exposure. Enterprise AI systems use this score to automate prioritization workflows, escalate investigations, and support explainable decision intelligence.

**3. Confidence Score**

Confidence Score represents the reliability or certainty level associated with AI-generated analysis. Modern AI governance frameworks require explainability and auditability of automated decisions.

Values between 50 and 100 simulate corroborating intelligence signals such as telemetry evidence, anomaly frequency, historical pattern matches, or multiple AI agent consensus validation.

Executives and analysts rely on confidence scoring to determine whether immediate action is warranted or whether additional human validation is required.

**4. MITRE Technique**

MITRE ATT&CK techniques map simulated activities to known adversarial tactics observed in real-world cyber operations.

Examples include phishing campaigns, credential misuse, command execution abuse, or ransomware encryption behaviors.

Mapping AI analytics to MITRE techniques demonstrates compliance readiness, RMF alignment, and Zero Trust operational maturity required within Federal and DoD cybersecurity environments.

Collectively, these fields demonstrate enterprise explainable AI, executive risk intelligence, governance transparency, and cybersecurity readiness.

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

if avg_risk<30:
    risk="LOW"
elif avg_risk<60:
    risk="MEDIUM"
elif avg_risk<80:
    risk="HIGH"
else:
    risk="CRITICAL"

fedramp=round(100-avg_risk,2)

# ---------------------------------------------------
# FORMULAS
# ---------------------------------------------------

st.markdown("""

### Risk Calculation Methodology

Average Risk Score = Mean(Agentic Risk Score)

Risk Category Thresholds:

LOW < 30  
MEDIUM 30–59  
HIGH 60–79  
CRITICAL ≥ 80

FedRAMP Readiness Score = 100 − Average Risk Score

Higher FedRAMP readiness represents stronger cybersecurity posture and operational resilience.

""")


# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

col1,col2,col3,col4=st.columns(4)

col1.metric("Total Records",len(df))
col2.metric("Average Agentic Risk Score",avg_risk)
col3.metric("Overall Risk Category",risk)
col4.metric("FedRAMP Readiness Score",fedramp)

st.divider()

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

    st.bar_chart(
df["MITRE Technique"].value_counts()
)

# ---------------------------------------------------
# CAMERA
# ---------------------------------------------------

if module=="iPhone Camera AI Vision":

    image=st.camera_input("Capture Image")

    if image:

        st.image(image)

        st.success("AI Vision Analysis Complete")

        st.write(
"Threat Probability Index:",
random.randint(1,100)
)

# ---------------------------------------------------
# PDF EXPORT
# ---------------------------------------------------

def create_pdf():

    buffer=io.BytesIO()

    doc=SimpleDocTemplate(buffer)

    styles=getSampleStyleSheet()

    story=[]

    story.append(
Paragraph(
"KALSNET Executive AI Report",
styles["Title"]
))

    story.append(
Spacer(1,0.3*inch)
)

    story.append(
Paragraph(
f"Average Risk Score: {avg_risk}",
styles["Normal"]
))

    story.append(
Paragraph(
f"Risk Category: {risk}",
styles["Normal"]
))

    story.append(
Paragraph(
f"FedRAMP Score: {fedramp}",
styles["Normal"]
))

    doc.build(story)

    buffer.seek(0)

    return buffer

st.sidebar.download_button(
"Export CSV",
df.to_csv(index=False).encode(),
"enterprise_results.csv"
)

st.sidebar.download_button(
"Export Executive PDF",
create_pdf(),
"enterprise_report.pdf"
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
