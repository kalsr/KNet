


# streamlit run app.py

import streamlit as st

import pandas as pd

import numpy as np

import json

from fpdf import FPDF

import matplotlib.pyplot as plt

import os



# -----------------------------

# PAGE CONFIG

# -----------------------------

st.set_page_config(page_title="Agentic AI Task Executor", layout="wide")



# -----------------------------

# HEADER / BRANDING

# -----------------------------

st.markdown(

    "<h1 style='text-align: center; font-weight: bold;'>Agentic AI Autonomous Task Executor</h1>",

    unsafe_allow_html=True

)



st.markdown(

    "<h3 style='text-align: center; color: blue; font-weight: bold;'>Developed by Randy Singh from Kalsnet (KNet) Consulting Group</h3>",

    unsafe_allow_html=True

)



st.write("---")



# -----------------------------

# USER INPUT

# -----------------------------

task = st.text_input("Enter an autonomous task for the AI agent:")



num_records = st.slider("Select number of data records", 10, 100, 20)



# -----------------------------

# AGENTIC AI SIMULATION

# -----------------------------

def generate_data(n):

    data = pd.DataFrame({

        "Revenue": np.random.randint(1000, 5000, n),

        "Cost": np.random.randint(500, 3000, n)

    })

    

    # FORMULAS

    data["Profit"] = data["Revenue"] - data["Cost"]

    data["Profit Margin (%)"] = (data["Profit"] / data["Revenue"]) * 100

    

    return data



# -----------------------------

# PDF EXPORT FUNCTION

# -----------------------------

def create_pdf(data, filename="report.pdf"):

    pdf = FPDF()

    pdf.add_page()

    

    pdf.set_font("Arial", size=10)

    

    pdf.cell(200, 10, txt="Agentic AI Report", ln=True)

    

    for i, row in data.iterrows():

        pdf.cell(200, 8, txt=str(row.to_dict()), ln=True)

    

    pdf.output(filename)



# -----------------------------

# MAIN EXECUTION

# -----------------------------

if st.button("Run Agentic AI Task"):



    st.subheader("🧠 Agent Planning")

    st.write(f"Task Received: **{task}**")

    

    st.write("Steps:")

    st.write("1. Generate Data")

    st.write("2. Apply Business Logic")

    st.write("3. Analyze Results")

    st.write("4. Visualize & Export")



    # Generate Data

    df = generate_data(num_records)



    st.subheader("📊 Generated Data")

    st.dataframe(df)



    # -----------------------------

    # CHARTS

    # -----------------------------

    st.subheader("📈 Data Visualization")



    # BAR CHART

    st.write("### Revenue vs Cost")

    st.bar_chart(df[["Revenue", "Cost"]])



    # PIE CHART

    st.write("### Profit Distribution")



    fig, ax = plt.subplots()

    ax.pie(df["Profit"], labels=None, autopct='%1.1f%%')

    ax.set_title("Profit Share Distribution")

    st.pyplot(fig)



    # -----------------------------

    # EXPORTS

    # -----------------------------

    st.subheader("📤 Export Results")



    # CSV

    csv = df.to_csv(index=False)

    st.download_button("Download CSV", csv, "data.csv")



    # JSON

    json_data = df.to_json(orient="records")

    st.download_button("Download JSON", json_data, "data.json")



    # PDF

    pdf_file = "report.pdf"

    create_pdf(df, pdf_file)



    with open(pdf_file, "rb") as f:

        st.download_button("Download PDF", f, "report.pdf")



    # -----------------------------

    # EXPLANATIONS

    # -----------------------------

    st.subheader("📘 Explanation of AI Logic")



    st.write("""

    This Agentic AI system follows a structured pipeline:



    1. **Task Interpretation**

       - Converts user input into an execution plan.



    2. **Data Generation**

       - Simulates real-world structured data.



    3. **Computation Layer**

       - Profit = Revenue - Cost

       - Profit Margin = (Profit / Revenue) * 100



    4. **Visualization**

       - Bar Chart → compares revenue vs cost

       - Pie Chart → shows proportional profit distribution



    5. **Export Engine**

       - CSV → tabular format

       - JSON → structured API format

       - PDF → human-readable report

    """)



    st.success("✅ Agentic AI Task Completed Successfully!")
