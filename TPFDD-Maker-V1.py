# TPFDD-GENERATOR-V1

import streamlit as st

import pandas as pd

import random

from datetime import datetime, timedelta

import json



# PDF (REQUIRED LIB)

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table

from reportlab.lib.styles import getSampleStyleSheet



# -----------------------------

# PAGE CONFIG

# -----------------------------

st.set_page_config(layout="wide")



# -----------------------------

# TITLE

# -----------------------------

st.markdown(

    "<h1 style='text-align:center; color:blue;'>"

    "Enterprise TPFDD Simulator Web Platform<br>"

    "Developed by Randy Singh from Kalsnet (KNet) Group"

    "</h1>",

    unsafe_allow_html=True

)



# -----------------------------

# SIDEBAR

# -----------------------------

st.sidebar.header("Controls")



num_records = st.sidebar.slider("Synthetic TPFDD Records", 0, 300, 100)



scenario = st.sidebar.selectbox(

    "Scenario",

    ["Steady State", "Rapid Deployment", "Major Theater War"]

)



generate_btn = st.sidebar.button("Generate TPFDD")

simulate_btn = st.sidebar.button("Run Simulation")

reset_btn = st.sidebar.button("Reset")



# -----------------------------

# SESSION STATE

# -----------------------------

if "df" not in st.session_state:

    st.session_state.df = pd.DataFrame()



# -----------------------------

# DATA GENERATION

# -----------------------------

def generate_tpfdd(n):

    data = []

    base_date = datetime.now()



    for i in range(n):

        ald = base_date + timedelta(days=random.randint(1, 5))

        ead = ald + timedelta(days=random.randint(2, 5))

        rdd = ead + timedelta(days=random.randint(3, 10))



        data.append({

            "ULN": f"ULN{i}",

            "Parent ULN": f"PARENT{random.randint(1,10)}",

            "Force Type": random.choice(["Combat", "Support", "Logistics"]),

            "Mode": random.choice(["Air", "Sea"]),

            "POE": random.choice(["Dover AFB", "Norfolk", "San Diego"]),

            "POD": random.choice(["Qatar", "Kuwait", "Germany"]),

            "Personnel": random.randint(50, 800),

            "Weight (STON)": random.randint(10, 500),

            "ALD": ald,

            "EAD": ead,

            "RDD": rdd,

            "Priority": random.randint(1, 5),

            "Status": "Planned"

        })



    return pd.DataFrame(data)



# -----------------------------

# SIMULATION ENGINE

# -----------------------------

def simulate(df):

    df = df.copy()



    for i in range(len(df)):

        if df.loc[i, "Mode"] == "Air":

            transit = random.randint(1, 3)

        else:

            transit = random.randint(7, 20)



        arrival = df.loc[i, "EAD"] + timedelta(days=transit)



        if arrival <= df.loc[i, "RDD"]:

            df.loc[i, "Status"] = "On-Time"

        else:

            df.loc[i, "Status"] = "Delayed"



    return df



# -----------------------------

# BUTTON ACTIONS

# -----------------------------

if generate_btn:

    st.session_state.df = generate_tpfdd(num_records)



if simulate_btn and not st.session_state.df.empty:

    st.session_state.df = simulate(st.session_state.df)



if reset_btn:

    st.session_state.df = pd.DataFrame()



df = st.session_state.df



# -----------------------------

# DISPLAY DATA

# -----------------------------

st.subheader("TPFDD Data")



if not df.empty:

    st.dataframe(df, use_container_width=True)

else:

    st.info("No data generated yet.")



# -----------------------------

# DASHBOARD

# -----------------------------

if not df.empty:

    st.subheader("Operational Dashboard")



    col1, col2 = st.columns(2)



    with col1:

        st.write("### Mode Distribution")

        st.bar_chart(df["Mode"].value_counts())



        st.write("### Status Distribution")

        st.bar_chart(df["Status"].value_counts())



    with col2:

        st.write("### Personnel by Force Type")

        st.bar_chart(df.groupby("Force Type")["Personnel"].sum())



        st.write("### RDD Timeline")

        timeline = df.copy()

        timeline["RDD"] = pd.to_datetime(timeline["RDD"])

        st.line_chart(timeline["RDD"].value_counts().sort_index())



# -----------------------------

# EXPORT FUNCTIONS

# -----------------------------

if not df.empty:

    st.subheader("Export Options")



    col1, col2, col3 = st.columns(3)



    # CSV

    csv = df.to_csv(index=False)

    col1.download_button("Download CSV", csv, "tpfdd.csv")



    # JSON

    json_data = df.to_json(orient="records", date_format="iso")

    col2.download_button("Download JSON", json_data, "tpfdd.json")



    # PDF GENERATION (CORRECT)

    def create_pdf(dataframe):

        file_path = "/mnt/data/tpfdd_report.pdf"



        doc = SimpleDocTemplate(file_path)

        styles = getSampleStyleSheet()



        content = []

        content.append(Paragraph("Enterprise TPFDD Report", styles["Title"]))

        content.append(Spacer(1, 10))



        # Convert dataframe to table

        table_data = [list(dataframe.columns)]

        for _, row in dataframe.head(50).iterrows():

            table_data.append([str(x) for x in row])



        table = Table(table_data)

        content.append(table)



        doc.build(content)

        return file_path



    if col3.button("Generate PDF"):

        pdf_file = create_pdf(df)



        with open(pdf_file, "rb") as f:

            col3.download_button(

                "Download PDF",

                f,

                file_name="tpfdd_report.pdf"

            )



# -----------------------------

# FOOTER

# -----------------------------

st.markdown("---")

st.success("✔ Enterprise TPFDD Simulation Ready")