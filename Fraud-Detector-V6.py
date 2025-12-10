

# Fraud-Detector-V6
# app.py — Full-featured Fraud/Scam Detector with dynamic ML & LLM
# Run with: streamlit run app.py

import os
import io
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

from fpdf import FPDF
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay,
                             roc_curve, auc, precision_recall_fscore_support)
from sklearn.model_selection import train_test_split

# Optional LLM imports
try:
    import openai
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except Exception:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    CLAUDE_AVAILABLE = True
except Exception:
    CLAUDE_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except Exception:
    GEMINI_AVAILABLE = False

try:
    from gpt4all import GPT4All
    GPT4ALL_AVAILABLE = True
except Exception:
    GPT4ALL_AVAILABLE = False

# ---------------- page config ----------------
st.set_page_config(
    page_title="Fraud / Scam Detector — Unified ML & LLM",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- custom CSS ----------------
st.markdown("""
<style>
.big-title {
    font-size: 38px !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    background: linear-gradient(90deg,#0a63c7,#1ea3ff);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 6px;
}
.subtitle {
    font-size: 18px !important;
    font-weight: 500 !important;
    color: #dbeeff;
    text-align: center;
    margin-bottom: 14px;
}
.top-bar {
    display:flex;
    justify-content:center;
    gap:10px;
    margin-bottom:18px;
}
.top-btn {
    padding:10px 18px;
    border-radius:10px;
    font-weight:800;
    font-size:15px;
    color:white !important;
    text-decoration:none;
    border: 2px solid rgba(0,0,0,0.15);
}
.top-btn.gen { background: linear-gradient(90deg,#28e07a,#0cc96b); }
.top-btn.upload { background: linear-gradient(90deg,#33b3ff,#1976d2); }
.top-btn.run { background: linear-gradient(90deg,#3aa0ff,#0b6fb3); }
.top-btn.export { background: linear-gradient(90deg,#f1c40f,#f39c12); color:black !important;}
.top-btn.reset { background: linear-gradient(90deg,#ff4b4b,#c40000); }
.small-note { color:#cfe9ff; font-size:13px; margin-bottom:6px; }
</style>
""", unsafe_allow_html=True)

# ---------------- header ----------------
st.markdown("<div class='big-title'>Fraud / Scam Detector — Unified ML & LLM</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Designed & Developed by Randy Singh - KNet Consulting</div>", unsafe_allow_html=True)

# ---------------- top controls ----------------
st.markdown("<div class='top-bar'>"
            "<a class='top-btn gen' href='?page=home'>Home</a>"
            "<a class='top-btn gen' href='?page=sample'>Sample Data</a>"
            "<a class='top-btn run' href='?page=analysis'>Analysis</a>"
            "<a class='top-btn run' href='?page=ml'>ML Metrics</a>"
            "<a class='top-btn upload' href='?page=heatmap'>Heatmap</a>"
            "<a class='top-btn export' href='?page=export'>Export</a>"
            "</div>", unsafe_allow_html=True)

# ---------------- read page param ----------------
page = st.experimental_get_query_params().get("page", ["home"])[0]

# ---------------- utilities ----------------
def generate_sample_data(n):
    rng = np.random.default_rng()
    amounts = rng.integers(10, 5000, size=n)
    device_changes = rng.integers(0, 5, size=n)
    ip_distance = rng.integers(0, 1000, size=n)
    velocity_score = rng.integers(1, 100, size=n)
    is_fraud = ((amounts > 3000) | (device_changes >= 3) | (velocity_score > 80)).astype(int)
    df = pd.DataFrame({
        "transaction_id": np.arange(1, n+1),
        "amount": amounts,
        "device_changes": device_changes,
        "ip_distance": ip_distance,
        "velocity_score": velocity_score,
        "is_fraud": is_fraud
    })
    return df

def generate_pdf_report_bytes(df, analysis_results, llm_output=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Fraud/Scam Detection Report", 0, 1, "C")
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1)
    pdf.ln(4)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Summary Metrics", 0, 1)
    pdf.set_font("Arial", "", 11)
    for k, v in analysis_results.items():
        pdf.cell(0, 8, f"{k}: {v}", 0, 1)
    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Top ML flagged events (sample):", 0, 1)
    pdf.set_font("Arial", "", 10)
    sample = df.head(20).to_dict(orient="records")
    for r in sample:
        pdf.multi_cell(0, 6, str(r))
    if llm_output:
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "LLM Analysis", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 6, llm_output)
    out = io.BytesIO()
    pdf.output(out)
    out.seek(0)
    return out.read()

def run_llm_analysis_text(log_text):
    prompt = ("You are a cybersecurity log analyst. Analyze these logs and identify:\n"
              "- Potential fraud or scam behavior\n"
              "- Indicators of compromise\n"
              "- Risk summary (0–100)\n"
              "- Key suspicious events\n\n"
              f"LOGS:\n{log_text}\n\n")
    if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
        try:
            client = OpenAI()
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            return "OpenAI Response:\n" + resp.choices[0].message["content"]
        except Exception as e:
            return f"OpenAI call failed: {e}"
    if CLAUDE_AVAILABLE and os.getenv("ANTHROPIC_API_KEY"):
        try:
            client = anthropic.Anthropic()
            resp = client.messages.create(
                model="claude-3-haiku-20240307",
                messages=[{"role":"user","content":prompt}],
                max_tokens=400
            )
            return "Claude Response:\n" + getattr(resp, "content", str(resp))
        except Exception as e:
            return f"Claude call failed: {e}"
    if GEMINI_AVAILABLE and os.getenv("GOOGLE_API_KEY"):
        try:
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return "Gemini Response:\n" + resp.text
        except Exception as e:
            return f"Gemini call failed: {e}"
    if GPT4ALL_AVAILABLE:
        try:
            model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
            out = model.generate(prompt)
            return "GPT4All Response:\n" + out
        except Exception as e:
            return f"GPT4All call failed: {e}"
    return "No LLM available or no API keys configured."

# ---------------- session state ----------------
if "df" not in st.session_state:
    st.session_state.df = generate_sample_data(50)
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = {}
if "llm_output" not in st.session_state:
    st.session_state.llm_output = None

# ---------------- PAGE: HOME ----------------
if page == "home":
    st.header("Welcome")
    st.markdown("""
    Use the top navigation to:
    - Generate sample data  
    - Upload your own dataset (CSV)  
    - Run ML & heuristic analysis  
    - View heatmaps, confusion matrices, ROC, and export reports  
    """)
    uploaded = st.file_uploader("Upload CSV/JSON/TXT/LOG (optional)", type=["csv","json","txt","log"])
    if uploaded is not None:
        try:
            name = uploaded.name.lower()
            if name.endswith(".csv"):
                df = pd.read_csv(uploaded)
            elif name.endswith(".json"):
                df = pd.read_json(uploaded)
            else:
                raw = uploaded.read().decode("utf-8", errors="ignore").splitlines()
                df = pd.DataFrame({"line": raw})
            st.session_state.df = df
            st.success(f"Loaded {uploaded.name} with {len(df)} rows")
        except Exception as e:
            st.error(f"Failed to load file: {e}")
    st.markdown("---")
    st.markdown("### Current dataset preview (first 10 rows)")
    st.dataframe(st.session_state.df.head(10))

# ---------------- PAGE: SAMPLE DATA ----------------
if page == "sample":
    st.header("Sample Data Generator")
    st.write("Pick how many synthetic transactions to generate for testing & demos.")
    n = st.slider("Number of sample records", min_value=10, max_value=2000, value=100, step=10, key="sample_count")
    if st.button("Generate Sample Data"):
        st.session_state.df = generate_sample_data(int(n))
        st.session_state.analysis_results = {}
        st.success(f"Generated {n} sample records.")
    st.markdown("Data preview:")
    st.dataframe(st.session_state.df.head(200))
    if "is_fraud" in st.session_state.df.columns:
        fig = px.pie(st.session_state.df, names="is_fraud", title="Fraud vs Non-Fraud (sample)")
        st.plotly_chart(fig, use_container_width=True)
    csv_bytes = st.session_state.df.to_csv(index=False).encode("utf-8")
    st.download_button("Download sample CSV", data=csv_bytes, file_name="sample_transactions.csv", mime="text/csv")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<button class='top-btn reset' onclick='location.reload()'>RESET (browser)</button>", unsafe_allow_html=True)

# ---------------- PAGE: ANALYSIS ----------------
if page == "analysis":
    st.header("Fraud Analysis")
    df = st.session_state.df.copy()
    required_cols = ["amount", "device_changes", "ip_distance", "velocity_score"]
    for c in required_cols:
        if c not in df.columns:
            df[c] = 0

    def compute_heuristic_row(row):
        s = 0
        if row["amount"] > 3000: s += 25
        if row["device_changes"] >= 3: s += 30
        if row["ip_distance"] > 500: s += 20
        if row["velocity_score"] > 80: s += 25
        return min(100, int(s))
    df["heuristic_score"] = df.apply(compute_heuristic_row, axis=1)
    df["ml_score"] = np.clip(df["velocity_score"]*0.9 + df["amount"]*0.01, 0, 100)
    df["combined_score"] = (0.6*df["ml_score"] + 0.4*df["heuristic_score"]).round(2)

    iso = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)
    features_for_iso = df[required_cols].astype(float)
    try:
        iso.fit(features_for_iso)
        df["iso_pred"] = iso.predict(features_for_iso)
        df["ml_flagged"] = df["iso_pred"].apply(lambda x: True if x==-1 else False)
    except Exception as e:
        st.error(f"IsolationForest failed: {e}")
        df["ml_flagged"] = False

    ml_score_mean = float(df["ml_score"].mean())
    heuristic_mean = float(df["heuristic_score"].mean())
    combined_mean = float(df["combined_score"].mean())
    flagged_count = int(df["ml_flagged"].sum())

    st.subheader("Score Summary")
    st.metric("ML Score (avg)", f"{ml_score_mean:.2f}")
    st.metric("Heuristic Score (avg)", f"{heuristic_mean:.2f}")
    st.metric("Combined Score (avg)", f"{combined_mean:.2f}")
    st.metric("ML Anomaly flagged (count)", f"{flagged_count}")

    flagged_df = df[df["ml_flagged"]].sort_values("combined_score", ascending=False)
    st.subheader("Top flagged events")
    if not flagged_df.empty:
        st.dataframe(flagged_df.head(200))
        st.download_button("Download flagged events CSV", flagged_df.to_csv(index=False).encode("utf-8"),
                           file_name="flagged_events.csv", mime="text/csv")
    else:
        st.info("No anomalies flagged by IsolationForest.")

    st.subheader("Visualizations")
    fig = px.bar(x=["ML Score", "Heuristic Score", "Combined Score"],
                 y=[ml_score_mean, heuristic_mean, combined_mean],
                 title="Average Scores",
                 color=[ml_score_mean, heuristic_mean, combined_mean],
                 color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(fig, use_container_width=True)

    rem = max(0, 100 - (ml_score_mean + heuristic_mean))
    pie_sizes = [ml_score_mean, heuristic_mean, rem]
    pie_labels = ["ML","Heuristic","Remaining"]
    fig2 = px.pie(values=pie_sizes, names=pie_labels,
                  title="Score Composition (avg)",
                  color_discrete_map={"ML":"#1f77b4", "Heuristic":"#ff7f0e","Remaining":"#2ca02c"})
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Correlation Heatmap")
    corr = df[required_cols + ["combined_score"]].corr()
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

    st.session_state.analysis_results = {
        "ml_score_mean": round(ml_score_mean,2),
        "heuristic_mean": round(heuristic_mean,2),
        "combined_mean": round(combined_mean,2),
        "flagged_count": flagged_count
    }
    st.session_state.df = df

# ---------------- PAGE: ML METRICS ----------------
if page == "ml":
    st.header("ML Metrics & Model Evaluation")
    df = st.session_state.df.copy()
    if "is_fraud" not in df.columns:
        st.info("No 'is_fraud' label column present.")
    else:
        X = df[required_cols].astype(float)
        y = df["is_fraud"].astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
        clf = RandomForestClassifier(n_estimators=200, random_state=42)
        with st.spinner("Training RandomForest..."):
            clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        y_prob = clf.predict_proba(X_test)[:,1]
        prec, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average="binary", zero_division=0)
        st.metric("Precision", f"{prec:.3f}")
        st.metric("Recall", f"{recall:.3f}")
        st.metric("F1-score", f"{f1:.3f}")
        cm = confusion_matrix(y_test, y_pred)
        fig_cm, ax_cm = plt.subplots()
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["non-fraud","fraud"])
        disp.plot(ax=ax_cm, cmap="Blues", values_format='d')
        st.subheader("Confusion Matrix")
        st.pyplot(fig_cm)
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        fig_roc, ax_roc = plt.subplots()
        ax_roc.plot(fpr,tpr,label=f"AUC={roc_auc:.3f}")
        ax_roc.plot([0,1],[0,1], linestyle="--", color="gray")
        ax_roc.set_xlabel("False Positive Rate")
        ax_roc.set_ylabel("True Positive Rate")
        ax_roc.set_title("ROC Curve")
        ax_roc.legend(loc="lower right")
        st.pyplot(fig_roc)
        st.subheader("Feature importances (RandomForest)")
        imp = pd.Series(clf.feature_importances_, index=X.columns).sort_values(ascending=False)
        st.bar_chart(imp)

# ---------------- PAGE: HEATMAP ----------------
if page == "heatmap":
    st.header("Fraud Heatmap / Feature Correlations")
    df = st.session_state.df.copy()
    if set(required_cols).issubset(df.columns):
        corr = df[required_cols + ["combined_score"]].corr()
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
        st.markdown("### Feature Distribution")
        fig2, ax2 = plt.subplots(1, len(required_cols), figsize=(16,4))
        for i, c in enumerate(required_cols):
            sns.histplot(df[c], bins=20, ax=ax2[i], kde=True, color="#1f77b4")
            ax2[i].set_title(c)
        st.pyplot(fig2)
    else:
        st.info("Insufficient columns for heatmap.")

# ---------------- PAGE: EXPORT ----------------
if page == "export":
    st.header("Export PDF / CSV")
    df = st.session_state.df
    res = st.session_state.analysis_results
    llm_out = st.session_state.llm_output
    if st.button("Run LLM Analysis on top 100 rows"):
        try:
            text = df.head(100).to_csv(index=False)
            llm_out = run_llm_analysis_text(text)
            st.session_state.llm_output = llm_out
        except Exception as e:
            st.error(f"LLM call failed: {e}")
    if llm_out:
        st.subheader("LLM Analysis Output")
        st.text_area("LLM Analysis", llm_out, height=200)
    pdf_bytes = generate_pdf_report_bytes(df, res, llm_out)
    st.download_button("Download PDF Report", data=pdf_bytes, file_name="fraud_report.pdf", mime="application/pdf")
    st.download_button("Download Full CSV", data=df.to_csv(index=False).encode("utf-8"),
                       file_name="full_dataset.csv", mime="text/csv")

# ---------------- persistent Reset button ----------------
st.markdown("<br><div style='text-align:center'>"
            "<button class='top-btn reset' onclick='location.reload()'>RESET (browser)</button>"
            "</div>", unsafe_allow_html=True)
