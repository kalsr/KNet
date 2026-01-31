# Kalsnet_top8_cyber_attacks_demo.py



import streamlit as st

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from fpdf import FPDF

from datetime import datetime



# ==========================================================

# PAGE CONFIG

# ==========================================================

st.set_page_config(page_title="Top 8 Cyber Attacks Demo", layout="wide")



# ==========================================================

# HEADER BRANDING

# ==========================================================

st.markdown("""

<h1 style="text-align:center; color:blue; font-size:45px;">

Top 8 Cyber Attacks – Interactive Defense Demo

</h1>



<h3 style="text-align:center;">

Designed & Developed by <b>Randy Singh</b>  

<br>Kalsnet (KNet) Consulting Group

</h3>

<hr>

""", unsafe_allow_html=True)



# ==========================================================

# ATTACK LIST

# ==========================================================

attacks = {

    "🎣 Phishing Attack": "Fake emails/messages trick users into sharing credentials.",

    "🔒💰 Ransomware": "Malware locks files and demands payment.",

    "🚫💻 Denial-of-Service (DoS)": "Fake traffic overloads systems.",

    "🕵️‍♂️ Man-in-the-Middle (MitM)": "Attacker intercepts communications.",

    "🗄️⚠️ SQL Injection": "Weak forms allow database theft.",

    "💻📜 Cross-Site Scripting (XSS)": "Malicious scripts run in browsers.",

    "⏳🐞 Zero-Day Exploit": "Attack uses unknown software flaw.",

    "🌍🔁 DNS Spoofing": "Users redirected to fake websites."

}



# ==========================================================

# SIDEBAR DATA CONTROLS

# ==========================================================

st.sidebar.header("⚙ Data Controls")



data_mode = st.sidebar.radio(

    "Choose Data Source:",

    ["Generate Synthetic Data", "Upload My Own CSV Data"]

)



df = None



# ==========================================================

# SYNTHETIC DATA GENERATION

# ==========================================================

if data_mode == "Generate Synthetic Data":

    records = st.sidebar.slider("Synthetic Records (0–100)", 0, 100, 40)



    if st.sidebar.button("🔴 RESET & REGENERATE DATA"):

        st.session_state["reset"] = True



    if records > 0:

        df = pd.DataFrame({

            "Attack_Type": np.random.choice(list(attacks.keys()), records),

            "Severity": np.random.choice(["Low", "Medium", "High", "Critical"], records),

            "Users_Impacted": np.random.randint(1, 500, records),

            "Detected": np.random.choice(["Yes", "No"], records)

        })



# ==========================================================

# USER CSV UPLOAD

# ==========================================================

else:

    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file:

        df = pd.read_csv(uploaded_file)



# ==========================================================

# STOP IF NO DATA

# ==========================================================

if df is None:

    st.info("Please generate synthetic data or upload your dataset to begin.")

    st.stop()



# ==========================================================

# EXECUTIVE DASHBOARD

# ==========================================================

st.subheader("📊 Cyber Attack Executive Dashboard")



col1, col2, col3, col4 = st.columns(4)



col1.metric("Total Attack Records", len(df))

col2.metric("Critical Attacks", len(df[df["Severity"] == "Critical"]))

col3.metric("High Severity", len(df[df["Severity"] == "High"]))

col4.metric("Undetected Attacks", len(df[df["Detected"] == "No"]))



st.markdown("---")



# ==========================================================

# PIE CHART: ATTACK DISTRIBUTION

# ==========================================================

st.subheader("🧩 Attack Distribution (Pie Chart)")



attack_counts = df["Attack_Type"].value_counts()



fig1, ax1 = plt.subplots()

ax1.pie(attack_counts, labels=attack_counts.index, autopct="%1.1f%%")

ax1.set_title("Cyber Attack Type Breakdown")

st.pyplot(fig1)



# ==========================================================

# BAR GRAPH: SEVERITY LEVELS

# ==========================================================

st.subheader("📌 Severity Levels (Bar Chart)")



severity_counts = df["Severity"].value_counts()



fig2, ax2 = plt.subplots()

ax2.bar(severity_counts.index, severity_counts.values)

ax2.set_title("Attack Severity Distribution")

ax2.set_xlabel("Severity")

ax2.set_ylabel("Count")

st.pyplot(fig2)



# ==========================================================

# ATTACK BUTTONS UI

# ==========================================================

st.markdown("## 🚨 Select an Attack Type to Demo")



cols = st.columns(4)

selected_attack = None



for i, attack in enumerate(attacks.keys()):

    with cols[i % 4]:

        if st.button(attack, use_container_width=True):

            selected_attack = attack



# ==========================================================

# SHOW ATTACK DETAILS

# ==========================================================

if selected_attack:

    st.markdown("---")

    st.header(f"Demo Attack: {selected_attack}")

    st.write("### Description:")

    st.info(attacks[selected_attack])



    attack_data = df[df["Attack_Type"] == selected_attack]



    st.write("### Sample Records:")

    st.dataframe(attack_data)



    # ======================================================

    # EXPORT CSV

    # ======================================================

    csv_data = attack_data.to_csv(index=False).encode("utf-8")



    st.download_button(

        label="⬇ Download Results (CSV)",

        data=csv_data,

        file_name=f"{selected_attack}_results.csv",

        mime="text/csv"

    )



    # ======================================================

    # EXPORT PDF REPORT

    # ======================================================

    def generate_pdf(attack_name, dataframe):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=14)



        pdf.cell(200, 10, txt="KNet Cyber Attack Executive Report", ln=True, align="C")

        pdf.set_font("Arial", size=11)



        pdf.cell(200, 10, txt=f"Attack Type: {attack_name}", ln=True)

        pdf.cell(200, 10, txt=f"Generated: {datetime.now()}", ln=True)



        pdf.ln(10)

        pdf.cell(200, 10, txt="Top Records:", ln=True)



        pdf.ln(5)



        for _, row in dataframe.head(8).iterrows():

            pdf.cell(

                200, 8,

                txt=f"Severity: {row['Severity']} | Users Impacted: {row['Users_Impacted']} | Detected: {row['Detected']}",

                ln=True

            )



        filename = "Attack_Report.pdf"

        pdf.output(filename)

        return filename



    if st.button("📄 Generate PDF Report"):

        pdf_file = generate_pdf(selected_attack, attack_data)



        with open(pdf_file, "rb") as f:

            st.download_button(

                label="⬇ Download PDF Report",

                data=f,

                file_name=f"{selected_attack}_Report.pdf",

                mime="application/pdf"

            )



# ==========================================================

# FULL DATA TABLE

# ==========================================================

st.markdown("---")

st.subheader("📌 Full Dataset Preview")

st.dataframe(df)

