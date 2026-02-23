# ===============================================
# KALSNET ENTERPRISE AI PLATFORM
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
# FORCE BLUE HEADER (100% GUARANTEED)
# ---------------------------------------------------

st.markdown("""

<h1 style="color:#007BFF !important;
font-weight:1000;
font-size:52px;
text-align:center;">

KALSNET AI VISION ENTERPRISE PLATFORM

</h1>

<h3 style="color:#007BFF !important;
font-weight:900;
text-align:center;">

Developed by Randy Singh | Kalsnet (KNet) Consulting Group

</h3>

""",unsafe_allow_html=True)

st.divider()

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

data_volume=st.sidebar.slider(

"Synthetic Data Volume",0,200,50

)

dod_mode=st.sidebar.checkbox(

"Enable Zero Trust / DoD Mode"

)

if st.sidebar.button("Reset & Refresh Data"):

    st.rerun()


# ---------------------------------------------------
# MODE EXPLANATIONS (FIXED)
# ---------------------------------------------------

mode_explanations={

"Executive Boardroom Dashboard":

"Provides executive enterprise risk visibility.",

"Federal / DoD AI Security":

"Simulates Zero Trust cybersecurity aligned with RMF, NIST and MITRE ATT&CK.",

"iPhone Camera AI Vision":

"Demonstrates AI mobile visual analytics.",

"Personal AI Assistant":

"AI assistant decision automation simulation.",

"Commercial AI Platform":

"Enterprise fraud monitoring analytics.",

"Kalsnet Enterprise Integration":

"Hybrid cloud enterprise integrations."

}

# SAFE CALL — NEVER FAILS

st.info(

mode_explanations.get(

module,

"No description available."

)

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

"Agentic Risk Score":

np.random.randint(1,100,records),

"Confidence Score":

np.random.randint(50,100,records),

"MITRE Technique":

np.random.choice(mitre,records)

}

    return pd.DataFrame(data)


df=generate_data(data_volume)

# ---------------------------------------------------
# FIELD EXPLANATION
# ---------------------------------------------------

st.markdown("""

### Synthetic Data Record Fields

Category — event severity classification.

Agentic Risk Score — AI threat probability.

Confidence Score — model certainty.

MITRE Technique — adversary behavior mapping.

""")

st.subheader("Synthetic Records")

st.dataframe(df,use_container_width=True)

# ---------------------------------------------------
# RISK ENGINE
# ---------------------------------------------------

avg_risk=round(

df["Agentic Risk Score"].mean(),

2

)

if avg_risk<30:

    risk_level="LOW"

elif avg_risk<60:

    risk_level="MEDIUM"

elif avg_risk<80:

    risk_level="HIGH"

else:

    risk_level="CRITICAL"

fedramp_score=round(

100-avg_risk,

2

)

st.markdown("""

Average Risk Score = Mean Agentic Risk Score

Risk Levels:

LOW <30

MEDIUM 30-59

HIGH 60-79

CRITICAL ≥80

FedRAMP Readiness = 100 − Average Risk Score

""")

# ---------------------------------------------------
# GAUGE
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

st.subheader(module)

if dod_mode:

    st.warning("Zero Trust Enabled")

c1,c2,c3,c4=st.columns(4)

c1.metric("Total Records",len(df))

c2.metric("Average Risk Score",avg_risk)

c3.metric("Risk Category",risk_level)

c4.metric("FedRAMP Score",fedramp_score)

st.divider()

executive_gauge(avg_risk)

# ---------------------------------------------------
# MITRE FIXED
# ---------------------------------------------------

if module=="Federal / DoD AI Security":

    st.subheader("MITRE ATT&CK Techniques")

    st.bar_chart(

df["MITRE Technique"].value_counts()

)

# ---------------------------------------------------
# CAMERA
# ---------------------------------------------------

if module=="iPhone Camera AI Vision":

    image=st.camera_input("Capture")

    if image:

        st.image(image)

        st.success("AI Vision Analysis Complete")

        st.write(

"Threat Probability:",

random.randint(1,100)

)

# ---------------------------------------------------

st.success(

"Enterprise AI Platform Running Successfully"

)
