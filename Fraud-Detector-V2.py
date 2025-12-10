
# Unified Fraud/Scam Detector (Single-file Streamlit app)

Features:
# Single-page with sidebar navigation
# ML-only offline mode (IsolationForest)
# LLM+ML online mode (optional LLMs if API keys/libs present)
# Generate sample data, upload logs (txt/log/csv/json)
# Heuristic + ML analysis, combined scoring
# Fraud heatmap visualization
# Export PDF report (downloadable)
# Dark mode toggle (basic via CSS)
# Colored buttons (styled with CSS)
# Keeps your original parsing/analysis logic

import os
import re
import io
import json
import random
import base64
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import IsolationForest
from fpdf import FPDF

# Optional LLM imports - try them but do not require them
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
# Styling: dark mode + button colors
# ------------------------------
st.set_page_config(page_title="Fraud/Scam Detector - Unified", layout="wide")

# Basic CSS for colored buttons and dark mode switch
def local_css(dark_mode=False):
    dark_css = """
    .stApp { background-color: #0e1117; color: #e6eef8; }
    .reportview-container .main .block-container{ padding-top:1rem; }
    """
    light_css = """
    .stApp { background-color: white; color: black; }
    .reportview-container .main .block-container{ padding-top:1rem; }
    """
    btn_css = """
    <style>
    .stButton>button { border-radius: 8px; padding: 10px 18px; font-weight:600; }
    .btn-red { background: linear-gradient(90deg,#e74c3c,#c0392b); color: white; }
    .btn-green { background: linear-gradient(90deg,#28b463,#1e8449); color: white; }
    .btn-blue { background: linear-gradient(90deg,#3498db,#2e86c1); color: white; }
    .btn-secondary { background: linear-gradient(90deg,#95a5a6,#7f8c8d); color: white; }
    .small { padding:6px 10px; font-size:0.9rem; }
    </style>
    """
    st.markdown(btn_css, unsafe_allow_html=True)
    st.markdown(dark_css if dark_mode else light_css, unsafe_allow_html=True)

# ------------------------------
# Core analysis code (from your original app)
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
    return score, list(dict.fromkeys(flags))  # keep order, unique

# LLM analysis: tries OpenAI, Claude, Gemini, GPT4All in that order
def run_llm_analysis(logs):
    prompt = ("You are a cybersecurity log analyst. Analyze these logs and identify:\n"
              "- Potential fraud or scam behavior\n"
              "- Indicators of compromise\n"
              "- Risk summary (0–100)\n"
              "- Key suspicious events\n\n"
              f"LOGS:\n{chr(10).join(logs)}\n\n")
    # OpenAI (requires OPENAI_API_KEY in env)
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
    # Anthropic
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
    # Gemini
    if GEMINI_AVAILABLE and os.getenv("GOOGLE_API_KEY"):
        try:
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-flash")
            resp = model.generate_content(prompt)
            return "Gemini Response:\n" + resp.text
        except Exception as e:
            st.warning(f"Gemini call failed: {e}")
    # GPT4All local
    if GPT4ALL_AVAILABLE:
        try:
            model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
            response = model.generate(prompt)
            return "GPT4All Response:\n" + response
        except Exception as e:
            st.warning(f"GPT4All call failed: {e}")
    return "No LLM API keys configured or LLM failed to run."

# Parsing and loading functions (adapted for streamlit file uploader)
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
            # Heuristics to choose parser
            if any("GET" in l or "POST" in l for l in raw):
                return parse_apache(raw)
            if any("invalid user" in l.lower() or "auth" in name.lower() for l in raw):
                return parse_linux_log(raw)
            if any("Event" in l or "Windows" in l for l in raw):
                return parse_windows_log(raw)
            return [l.strip() for l in raw]
        else:
            # Attempt to read as text
            uploaded_file.seek(0)
            raw = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
            return [l.strip() for l in raw]
    except Exception as e:
        st.error(f"Failed to read uploaded file: {e}")
        return []

# Sample data generation
SAMPLE_EVENTS = ["Failed login from IP 192.168.1.55","User admin attempted unauthorized access",
                 "Multiple login attempts detected","Access granted for normal user",
                 "Apache error 403 for /admin","Suspicious POST request from 10.0.0.22",
                 "Brute-force pattern detected","Linux auth.log: invalid user root",
                 "Windows EventLog: access denied","Firewall blocked outgoing connection"]

def generate_sample_data(n=40):
    return [f"[Event {i+1}] {random.choice(SAMPLE_EVENTS)}" for i in range(n)]

# Plot functions using matplotlib (single plot per rule)
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
    # Create a frequency heatmap of keywords across logs (rows = logs sample, cols = keywords)
    if not logs:
        st.info("No logs to build heatmap.")
        return
    n = min(len(logs), 80)  # limit rows for display
    sample = logs[:n]
    mat = np.zeros((n, len(KEYWORDS)), dtype=int)
    for i, row in enumerate(sample):
        low = row.lower()
        for j, kw in enumerate(KEYWORDS):
            mat[i, j] = 1 if kw in low else 0
    # Sum across rows to get keyword counts and show simple heatmap
    fig, ax = plt.subplots(figsize=(8, min(6, 0.12 * n + 1)))
    cax = ax.imshow(mat, aspect="auto")
    ax.set_yticks(np.arange(len(sample)))
    ax.set_yticklabels([f"{i+1}" for i in range(len(sample))], fontsize=6)
    ax.set_xticks(np.arange(len(KEYWORDS)))
    ax.set_xticklabels(KEYWORDS, rotation=45, fontsize=9)
    ax.set_title("Keyword Presence Heatmap (rows = sample events)")
    fig.colorbar(cax, orientation="vertical", fraction=0.03)
    st.pyplot(fig)

# PDF report generator returns bytes
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
# Streamlit app layout and logic
# ---------------------------------
if "logs" not in st.session_state:
    st.session_state.logs = []
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = {}

# Sidebar
with st.sidebar:
    st.markdown("<h2>Fraud/Scam Detector</h2>", unsafe_allow_html=True)
    mode = st.radio("Mode", ["ML-only", "LLM+ML"])
    dark_mode = st.checkbox("Dark mode", value=False)
    local_css(dark_mode=dark_mode)
    st.markdown("---")
    st.markdown("### Actions")
    # Buttons styled via markdown wrappers
    if st.button("Generate Sample Data"):
        n = st.sidebar.slider("Number of sample events", min_value=10, max_value=500, value=40)
        st.session_state.logs = generate_sample_data(n)
        st.success(f"Generated {n} sample events.")
    if st.button("Reset Data"):
        st.session_state.logs = []
        st.session_state.analysis_results = {}
        st.success("Data reset.")
    uploaded_file = st.file_uploader("Upload log file (.log/.txt/.csv/.json)", type=["log","txt","csv","json"])
    if uploaded_file is not None:
        logs_loaded = load_file_auto_streamlit(uploaded_file)
        if logs_loaded:
            st.session_state.logs = logs_loaded
            st.success(f"Loaded {len(logs_loaded)} log entries from {uploaded_file.name}")
    st.markdown("---")
    st.markdown("### Export")
    if st.button("Run Analysis", help="Run ML + heuristic analysis"):
        if not st.session_state.logs:
            st.warning("Please upload or generate logs first.")
        else:
            # perform analysis
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
            st.success("Analysis complete. See main page for details.")
    if st.button("Export PDF Report"):
        if not st.session_state.analysis_results:
            st.warning("Run analysis before exporting.")
        else:
            llm_output = None
            if mode == "LLM+ML":
                with st.spinner("Running LLM analysis..."):
                    llm_output = run_llm_analysis(st.session_state.logs)
            pdf_bytes = generate_pdf_report_bytes(st.session_state.analysis_results, llm_output)
            bname = f"Fraud_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            st.download_button("Download PDF", data=pdf_bytes, file_name=bname, mime="application/pdf")

# Main area
st.title("Fraud / Scam Detector — Unified ML & LLM")
st.markdown("Designed & Developed by Randy Singh - KNet Consulting")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Logs / Input")
    if st.session_state.logs:
        st.code("\n".join(st.session_state.logs[:500]), language="text")
        st.caption(f"Showing first {min(500, len(st.session_state.logs))} lines. Total events: {len(st.session_state.logs)}")
    else:
        st.info("No logs loaded. Use the sidebar to generate sample data or upload a file.")

    st.markdown("---")
    st.header("Analysis Results")
    if st.session_state.analysis_results:
        res = st.session_state.analysis_results
        st.metric("ML Score", res["ml_score"])
        st.metric("Heuristic Score", res["heuristic_score"])
        st.metric("Combined Score", res["combined_score"])
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
        st.info("No analysis results. Click 'Run Analysis' in the sidebar.")

    st.markdown("---")
    st.header("Visualizations")
    if st.session_state.analysis_results:
        plot_scores(st.session_state.analysis_results.get("ml_score",0),
                    st.session_state.analysis_results.get("heuristic_score",0),
                    st.session_state.analysis_results.get("combined_score",0))
        st.subheader("Fraud Heatmap")
        plot_heatmap(st.session_state.logs)
    else:
        st.info("Run analysis to see visualizations.")

with col2:
    st.header("Quick Controls & LLM")
    st.markdown("**Current Mode:** " + mode)
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
                with st.spinner("Running LLM... this may take a while if using remote APIs"):
                    llm_out = run_llm_analysis(st.session_state.logs)
                st.subheader("LLM Output")
                st.text_area("LLM Analysis", value=llm_out, height=300)
    else:
        st.info("ML-only mode: LLM calls are disabled.")

    st.markdown("---")
    st.header("Utilities")
    # small controls
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
st.caption("Converted from a Tkinter single-file desktop app into Streamlit by ChatGPT. All core analysis logic preserved.")
