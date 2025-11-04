

# agentic_ai_dashboard.py
# ------------------------------------------------------------
# Agentic AI Dashboard by Randy Singh, KNet Consulting Group
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Agentic AI Use Cases - KNet Consulting",
    page_icon="🤖",
    layout="wide",
)

# ---------------- STYLES ----------------
st.markdown("""
    <style>
        /* Align content to left with padding */
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
            font-size: 17px;
            margin-bottom: 20px;
        }
        .menu-btn {
            display: block;
            width: 100%;
            padding: 16px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            color: white;
            margin: 8px 0;
            cursor: pointer;
            text-align: center;
            transition: 0.3s;
        }
        .menu-btn:hover {
            filter: brightness(1.15);
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.sidebar.markdown(
    '<div class="main-title">🤖 Agentic AI Dashboard</div>'
    '<div class="sub-title">KNet Consulting Group</div>',
    unsafe_allow_html=True,
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

page = st.sidebar.selectbox("📂 Select Use Case", ["🏠 Main Menu"] + list(use_cases.keys()))

# ---------------- MAIN MENU ----------------
if page == "🏠 Main Menu":
    st.markdown("### 📋 Choose an Agentic AI Use Case Below:")

    for case, color in use_cases.items():
        html_button = f"""
        <a href='?page={case.replace(" ", "_")}' target='_self'>
        <button class="menu-btn" style="background-color:{color};">{case}</button></a>
        """
        st.markdown(html_button, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<center>© 2025 KNet Consulting Group | Powered by Streamlit</center>", unsafe_allow_html=True)

else:
    # ---------------- INDIVIDUAL USE CASE ----------------
    st.markdown(f"## 🧠 {page}")
    st.write("Use the slider below to generate synthetic data points for this use case:")

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

    st.dataframe(data, use_container_width=True)

    # ---------------- VISUALIZATION ----------------
    st.subheader("📊 Visualization")

    numeric_data = data.select_dtypes(include=[np.number]).drop(columns="ID", errors="ignore")
    mean_values = numeric_data.mean()

    col1, col2, col3 = st.columns(3)

    # Bar Chart
    with col1:
        fig, ax = plt.subplots()
        ax.bar(mean_values.index, mean_values.values, color=["#2196F3", "#FF9800", "#4CAF50"])
        ax.set_title("Average Metrics")
        plt.xticks(rotation=20)
        st.pyplot(fig)

    # Pie Chart
    with col2:
        fig2, ax2 = plt.subplots()
        ax2.pie(mean_values, labels=mean_values.index, autopct="%1.1f%%", startangle=90)
        ax2.set_title("Metric Distribution (%)")
        st.pyplot(fig2)

    # Line Chart
    with col3:
        fig3, ax3 = plt.subplots()
        for col in numeric_data.columns:
            ax3.plot(data["ID"], data[col], label=col)
        ax3.legend()
        ax3.set_title("Trend Over Data Points")
        st.pyplot(fig3)

    # ---------------- DOWNLOAD DATA ----------------
    st.subheader("📥 Download Data")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_data = data.to_csv(index=False).encode("utf-8")
    json_data = data.to_json(orient="records", indent=2).encode("utf-8")
    excel_buffer = BytesIO()
    data.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)

    st.download_button("⬇️ Download CSV", csv_data, f"{page.replace(' ','_')}_{ts}.csv", "text/csv")
    st.download_button("⬇️ Download JSON", json_data, f"{page.replace(' ','_')}_{ts}.json", "application/json")
    st.download_button(
        "⬇️ Download Excel",
        excel_buffer,
        f"{page.replace(' ','_')}_{ts}.xlsx",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # ---------------- FOOTER ----------------
    st.markdown("---")
    st.markdown(
        "<center><a href='?page=🏠_Main_Menu'><button style='padding:8px 18px;"
        "border:none;border-radius:6px;background-color:#0a2540;color:white;'>⬅️ Back to Main Menu</button></a></center>",
        unsafe_allow_html=True,
    )
    st.markdown("<br><center>© 2025 KNet Consulting Group | Powered by Streamlit</center>", unsafe_allow_html=True)
