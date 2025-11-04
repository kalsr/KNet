

# Agentic_AI_Dashboard_V3.py
# Fixed version – all use-case buttons work, only selected use case visible, Reset & Refresh stable
# THIS APPLICATION IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Agentic AI Dashboard - Designed by Randy Singh From KNet Consulting",
                   page_icon="", layout="wide")

# ---------------- UTILITIES ----------------
def keyify(name: str) -> str:
    return name.replace(" ", "_")

def parse_uploaded_bytes(bytes_io: bytes, filename: str) -> pd.DataFrame:
    ext = filename.split(".")[-1].lower()
    bio = BytesIO(bytes_io)
    if ext == "csv":
        return pd.read_csv(bio)
    elif ext in ("xls", "xlsx"):
        return pd.read_excel(bio)
    elif ext == "json":
        return pd.read_json(bio)
    else:
        raise ValueError("Unsupported file type")

def make_synthetic_df(case_name: str, n: int) -> pd.DataFrame:
    metrics_map = {
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
    cols = metrics_map.get(case_name, ["Metric_A", "Metric_B", "Metric_C"])
    np.random.seed(42)
    return pd.DataFrame({
        "ID": range(1, n + 1),
        cols[0]: np.random.uniform(40, 100, n).round(2),
        cols[1]: np.random.uniform(40, 100, n).round(2),
        cols[2]: np.random.uniform(40, 100, n).round(2),
    })

# ---------------- STATE INIT ----------------
if "selected_case" not in st.session_state:
    st.session_state["selected_case"] = None

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

# ---------------- LAYOUT ----------------
if st.session_state["selected_case"] is None:
    # ---- MAIN MENU (all use-case buttons visible) ----
    st.title(" Agentic AI Dashboard")
    st.write("Select a use case below to explore synthetic data, upload datasets, visualize, and download results.")
    for case, color in use_cases.items():
        if st.button(case, use_container_width=True, type="primary", key=f"btn_{keyify(case)}"):
            st.session_state["selected_case"] = case
            st.rerun()
else:
    # ---- USE CASE PAGE ----
    selected_case = st.session_state["selected_case"]
    case_key = keyify(selected_case)
    data_key = f"data_{case_key}"
    uploaded_key = f"uploaded_bytes_{case_key}"
    uploaded_name_key = f"uploaded_name_{case_key}"
    gen_key = f"gen_n_{case_key}"

    # Header
    st.markdown(f"<h2 style='color:#2196F3;'> {selected_case}</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Back button
    if st.button(" Back to Main Menu"):
        st.session_state["selected_case"] = None
        st.rerun()

    # Upload section
    st.subheader(" Upload Dataset (CSV / Excel / JSON)")
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "json"], key=f"upload_{case_key}")

    if uploaded_file is not None:
        try:
            bytes_data = uploaded_file.read()
            st.session_state[uploaded_key] = bytes_data
            st.session_state[uploaded_name_key] = uploaded_file.name
            df = parse_uploaded_bytes(bytes_data, uploaded_file.name)
            st.session_state[data_key] = df
            st.success(" Dataset uploaded successfully!")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    # Synthetic data slider
    st.subheader(" Synthetic Data Generator")
    n = st.slider("Generate data points", 0, 100, st.session_state.get(gen_key, 50), key=f"slider_{case_key}")
    st.session_state[gen_key] = n

    # Buttons: Refresh, Reset
    col1, col2 = st.columns(2)
    with col1:
        if st.button(" Refresh Data"):
            if uploaded_key in st.session_state and st.session_state[uploaded_key]:
                df = parse_uploaded_bytes(st.session_state[uploaded_key], st.session_state[uploaded_name_key])
                st.session_state[data_key] = df
                st.success(" Data refreshed from uploaded file.")
            else:
                df = make_synthetic_df(selected_case, n)
                st.session_state[data_key] = df
                st.success(" Synthetic data regenerated.")

    with col2:
        if st.button(" Reset Use Case"):
            # Safely clear all keys related to this case
            for k in [uploaded_key, uploaded_name_key, data_key, gen_key]:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state["selected_case"] = None
            st.success(" Use case reset successfully.")
            st.rerun()

    # Generate synthetic data if no upload
    if uploaded_key not in st.session_state or not st.session_state.get(uploaded_key):
        if n > 0:
            st.session_state[data_key] = make_synthetic_df(selected_case, n)
        else:
            st.session_state[data_key] = pd.DataFrame()

    # Display data if exists
    if data_key in st.session_state and not st.session_state[data_key].empty:
        df = st.session_state[data_key]
        st.subheader(" Data Preview")
        st.dataframe(df, use_container_width=True)

        # Visualizations
        st.subheader(" Visualizations")
        numeric_data = df.select_dtypes(include=[np.number]).drop(columns="ID", errors="ignore")
        mean_vals = numeric_data.mean()

        c1, c2, c3 = st.columns(3)

        # Bar Chart
        with c1:
            fig, ax = plt.subplots()
            ax.bar(mean_vals.index, mean_vals.values)
            ax.set_title("Average Metrics")
            plt.xticks(rotation=15)
            st.pyplot(fig)

        # Pie Chart
        with c2:
            fig2, ax2 = plt.subplots()
            ax2.pie(mean_vals.values, labels=mean_vals.index, autopct="%1.1f%%", startangle=90)
            ax2.set_title("Metric Distribution")
            st.pyplot(fig2)

        # Line Chart
        with c3:
            fig3, ax3 = plt.subplots()
            x = df["ID"] if "ID" in df.columns else range(1, len(df) + 1)
            for col in numeric_data.columns:
                ax3.plot(x, numeric_data[col], label=col)
            ax3.legend()
            ax3.set_title("Trend Over Data Points")
            st.pyplot(fig3)

        # Summary
        st.markdown("**Quick Insights:**")
        st.write(f"- Best Metric: **{mean_vals.idxmax()}** ({mean_vals.max():.2f})")
        st.write(f"- Weakest Metric: **{mean_vals.idxmin()}** ({mean_vals.min():.2f})")
        st.write(f"- Overall Avg: {mean_vals.mean():.2f}")

        # Download section
        st.subheader(" Download Results")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        json_bytes = df.to_json(orient="records", indent=2).encode("utf-8")
        excel_buf = BytesIO()
        df.to_excel(excel_buf, index=False)
        excel_buf.seek(0)

        st.download_button(" Download CSV", csv_bytes, f"{case_key}_{ts}.csv", "text/csv")
        st.download_button(" Download JSON", json_bytes, f"{case_key}_{ts}.json", "application/json")
        st.download_button(" Download Excel", excel_buf, f"{case_key}_{ts}.xlsx",
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.info("No data yet. Upload a file or use the slider to generate synthetic data.")

# ---------------- END ----------------

