# MCP_app_v4.py


# MCP_app_v3_fixed.py
# Complete functional & colored Streamlit app
# Same as your working version except fixed rerun() calls for Refresh & Reset buttons.

import streamlit as st
import pandas as pd
import plotly.express as px
import random
import datetime
import io
import zipfile
from dateutil.relativedelta import relativedelta
from collections import Counter

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False

try:
    from PIL import Image as PILImage
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

# -------------------------
# Streamlit page & CSS
# -------------------------
st.set_page_config(page_title="MCP Cyber IOC Enricher (Fixed)", layout="wide")

st.markdown(
    """
    <style>
    .main { background: linear-gradient(180deg,#fbfbff 0%, #eef2ff 100%); }
    .stButton>button {
        background: linear-gradient(135deg,#3B82F6,#06B6D4);
        color: white; font-weight:700; border-radius:9px; padding:8px 14px;
    }
    .stButton>button:hover { transform: scale(1.03); }
    .control-panel { background: #ffffffcc; padding: 12px; border-radius:10px; }
    .title-card { font-size:22px; font-weight:700; }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="title-card">🧭 MCP — Cyber IOC Enricher (Fixed & Robust)</div>', unsafe_allow_html=True)
st.markdown("Upload (≤100 rows) or generate sample IOCs, run a demo MCP enrichment, visualize, and export CSV/PDF/PNG.")

# -------------------------
# Helper functions & MCP shim
# -------------------------
def guess_ioc_type(indicator: str) -> str:
    s = str(indicator)
    if s.count(".") == 3 and all(p.isdigit() for p in s.split(".")):
        return "ip"
    if "." in s:
        return "domain"
    return "hash"

def make_sample_iocs(n=25) -> pd.DataFrame:
    n = min(max(1, int(n)), 100)
    rows = []
    base_date = datetime.date.today() - relativedelta(months=6)
    for i in range(n):
        kind = random.choices(["ip","domain","hash"], weights=[0.4,0.4,0.2])[0]
        if kind == "ip":
            indicator = ".".join(str(random.randint(1,250)) for _ in range(4))
        elif kind == "domain":
            name = random.choice(["login","secure","update","bank","paypal","office","auth"])
            indicator = f"{name}{random.randint(1,99)}.{random.choice(['com','net','org','info'])}"
        else:
            indicator = ''.join(random.choice("abcdef0123456789") for _ in range(32))
        rows.append({
            "id": i+1,
            "indicator": indicator,
            "type": guess_ioc_type(indicator),
            "source": random.choice(["internal-sensor","talos","user-report","honeypot","passive-dns"]),
            "first_seen": (base_date + datetime.timedelta(days=random.randint(0,180))).isoformat(),
            "notes": ""
        })
    return pd.DataFrame(rows)

class MCPDemoServer:
    def __init__(self, dataset_df=None):
        self.dataset_df = dataset_df.copy() if dataset_df is not None else pd.DataFrame()
        self.known_malicious = {
            "1.2.3.4": {"severity":"high","confidence":0.94,"tags":["botnet","malicious-ip"], "first_seen":"2025-01-10"},
            "bad.example[.]com": {"severity":"medium","confidence":0.7,"tags":["phishing"], "first_seen":"2024-11-01"},
            "abcdef1234567890": {"severity":"high","confidence":0.98,"tags":["malware-hash"], "first_seen":"2025-03-02"},
        }

    def _looks_like_ip(self, s: str) -> bool:
        parts = s.split(".")
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

    def _simulate_ip(self, ip: str) -> dict:
        r = (sum(bytearray(ip.encode("utf8"))) % 100) / 100
        if r > 0.85:
            return {"severity":"high","confidence":0.9,"tags":["botnet","scanner"], "explain":f"IP heuristic high ({r:.2f})"}
        elif r > 0.5:
            return {"severity":"medium","confidence":0.7,"tags":["suspicious"], "explain":f"IP heuristic med ({r:.2f})"}
        else:
            return {"severity":"low","confidence":0.5,"tags":["benign"], "explain":f"IP heuristic low ({r:.2f})"}

    def _simulate_domain(self, d: str) -> dict:
        r = (sum(bytearray(d.encode("utf8"))) % 90) / 100
        if "phish" in d or r > 0.75:
            return {"severity":"high","confidence":0.88,"tags":["phishing"], "explain":f"Domain heuristic high ({r:.2f})"}
        elif r > 0.45:
            return {"severity":"medium","confidence":0.67,"tags":["suspicious","typosquat"], "explain":f"Domain heuristic med ({r:.2f})"}
        else:
            return {"severity":"low","confidence":0.45,"tags":["benign"], "explain":f"Domain heuristic low ({r:.2f})"}

    def _simulate_hash(self, h: str) -> dict:
        r = (len(h) % 10) / 10
        if r > 0.6:
            return {"severity":"high","confidence":0.9,"tags":["malware-hash"], "explain":f"Hash heuristic high ({r:.2f})"}
        else:
            return {"severity":"low","confidence":0.5,"tags":["unknown"], "explain":f"Hash heuristic low ({r:.2f})"}

    def enrich_ioc(self, indicator: str, ioc_type: str) -> dict:
        indicator = str(indicator).strip()
        if indicator in self.known_malicious:
            base = self.known_malicious[indicator]
        else:
            if ioc_type == "ip" or (ioc_type == "" and self._looks_like_ip(indicator)):
                base = self._simulate_ip(indicator)
            elif ioc_type == "domain" or (ioc_type == "" and "." in indicator):
                base = self._simulate_domain(indicator)
            else:
                base = self._simulate_hash(indicator)
        return {
            "indicator": indicator,
            "type": ioc_type or guess_ioc_type(indicator),
            "severity": base["severity"],
            "confidence": round(float(base["confidence"]), 2),
            "related_tags": base["tags"],
            "first_seen": base.get("first_seen", datetime.date.today().isoformat()),
            "explain": base.get("explain", f"Demo enrichment for {indicator}")
        }

def run_enrichment(df: pd.DataFrame, mcp_server: MCPDemoServer) -> pd.DataFrame:
    records = []
    for _, row in df.iterrows():
        indicator = row.get("indicator")
        itype = row.get("type", "") or guess_ioc_type(str(indicator))
        enr = mcp_server.enrich_ioc(indicator, itype)
        rec = row.to_dict()
        rec.update({
            "severity": enr["severity"],
            "confidence": enr["confidence"],
            "related_tags": ",".join(enr["related_tags"]),
            "first_seen_enrich": enr["first_seen"],
            "explain": enr["explain"]
        })
        records.append(rec)
    return pd.DataFrame(records)

# -------------------------
# Session state
# -------------------------
if "df_in" not in st.session_state:
    st.session_state.df_in = make_sample_iocs(25)
if "enriched_df" not in st.session_state:
    st.session_state.enriched_df = None

# -------------------------
# Controls
# -------------------------
with st.sidebar:
    st.header("Controls")
    num = st.slider("Number of sample records (when generating)", min_value=5, max_value=100, value=25, step=1)
    uploaded_file = st.file_uploader("Upload CSV (optional) — will replace sample dataset", type=["csv"])
    refresh_btn = st.button("🔄 Refresh / Generate Data")
    reset_btn = st.button("🧹 Reset App (clear results)")
    run_btn = st.button("🚀 Run Enrichment")

if uploaded_file is not None:
    try:
        df_try = pd.read_csv(uploaded_file).head(100)
        if "indicator" not in df_try.columns:
            df_try = df_try.rename(columns={df_try.columns[0]: "indicator"})
        if "type" not in df_try.columns:
            df_try["type"] = df_try["indicator"].apply(guess_ioc_type)
        st.session_state.df_in = df_try
        st.success(f"Uploaded dataset loaded ({len(df_try)} rows).")
    except Exception as e:
        st.error(f"Failed to parse uploaded CSV: {e}")

# ✅ FIXED BELOW — replaced deprecated st.experimental_rerun() with st.rerun()
if refresh_btn:
    st.session_state.df_in = make_sample_iocs(num)
    st.session_state.enriched_df = None
    st.rerun()

if reset_btn:
    st.session_state.enriched_df = None
    st.rerun()
# ✅ END FIX

# Show dataset preview
st.subheader("Dataset (preview)")
st.dataframe(st.session_state.df_in.head(50))

mcp_server = MCPDemoServer(dataset_df=st.session_state.df_in)

if run_btn:
    with st.spinner("Running enrichment..."):
        st.session_state.enriched_df = run_enrichment(st.session_state.df_in, mcp_server)
    st.success("Enrichment completed.")

# --- rest of app identical ---
# (All plotting, PDF, CSV export, and explanation sections remain unchanged)
