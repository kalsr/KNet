# TPFDD maker
import streamlit as st

import pandas as pd

import numpy as np

import random

from datetime import datetime, timedelta

import json

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from reportlab.lib.styles import getSampleStyleSheet



# -----------------------------

# PAGE CONFIG

# -----------------------------

st.set_page_config(page_title="TPFDD Generator", layout="wide")



# -----------------------------

# TITLE

# -----------------------------

st.markdown(

    "<h1 style='text-align: center; color: blue;'>"

    "TPFDD Generator Application<br>"

    "Developed by Randy Singh from Kalsnet (KNet) Group"

    "</h1>",

    unsafe_allow_html=True

)



# -----------------------------

# SIDEBAR CONTROLS

# -----------------------------

st.sidebar.header("Controls")



num_records = st.sidebar.slider("Synthetic Data Records", 0, 300, 50)



generate_btn = st.sidebar.button("Generate TPFDD")

reset_btn = st.sidebar.button("Reset Data")



# -----------------------------

# SESSION STATE

# -----------------------------

if "df" not in st.session_state:

    st.session_state.df = pd.DataFrame()



# -----------------------------

# DATA GENERATION FUNCTION

# -----------------------------

def generate_tpfdd(n):

    data = []

    for i in range(n):

        uln = f"ULN{1000+i}"

        uic = f"UIC{random.randint(100,999)}"

        personnel = random.randint(10, 500)

        weight = round(random.uniform(1, 100), 2)

        mode = random.choice(["Air", "Sea", "Land"])

        origin = random.choice(["CONUS", "EUCOM", "INDOPACOM"])

        destination = random.choice(["CENTCOM", "AFRICOM", "SOUTHCOM"])

        

        base_date = datetime.today()

        ald = base_date + timedelta(days=random.randint(1,10))

        rdd = ald + timedelta(days=random.randint(5,20))

        

        data.append({

            "ULN": uln,

            "UIC": uic,

            "Personnel": personnel,

            "Weight(STON)": weight,

            "Mode": mode,

            "Origin": origin,

            "Destination": destination,

            "ALD": ald.date(),

            "RDD": rdd.date()

        })

        

    return pd.DataFrame(data)



# -----------------------------

# BUTTON ACTIONS

# -----------------------------

if generate_btn:

    st.session_state.df = generate_tpfdd(num_records)



if reset_btn:

    st.session_state.df = pd.DataFrame()



df = st.session_state.df



# -----------------------------

# DISPLAY DATA

# -----------------------------

st.subheader("Generated TPFDD Data")



if not df.empty:

    st.dataframe(df, use_container_width=True)

else:

    st.info("No data generated yet.")



# -----------------------------

# VISUALIZATIONS

# -----------------------------

if not df.empty:

    st.subheader("Analytics Dashboard")



    col1, col2 = st.columns(2)



    with col1:

        st.write("### Movement Mode Distribution")

        st.bar_chart(df["Mode"].value_counts())



    with col2:

        st.write("### Personnel by Destination")

        st.bar_chart(df.groupby("Destination")["Personnel"].sum())



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

    json_data = df.to_json(orient="records")

    col2.download_button("Download JSON", json_data, "tpfdd.json")



    # PDF

    def create_pdf(dataframe):

        file_path = "tpfdd.pdf"

        doc = SimpleDocTemplate(file_path)

        styles = getSampleStyleSheet()



        content = []

        content.append(Paragraph("TPFDD Report", styles["Title"]))

        content.append(Spacer(1, 10))



        for _, row in dataframe.iterrows():

            line = ", ".join([f"{col}: {row[col]}" for col in dataframe.columns])

            content.append(Paragraph(line, styles["Normal"]))

            content.append(Spacer(1, 5))



        doc.build(content)

        return file_path



    if col3.button("Generate PDF"):

        pdf_file = create_pdf(df)

        with open(pdf_file, "rb") as f:

            col3.download_button("Download PDF", f, "tpfdd.pdf")



# -----------------------------

# FOOTER

# -----------------------------

st.markdown("---")

st.markdown("### System Status")

st.success("Application Ready | Synthetic TPFDD Generator Active")

""

