# dental_app.py

import streamlit as st

import pandas as pd

import random

import json

from datetime import datetime, timedelta



# -------------------------------

# Utility Functions

# -------------------------------

def generate_sample_records(n=50):

    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona",

             "George", "Hannah", "Ivan", "Julia"]

    procedures = ["Cleaning", "Filling", "Root Canal", "Extraction", "Braces"]



    records = []

    for i in range(n):

        record = {

            "PatientID": i + 1,

            "Name": random.choice(names),

            "Procedure": random.choice(procedures),

            "AppointmentDate": (datetime.today() + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),

            "Status": random.choice(["Waiting", "In Progress", "Completed"]),

        }

        records.append(record)

    return pd.DataFrame(records)



def save_records(df, filename="records.json"):

    df.to_json(filename, orient="records")



def load_records(filename="records.json"):

    try:

        return pd.read_json(filename)

    except Exception:

        return pd.DataFrame()



# -------------------------------

# Streamlit UI

# -------------------------------

st.set_page_config(page_title="Dental Practice Workflow", layout="wide")

st.title("🦷 Dental Practice Workflow System")



# Sidebar menu

menu = st.sidebar.radio("Choose Action", ["Dashboard", "Generate Records", "Upload Data", "Clear Records"])



# -------------------------------

# Dashboard

# -------------------------------

if menu == "Dashboard":

    st.header("📊 Patient Queue Summary")



    df = load_records()

    if df.empty:

        st.warning("No records found. Please generate or upload data.")

    else:

        waiting = (df["Status"] == "Waiting").sum()

        in_progress = (df["Status"] == "In Progress").sum()

        completed = (df["Status"] == "Completed").sum()



        col1, col2, col3 = st.columns(3)

        col1.metric("Waiting", waiting)

        col2.metric("In Progress", in_progress)

        col3.metric("Completed", completed)



        st.subheader("Patient Records")

        st.dataframe(df)



# -------------------------------

# Generate Sample Records

# -------------------------------

elif menu == "Generate Records":

    st.header("📋 Generate Sample Records")

    num = st.slider("Number of records", 10, 200, 50)

    if st.button("Generate"):

        df = generate_sample_records(num)

        save_records(df)

        st.success(f"✅ {num} records generated and saved.")

        st.dataframe(df)



# -------------------------------

# Upload Your Own Data

# -------------------------------

elif menu == "Upload Data":

    st.header("📂 Upload Your Own Data")

    uploaded_file = st.file_uploader("Upload JSON or CSV", type=["json", "csv"])

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_json(uploaded_file)

        save_records(df)

        st.success("✅ Data uploaded and saved.")

        st.dataframe(df)



# -------------------------------

# Clear Records

# -------------------------------

elif menu == "Clear Records":

    st.header("🧹 Clear Records")

    if st.button("Clear All"):

        save_records(pd.DataFrame())

        st.success("✅ All records cleared.")