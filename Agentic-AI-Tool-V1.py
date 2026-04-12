

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

st.markdown("<h4 style='text-align:center; color:blue;'>Groq Multi-Key Enabled | Kalsnet (KNet)</h4>", unsafe_allow_html=True)

# =============================
# LOAD GROQ KEYS (MULTI-KEY)
# =============================
from groq import Groq

def load_groq_keys():
    keys = []

    for i in range(1,6):  # support up to 5 keys
        key_name = f"GROQ_API_KEY_{i}"
        if key_name in st.secrets:
            keys.append(st.secrets[key_name])

    # fallback single key
    if "GROQ_API_KEY" in st.secrets:
        keys.append(st.secrets["GROQ_API_KEY"])

    return keys

GROQ_KEYS = load_groq_keys()

# =============================
# INIT CLIENTS
# =============================
clients = []
for key in GROQ_KEYS:
    try:
        clients.append(Groq(api_key=key))
    except:
        pass

current_client_index = 0

if len(clients) > 0:
    st.sidebar.success(f"✅ {len(clients)} Groq Keys Loaded")
else:
    st.sidebar.error("❌ No Groq Keys Found")

# =============================
# LLM CALL WITH FAILOVER
# =============================
def call_llm(prompt):
    global current_client_index

    for i in range(len(clients)):
        try:
            client = clients[(current_client_index + i) % len(clients)]

            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            current_client_index = (current_client_index + i) % len(clients)

            st.sidebar.write(f"🔑 Using Key #{current_client_index+1}")

            return response.choices[0].message.content

        except Exception as e:
            continue

    # FALLBACK MODE
    return offline_fallback(prompt)

# =============================
# OFFLINE FALLBACK
# =============================
def offline_fallback(prompt):

    if "plan" in prompt.lower():
        return "Step 1: Understand → Step 2: Generate Data → Step 3: Analyze → Step 4: Visualize → Step 5: Report"

    if "explain" in prompt.lower():
        return "Columns represent key attributes of generated dataset."

    if "analyze" in prompt.lower():
        return "Dataset shows trends, patterns, and variability."

    if "critique" in prompt.lower():
        return "Improve by adding more data sources and advanced models."

    return "Autonomous execution complete."

# =============================
# AGENTS
# =============================
def planner_agent(task):
    return call_llm(f"Break into steps:\n{task}")

def data_agent(task):

    try:
        prompt = f"""
        Create dataset for: {task}
        Return JSON:
        columns + data
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
    return call_llm(f"Analyze:\n{df.head().to_string()}")

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

    # VISUALS
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

    # EXPORT
    st.subheader("📤 Export")

    st.download_button("Download CSV", df.to_csv(index=False), "data.csv")
    st.download_button("Download JSON", df.to_json(), "data.json")

    pdf_file = create_pdf(insights + "\n\n" + critique)
    with open(pdf_file, "rb") as f:
        st.download_button("Download PDF", f, "report.pdf")

    st.success("✅ Multi-Key Agentic AI Execution Complete")
