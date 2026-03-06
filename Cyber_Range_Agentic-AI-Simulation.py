


# Cyber Range Application



import streamlit as st

import pandas as pd

import numpy as np

import random

import json

from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.lib.styles import getSampleStyleSheet

import plotly.express as px

from sklearn.ensemble import IsolationForest



st.set_page_config(layout="wide")



# ----------------------------------------------------

# HEADER

# ----------------------------------------------------



st.markdown(

"""

<h1 style='background-color:#0b3d91;color:white;padding:15px;text-align:center'>

Agentic AI Cyber Range Platform

<br>

Developed by Randy Singh – Kalsnet (KNet) Consulting Group

</h1>

""",

unsafe_allow_html=True

)



# ----------------------------------------------------

# SIDEBAR CONTROLS

# ----------------------------------------------------



st.sidebar.header("Synthetic Cyber Data Generator")



records = st.sidebar.slider("Number of Records",0,200,50)



generate = st.sidebar.button("Generate Data")

reset = st.sidebar.button("Reset Data")



# ----------------------------------------------------

# ATTACK LIBRARY

# ----------------------------------------------------



attack_types = {



"Vulnerability Scanning":{

"impact":"Attackers discover weaknesses in systems.",

"mitigation":"Patch vulnerabilities and run vulnerability management."

},



"Password Brute Force":{

"impact":"Accounts may be compromised.",

"mitigation":"Enable MFA and account lockout policies."

},



"Lateral Movement":{

"impact":"Attacker spreads through network.",

"mitigation":"Use network segmentation and zero trust."

},



"Privilege Escalation":{

"impact":"Attacker gains admin privileges.",

"mitigation":"Monitor privilege use and patch OS vulnerabilities."

},



"Malware Deployment":{

"impact":"Data theft or ransomware infection.",

"mitigation":"Use endpoint protection and monitoring."

},



"Phishing":{

"impact":"User credentials stolen.",

"mitigation":"Security awareness training and email filtering."

},



"SQL Injection":{

"impact":"Database compromise.",

"mitigation":"Use prepared statements and input validation."

},



"DDoS":{

"impact":"Service outages.",

"mitigation":"Traffic filtering and CDN protection."

}



}



severity_levels=["Low","Medium","High","Critical"]



# ----------------------------------------------------

# DATA GENERATOR

# ----------------------------------------------------



def generate_data(n):



    rows=[]



    for i in range(n):



        attack=random.choice(list(attack_types.keys()))

        severity=random.choice(severity_levels)



        source=f"192.168.1.{random.randint(1,254)}"

        target=f"10.0.0.{random.randint(1,254)}"



        likelihood=random.randint(1,5)

        impact=random.randint(1,5)

        severity_weight=random.randint(1,5)



        risk_score = severity_weight * likelihood * impact



        rows.append([

        attack,severity,source,target,likelihood,impact,severity_weight,risk_score

        ])



    df=pd.DataFrame(rows,columns=[

    "Attack",

    "Severity",

    "Source IP",

    "Target IP",

    "Likelihood",

    "Impact",

    "Severity Weight",

    "Risk Score"

    ])



    return df



# ----------------------------------------------------

# GENERATE / RESET

# ----------------------------------------------------



if generate:

    df=generate_data(records)

    st.session_state["data"]=df



if reset:

    st.session_state["data"]=pd.DataFrame()



# ----------------------------------------------------

# DATA VIEW

# ----------------------------------------------------



if "data" in st.session_state and not st.session_state["data"].empty:



    df=st.session_state["data"]



    st.subheader("Cyber Event Logs")



    st.dataframe(df)



    # -----------------------------------------------

    # ANOMALY DETECTION

    # -----------------------------------------------



    st.subheader("AI Anomaly Detection")



    model=IsolationForest(contamination=0.1)



    df["anomaly"]=model.fit_predict(df[["Risk Score"]])



    anomalies=df[df["anomaly"]==-1]



    st.write("Detected anomalies:",len(anomalies))



    st.dataframe(anomalies)



    # -----------------------------------------------

    # VISUALIZATIONS

    # -----------------------------------------------



    col1,col2=st.columns(2)



    with col1:



        fig=px.bar(df,x="Attack",title="Attack Distribution")

        st.plotly_chart(fig)



    with col2:



        fig2=px.pie(df,names="Severity",title="Severity Distribution")

        st.plotly_chart(fig2)



# ----------------------------------------------------

# CYBER AGENTS

# ----------------------------------------------------



st.subheader("Agentic Cyber Defense & Attack Simulation")



col1,col2,col3,col4,col5=st.columns(5)



with col1:



    if st.button("Red Team"):



        st.write("Simulated Attacker Actions")



        st.write("""

• Vulnerability scanning  

• Password brute force  

• Lateral movement  

• Privilege escalation  

• Malware deployment  

""")



with col2:



    if st.button("Blue Team"):



        st.write("""

Defensive operations



• Monitor logs  

• Detect anomalies  

• Trigger alerts  

• Block IPs  

• Deploy patches

""")



with col3:



    if st.button("SOC Analyst"):



        st.write("""

SOC analyst responsibilities



• Investigate alerts  

• Correlate logs  

• Produce incident reports

""")



with col4:



    if st.button("Incident Response"):



        st.write("""

Incident response actions



• Contain attack  

• Eradicate malware  

• Recover systems

""")



with col5:



    if st.button("Threat Hunter"):



        st.write("""

Threat hunting activities



• Identify hidden threats  

• Behavioral analysis  

• Pattern detection

""")



# ----------------------------------------------------

# VULNERABILITY EXPLANATION

# ----------------------------------------------------



st.subheader("Cyber Attack Knowledge Base")



selected_attack=st.selectbox("Select Attack Type",list(attack_types.keys()))



st.write("Impact:")



st.info(attack_types[selected_attack]["impact"])



st.write("Mitigation Strategy")



st.success(attack_types[selected_attack]["mitigation"])



# ----------------------------------------------------

# FORMULAS

# ----------------------------------------------------



st.subheader("Risk Calculation Model")



st.code("""

Risk Score = Severity Weight × Likelihood × Impact

""")



st.write("Example")



st.code("""

Severity Weight = 4

Likelihood = 5

Impact = 3



Risk Score = 4 × 5 × 3 = 60

""")



# ----------------------------------------------------

# EXPORT

# ----------------------------------------------------



st.subheader("Export Results")



if "data" in st.session_state:



    df=st.session_state["data"]



    if st.button("Export CSV"):

        df.to_csv("cyber_range_data.csv",index=False)

        st.success("CSV exported")



    if st.button("Export JSON"):

        df.to_json("cyber_range_data.json")

        st.success("JSON exported")



    if st.button("Export PDF"):



        doc=SimpleDocTemplate("cyber_report.pdf")

        styles=getSampleStyleSheet()



        elements=[]

        elements.append(Paragraph("KNet Cyber Range Report",styles["Title"]))



        for i,row in df.iterrows():

            elements.append(Paragraph(str(row.to_dict()),styles["BodyText"]))



        doc.build(elements)



        st.success("PDF report generated")