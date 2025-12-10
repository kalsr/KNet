

# app.py - Unified Fraud/Scam Detector (Streamlit single-file)
# Modified per user: top blue banner, top horizontal colored buttons,
# Reset button red, score explanations with ":" and calculated value, pie charts.
import os
import re
import io
import json
import random
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import IsolationForest
from fpdf import FPDF

# Optional LLM imports (non-fatal)
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

# ------------------------------
# Page config and CSS
# ------------------------------
st.set_page_config(page_title="Fraud/Scam Detector - Unified", layout="wide")

# Custom CSS:
# - Blue top banner
# - Button shapes + colors (targeted by aria-label)
# - Smaller fonts for certain areas
CUSTOM_CSS = """
<style>
/* Top blue banner */
.header-box {
  background: linear-gradient(90deg,#1e90ff,#0f62fe);
  color: white;
  padding: 18px;
  border-radius: 8px;
  font-family: "Calibri", sans-serif;
}
.header-title { font-size:22px; font-weight:700; margin:0; }
.header-sub { font-size:14px; margin:0; opacity:0.95; }

/* General button style - rounded rectangle look */
.stButton>button {
  border-radius: 8px !important;
  padding: 10px 18px !important;
  font-weight: 700 !important;
  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  border: none !important;
}

/* Specific colors using aria-label (Streamlit sets aria-label equal to label text) */
button[aria-label="Generate Sample Data"] {
  background: linear-gradient(90deg,#28b463,#1e8449) !important; color: white !important;
}
button[aria-label="Upload Log File"] {
  background: linear-gradient(90deg,#3498db,#2e86c1) !important; color: white !important;
}
button[aria-label="Run Analysis"] {
  background: linear-gradient(90deg,#2d98da,#1b6fa8) !important; color: white !important;
}
button[aria-label="Export PDF Report"] {
  background: linear-gradient(90deg,#7f8c8d,#95a5a6) !important; color: white !important;
}
button[aria-label="Reset Data"] {
  background: linear-gradient(90deg,#e74c3c,#c0392b) !important; color: white !important;
}

/* File uploader style (make it less tall) */
div.stFileUploader { padding: 6px 0px 6px 0px; }

/* Small explanatory text */
.score-explain { font-size: 14px; line-height: 1.4; }

/* Pie chart center text */
.pie-center { font-weight: 700; font-size: 12px; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ------------------------------
# Core analysis code (preserved)
# ------------------------------
KEYWORDS = ["failed","error","invalid","unauthorized","denied","403","blocked","brute","suspicious"]

def extract_features(line):
    line_low = line.lower()
    keyword_vec = [1 if k in line_low else 0 for k in KEYWORDS]
    digit_count = sum(c.isdigit() for c in line)
    uppercase_count = sum(c.isupper() for c in line)
    length = len(line)
    return np.array(keyword_vec + [digit_count, uppercase_count, length])

def train_ml_model():
    benign = ["User login OK","GET /home 200 OK","Regular system check","Read operation successful",
              "File opened normally","Heartbeat OK"]
    suspicious = ["Failed login attempt from 192.168.1.22","Multiple failed password attempts",
                  "Unauthorized access detected","Apache error 403 /admin",
                  "Invalid user root Linux auth","Windows EventLog access denied",
                  "Brute-force attack detected","Suspicious POST request 10.0.0.5"]
    all_logs = benign + suspicious
    X = np.array([extract_features(l) for l in all_logs])
    model = IsolationForest(n_estimators=200, contamination=0.35, random_state=42)
    model.fit(X)
    return model

ML_MODEL = train_ml_model()

def ml_analyze(logs):
    if len(logs) == 0:
        return 0, []
    X = np.array([extract_features(l) for l in logs])
    preds = ML_MODEL.predict(X)
    score = int(np.sum(preds == -1) * 10)
    anomalies = [logs[i] for i in range(len(logs)) if preds[i] == -1]
    return score, anomalies

def heuristic_analysis(logs):
    score, flags = 0, []
    for l in logs:
        l_low = l.lower()
        if "failed" in l_low: score += 5; flags.append(l)
        if "unauthorized" in l_low: score += 7; flags.append(l)
        if "invalid user" in l_low: score += 6; flags.append(l)
        if "403" in l_low: score += 4; flags.append(l)
        if "brute" in l_low: score += 10; flags.append(l)
        if "suspicious" in l_low: score += 10; flags.append(l)
    return score, list(dict.fromkeys(flags))

# LLM analysis (unchanged)
def run_llm_analysis(logs):
    prompt = ("You are a cybersecurity log analyst. Analyze these logs and identify:\n"
              "- Potential fraud or scam behavior\n"
              "- Indicators of compromise\n"
              "- Risk summary (0–100)\n"
              "- Key suspicious events\n\n"
              f"LOGS:\n{chr(10).join(logs)}\n\n")
    if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
        try:
            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            return "OpenAI GPT Response:\n" + response.choices[0].message["content"]
        except Exception as e:
            st.warning(f"OpenAI call failed: {e}")
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
            st.warning(f"Claude call failed: {e}")
    if GEMINI_AVAILABLE and os.getenv("GOOGLE_API_KEY"):
        try:
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return "Gemini Response:\n" + resp.text
        except Exception as e:
            st.warning(f"Gemini call failed: {e}")
    if GPT4ALL_AVAILABLE:
        try:
            model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
            response = model.generate(prompt)
            return "GPT4All Response:\n" + response
        except Exception as e:
            st.warning(f"GPT4All call failed: {e}")
    return "No LLM API keys configured or LLM failed to run."

# Parsers (unchanged)
APACHE_REGEX = re.compile(r'(\d+\.\d+\.\d+\.\d+).*"(GET|POST|PUT|DELETE).*" (\d{3})')
LINUX_REGEX = re.compile(r'(invalid user|failed password|authentication failure)', re.IGNORECASE)
WINDOWS_REGEX = re.compile(r'(Access denied|Failed login|Audit failure|EventID:\s*\d+)', re.IGNORECASE)

def parse_apache(lines):
    parsed = []
    for l in lines:
        m = APACHE_REGEX.search(l)
        if m:
            ip, method, code = m.groups()
            parsed.append(f"ApacheLog | IP:{ip} | METHOD:{method} | STATUS:{code}")
        else:
            parsed.append(l.strip())
    return parsed

def parse_linux_log(lines):
    parsed = []
    for l in lines:
        if LINUX_REGEX.search(l):
            parsed.append("LinuxAuth | SUSPICIOUS: " + l.strip())
        else:
            parsed.append("LinuxLog | " + l.strip())
    return parsed

def parse_windows_log(lines):
    parsed = []
    for l in lines:
        if WINDOWS_REGEX.search(l):
            parsed.append("WinEvent | ALERT: " + l.strip())
        else:
            parsed.append("WinEvent | " + l.strip())
    return parsed

def load_file_auto_streamlit(uploaded_file):
    if uploaded_file is None:
        return []
    name = uploaded_file.name.lower()
    try:
        if name.endswith(".json"):
            data = json.load(uploaded_file)
            return [str(x) for x in data]
        elif name.endswith(".csv"):
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file)
            return df.astype(str).agg(" | ".join, axis=1).tolist()
        elif name.endswith(".log") or name.endswith(".txt"):
            uploaded_file.seek(0)
            raw = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
            if any("GET" in l or "POST" in l for l in raw):
                return parse_apache(raw)
            if any("invalid user" in l.lower() or "auth" in name.lower() for l in raw):
                return parse_linux_log(raw)
            if any("Event" in l or "Windows" in l for l in raw):
                return parse_windows_log(raw)
            return [l.strip() for l in raw]
        else:
            uploaded_file.seek(0)
            raw = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
            return [l.strip() for l in raw]
    except Exception as e:
        st.error(f"Failed to read uploaded file: {e}")
        return []

# Sample data generator
SAMPLE_EVENTS = ["Failed login from IP 192.168.1.55","User admin attempted unauthorized access",
                 "Multiple login attempts detected","Access granted for normal user",
                 "Apache error 403 for /admin","Suspicious POST request from 10.0.0.22",
                 "Brute-force pattern detected","Linux auth.log: invalid user root",
                 "Windows EventLog: access denied","Firewall blocked outgoing connection"]

def generate_sample_data(n=40):
    return [f"[Event {i+1}] {random.choice(SAMPLE_EVENTS)}" for i in range(n)]

# Visualization helpers (unchanged)
def plot_scores(ml_score, heuristic_score, combined_score):
    labels = ["ML Score", "Heuristic Score", "Combined Score"]
    scores = [ml_score, heuristic_score, combined_score]
    fig, ax = plt.subplots(figsize=(6, 3.5))
    bars = ax.bar(labels, scores)
    ax.set_ylim(0, max(scores + [20]) + 15)
    ax.set_title("Fraud/Scam Score Visualization")
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, str(score),
                ha="center", fontweight="bold")
    st.pyplot(fig)

def plot_heatmap(logs):
    if not logs:
        st.info("No logs to build heatmap.")
        return
    n = min(len(logs), 80)
    sample = logs[:n]
    mat = np.zeros((n, len(KEYWORDS)), dtype=int)
    for i, row in enumerate(sample):
        low = row.lower()
        for j, kw in enumerate(KEYWORDS):
            mat[i, j] = 1 if kw in low else 0
    fig, ax = plt.subplots(figsize=(8, min(6, 0.12 * n + 1)))
    cax = ax.imshow(mat, aspect="auto")
    ax.set_yticks(np.arange(len(sample)))
    ax.set_yticklabels([f"{i+1}" for i in range(len(sample))], fontsize=6)
    ax.set_xticks(np.arange(len(KEYWORDS)))
    ax.set_xticklabels(KEYWORDS, rotation=45, fontsize=9)
    ax.set_title("Keyword Presence Heatmap (rows = sample events)")
    fig.colorbar(cax, orientation="vertical", fraction=0.03)
    st.pyplot(fig)

# PDF report generator (unchanged)
def generate_pdf_report_bytes(results, llm_output=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Fraud/Scam Detection Report", 0, 1, "C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1)
    pdf.ln(5)
    pdf.cell(0, 10, f"ML Score: {results.get('ml_score', 0)}", 0, 1)
    pdf.cell(0, 10, f"Heuristic Score: {results.get('heuristic_score', 0)}", 0, 1)
    pdf.cell(0, 10, f"Combined Score: {results.get('combined_score', 0)}", 0, 1)
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "ML Flagged Logs:", 0, 1)
    pdf.set_font("Arial", "", 11)
    for l in results.get("ml_flags", []):
        pdf.multi_cell(0, 8, "- " + l)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Heuristic Flags:", 0, 1)
    pdf.set_font("Arial", "", 11)
    for l in results.get("heuristic_flags", []):
        pdf.multi_cell(0, 8, "- " + l)
    if llm_output:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "LLM Analysis:", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, llm_output)
    out = io.BytesIO()
    pdf.output(out)
    out.seek(0)
    return out.read()

# ---------------------------------
# Session state initialization
# ---------------------------------
if "logs" not in st.session_state:
    st.session_state.logs = []
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = {}
if "llm_output" not in st.session_state:
    st.session_state.llm_output = None

# ---------------------------------
# Top banner (blue highlighted)
# ---------------------------------
st.markdown(
    """
    <div class="header-box">
      <p class="header-title">Fraud / Scam Detector — Unified ML & LLM</p>
      <p class="header-sub">Designed & Developed by Randy Singh - KNet Consulting</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------
# Top horizontal action row (Option 1)
# ---------------------------------
top_cols = st.columns([1.4, 1.4, 1.4, 1.4, 1.0, 1.0, 1.0])

with top_cols[0]:
    if st.button("Generate Sample Data"):
        # slider popup to choose number
        n = st.slider("Number of sample events", min_value=10, max_value=500, value=40, key="sample_slider")
        st.session_state.logs = generate_sample_data(n)
        st.session_state.analysis_results = {}
        st.success(f"Generated {n} sample events.")

with top_cols[1]:
    # File uploader; place Upload button next to it for consistent layout
    uploaded_file = st.file_uploader("", type=["log","txt","csv","json"], key="top_uploader")
    # Use a separate button to confirm upload (to allow styling)
    if st.button("Upload Log File"):
        if uploaded_file is None:
            st.warning("Pick a file using the uploader control first.")
        else:
            logs_loaded = load_file_auto_streamlit(uploaded_file)
            if logs_loaded:
                st.session_state.logs = logs_loaded
                st.session_state.analysis_results = {}
                st.success(f"Loaded {len(logs_loaded)} log entries from {uploaded_file.name}")

with top_cols[2]:
    if st.button("Run Analysis"):
        if not st.session_state.logs:
            st.warning("Please upload or generate logs first.")
        else:
            ml_score, ml_flags = ml_analyze(st.session_state.logs)
            heuristic_score, heuristic_flags = heuristic_analysis(st.session_state.logs)
            combined_score = ml_score + heuristic_score
            st.session_state.analysis_results = {
                "ml_score": ml_score,
                "heuristic_score": heuristic_score,
                "combined_score": combined_score,
                "ml_flags": ml_flags,
                "heuristic_flags": heuristic_flags
            }
            st.success("Analysis complete. See results below.")

with top_cols[3]:
    if st.button("Export PDF Report"):
        if not st.session_state.analysis_results:
            st.warning("Run analysis before exporting.")
        else:
            llm_out = None
            if st.session_state.llm_output:
                llm_out = st.session_state.llm_output
            pdf_bytes = generate_pdf_report_bytes(st.session_state.analysis_results, llm_out)
            bname = f"Fraud_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            st.download_button("Download PDF", data=pdf_bytes, file_name=bname, mime="application/pdf")

with top_cols[4]:
    if st.button("Reset Data"):
        st.session_state.logs = []
        st.session_state.analysis_results = {}
        st.session_state.llm_output = None
        st.success("Data reset.")

with top_cols[5]:
    mode = st.selectbox("Mode", ["ML-only", "LLM+ML"], index=0)

with top_cols[6]:
    dark_mode = st.checkbox("Dark mode", value=False)
    # simple theme switch: injecting minimal dark CSS if checked
    if dark_mode:
        st.markdown(
            """
            <style>
            .stApp { background-color: #0e1117; color: #e6eef8; }
            .stMarkdown, .stText { color: #e6eef8; }
            </style>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# ---------------------------------
# Main layout: logs + analysis results + visuals
# ---------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Logs / Input")
    if st.session_state.logs:
        st.code("\n".join(st.session_state.logs[:500]), language="text")
        st.caption(f"Showing first {min(500, len(st.session_state.logs))} lines. Total events: {len(st.session_state.logs)}")
    else:
        st.info("No logs loaded. Use the top controls to generate sample data or upload a file.")

    st.markdown("---")
    st.header("Analysis Results")

    if st.session_state.analysis_results:
        res = st.session_state.analysis_results

        # Explanations followed by colon and the calculated score value
        # ML Score explanation
        ml_val = res.get("ml_score", 0)
        heuristic_val = res.get("heuristic_score", 0)
        combined_val = res.get("combined_score", 0)

        st.markdown("**ML Score calculation:** number of ML-flagged entries × 10  **:**  " + str(ml_val))
        st.markdown("**Heuristic Score calculation:** sum of heuristic rule weights for matches (failed=5, unauthorized=7, invalid user=6, 403=4, brute=10, suspicious=10)  **:**  " + str(heuristic_val))
        st.markdown("**Combined Score calculation:** ML Score + Heuristic Score  **:**  " + str(combined_val))

        st.divider()

        # Display metrics
        metric_cols = st.columns(3)
        metric_cols[0].metric("ML Score", ml_val)
        metric_cols[1].metric("Heuristic Score", heuristic_val)
        metric_cols[2].metric("Combined Score", combined_val)

        st.subheader("ML Flagged Entries")
        if res["ml_flags"]:
            st.text_area("ML Flags", value="\n".join(res["ml_flags"]), height=150)
        else:
            st.write("No ML flagged entries.")

        st.subheader("Heuristic Flags")
        if res["heuristic_flags"]:
            st.text_area("Heuristic Flags", value="\n".join(res["heuristic_flags"]), height=150)
        else:
            st.write("No heuristic flags.")
    else:
        st.info("No analysis results. Click 'Run Analysis' in the top controls.")

    st.markdown("---")
    st.header("Visualizations")
    if st.session_state.analysis_results:
        # bar chart
        plot_scores(ml_val, heuristic_val, combined_val)

        # pie chart: ML vs Heuristic vs Remaining (to 100)
        labels = ["ML Score", "Heuristic Score", "Remaining"]
        # Ensure non-negative remaining
        remaining = max(0, 100 - (ml_val + heuristic_val))
        sizes = [ml_val, heuristic_val, remaining]
        colors = ["#2ecc71", "#f1c40f", "#95a5a6"]
        fig1, ax1 = plt.subplots(figsize=(5,4))
        wedges, texts, autotexts = ax1.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=140, colors=colors, textprops={'color':'black'})
        ax1.axis('equal')
        ax1.set_title("Score Composition (ML vs Heuristic vs Remaining)")
        st.pyplot(fig1)

        st.subheader("Fraud Heatmap")
        plot_heatmap(st.session_state.logs)
    else:
        st.info("Run analysis to see visualizations.")

with col2:
    st.header("Quick Controls & LLM")
    st.markdown("**Current Mode:** " + ("LLM+ML" if mode == "LLM+ML" else "ML-only"))
    if mode == "LLM+ML":
        st.info("LLM mode selected. LLM API keys must be configured as environment variables. If no key is found, the LLM step will be skipped.")
        st.markdown("""
        **Supported (optional) LLMs**:
        - OpenAI GPT (OPENAI_API_KEY)
        - Anthropic Claude (ANTHROPIC_API_KEY)
        - Google Gemini (GOOGLE_API_KEY)
        - GPT4All (local model)
        """)
        if st.button("Run LLM Analysis (on current logs)"):
            if not st.session_state.logs:
                st.warning("No logs to analyze.")
            else:
                with st.spinner("Running LLM..."):
                    out = run_llm_analysis(st.session_state.logs)
                    st.session_state.llm_output = out
                    st.subheader("LLM Output")
                    st.text_area("LLM Analysis", value=out, height=300)
    else:
        st.info("ML-only mode: LLM calls are disabled.")

    st.markdown("---")
    st.header("Utilities")
    if st.button("Show sample summary (counts)"):
        if not st.session_state.logs:
            st.warning("No logs loaded")
        else:
            df = pd.DataFrame({"event": st.session_state.logs})
            df["has_keyword"] = df["event"].str.lower().apply(lambda x: any(k in x for k in KEYWORDS))
            st.write(df["has_keyword"].value_counts())
            st.write(df.head(10))

    if st.button("Download raw logs (.txt)"):
        if not st.session_state.logs:
            st.warning("No logs loaded")
        else:
            raw = "\n".join(st.session_state.logs)
            st.download_button("Download logs.txt", data=raw.encode("utf-8"), file_name="logs.txt", mime="text/plain")

st.markdown("---")
st.caption("Converted from a Tkinter single-file desktop app into Streamlit. Core analysis logic preserved.")
