import streamlit as st
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import os

# =============================
# CONFIG + HEADER (BLUE TITLE)
# =============================
st.set_page_config(page_title="Agentic AI Platform", layout="wide")

st.markdown("""
<h1 style='text-align:center; color:white; background-color:#003366; padding:15px; border-radius:10px;'>
🚀 Agentic AI Autonomous Platform
</h1>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center; color:blue;'>Developed by Randy Singh – Kalsnet (KNet)</h4>", unsafe_allow_html=True)

# =============================
# LLM SETUP (SAFE)
# =============================
try:
    from langchain_openai import ChatOpenAI
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
except:
    llm = None

def call_llm(prompt):
    try:
        return llm.invoke(prompt).content if llm else "LLM not available"
    except:
        return "LLM error"

# =============================
# AGENTS
# =============================
def planner_agent(task):
    return call_llm(f"Break this into steps:\n{task}")

def data_agent(task):
    try:
        prompt = f"""
        Create dataset for task: {task}
        Return JSON with:
        columns + data (10 rows)
        """
        res = call_llm(prompt)
        data_json = json.loads(res)
        return pd.DataFrame(data_json["data"], columns=data_json["columns"])
    except:
        if "cyber" in task.lower():
            return pd.DataFrame({
                "IP": [f"192.168.1.{i}" for i in range(1,50)],
                "Threat Score": np.random.randint(1,100,49),
                "Status": np.random.choice(["Safe","Suspicious","Malicious"],49)
            })
        elif "finance" in task.lower():
            return pd.DataFrame({
                "Revenue": np.random.randint(1000,5000,50),
                "Cost": np.random.randint(500,3000,50)
            })
        else:
            return pd.DataFrame({
                "Value": np.random.randint(1,100,50)
            })

def insight_agent(df):
    return call_llm(f"Analyze dataset:\n{df.head().to_string()}")

def critic_agent(text):
    return call_llm(f"Critique and improve:\n{text}")

def explain_columns(df):
    return call_llm(f"Explain each column in dataset:\n{df.columns.tolist()}")

# =============================
# FORECAST
# =============================
def forecast(df):
    numeric = df.select_dtypes(include=np.number).columns
    if len(numeric) == 0:
        return None

    target = numeric[0]
    df = df.reset_index()
    df["index"] = df.index

    X = df[["index"]]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(df)+i] for i in range(5)])
    return model.predict(future)

# =============================
# PDF EXPORT
# =============================
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for line in text.split("\n"):
        pdf.cell(200, 8, txt=line, ln=True)

    file = "report.pdf"
    pdf.output(file)
    return file

# =============================
# UI CONTROLS
# =============================
st.sidebar.title(" Controls")

task = st.sidebar.text_area("Enter Task")
run = st.sidebar.button("Run Agentic AI")

# =============================
# MAIN EXECUTION
# =============================
if run:

    st.subheader(" Planner Agent")
    plan = planner_agent(task)
    st.write(plan)

    # AUTONOMOUS DATA
    st.subheader(" Autonomous Data Generation")
    df = data_agent(task)
    st.dataframe(df)

    # COLUMN EXPLANATION
    st.subheader(" Field Explanation")
    explanation = explain_columns(df)
    st.write(explanation)

    # DYNAMIC VISUALS
    st.subheader(" Dynamic Charts")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) >= 2:
        st.bar_chart(df[numeric_cols[:2]])
    elif len(numeric_cols) == 1:
        st.line_chart(df[numeric_cols[0]])

    # PIE CHART
    if len(numeric_cols) > 0:
        fig, ax = plt.subplots()
        ax.hist(df[numeric_cols[0]])
        st.pyplot(fig)

    # FORECAST
    st.subheader(" Forecast")
    preds = forecast(df)
    if preds is not None:
        st.write(preds)

    # INSIGHTS
    st.subheader(" Insights")
    insights = insight_agent(df)
    st.write(insights)

    # CRITIC
    st.subheader(" Critic")
    critique = critic_agent(insights)
    st.write(critique)

    # EXPORTS
    st.subheader(" Export Options")

    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", df.to_json(), "data.json")

    pdf_file = create_pdf(insights + "\n\n" + critique + "\n\n" + explanation)
    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, "report.pdf")

    st.success(" Fully Autonomous Agentic AI Completed")