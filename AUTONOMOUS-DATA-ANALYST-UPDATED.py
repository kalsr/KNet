###KKK

# Autonomous Data Analyst (Agentic AI)
# THIS CODE IS DEVELOPED BY RANDY SINGH FROM KNet CONSULTING GROUP.

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import io
import json
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from scipy import stats
import matplotlib.pyplot as plt

# --- Utility functions (agents) ---

def generate_sample(n=100, seed=42):
    np.random.seed(seed)
    start_date = datetime.now() - timedelta(days=365)
    data = {
        "id": list(range(1, n+1)),
        "timestamp": [(start_date + timedelta(days=int(x))).isoformat() for x in np.random.randint(0, 365, size=n)],
        "customer_age": np.random.randint(18, 80, size=n),
        "income": np.round(np.random.normal(70000, 20000, size=n), 2),
        "purchases_last_30d": np.random.poisson(2, size=n),
        "avg_order_value": np.round(np.abs(np.random.normal(120, 60, size=n)), 2),
        "country": np.random.choice(["US", "UK", "DE", "IN", "CA"], size=n, p=[0.5,0.15,0.1,0.15,0.1]),
        "product_category": np.random.choice(["Electronics","Clothing","Home","Sports","Books"], size=n),
        "is_subscriber": np.random.choice([0,1], size=n, p=[0.6,0.4]),
    }
    df = pd.DataFrame(data)
    df["churn_risk_score"] = np.clip(np.round(0.5 + (60 - df["customer_age"])/120 + (np.random.randn(n)*0.1) - df["is_subscriber"]*0.2, 3), 0, 1)
    df["will_churn"] = (df["churn_risk_score"] > 0.55).astype(int)
    df["revenue_30d"] = (df["purchases_last_30d"] * df["avg_order_value"]).round(2)
    return df

def data_ingestor(uploaded_file):
    if uploaded_file is None:
        return None, "no_file"
    name = uploaded_file.name.lower()
    try:
        if name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif name.endswith(".json"):
            df = pd.read_json(uploaded_file)
        else:
            st.error("Unsupported file type. Upload .csv or .json.")
            return None, "error"
        return df, "ok"
    except Exception as e:
        return None, f"error: {e}"

def data_cleaner(df, report):
    df = df.copy()
    original_shape = df.shape
    df.columns = [c.strip().replace(" ", "_") for c in df.columns]
    for c in df.columns:
        if "time" in c or "date" in c:
            try:
                df[c] = pd.to_datetime(df[c])
            except:
                pass
    num_cols = df.select_dtypes(include=[np.number]).columns
    for c in num_cols:
        if df[c].isna().any():
            med = df[c].median()
            df[c] = df[c].fillna(med)
            report["cleaning"].append(f"Filled missing numeric {c} with median {med}")
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        df = df.drop_duplicates()
        report["cleaning"].append(f"Dropped {dup_count} duplicate rows")
    report["cleaning"].append(f"Original shape {original_shape} -> cleaned shape {df.shape}")
    return df

def summary_agent(df, report):
    summary = {}
    summary["n_rows"] = int(df.shape[0])
    summary["n_columns"] = int(df.shape[1])
    numeric = df.select_dtypes(include=[np.number])
    summary["numeric_summary"] = numeric.describe().to_dict()
    cats = {}
    for c in df.select_dtypes(include=['object', 'category']).columns:
        cats[c] = df[c].value_counts().head(5).to_dict()
    summary["top_categories"] = cats
    report["summary"].append(f"Dataset rows: {summary['n_rows']}, cols: {summary['n_columns']}")
    return summary

def anomaly_detector(df, report, z_thresh=3.0):
    numeric = df.select_dtypes(include=[np.number])
    anomalies = {}
    z = np.abs(stats.zscore(numeric, nan_policy='omit'))
    if z.size == 0:
        report["anomalies"].append("No numeric columns for anomaly detection.")
        return anomalies
    z = np.nan_to_num(z)
    rows_with_anom = (z > z_thresh).any(axis=1)
    anomaly_indices = df.index[rows_with_anom].tolist()
    anomalies["count"] = int(rows_with_anom.sum())
    anomalies["indices"] = anomaly_indices
    if anomalies["count"] > 0:
        report["anomalies"].append(f"Detected {anomalies['count']} anomalous rows using z>{z_thresh}.")
    else:
        report["anomalies"].append("No anomalies detected by z-score.")
    return anomalies

def segmentation_agent(df, report, n_clusters=3):
    numeric = df.select_dtypes(include=[np.number]).fillna(0)
    if numeric.shape[1] == 0:
        report["segmentation"].append("No numeric columns to perform clustering.")
        return df, None
    scaler = StandardScaler()
    X = scaler.fit_transform(numeric)
    k = min(n_clusters, max(1, X.shape[0] // 5))
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X)
    df2 = df.copy().reset_index(drop=True)
    df2["segment"] = labels
    report["segmentation"].append(f"Assigned {k} segments via KMeans.")
    return df2, {"k": k, "inertia": float(km.inertia_)}

def modeling_agent(df, report, target_column=None):
    numeric = df.select_dtypes(include=[np.number]).copy()
    if target_column is None:
        for candidate in ["will_churn", "target", "revenue_30d"]:
            if candidate in numeric.columns:
                target_column = candidate
                break
    if target_column is None or target_column not in numeric.columns:
        report["modeling"].append("No numeric target found; skipping predictive modeling.")
        return None
    y = numeric[target_column]
    X = numeric.drop(columns=[target_column])
    if X.shape[1] == 0 or len(X) < 10:
        report["modeling"].append("Not enough numeric features/rows for modeling.")
        return None
    corrs = X.corrwith(y).abs().sort_values(ascending=False)
    top_feat = corrs.index[0]
    model = LinearRegression()
    model.fit(X[[top_feat]], y)
    score = model.score(X[[top_feat]], y)
    report["modeling"].append(f"Trained LinearRegression to predict {target_column} using {top_feat} (R^2 = {score:.3f}).")
    return {"target": target_column, "feature": top_feat, "r2": float(score)}

# --- Streamlit UI ---

st.set_page_config(page_title="Agentic-AI Demo — Autonomous Data Analyst", layout="wide")

# CSS styles
st.markdown("""
<style>
.stButton > button {
    background: linear-gradient(90deg,#2ECC71,#27AE60);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    font-weight: bold;
    cursor: pointer;
}
.stButton > button:hover {
    opacity: 0.9;
}
.reset-button > button {
    background: linear-gradient(90deg,#E74C3C,#C0392B) !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Autonomous Data Analyst Designed & Developed By Randy Singh.")
st.write("An Orchestrator which Coordinates Small Specialized Agentic-AI Agents (Ingestor, Cleaner, Summarizer, Anomaly Detector, Segmenter, Modeler, Reporter).")

# Top controls
col1, col2, col3 = st.columns([2,1,1])

with col1:
    st.info("Status: Idle")

with col2:
    sample_size = st.number_input("Number of Sample Records", min_value=10, max_value=100, value=100, step=10)
    if st.button("Generate Sample Records"):
        df_generated = generate_sample(sample_size)
        st.session_state["df"] = df_generated
        st.success(f"Generated {sample_size} sample records (stored in-memory).")

with col3:
    uploaded = st.file_uploader("Upload CSV or JSON", type=["csv","json"])

# Initialize state
if "df" not in st.session_state:
    st.session_state["df"] = None
if "report" not in st.session_state:
    st.session_state["report"] = {"cleaning": [], "summary": [], "anomalies": [], "segmentation": [], "modeling": [], "notes": []}

if uploaded is not None:
    df_ing, status = data_ingestor(uploaded)
    if df_ing is not None:
        st.session_state["df"] = df_ing
        st.success(f"Loaded dataset shape: {st.session_state['df'].shape}")
    else:
        st.error(f"Load failed: {status}")

if st.session_state["df"] is None:
    st.info("No dataset loaded. Use 'Generate' or upload a CSV/JSON.")
    st.stop()

df = st.session_state["df"]
st.subheader("Preview")
st.dataframe(df.head(20))

# Pipeline controls
st.markdown("### Run pipeline")
colA, colB, colC, colD = st.columns(4)

with colA:
    clean_btn = st.button("Run Cleaning", key="clean")

with colB:
    analyze_btn = st.button("Run Full Analysis", key="analyze")

with colC:
    export_btn = st.button("Download Data/Report", key="export")

with colD:
    reset_btn = st.button("Reset / Clear Data", key="reset", type="primary")

# Reset
if reset_btn:
    st.session_state["df"] = None
    st.session_state["report"] = {"cleaning": [], "summary": [], "anomalies": [], "segmentation": [], "modeling": [], "notes": []}
    if "last_report" in st.session_state:
        del st.session_state["last_report"]
    st.warning("Session cleared. Load new data or generate sample records to continue.")
    st.stop()

report = st.session_state["report"]

# Run cleaning
if clean_btn:
    df = data_cleaner(df, report)
    st.session_state["df"] = df
    st.success("Cleaning complete.")
    st.write("Cleaning notes:")
    for item in report["cleaning"][-5:]:
        st.write("-", item)

# Full analysis
if analyze_btn:
    df = data_cleaner(df, report)
    summary = summary_agent(df, report)
    anomalies = anomaly_detector(df, report)
    df_segmented, seg_info = segmentation_agent(df, report, n_clusters=4)
    if df_segmented is not None:
        df = df_segmented
        st.session_state["df"] = df
    model_info = modeling_agent(df, report)
    final_report = {
        "when": datetime.utcnow().isoformat() + "Z",
        "summary": summary,
        "anomalies": anomalies,
        "segmentation_info": seg_info,
        "model_info": model_info,
        "notes": report
    }
    st.session_state["last_report"] = final_report
    st.success("Full analysis complete — results stored in session.")
    st.subheader("Top Findings")
    st.write("Rows:", summary["n_rows"], "Columns:", summary["n_columns"])
    st.write("Anomalies detected:", anomalies.get("count", 0))
    if model_info:
        st.write(f"Model: predict {model_info['target']} using {model_info['feature']} (R^2={model_info['r2']:.3f})")

    # --- Visualization Section ---
    st.markdown("### Visual Insights")

    # Pie chart: distribution by country
    fig1, ax1 = plt.subplots()
    df["country"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax1)
    ax1.set_ylabel("")
    ax1.set_title("Customer Distribution by Country")
    st.pyplot(fig1)

    # Bar chart: revenue per product category
    fig2, ax2 = plt.subplots()
    df.groupby("product_category")["revenue_30d"].mean().plot(kind="bar", ax=ax2)
    ax2.set_title("Avg Revenue by Product Category")
    ax2.set_ylabel("Revenue (30d)")
    st.pyplot(fig2)

    # Line chart: revenue trend over time
    if "timestamp" in df.columns:
        df_time = df.copy()
        df_time["timestamp"] = pd.to_datetime(df_time["timestamp"])
        rev_trend = df_time.groupby(df_time["timestamp"].dt.to_period("M"))["revenue_30d"].sum()
        fig3, ax3 = plt.subplots()
        rev_trend.plot(ax=ax3, marker="o")
        ax3.set_title("Revenue Trend Over Time")
        ax3.set_ylabel("Revenue (30d)")
        st.pyplot(fig3)

# Export
if export_btn or ("last_report" in st.session_state):
    df_export = st.session_state["df"]
    report_export = st.session_state.get("last_report", {
        "when": datetime.utcnow().isoformat()+"Z",
        "summary": {},
        "anomalies": {},
        "segmentation_info": {},
        "model_info": None,
        "notes": st.session_state.get("report", {})
    })
    csv_buffer = io.StringIO()
    df_export.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode()
    json_bytes = json.dumps(json.loads(df_export.to_json(orient="records")), indent=2).encode()
    report_bytes = json.dumps(report_export, indent=2).encode()
    st.download_button("Download Processed CSV", data=csv_bytes, file_name="processed_data.csv", mime="text/csv")
    st.download_button("Download Processed JSON", data=json_bytes, file_name="processed_data.json", mime="application/json")
    st.download_button("Download Analysis Report (JSON)", data=report_bytes, file_name="analysis_report.json", mime="application/json")

# Show notes
st.markdown("### Pipeline Notes")
for k, v in st.session_state["report"].items():
    st.write(f"**{k}**")
    if isinstance(v, list):
        for item in v[-5:]:
            st.write("-", item)
    else:
        st.write(v)



