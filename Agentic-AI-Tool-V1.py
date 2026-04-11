

import streamlit as st

import pandas as pd

import numpy as np

import json

import matplotlib.pyplot as plt

import seaborn as sns

from sqlalchemy import create_engine

from sklearn.linear_model import LinearRegression

from fpdf import FPDF

import os



# LangChain / OpenAI

from langchain.chat_models import ChatOpenAI

from langchain.prompts import PromptTemplate



# -----------------------------

# CONFIG

# -----------------------------

st.set_page_config(page_title="Agentic AI Platform", layout="wide")



# -----------------------------

# HEADER

# -----------------------------

st.markdown("<h1 style='text-align:center;'>🚀 Agentic AI Autonomous Platform</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:blue;'>Developed by Randy Singh from Kalsnet (KNet) Consulting Group</h3>", unsafe_allow_html=True)



# -----------------------------

# INIT LLM

# -----------------------------

llm = ChatOpenAI(temperature=0.3)



# -----------------------------

# AGENTS

# -----------------------------



def planner_agent(task):

    prompt = f"""

    You are a planning agent.

    Break this task into structured steps:

    Task: {task}

    """

    return llm.predict(prompt)



def critic_agent(result):

    prompt = f"""

    You are a critic agent.

    Evaluate this result and suggest improvements:

    {result}

    """

    return llm.predict(prompt)



def insight_agent(df):

    prompt = f"""

    Analyze this dataset and provide business insights:

    {df.head().to_string()}

    """

    return llm.predict(prompt)



# -----------------------------

# DATA PROCESSING

# -----------------------------

def process_data(df):

    df = df.copy()

    

    if "Revenue" in df.columns and "Cost" in df.columns:

        df["Profit"] = df["Revenue"] - df["Cost"]

        df["Profit Margin (%)"] = (df["Profit"] / df["Revenue"]) * 100

    

    return df



# -----------------------------

# FORECASTING MODEL

# -----------------------------

def forecast(df):

    if "Revenue" not in df.columns:

        return None

    

    df = df.reset_index()

    df["index"] = df.index

    

    X = df[["index"]]

    y = df["Revenue"]

    

    model = LinearRegression()

    model.fit(X, y)

    

    future = np.array([[len(df)+i] for i in range(5)])

    preds = model.predict(future)

    

    return preds



# -----------------------------

# PDF EXPORT

# -----------------------------

def create_pdf(text):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=10)

    

    for line in text.split("\n"):

        pdf.cell(200, 8, txt=line, ln=True)

    

    file = "report.pdf"

    pdf.output(file)

    return file



# -----------------------------

# SIDEBAR

# -----------------------------

st.sidebar.title("⚙️ Controls")



task = st.sidebar.text_area("Enter Task")



uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])



db_url = st.sidebar.text_input("SQL Connection String", "sqlite:///data.db")



run = st.sidebar.button("Run Agentic AI")



# -----------------------------

# MAIN EXECUTION

# -----------------------------

if run:



    st.subheader("🧠 Planner Agent")

    plan = planner_agent(task)

    st.write(plan)



    # -------------------------

    # LOAD DATA

    # -------------------------

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.DataFrame({

            "Revenue": np.random.randint(1000,5000,50),

            "Cost": np.random.randint(500,3000,50)

        })



    # -------------------------

    # SQL STORAGE

    # -------------------------

    engine = create_engine(db_url)

    df.to_sql("agent_data", engine, if_exists="replace")



    st.subheader("📊 Raw Data")

    st.dataframe(df)



    # -------------------------

    # PROCESS DATA

    # -------------------------

    df = process_data(df)



    st.subheader("📈 Processed Data")

    st.dataframe(df)



    # -------------------------

    # VISUALS

    # -------------------------

    col1, col2 = st.columns(2)



    with col1:

        st.write("### Revenue vs Cost")

        st.bar_chart(df[["Revenue","Cost"]])



    with col2:

        st.write("### Profit Distribution")

        fig, ax = plt.subplots()

        ax.pie(df["Profit"], autopct='%1.1f%%')

        st.pyplot(fig)



    # -------------------------

    # FORECAST

    # -------------------------

    st.subheader("🔮 Forecasting")

    preds = forecast(df)



    if preds is not None:

        st.write("Future Revenue Prediction:", preds)



    # -------------------------

    # INSIGHTS (LLM)

    # -------------------------

    st.subheader("🧠 AI Insights")

    insights = insight_agent(df)

    st.write(insights)



    # -------------------------

    # CRITIC

    # -------------------------

    st.subheader("🧪 Critic Review")

    critique = critic_agent(insights)

    st.write(critique)



    # -------------------------

    # EXPORTS

    # -------------------------

    st.subheader("📤 Export")



    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")

    st.download_button("Download JSON", df.to_json(), "data.json")



    pdf_file = create_pdf(insights + "\n\n" + critique)

    with open(pdf_file, "rb") as f:

        st.download_button("Download PDF", f, "report.pdf")



    st.success("✅ Fully Agentic AI Workflow Completed")
