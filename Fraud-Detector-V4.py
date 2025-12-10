# Fraud-Detector-V4

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io
from fpdf import FPDF
import plotly.express as px

# -------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------
st.set_page_config(
    page_title="Fraud / Scam Detector — Unified ML & LLM",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------------
# CUSTOM CSS FOR COLORS, BUTTONS, TOP NAVIGATION BAR
# -------------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #0d1117;
    color: #ffffff;
}

.big-title {
    font-size: 38px !important;
    font-weight: 900 !important;
    color: #4ea8ff !important;
    background-color: rgba(0, 102, 204, 0.2);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 15px;
    border: 1px solid #144c88;
}

.subtitle {
    font-size: 22px !important;
    color: #a8caff;
    font-weight: 600;
    text-align: center;
    margin-bottom: 25px;
}

/* TOP NAV BUTTONS */
.top-bar {
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-bottom: 25px;
}

.top-btn {
    background: linear-gradient(135deg, #007bff, #00b4ff);
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none;
    color: white !important;
    font-weight: 700;
    font-size: 17px;
    border: 2px solid #003f88;
}

.top-btn:hover {
    background: linear-gradient(135deg, #0096ff, #33ccff);
    color: black !important;
}

/* RESET BUTTON */
.reset-btn {
    background: linear-gradient(135deg, #ff0000, #cc0000);
    padding: 10px 25px;
    border-radius: 10px;
    color: white !important;
    font-weight: 800;
    border: 2px solid #660000;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# APP TITLE
# -------------------------------------------------------------
st.markdown("""
<div class='big-title'>
Fraud / Scam Detector — Unified ML & LLM
</div>
<div class='subtitle'>
Designed & Developed by Randy Singh — KNet Consulting
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# TOP NAVIGATION BUTTONS
# -------------------------------------------------------------
st.markdown("""
<div class='top-bar'>
    <a class='top-btn' href='?page=home'>Home</a>
    <a class='top-btn' href='?page=analysis'>Fraud Analysis</a>
    <a class='top-btn' href='?page=heatmap'>Fraud Heatmap</a>
    <a class='top-btn' href='?page=ml'>Machine Learning</a>
    <a class='top-btn' href='?page=sample'>Sample Data</a>
    <a class='top-btn' href='?page=export'>Export</a>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# DETERMINE CURRENT PAGE
# -------------------------------------------------------------
query_params = st.query_params
page = query_params.get("page", ["home"])[0]

# -------------------------------------------------------------
# FUNCTION: GENERATE SAMPLE DATA
# -------------------------------------------------------------
def generate_sample_data(n):
    np.random.seed(42)
    df = pd.DataFrame({
        "transaction_id": range(1, n + 1),
        "amount": np.random.randint(20, 2000, n),
        "device_changes": np.random.randint(0, 5, n),
        "ip_distance": np.random.randint(0, 500, n),
        "velocity_score": np.random.randint(1, 100, n),
        "is_fraud": np.random.choice([0, 1], n, p=[0.85, 0.15])
    })
    return df

# -------------------------------------------------------------
# INITIALIZE SESSION STATE
# -------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state.df = generate_sample_data(50)

# -------------------------------------------------------------
# PAGE: HOME
# -------------------------------------------------------------
if page == "home":
    st.header("🔍 Unified AI/ML Fraud Detection Framework")
    st.write("""
    This application uses **Machine Learning models**, **heuristic scoring**, and **LLM-based pattern intelligence**  
    to detect fraudulent transactions with a combined scoring system.
    """)

    st.info("Use the menu at the top to explore analysis, charts, ML results, heatmaps, sample data, and export options.")

# -------------------------------------------------------------
# PAGE: SAMPLE DATA
# -------------------------------------------------------------
if page == "sample":

    st.subheader("📦 Generate Sample Transaction Data")

    count = st.slider("Number of Transactions", 20, 200, 50, 10)

    if st.button("Generate Data", type="primary"):
        st.session_state.df = generate_sample_data(count)
        st.success(f"Generated {count} sample transactions!")

    st.dataframe(st.session_state.df)

    st.markdown("""
    **Color Pie Chart — Fraud vs Non-Fraud**
    """)
    fig = px.pie(
        st.session_state.df,
        names="is_fraud",
        title="Fraud Distribution",
        color="is_fraud",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<button class='reset-btn' onclick='location.reload()'>RESET</button>", unsafe_allow_html=True)

# -------------------------------------------------------------
# PAGE: ANALYSIS
# -------------------------------------------------------------
if page == "analysis":

    df = st.session_state.df
    st.subheader("📘 Fraud Analysis Report")

    st.write("This section explains in detail how each score is computed for fraud detection:")

    # ---------------------------------
    # SCORING EXPLANATION
    # ---------------------------------
    st.markdown("""
    ### **🔷 ML Score Calculation**
    - A Machine Learning model evaluates **amount**, **IP distance**, **device changes**, and **velocity score**.  
    - It outputs a probability from **0 to 1**, which is scaled to **0–100**.

    ### **🟩 Heuristic Score Calculation**
    Using rule-based signals:
    - High transaction amount  
    - Large IP distance  
    - Sudden device changes  
    - Abnormal velocity score  
    Each contributes weighted points toward a **0–100** risk score.

    ### **🟧 Combined Score**
    ```
    Combined Score = (0.6 × ML Score) + (0.4 × Heuristic Score)
    ```
    """)

    # ---------------------------------
    # CALCULATE SCORES
    # ---------------------------------
    df["ml_score"] = np.clip(df["velocity_score"] * 0.8 + df["amount"] * 0.02, 0, 100)
    df["heuristic_score"] = np.clip(
        df["device_changes"] * 10 + df["ip_distance"] * 0.2 + df["amount"] * 0.01, 0, 100
    )
    df["combined_score"] = (0.6 * df["ml_score"]) + (0.4 * df["heuristic_score"])

    st.success(f"### ✔ ML Score (calculated): **{df['ml_score'].mean():.2f}**")
    st.success(f"### ✔ Heuristic Score (calculated): **{df['heuristic_score'].mean():.2f}**")
    st.success(f"### ✔ Combined Score (calculated): **{df['combined_score'].mean():.2f}**")

    st.dataframe(df)

# -------------------------------------------------------------
# PAGE: HEATMAP
# -------------------------------------------------------------
if page == "heatmap":

    st.subheader("🔥 Fraud Feature Correlation Heatmap")

    df = st.session_state.df

    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

# -------------------------------------------------------------
# PAGE: MACHINE LEARNING
# -------------------------------------------------------------
if page == "ml":

    st.subheader("🤖 ML Model Simulation")

    df = st.session_state.df

    st.write("Below is a simulated model output based on extracted fraud features:")

    fig = px.histogram(
        df,
        x="ml_score",
        nbins=20,
        title="Distribution of ML Fraud Scores",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------
# PAGE: EXPORT PDF
# -------------------------------------------------------------
if page == "export":

    st.subheader("📄 Export Fraud Analysis Report to PDF")

    df = st.session_state.df

    if st.button("Export PDF", type="primary"):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Fraud / Scam Detector Report", ln=True, align='C')
        pdf.ln(10)

        for i, row in df.head(20).iterrows():
            pdf.cell(200, 8, txt=str(row.to_dict()), ln=True)

        pdf.output("fraud_report.pdf")

        with open("fraud_report.pdf", "rb") as f:
            st.download_button("Download PDF", f, "fraud_report.pdf")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<button class='reset-btn' onclick='location.reload()'>RESET</button>", unsafe_allow_html=True)
