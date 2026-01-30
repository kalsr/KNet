





#cyber_defense_demo.py



import streamlit as st

import pandas as pd

import numpy as np

from datetime import datetime

from fpdf import FPDF



# -------------------------------

# PAGE CONFIG

# -------------------------------

st.set_page_config(

    page_title="Defense-in-Depth Cyberscecurity Demo",

    layout="wide"

)



# -------------------------------

# HEADER BRANDING

# -------------------------------

st.markdown("""

<h1 style="text-align:center; color:blue;">

Defense-in-Depth Cybersecurity Strategy Demo  

</h1>



<h3 style="text-align:center;">

Developed by <b>Randy Singh</b> | Kalsnet (KNet) Consulting Group

</h3>

<hr>

""", unsafe_allow_html=True)



# -------------------------------

# SIDEBAR CONTROLS

# -------------------------------

st.sidebar.header("⚙ Data Controls")



data_mode = st.sidebar.radio(

    "Choose Data Source:",

    ["Generate Synthetic Data", "Upload My Own Data"]

)



df = None



# -------------------------------

# SYNTHETIC DATA GENERATOR

# -------------------------------

if data_mode == "Generate Synthetic Data":

    record_count = st.sidebar.slider(

        "Select Number of Synthetic Records",

        min_value=0,

        max_value=100,

        value=25

    )



    if record_count > 0:

        df = pd.DataFrame({

            "User": [f"user{i}" for i in range(record_count)],

            "Login_Attempts": np.random.randint(1, 15, record_count),

            "Firewall_Blocks": np.random.randint(0, 20, record_count),

            "Threat_Level": np.random.choice(["Low", "Medium", "High"], record_count),

            "Cloud_Activity": np.random.choice(["Normal", "Suspicious"], record_count),

            "DLP_Alerts": np.random.randint(0, 10, record_count)

        })



# -------------------------------

# USER UPLOAD

# -------------------------------

else:

    uploaded_file = st.sidebar.file_uploader(

        "Upload CSV File",

        type=["csv"]

    )



    if uploaded_file:

        df = pd.read_csv(uploaded_file)



# -------------------------------

# DISPLAY DATA

# -------------------------------

if df is not None:

    st.subheader(" Active Security Dataset")

    st.dataframe(df)



# -------------------------------

# DEFENSE LAYERS LIST

# -------------------------------

layers = [

    " IAM (Identity & Access Management)",

    " Firewalls",

    " EDR & NDR",

    " IDS / IPS",

    " SIEM",

    " Cloud Security",

    " DLP (Data Loss Prevention)",

    " Incident Response",

    " Security Awareness"

]



st.markdown("##  Defense-in-Depth Security Layers")



# -------------------------------

# BUTTON GRID UI

# -------------------------------

cols = st.columns(3)



selected_layer = None



for i, layer in enumerate(layers):

    with cols[i % 3]:

        if st.button(layer, use_container_width=True):

            selected_layer = layer



# -------------------------------

# LAYER OUTPUT SIMULATION

# -------------------------------

if selected_layer:

    st.markdown(f"##  Selected Layer: {selected_layer}")



    if df is not None:



        if "IAM" in selected_layer:

            st.success("IAM Analysis: Detecting unusual login attempts...")

            st.write(df[["User", "Login_Attempts"]].sort_values("Login_Attempts", ascending=False))



        elif "Firewalls" in selected_layer:

            st.warning("Firewall Defense: Reviewing blocked traffic...")

            st.write(df[["User", "Firewall_Blocks"]].sort_values("Firewall_Blocks", ascending=False))



        elif "EDR" in selected_layer:

            st.info("Endpoint Detection: Monitoring suspicious endpoint behavior...")

            st.write(df.sample(min(5, len(df))))



        elif "IDS" in selected_layer:

            st.error("IDS/IPS Alert Simulation: Malicious behavior detected!")

            st.write(df[df["Threat_Level"] == "High"])



        elif "SIEM" in selected_layer:

            st.info("SIEM Correlation: Aggregating event logs...")

            st.write(df.groupby("Threat_Level").count())



        elif "Cloud" in selected_layer:

            st.warning("Cloud Workload Monitoring...")

            st.write(df[df["Cloud_Activity"] == "Suspicious"])



        elif "DLP" in selected_layer:

            st.error("DLP Alerts: Sensitive data leak prevention triggered!")

            st.write(df[df["DLP_Alerts"] > 5])



        elif "Incident" in selected_layer:

            st.success("Incident Response Plan Activated: Containment steps generated.")

            st.write("✔ Identify → Contain → Eradicate → Recover → Lessons Learned")



        elif "Awareness" in selected_layer:

            st.info("Security Awareness: Training reduces phishing and insider risk.")

            st.write("✔ Monthly training + simulations recommended.")



# -------------------------------

# EXPORT SECTION

# -------------------------------

st.markdown("---")

st.markdown("##  Export Reports")



if df is not None:



    # Export CSV

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="⬇ Download Output as CSV",

        data=csv_data,

        file_name="cyber_defense_output.csv",

        mime="text/csv"

    )



    # Export PDF

    def generate_pdf(dataframe):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=12)



        pdf.cell(200, 10, txt="Defense-in-Depth Cybersecurity Report", ln=True, align="C")

        pdf.cell(200, 10, txt=f"Generated: {datetime.now()}", ln=True)



        pdf.ln(10)



        for col in dataframe.columns:

            pdf.cell(40, 10, col, border=1)

        pdf.ln()



        for _, row in dataframe.head(10).iterrows():

            for val in row:

                pdf.cell(40, 10, str(val), border=1)

            pdf.ln()



        file_name = "cyber_defense_report.pdf"

        pdf.output(file_name)

        return file_name



    if st.button(" Generate PDF Report (Top 10 Records)"):

        pdf_file = generate_pdf(df)

        with open(pdf_file, "rb") as f:

            st.download_button(

                label="⬇ Download PDF Report",

                data=f,

                file_name="cyber_defense_report.pdf",

                mime="application/pdf"

            )



else:


    st.info("Please generate or upload data to enable exports.")


