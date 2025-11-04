

# agentic_ai_dashboard_V1.py
# ------------------------------------------------------------
# Agentic AI Dashboard v2 - Developed by Randy Singh, KNet Consulting Group
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Agentic AI Dashboard - KNet Consulting",
    page_icon="🤖",
    layout="wide"
)

# ---------------- STYLES ----------------
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1100px;
        }
        .main-title {
            color: #0a2540;
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 6px;
        }
        .sub-title {
            color: #555;
            font-size: 16px;
            margin-bottom: 20px;
        }
        .upload-btn {
            background-color: #2196F3;
            color: white;
            font-weight: 600;
            border-radius: 6px;
            padding: 8px 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.sidebar.markdown(
    '<div class="main-title">🤖 Agentic AI Dashboard</div>'
    '<div class="sub-title">KNet Consulting Group</div>',
    unsafe_allow_html=True
)

# ---------------- CONTROLS ----------------
st.sidebar.header("⚙️ Controls")

if st.sidebar.button("🔄 Refresh"):
    st.rerun()

if st.sidebar.button("🧹 Reset"):
    st.session_state.clear()
    st.rerun()

# ---------------- USE CASES ----------------
use_cases = {
    "AI Customer Service Agents": "#4CAF50",
    "Autonomous Coding & DevOps Agents": "#2196F3",
    "Financial Analysis & Trading Agents": "#9C27B0",
    "Business Process Automation Agents": "#FF9800",
    "AI Research & Knowledge Discovery Agents": "#3F51B5",
    "Cybersecurity & Threat-Hunting Agents": "#E91E63",
    "Personal AI Assistants": "#009688",
    "E-commerce & Marketing Automation Agents": "#795548",
    "Autonomous Robotics & Logistics Agents": "#607D8B",
    "Healthcare & Clinical Decision Agents": "#8BC34A"
}

# ---------------- PAGE SELECT ----------------
page = st.sidebar.selectbox("📂 Select Use Case", list(use_cases.keys()))

# ---------------- MAIN PANEL ----------------
st.markdown(f"## 🧠 {page}")
st.write("You can either upload your own dataset or generate synthetic data using the slider below.")

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📤 Upload your own dataset (CSV, Excel, or JSON)",
    type=["csv", "xlsx", "json"]
)

# ---------------- LOAD OR GENERATE DATA ----------------
data = None

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()

    try:
        if file_type == "csv":
            data = pd.read_csv(uploaded_file)
        elif file_type == "xlsx":
            data = pd.read_excel(uploaded_file)
        elif file_type == "json":
            data = pd.read_json(uploaded_file)
        st.success("✅ Data uploaded successfully!")
    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

else:
    st.info("Or generate synthetic data using the slider below 👇")
    n = st.slider("Generate synthetic data points", 1, 100, 50)

    np.random.seed(42)

    metrics = {
        "AI Customer Service Agents": ["Response_Time(ms)", "Resolution_Rate(%)", "Customer_Satisfaction(%)"],
        "Autonomous Coding & DevOps Agents": ["Efficiency_Score", "Error_Rate(%)", "Automation_Level(%)"],
        "Financial Analysis & Trading Agents": ["ROI(%)", "Risk_Index", "Decision_Accuracy(%)"],
        "Business Process Automation Agents": ["Process_Speed(%)", "Cost_Savings(%)", "Workflow_Accuracy(%)"],
        "AI Research & Knowledge Discovery Agents": ["Insight_Accuracy(%)", "Paper_Coverage(%)", "Novelty_Index"],
        "Cybersecurity & Threat-Hunting Agents": ["Threat_Detection_Rate(%)", "Response_Latency(ms)", "Anomaly_Score"],
        "Personal AI Assistants": ["Task_Completion(%)", "Context_Retention(%)", "Personalization_Score"],
        "E-commerce & Marketing Automation Agents": ["Conversion_Rate(%)", "Engagement_Score", "Revenue_Growth(%)"],
        "Autonomous Robotics & Logistics Agents": ["Delivery_Success(%)", "Energy_Usage(kWh)", "Route_Optimization(%)"],
        "Healthcare & Clinical Decision Agents": ["Diagnosis_Accuracy(%)", "Treatment_Success(%)", "Compliance_Rate(%)"]
    }

    cols = metrics.get(page, [])
    data = pd.DataFrame({
        "ID": range(1, n + 1),
        cols[0]: np.random.uniform(40, 100, n).round(2),
        cols[1]: np.random.uniform(40, 100, n).round(2),
        cols[2]: np.random.uniform(40, 100, n).round(2),
    })

# ---------------- SHOW DATA ----------------
if data is not None:
    st.subheader("📋 Data Preview")
    st.dataframe(data, use_container_width=True)

    # ---------------- VISUALIZATION ----------------
    numeric_data = data.select_dtypes(include=[np.number]).drop(columns="ID", errors="ignore")

    if len(numeric_data.columns) >= 2:
        st.subheader("📊 Visualizations")

        col1, col2, col3 = st.columns(3)
        mean_vals = numeric_data.mean()

        # Bar Chart
        with col1:
            fig, ax = plt.subplots()
            ax.bar(mean_vals.index, mean_vals.values, color=["#2196F3", "#FF9800", "#4CAF50"])
            ax.set_title("Average Metrics")
            plt.xticks(rotation=20)
            st.pyplot(fig)

        # Pie Chart
        with col2:
            fig2, ax2 = plt.subplots()
            ax2.pie(mean_vals, labels=mean_vals.index, autopct="%1.1f%%", startangle=90)
            ax2.set_title("Metric Distribution (%)")
            st.pyplot(fig2)

        # Line Chart
        with col3:
            fig3, ax3 = plt.subplots()
            for col in numeric_data.columns:
                ax3.plot(data.index + 1, numeric_data[col], label=col)
            ax3.legend()
            ax3.set_title("Trend Over Data Points")
            st.pyplot(fig3)

        # ---------------- DOWNLOADS ----------------
        st.subheader("📥 Download Data")

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv = data.to_csv(index=False).encode("utf-8")
        json = data.to_json(orient="records", indent=2).encode("utf-8")
        excel_buffer = BytesIO()
        data.to_excel(excel_buffer, index=False)
        excel_buffer.seek(0)

        st.download_button("⬇️ Download CSV", csv, f"{page.replace(' ','_')}_{ts}.csv", "text/csv")
        st.download_button("⬇️ Download JSON", json, f"{page.replace(' ','_')}_{ts}.json", "application/json")
        st.download_button(
            "⬇️ Download Excel",
            excel_buffer,
            f"{page.replace(' ','_')}_{ts}.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("Not enough numeric columns for visualization.")
else:
    st.warning("No data available. Please upload or generate synthetic data.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center>© 2025 KNet Consulting Group | Powered by Streamlit</center>",
    unsafe_allow_html=True
)
