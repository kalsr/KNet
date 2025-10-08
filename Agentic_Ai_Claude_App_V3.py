# Author: KNet Consulting (demo)


import streamlit as st
import pandas as pd
import numpy as np
import os, io, json, random
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
from datetime import datetime, timedelta

# Try import Anthropic safely
try:
    from anthropic import Anthropic
    ANTHROPIC_SDK_AVAILABLE = True
except Exception:
    ANTHROPIC_SDK_AVAILABLE = False

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Agentic Cyber AI Analysis Hub - Randy Singh", layout="wide", initial_sidebar_state="expanded")

# ---------------------------
# Helper utilities
# ---------------------------
def now_iso():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def init_state():
    if "df" not in st.session_state:
        st.session_state.df = pd.DataFrame()
    if "analysis" not in st.session_state:
        st.session_state.analysis = {}
    if "role" not in st.session_state:
        st.session_state.role = "Viewer"

def generate_sample_data(n=50):
    rng = np.random.default_rng(seed=42)
    timestamps = [datetime.utcnow() - timedelta(minutes=int(i * 5)) for i in range(n)]
    threats = ["Malware", "Phishing", "DDoS", "Ransomware", "SQL Injection", "Insider Threat"]
    severities = ["Low", "Medium", "High", "Critical"]
    df = pd.DataFrame({
        "timestamp": timestamps,
        "source_ip": [f"10.0.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)],
        "dest_ip": [f"192.168.{rng.integers(0,256)}.{rng.integers(1,255)}" for _ in range(n)],
        "threat_type": rng.choice(threats, size=n),
        "severity": rng.choice(severities, size=n, p=[0.45,0.3,0.2,0.05]),
        "impact_score": rng.integers(10,101, size=n)
    })
    df["quarantined"] = False
    return df

def detect_columns(df):
    """Detect common column names and return standardized mapping."""
    cols = {c.lower().strip(): c for c in df.columns}
    mapping = {}
    # severity-like
    for candidate in ["severity", "sev", "level", "risk"]:
        if candidate in cols:
            mapping["severity"] = cols[candidate]
            break
    # threat-like
    for candidate in ["threat", "threat_type", "type"]:
        if candidate in cols:
            mapping["threat"] = cols[candidate]
            break
    # timestamp-like
    for candidate in ["timestamp", "time", "datetime", "ts"]:
        if candidate in cols:
            mapping["timestamp"] = cols[candidate]
            break
    # ip-like
    for candidate in ["source_ip", "src_ip", "src", "ip"]:
        if candidate in cols:
            mapping["src_ip"] = cols[candidate]
            break
    for candidate in ["dest_ip", "dst_ip", "dst", "destination"]:
        if candidate in cols:
            mapping["dst_ip"] = cols[candidate]
            break
    return mapping

def create_plottable_df(df):
    # make copy and standardize column names to lowercase keys for internal usage
    df2 = df.copy()
    df2.columns = [c.strip() for c in df2.columns]
    mapping = detect_columns(df2)
    # unify names
    if "timestamp" in mapping:
        ts_col = mapping["timestamp"]
        try:
            df2[ts_col] = pd.to_datetime(df2[ts_col])
        except Exception:
            # leave as-is
            pass
    return df2, mapping

def anthropic_analyze(df):
    """Call Anthropic Claude if available and API key present."""
    if not ANTHROPIC_SDK_AVAILABLE:
        return {"error": "Anthropic SDK not installed."}
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return {"error": "No ANTHROPIC_API_KEY configured."}
    try:
        client = Anthropic(api_key=api_key)
        prompt = f"""
You are a cyber security analyst. Summarize patterns, severity distribution and mitigations from this data:
{df.to_json(orient='records', indent=2)}
"""
        response = client.messages.create(
            model="claude-2.1",  # or any available model; adapt if needed
            messages=[{"role":"user","content":prompt}],
            max_tokens=600
        )
        # response parsing depends on sdk version
        try:
            text = response.content[0].text
        except Exception:
            text = str(response)
        return {"ai_text": text}
    except Exception as e:
        return {"error": str(e)}

def local_rule_based_analysis(df, mapping):
    summary = {}
    insights = []
    # severity counts (if available)
    sev_col = mapping.get("severity")
    if sev_col and sev_col in df.columns:
        counts = df[sev_col].value_counts().to_dict()
        summary["severity_counts"] = counts
        high_count = counts.get("High", 0) + counts.get("Critical", 0)
        if high_count > 0:
            insights.append(f" {high_count} high/critical events detected.")
        else:
            insights.append(" No high/critical events detected.")
    else:
        summary["severity_counts"] = None
        insights.append(" Severity column not found; skipping severity breakdown.")
    # threat types
    th_col = mapping.get("threat")
    if th_col and th_col in df.columns:
        top = df[th_col].value_counts().nlargest(5).to_dict()
        summary["top_threats"] = top
        insights.append(f"Top threats: {', '.join(list(top.keys())[:5])}")
    else:
        summary["top_threats"] = None
    # time series trend if timestamp exists
    ts_col = mapping.get("timestamp")
    if ts_col and ts_col in df.columns:
        try:
            ser = pd.to_datetime(df[ts_col])
            trend = ser.dt.floor("D").value_counts().sort_index()
            summary["trend"] = trend.to_dict()
        except Exception:
            summary["trend"] = None
    else:
        summary["trend"] = None
    # basic mitigations
    summary["recommendations"] = [
        "Harden email gateway and enable advanced phishing detection.",
        "Patch and update vulnerable systems regularly.",
        "Segment networks and restrict lateral movement."
    ]
    return {"summary": summary, "insights": insights}

def convert_df_bytes(df, fmt):
    if fmt == "csv":
        return df.to_csv(index=False).encode("utf-8")
    if fmt == "json":
        return df.to_json(orient="records", indent=2).encode("utf-8")
    if fmt == "excel":
        out = io.BytesIO()
        with pd.ExcelWriter(out, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="results")
        return out.getvalue()
    return None

def plot_severity_trend(summary):
    # summary['trend'] expected dict date->count
    trend = summary.get("trend")
    if not trend:
        st.info("No timestamp/trend data available for severity trend.")
        return
    series = pd.Series(trend).sort_index()
    fig = px.line(series, x=series.index, y=series.values, labels={"x":"date","y":"count"}, title="Records per Day")
    st.plotly_chart(fig, use_container_width=True)

def plot_threat_heatmap(df, mapping):
    th_col = mapping.get("threat")
    sev_col = mapping.get("severity")
    if not th_col or not sev_col or th_col not in df.columns or sev_col not in df.columns:
        st.info("PLEASE NOTE: Threat Heatmap Requires Both Threat and Severity Columns.")
        return
    pivot = pd.crosstab(df[th_col], df[sev_col])
    fig = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=pivot.columns.astype(str),
        y=pivot.index.astype(str),
        colorscale="YlOrRd"
    ))
    fig.update_layout(title="Threat Type vs Severity Heatmap", xaxis_title="Severity", yaxis_title="Threat Type", height=500)
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# UI: role selection + theming
# ---------------------------
init_state()
st.sidebar.title("Agentic Cyber AI — Access & Actions")
selected_role = st.sidebar.selectbox("Role", ["Admin","Analyst","Viewer"], index=["Admin","Analyst","Viewer"].index(st.session_state.role))
st.session_state.role = selected_role

role_style = {
    "Admin": {"bg":"#2a1a1a", "header":"#b30000", "logo":""},
    "Analyst": {"bg":"#0b2545", "header":"#005f99", "logo":""},
    "Viewer": {"bg":"#083d18", "header":"#145A32", "logo":""}
}
style = role_style.get(st.session_state.role, role_style["Viewer"])

st.markdown(f"""
<div style="background:{style['header']}; padding:12px; border-radius:8px; color:white; text-align:center;">
    <h2>{style['logo']} Agentic Cyber AI Analysis — {st.session_state.role}</h2>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Action controls
# ---------------------------
st.markdown("")  # spacer

col_gen, col_upload, col_analyze, col_download, col_reset = st.columns([1,1,1,1,1])

# sample size slider
if st.session_state.role in ("Admin","Analyst"):
    sample_size = st.sidebar.slider("Sample records to generate", 10, 100, 50, 5)
else:
    sample_size = 50  # default, viewer can't generate

# Buttons (styled by color)
with col_gen:
    if st.session_state.role in ("Admin","Analyst"):
        if st.button("Generate Sample Logs", key="gen"):
            st.session_state.df = generate_sample_data(sample_size)
            st.success(f"Generated {sample_size} sample records.")
            # scroll to top? not necessary

with col_upload:
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        try:
            dfu = pd.read_csv(uploaded)
            st.session_state.df = dfu
            st.success(f"Uploaded {uploaded.name} ({len(dfu)} rows).")
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")

with col_analyze:
    if st.button("Run Agentic AI Analysis", key="analyze"):
        if st.session_state.df is None or st.session_state.df.empty:
            st.warning("Generate or upload data first.")
        else:
            df2, mapping = create_plottable_df(st.session_state.df)
            # do local analysis + try anthropic
            local = local_rule_based_analysis(df2, mapping)
            ai_result = {}
            # attempt anthropic if key and sdk available
            if ANTHROPIC_SDK_AVAILABLE and os.getenv("ANTHROPIC_API_KEY"):
                ai_result = anthropic_analyze(df2)
            else:
                ai_result = {"note":"Anthropic not used (SDK or API key missing)."}
            # combine
            st.session_state.analysis = {"mapping": mapping, "local": local, "ai": ai_result}
            st.success("Agentic analysis complete.")

with col_download:
    if st.session_state.df is not None and not st.session_state.df.empty:
        if st.button("Download CSV"):
            csv_b = convert_df_bytes(st.session_state.df, "csv")
            st.download_button("Download CSV File", data=csv_b, file_name="agentic_results.csv", mime="text/csv")
        if st.button("Download JSON"):
            jb = convert_df_bytes(st.session_state.df, "json")
            st.download_button("Download JSON File", data=jb, file_name="agentic_results.json", mime="application/json")
        if st.button("Download Excel"):
            xb = convert_df_bytes(st.session_state.df, "excel")
            st.download_button("Download Excel File", data=xb, file_name="agentic_results.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        if st.button("Download CSV", disabled=True):
            pass

with col_reset:
    if st.session_state.role == "Admin":
        if st.button(" Reset Data"):
            st.session_state.df = pd.DataFrame()
            st.session_state.analysis = {}
            st.success("Session reset.")
    else:
        if st.button(" Reset Data", disabled=True):
            pass

st.markdown("---")

# ---------------------------
# Data display (large, scrollable)
# ---------------------------
if st.session_state.df is None or st.session_state.df.empty:
    st.info("No data available — generate sample logs or upload a CSV to begin.")
else:
    st.subheader("Logs (scrollable)")
    # Show a tall scrollable table (height controls scrollbar)
    st.dataframe(st.session_state.df, height=520)  # scrollbar appears for large data

    # Show record count & mapping
    df2, mapping = create_plottable_df(st.session_state.df)
    st.markdown(f" Detected columns mapping: {mapping}")

    # Interactive Charts: severity trend & threat heatmap
    st.subheader("Interactive Dashboards")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Severity Trend**")
        if st.session_state.analysis and st.session_state.analysis.get("local"):
            plot_severity_trend(st.session_state.analysis["local"]["summary"])
        else:
            # attempt to compute trend even if analysis not yet run
            try:
                if mapping.get("timestamp") and mapping.get("timestamp") in df2.columns:
                    trend_ser = pd.to_datetime(df2[mapping["timestamp"]]).dt.floor("D").value_counts().sort_index()
                    fig = px.line(trend_ser, x=trend_ser.index, y=trend_ser.values, labels={"x":"date","y":"count"}, title="Records per Day")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No timestamp column for trend.")
            except Exception as e:
                st.error(f"Trend error: {e}")

    with col2:
        st.markdown("**Threat Heatmap**")
        try:
            plot_threat_heatmap(df2, mapping)
        except Exception as e:
            st.error(f"Heatmap error: {e}")

    st.markdown("---")

    # Agentic Analysis results
    st.subheader("Agentic Analysis")
    if st.session_state.analysis:
        # Local summary
        local = st.session_state.analysis.get("local", {})
        if local:
            st.markdown("**Local rule-based insights**")
            for i in local.get("insights", []):
                st.write("- " + i)
            st.markdown("Recommendations:")
            for rec in local.get("summary", {}).get("recommendations", []):
                st.write("• " + rec)
        # AI result if present
        ai = st.session_state.analysis.get("ai", {})
        if ai:
            if "error" in ai:
                st.warning("Anthropic error: " + ai["error"])
            elif "ai_text" in ai:
                st.markdown("**Agentic AI (Claude) summary**")
                st.write(ai["ai_text"])
            else:
                st.info(ai.get("note", "No AI summary available."))
    else:
        st.info("Click 'Run Agentic AI Analysis' to produce insights.")

st.markdown("---")
st.caption("PLEASE NOTE ONLY ADMIN ROLE CAN RESET THE DATA. YOU CAN CHOOSE, ADMIN, ANALYSIS & VIEWER ROLES.")
st.caption("Agentic Cyber AI Analysis Hub — Demo. Role & API handling are local DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.")

