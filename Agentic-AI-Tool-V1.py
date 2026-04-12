

import streamlit as st
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import os

# =============================
# CONFIG + BLUE HEADER
# =============================
st.set_page_config(page_title="Agentic AI Platform", layout="wide")

st.markdown("""
<h1 style='text-align:center; color:white; background-color:#003366; padding:15px; border-radius:10px;'>
🚀 Agentic AI Autonomous Platform
</h1>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center; color:blue;'>Groq-Powered | Developed by Randy Singh</h4>", unsafe_allow_html=True)

# =============================
# GROQ LLM SETUP
# =============================
llm = None

try:
    from groq import Groq

    api_key = None
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["	gsk_...5h55"]
    elif "GROQ_API_KEY" in os.environ:
        api_key = os.environ["	gsk_...5h55"]

    if api_key:
        client = Groq(api_key=api_key)
        llm = client
        st.sidebar.success("✅ Groq Connected")
    else:
        st.sidebar.warning("⚠️ No Groq API Key → Running Offline Mode")

except Exception as e:
    st.sidebar.warning(f"Groq Load Failed: {e}")

# =============================
# LLM CALL
# =============================
def call_llm(prompt):

    if llm:
        try:
            response = llm.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except:
            return "⚠️ Groq LLM error"

    # 🔥 OFFLINE FALLBACK (VERY IMPORTANT)
    if "plan" in prompt.lower():
        return "Step 1: Understand task → Step 2: Generate data → Step 3: Analyze → Step 4: Visualize → Step 5: Report"

    if "explain" in prompt.lower():
        return "These columns represent key attributes relevant to the generated dataset."

    if "analyze" in prompt.lower():
        return "The dataset shows patterns, variability, and potential insights."

    if "critique" in prompt.lower():
        return "Enhance model with more data sources, validation, and predictive analytics."

    return "Autonomous execution completed."

# =============================
# AGENTS
# =============================
def planner_agent(task):
    return call_llm(f"Break into steps:\n{task}")

def data_agent(task):

    try:
        prompt = f"""
        Create dataset for: {task}
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
        elif "hr" in task.lower():
            return pd.DataFrame({
                "Employee": [f"Emp{i}" for i in range(50)],
                "Salary": np.random.randint(50000,150000,50),
                "Performance": np.random.randint(1,5,50)
            })
        else:
            return pd.DataFrame({
                "Value": np.random.randint(1,100,50)
            })

def insight_agent(df):
    return call_llm(f"Analyze dataset:\n{df.head().to_string()}")

def critic_agent(text):
    return call_llm(f"Critique:\n{text}")

def explain_columns(df):
    return call_llm(f"Explain columns:\n{df.columns.tolist()}")

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
# SIDEBAR
# =============================
st.sidebar.title("⚙️ Controls")

task = st.sidebar.text_area("Enter Task")
run = st.sidebar.button("Run Agentic AI")

# =============================
# MAIN EXECUTION
# =============================
if run:

    st.subheader("🧠 Planner")
    st.write(planner_agent(task))

    st.subheader("🤖 Autonomous Data")
    df = data_agent(task)
    st.dataframe(df)

    st.subheader("📘 Field Explanation")
    st.write(explain_columns(df))

    # CHARTS
    st.subheader("📊 Visualizations")

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(numeric_cols) >= 2:
        st.bar_chart(df[numeric_cols[:2]])
    elif len(numeric_cols) == 1:
        st.line_chart(df[numeric_cols[0]])

    if len(numeric_cols) > 0:
        fig, ax = plt.subplots()
        ax.hist(df[numeric_cols[0]])
        st.pyplot(fig)

    # FORECAST
    st.subheader("🔮 Forecast")
    preds = forecast(df)
    if preds is not None:
        st.write(preds)

    # INSIGHTS
    st.subheader("🧠 Insights")
    insights = insight_agent(df)
    st.write(insights)

    # CRITIC
    st.subheader("🧪 Critic")
    critique = critic_agent(insights)
    st.write(critique)

    # EXPORTS
    st.subheader("📤 Export")

    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", df.to_json(), "data.json")

    pdf_file = create_pdf(insights + "\n\n" + critique)
    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, "report.pdf")

    st.success("✅ Agentic AI Execution Completed")
