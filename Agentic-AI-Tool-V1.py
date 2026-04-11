


import streamlit as st
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import os

# ✅ FIXED: Updated LangChain import
try:
    from langchain_openai import ChatOpenAI
    LANGCHAIN_AVAILABLE = True
except:
    LANGCHAIN_AVAILABLE = False

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(page_title="Agentic AI Platform", layout="wide")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<h1 style='text-align:center;'>🚀 Agentic AI Autonomous Platform</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:blue;'>Developed by Randy Singh - Kalsnet (KNet)</h3>", unsafe_allow_html=True)

# -----------------------------
# INIT LLM (SAFE)
# -----------------------------
llm = None

if LANGCHAIN_AVAILABLE:
    try:
        if "OPENAI_API_KEY" in st.secrets:
            os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

        llm = ChatOpenAI(
            temperature=0.3,
            model="gpt-4o-mini"
        )
    except Exception as e:
        st.warning("LLM not initialized. Check API key or package install.")
else:
    st.warning("LangChain not installed. Running without AI features.")

# -----------------------------
# SAFE LLM CALL
# -----------------------------
def call_llm(prompt):
    if llm:
        try:
            return llm.invoke(prompt).content
        except:
            return "⚠️ LLM call failed."
    return "⚠️ No LLM available. Please configure API key."

# -----------------------------
# AGENTS
# -----------------------------
def planner_agent(task):
    prompt = f"Break this task into structured steps:\n{task}"
    return call_llm(prompt)

def critic_agent(result):
    prompt = f"Evaluate this result and suggest improvements:\n{result}"
    return call_llm(prompt)

def insight_agent(df):
    prompt = f"Analyze this dataset:\n{df.head().to_string()}"
    return call_llm(prompt)

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
# FORECAST
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
    return model.predict(future)

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
    st.write(planner_agent(task))

    # LOAD DATA
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.DataFrame({
            "Revenue": np.random.randint(1000,5000,50),
            "Cost": np.random.randint(500,3000,50)
        })

    # SQL
    engine = create_engine(db_url)
    df.to_sql("agent_data", engine, if_exists="replace")

    st.subheader("📊 Raw Data")
    st.dataframe(df)

    # PROCESS
    df = process_data(df)
    st.subheader("📈 Processed Data")
    st.dataframe(df)

    # VISUALS
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Revenue vs Cost")
        st.bar_chart(df[["Revenue","Cost"]])

    with col2:
        st.write("### Profit Distribution")
        fig, ax = plt.subplots()
        ax.pie(df["Profit"], autopct='%1.1f%%')
        st.pyplot(fig)

    # FORECAST
    st.subheader("🔮 Forecasting")
    preds = forecast(df)
    if preds is not None:
        st.write(preds)

    # INSIGHTS
    st.subheader("🧠 AI Insights")
    insights = insight_agent(df)
    st.write(insights)

    # CRITIC
    st.subheader("🧪 Critic Review")
    critique = critic_agent(insights)
    st.write(critique)

    # EXPORT
    st.subheader("📤 Export")
    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", df.to_json(), "data.json")

    pdf_file = create_pdf(insights + "\n\n" + critique)
    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, "report.pdf")

    st.success("✅ Fully Agentic AI Workflow Completed")