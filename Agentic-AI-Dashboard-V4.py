

# Agentic_AI_Dashboard_V4.py
# Developed by Randy Singh | KNet Consulting Group
# Professional, single-file Streamlit app for Agentic AI Use Cases

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
    # ---- MAIN MENU ----
    st.title("🤖 Agentic AI Dashboard")
    st.write("Select an Agentic AI Use Case to explore synthetic or uploaded datasets, visualize metrics, and export results.")

    for case, color in use_cases.items():
        if st.button(case, use_container_width=True, type="primary", key=f"btn_{keyify(case)}"):
            st.session_state["selected_case"] = case
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<center>© 2025 KNet Consulting Group | Powered by Streamlit</center>", unsafe_allow_html=True)

else:
    # ---- USE CASE PAGE ----
    selected_case = st.session_state["selected_case"]
    case_key = keyify(selected_case)
    color = use_cases.get(selected_case, "#2196F3")

    # --- HEADER BANNER ---
    st.markdown(
        f"""
        <div style='background:{color};padding:15px;border-radius:10px;margin-bottom:20px;'>
            <h2 style='color:white;margin:0;text-align:center;'>🧠 {selected_case}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- ACTION BUTTONS ---
    top_col1, top_col2 = st.columns([1, 1])
    with top_col1:
        if st.button("⬅️ Back to Main Menu"):
            st.session_state["selected_case"] = None
            st.rerun()
    with top_col2:
        if st.button("🧹 Reset Use Case"):
            for k in list(st.session_state.keys()):
                if case_key in k:
                    del st.session_state[k]
            st.session_state["selected_case"] = None
            st.success("✅ Use case reset successfully.")
            st.rerun()

    # --- UPLOAD SECTION ---
    st.subheader("📤 Upload Your Own Dataset")
    uploaded_file = st.file_uploader(
        "Upload CSV, Excel, or JSON file",
        type=["csv", "xlsx", "json"],
        key=f"upload_{case_key}"
    )

    data_key = f"data_{case_key}"
    uploaded_bytes_key = f"upload_bytes_{case_key}"
    uploaded_name_key = f"upload_name_{case_key}"

    if uploaded_file is not None:
        try:
            bytes_data = uploaded_file.read()
            st.session_state[uploaded_bytes_key] = bytes_data
            st.session_state[uploaded_name_key] = uploaded_file.name
            df = parse_uploaded_bytes(bytes_data, uploaded_file.name)
            st.session_state[data_key] = df
            st.success("✅ File uploaded and processed successfully!")
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")

    # --- SYNTHETIC DATA GENERATOR ---
    st.subheader("📈 Synthetic Data Generator")
    n = st.slider("Number of synthetic data points", 0, 100, 50, key=f"slider_{case_key}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Refresh Data"):
            if uploaded_bytes_key in st.session_state and st.session_state[uploaded_bytes_key]:
                df = parse_uploaded_bytes(st.session_state[uploaded_bytes_key], st.session_state[uploaded_name_key])
                st.session_state[data_key] = df
                st.success("✅ Data refreshed from uploaded file.")
            else:
                df = make_synthetic_df(selected_case, n)
                st.session_state[data_key] = df
                st.success("✅ Synthetic data regenerated.")
    with col2:
        if st.button("🧪 Generate Synthetic Data"):
            df = make_synthetic_df(selected_case, n)
            st.session_state[data_key] = df
            st.success("✅ Synthetic data created!")

    # --- DATA PREVIEW & VISUALIZATION ---
    if data_key in st.session_state and not st.session_state[data_key].empty:
        df = st.session_state[data_key]
        st.subheader("📋 Data Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Visualizations")
        numeric_data = df.select_dtypes(include=[np.number]).drop(columns="ID", errors="ignore")
        mean_vals = numeric_data.mean()

        c1, c2, c3 = st.columns(3)
        # Bar Chart
        with c1:
            fig, ax = plt.subplots()
            ax.bar(mean_vals.index, mean_vals.values, color=color)
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

        # Insights
        st.markdown("**Quick Insights:**")
        st.write(f"- 🥇 Best Metric: **{mean_vals.idxmax()}** ({mean_vals.max():.2f})")
        st.write(f"- ⚠️ Weakest Metric: **{mean_vals.idxmin()}** ({mean_vals.min():.2f})")
        st.write(f"- 📊 Overall Average: {mean_vals.mean():.2f}")

        # Downloads
        st.subheader("💾 Download Results")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        json_bytes = df.to_json(orient="records", indent=2).encode("utf-8")
        excel_buf = BytesIO()
        df.to_excel(excel_buf, index=False)
        excel_buf.seek(0)

        st.download_button("⬇️ Download CSV", csv_bytes, f"{case_key}_{ts}.csv", "text/csv")
        st.download_button("⬇️ Download JSON", json_bytes, f"{case_key}_{ts}.json", "application/json")
        st.download_button("⬇️ Download Excel", excel_buf, f"{case_key}_{ts}.xlsx",
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    else:
        st.info("📂 No data yet — upload a file or generate synthetic data above.")

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<center>© 2025 KNet Consulting Group | Developed by Randy Singh</center>", unsafe_allow_html=True)
