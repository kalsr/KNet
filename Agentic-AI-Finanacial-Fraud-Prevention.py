# Agentic-AI-Finanacial-Fraud-Prevention

import streamlit as st

import pandas as pd

import numpy as np

import plotly.express as px

from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.lib.styles import getSampleStyleSheet



# -------------------------------

# PAGE CONFIG

# -------------------------------

st.set_page_config(layout="wide")



# -------------------------------

# HEADER

# -------------------------------

st.markdown("""

<div style="background-color:#003366;padding:18px;border-radius:6px">

<h2 style="color:white;text-align:center">

Agentic AI Risk Analytics Platform<br>

<span style="font-size:16px">

The Power of Agentic AI in Fraud & Financial Crime Prevention<br>

Developed by Randy Singh – Kalsnet (KNet) Consulting Group

</span>

</h2>

</div>

""", unsafe_allow_html=True)



st.write("")



# -------------------------------

# EXPLANATION / NOTES PANEL

# -------------------------------

with st.expander("ℹ️ How Key Metrics are Calculated (Click to Expand)", expanded=True):

    st.markdown("""

**Risk Score:**  

- Synthetic baseline risk score between 0-100.  

- Represents transaction risk based on amount, frequency, geography, and customer behavior (rule-based in demo).



**Agentic Risk Score:**  

- Adjusted from Risk Score using a scenario multiplier:  

    - Fraud Detection: ×1.2  

    - AML Monitoring: ×1.1  

    - Sanctions: ×1.3  

    - Insider Risk: ×1.15  

- Clipped at 100. Reflects how autonomous AI agents evaluate risk dynamically.



**Risk Category:**  

- Derived from Risk Score:  

    - Low: 0–33  

    - Medium: 34–66  

    - High: 67–100



**Alert:**  

- Determined by Agentic Risk Score thresholds:  

    - 0–50 → Auto-Clear  

    - 51–75 → Review  

    - 76–100 → Escalate

- Shows if human analyst attention is required.



**Operational Efficiency Metrics:**  

- False Positives Reduced (%) = Auto-Clear ÷ Total Transactions  

- Auto-Resolved Alerts = Count of Auto-Clear  

- Escalated Alerts = Count of Escalate  

- Analyst Hours Saved = Auto-Clear × 0.25 hrs

""")



# -------------------------------

# SIDEBAR CONTROLS

# -------------------------------

st.sidebar.header("⚙️ Controls")



records = st.sidebar.slider("Synthetic Data Records", 0, 100, 50)

scenario = st.sidebar.selectbox(

    "Risk Scenario",

    ["Fraud Detection", "AML Monitoring", "Sanctions", "Insider Risk"]

)



reset = st.sidebar.button("🔄 Reset / Generate New Data")

uploaded_file = st.sidebar.file_uploader("Upload User CSV", type=["csv"])



# -------------------------------

# DATA GENERATION

# -------------------------------

def generate_data(n):

    df = pd.DataFrame({

        "Transaction_ID": [f"TX-{i:03d}" for i in range(1, n + 1)],

        "Amount": np.random.randint(500, 25000, n),

        "Risk_Score": np.random.randint(0, 100, n)

    })

    df["Risk_Category"] = pd.cut(

        df["Risk_Score"],

        bins=[-1, 33, 66, 100],

        labels=["Low", "Medium", "High"]

    )

    return df



if uploaded_file:

    df = pd.read_csv(uploaded_file)

elif records > 0:

    df = generate_data(records)

else:

    df = pd.DataFrame()



# -------------------------------

# AGENTIC AI ENGINE

# -------------------------------

def agentic_ai_engine(df, scenario):

    df = df.copy()

    factor = {

        "Fraud Detection": 1.2,

        "AML Monitoring": 1.1,

        "Sanctions": 1.3,

        "Insider Risk": 1.15

    }.get(scenario, 1)



    df["Agent_Risk"] = (df["Risk_Score"] * factor).clip(0, 100)



    df["Agent_Decision"] = np.where(

        df["Agent_Risk"] > 75, "Escalate",

        np.where(df["Agent_Risk"] > 50, "Review", "Auto-Clear")

    )



    df["Alert"] = np.where(df["Agent_Decision"] == "Escalate", "Yes", "No")

    return df



if not df.empty:

    df = agentic_ai_engine(df, scenario)



# -------------------------------

# OPERATIONAL EFFICIENCY METRICS

# -------------------------------

def efficiency_metrics(df):

    total = len(df)

    auto_clear = (df["Agent_Decision"] == "Auto-Clear").sum()

    escalated = (df["Agent_Decision"] == "Escalate").sum()



    return {

        "False Positives Reduced (%)": round((auto_clear / total) * 100, 1),

        "Auto-Resolved Alerts": auto_clear,

        "Escalated Alerts": escalated,

        "Analyst Hours Saved": round(auto_clear * 0.25, 1)

    }



# -------------------------------

# DASHBOARD

# -------------------------------

if not df.empty:



    # KPI CARDS

    metrics = efficiency_metrics(df)

    c1, c2, c3, c4 = st.columns(4)

    for col, (k, v) in zip([c1, c2, c3, c4], metrics.items()):

        col.metric(k, v)



    st.subheader("📊 Transaction Risk Data")

    st.dataframe(df, use_container_width=True)



    # CHARTS

    colA, colB, colC = st.columns(3)



    pie = px.pie(df, names="Risk_Category", title="Risk Category Distribution")

    colA.plotly_chart(pie, use_container_width=True)



    bar = px.bar(df["Alert"].value_counts(), title="Alerts Overview")

    colB.plotly_chart(bar, use_container_width=True)



    line = px.line(df, y="Agent_Risk", title="Agentic Risk Score Trend")

    colC.plotly_chart(line, use_container_width=True)



    # EXPLAINABLE AI INSIGHTS

    st.subheader("🧠 Agentic AI Strategy Insights")

    st.info(f"""

    In the **{scenario}** scenario, Agentic AI dynamically re-prioritized transactions,

    automatically resolving **{metrics['Auto-Resolved Alerts']}** low-risk events and

    escalating **{metrics['Escalated Alerts']}** high-risk cases.

    

    This demonstrates how Agentic AI:

    • Redefines the fraud & fincrime battlefield  

    • Boosts operational efficiency  

    • Reinvents prevention strategy through intelligent prioritization  

    """)



    # EXPORTS

    st.subheader("⬇️ Export Results")



    st.download_button(

        "Download CSV",

        df.to_csv(index=False),

        file_name="agentic_ai_fincrime_results.csv",

        mime="text/csv"

    )



    def generate_pdf(data):

        file_name = "agentic_ai_fincrime_report.pdf"

        doc = SimpleDocTemplate(file_name)

        styles = getSampleStyleSheet()

        content = [

            Paragraph("Agentic AI Fraud & Financial Crime Report", styles["Title"]),

            Paragraph(f"Scenario: {scenario}", styles["Normal"]),

            Paragraph("Synthetic data – demo purposes only.", styles["Italic"])

        ]

        for k, v in efficiency_metrics(data).items():

            content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

        doc.build(content)

        return file_name



    if st.button("Generate PDF Report"):

        pdf = generate_pdf(df)

        with open(pdf, "rb") as f:

            st.download_button("Download PDF", f, file_name=pdf, mime="application/pdf")



else:

    st.warning("Use the slider or upload data to begin.")