

# agentic_ai_dashboard.py
# Agentic AI Dashboard - Single-file app
# Developed by Randy Singh, KNet Consulting Group

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Agentic AI Dashboard - KNet Consulting",
                   page_icon="🤖", layout="wide")

# ---------------- UTILS ----------------
def keyify(name: str) -> str:
    return name.replace(" ", "_")

def parse_uploaded_bytes(bytes_io: bytes, filename: str) -> pd.DataFrame:
    """Return DataFrame from uploaded bytes based on extension."""
    ext = filename.split(".")[-1].lower()
    bio = BytesIO(bytes_io)
    if ext == "csv":
        return pd.read_csv(bio)
    elif ext in ("xls", "xlsx"):
        return pd.read_excel(bio)
    elif ext == "json":
        # pd.read_json can parse a file-like object
        try:
            return pd.read_json(bio)
        except ValueError:
            # fallback: load as records
            bio.seek(0)
            return pd.DataFrame(pd.read_json(bio, orient="records"))
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
    df = pd.DataFrame({
        "ID": range(1, n + 1),
        cols[0]: np.random.uniform(40, 100, n).round(2),
        cols[1]: np.random.uniform(40, 100, n).round(2),
        cols[2]: np.random.uniform(40, 100, n).round(2),
    })
    return df

# ---------------- APP DATA ----------------
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

# Keys used in session_state:
# - 'selected_case' -> string
# - 'uploaded_bytes_{case_key}', 'uploaded_name_{case_key}'
# - 'data_{case_key}' -> DataFrame (either uploaded or generated)
# - 'gen_n_{case_key}' -> integer for slider (1..100)

if 'selected_case' not in st.session_state:
    st.session_state['selected_case'] = None

# Read query param if user clicked HTML link button (anchors)
qp = st.experimental_get_query_params()
if 'case' in qp:
    chosen = qp.get('case')[0]
    # restore spaces
    chosen = chosen.replace("_", " ")
    if chosen in use_cases:
        st.session_state['selected_case'] = chosen

selected_case = st.session_state['selected_case']

# ---------------- LAYOUT ----------------
left_col, main_col = st.columns([1, 4])

# ----- LEFT: vertical colored buttons + controls -----
with left_col:
    st.markdown("<div style='padding:8px 6px'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:6px 0'>📂 Use Cases</h3>", unsafe_allow_html=True)

    # Render colored rectangular "buttons" as anchor links that set ?case=...
    for case, color in use_cases.items():
        case_q = keyify(case)
        btn_html = f"""
        <a href='?case={case_q}' style='text-decoration:none'>
            <div style='background:{color};padding:10px;border-radius:8px;margin:6px 0;color:white;font-weight:600;
                        text-align:center;box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
                {case}
            </div>
        </a>
        """
        st.markdown(btn_html, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='margin:6px 0'>⚙️ Actions</h4>", unsafe_allow_html=True)

    # Refresh & Reset operate on currently selected case
    if st.button("🔄 Refresh (selected use case)"):
        if selected_case:
            case_key = keyify(selected_case)
            # If uploaded bytes exist, reparse them; else regenerate synthetic from saved slider
            uploaded_key = f"uploaded_bytes_{case_key}"
            uploaded_name_key = f"uploaded_name_{case_key}"
            gen_key = f"gen_n_{case_key}"
            data_key = f"data_{case_key}"
            try:
                if uploaded_key in st.session_state and st.session_state.get(uploaded_key):
                    # reparse uploaded bytes
                    df = parse_uploaded_bytes(st.session_state[uploaded_key], st.session_state[uploaded_name_key])
                    st.session_state[data_key] = df
                    st.success("Refreshed: reloaded uploaded dataset for this use case.")
                else:
                    nval = st.session_state.get(gen_key, 50)
                    st.session_state[data_key] = make_synthetic_df(selected_case, nval)
                    st.success("Refreshed: regenerated synthetic data for this use case.")
            except Exception as e:
                st.error(f"Refresh failed: {e}")
        else:
            st.warning("Select a use case first (click a colored button).")

    if st.button("🧹 Reset (selected use case)"):
        if selected_case:
            case_key = keyify(selected_case)
            for k in [f"uploaded_bytes_{case_key}", f"uploaded_name_{case_key}",
                      f"data_{case_key}", f"gen_n_{case_key}"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.success(f"Reset: cleared data for '{selected_case}'.")
            # remove query param to go back to no selection
            st.experimental_set_query_params()
            st.session_state['selected_case'] = None
            st.experimental_rerun()
        else:
            st.warning("Select a use case first (click a colored button).")

    st.markdown("---")
    st.markdown("<small>© 2025 KNet Consulting Group</small>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ----- MAIN: selected case content -----
with main_col:
    st.title("🤖 Agentic AI Dashboard")
    st.write("Select an Agentic use case from the left. For each use case you can upload your own dataset or generate synthetic data; visualize and download results.")

    if not selected_case:
        st.info("Click any colored use-case button on the left to open its page.")
    else:
        st.markdown(f"## 🧠 {selected_case}")

        case_key = keyify(selected_case)
        data_key = f"data_{case_key}"
        uploaded_key = f"uploaded_bytes_{case_key}"
        uploaded_name_key = f"uploaded_name_{case_key}"
        gen_key = f"gen_n_{case_key}"

        # Upload area (per-use-case)
        st.markdown("### 📤 Upload dataset (CSV / XLSX / JSON)")
        uploaded_file = st.file_uploader(f"Upload for: {selected_case}", type=["csv", "xlsx", "json"], key=f"uploader_{case_key}")

        if uploaded_file is not None:
            # read bytes and persist to session_state so Refresh will work later
            try:
                bytes_data = uploaded_file.read()
                st.session_state[uploaded_key] = bytes_data
                st.session_state[uploaded_name_key] = uploaded_file.name
                df = parse_uploaded_bytes(bytes_data, uploaded_file.name)
                st.session_state[data_key] = df
                st.success("Uploaded and loaded dataset for this use case.")
            except Exception as e:
                st.error(f"Failed to parse upload: {e}")

        # Synthetic data slider
        st.markdown("### 📈 Synthetic Data Generator")
        # store slider value in session state key per-case
        default_n = st.session_state.get(gen_key, 50)
        n = st.slider("Generate synthetic data points", 0, 100, default_n, key=f"slider_{case_key}")
        st.session_state[gen_key] = n

        # Buttons to explicitly choose between uploaded or generated data
        use_uploaded = False
        if uploaded_key in st.session_state and st.session_state.get(uploaded_key):
            use_uploaded = st.checkbox("Use uploaded dataset (check to prefer uploaded file)", value=True)
        else:
            use_uploaded = False

        # If user wants generated data OR no uploaded exists -> generate
        if not use_uploaded:
            # If slider is 0 -> no data
            if n > 0:
                df_gen = make_synthetic_df(selected_case, n)
                st.session_state[data_key] = df_gen
            else:
                # zero rows
                st.session_state[data_key] = pd.DataFrame()

        # Preview data
        if data_key in st.session_state and st.session_state[data_key] is not None:
            df_show = st.session_state[data_key]
            st.subheader("📋 Data Preview")
            st.dataframe(df_show, use_container_width=True)

            # Visualizations - ensure there are numeric columns
            numeric_data = df_show.select_dtypes(include=[np.number]).drop(columns="ID", errors="ignore")
            if numeric_data.shape[1] >= 1 and numeric_data.shape[0] > 0:
                st.subheader("📊 Visualizations")
                mean_vals = numeric_data.mean()

                c1, c2, c3 = st.columns(3)
                # Bar
                with c1:
                    fig, ax = plt.subplots()
                    labels = mean_vals.index.tolist()
                    vals = mean_vals.values
                    # ensure there are 3 colors at least
                    colors = ["#2196F3", "#FF9800", "#4CAF50", "#9C27B0", "#607D8B"]
                    ax.bar(labels, vals, color=colors[:len(labels)])
                    ax.set_title("Average Metrics")
                    plt.xticks(rotation=15)
                    st.pyplot(fig)

                # Pie
                with c2:
                    fig2, ax2 = plt.subplots()
                    ax2.pie(vals, labels=labels, autopct="%1.1f%%", startangle=90)
                    ax2.set_title("Metric Distribution (%)")
                    st.pyplot(fig2)

                # Line
                with c3:
                    fig3, ax3 = plt.subplots()
                    # if index meaningful use ID else numeric index
                    x_axis = df_show["ID"] if "ID" in df_show.columns else range(1, len(df_show) + 1)
                    for col in numeric_data.columns:
                        ax3.plot(x_axis, numeric_data[col], label=col)
                    ax3.legend(loc="best")
                    ax3.set_title("Trend Over Data Points")
                    st.pyplot(fig3)

                # Simple textual summary
                st.markdown("**Quick summary:**")
                best_metric = mean_vals.idxmax()
                worst_metric = mean_vals.idxmin()
                st.write(f"- Average score across metrics: {mean_vals.mean():.2f}")
                st.write(f"- Best metric (highest mean): **{best_metric}** ({mean_vals[best_metric]:.2f})")
                st.write(f"- Lowest metric (lowest mean): **{worst_metric}** ({mean_vals[worst_metric]:.2f})")

                # Downloads
                st.subheader("📥 Download Results")
                ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                csv_bytes = df_show.to_csv(index=False).encode("utf-8")
                json_bytes = df_show.to_json(orient="records", indent=2).encode("utf-8")
                excel_buf = BytesIO()
                df_show.to_excel(excel_buf, index=False)
                excel_buf.seek(0)

                st.download_button("⬇️ Download CSV", csv_bytes, f"{case_key}_{ts}.csv", "text/csv")
                st.download_button("⬇️ Download JSON", json_bytes, f"{case_key}_{ts}.json", "application/json")
                st.download_button("⬇️ Download Excel", excel_buf, f"{case_key}_{ts}.xlsx",
                                   "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            else:
                st.warning("Not enough numeric data for visualization. Upload or generate >=1 numeric column.")
        else:
            st.info("No data available yet. Upload a file or set slider > 0 to generate synthetic data.")

# ---------------- END ----------------
