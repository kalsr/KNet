
# MCP_app_v1.py

# MCP_app.py — Enhanced Model Context Protocol Cyber IOC Enricher
# Author: Randeep Singh (Enhanced by ChatGPT)
# ----------------------------------------------------------------
# This Streamlit application simulates a mini MCP-style enrichment engine for
# Indicators of Compromise (IOCs). It can generate, enrich, visualize, and export
# results for up to 100 threat indicators. It uses a friendly color-themed UI,
# dynamic charts, and PDF/CSV export options.
# ----------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import random, datetime, io
from dateutil.relativedelta import relativedelta
from collections import Counter
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------------------
# Streamlit Page Configuration
# ---------------------------
st.set_page_config(page_title="MCP Cyber IOC Enricher", layout="wide")
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%);
    }
    .stButton>button {
        background: linear-gradient(135deg, #3B82F6, #06B6D4);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #2563EB, #0891B2);
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Helper Functions
# ---------------------------

def guess_ioc_type(indicator: str):
    """Guesses the IOC type (ip/domain/hash) based on format."""
    if indicator.count(".") == 3 and all(p.isdigit() for p in indicator.split(".")):
        return "ip"
    if "." in indicator:
        return "domain"
    return "hash"


def make_sample_iocs(n=25):
    """Generates n sample IOC records with mixed types and metadata."""
    n = min(max(1, int(n)), 100)
    samples = []
    base_date = datetime.date.today() - relativedelta(months=6)
    for i in range(n):
        kind = random.choices(["ip", "domain", "hash"], weights=[0.4, 0.4, 0.2])[0]
        if kind == "ip":
            indicator = ".".join(str(random.randint(1, 250)) for _ in range(4))
        elif kind == "domain":
            name = random.choice(["login", "secure", "update", "bank", "paypal", "office"])
            tld = random.choice(["com", "net", "org", "info"])
            indicator = f"{name}{random.randint(1,99)}.{tld}"
        else:
            indicator = ''.join(random.choice("abcdef0123456789") for _ in range(32))
        samples.append({
            "id": i + 1,
            "indicator": indicator,
            "type": guess_ioc_type(indicator),
            "source": random.choice(["internal-sensor", "talos", "user-report", "honeypot"]),
            "first_seen": (base_date + datetime.timedelta(days=random.randint(0, 180))).isoformat(),
            "notes": ""
        })
    return pd.DataFrame(samples)


# ---------------------------
# MCP Simulation Class
# ---------------------------
class MCPDemoServer:
    """Simulated MCP-style server that enriches IOC data heuristically."""

    def __init__(self, dataset_df=None):
        self.dataset_df = dataset_df.copy() if dataset_df is not None else pd.DataFrame()
        self.known_malicious = {
            "1.2.3.4": {"severity": "high", "confidence": 0.94, "tags": ["botnet", "malicious-ip"], "first_seen": "2025-01-10"},
            "bad.example[.]com": {"severity": "medium", "confidence": 0.7, "tags": ["phishing"], "first_seen": "2024-11-01"},
            "abcdef1234567890": {"severity": "high", "confidence": 0.98, "tags": ["malware-hash"], "first_seen": "2025-03-02"},
        }

    def enrich_ioc(self, indicator: str, ioc_type: str):
        """Main enrichment logic that returns severity, confidence, tags, and rationale."""
        indicator = str(indicator).strip()
        if indicator in self.known_malicious:
            base = self.known_malicious[indicator]
        elif ioc_type == "ip":
            base = self._simulate_ip(indicator)
        elif ioc_type == "domain":
            base = self._simulate_domain(indicator)
        else:
            base = self._simulate_hash(indicator)
        return {
            "indicator": indicator,
            "type": ioc_type,
            "severity": base["severity"],
            "confidence": round(float(base["confidence"]), 2),
            "related_tags": base["tags"],
            "first_seen": base.get("first_seen", datetime.date.today().isoformat()),
            "explain": base["explain"]
        }

    def _simulate_ip(self, ip):
        score = (sum(bytearray(ip.encode())) % 100) / 100
        if score > 0.85:
            return {"severity": "high", "confidence": 0.9, "tags": ["botnet"], "explain": f"IP heuristic high ({score:.2f})"}
        elif score > 0.5:
            return {"severity": "medium", "confidence": 0.7, "tags": ["suspicious"], "explain": f"IP heuristic medium ({score:.2f})"}
        else:
            return {"severity": "low", "confidence": 0.5, "tags": ["benign"], "explain": f"IP heuristic low ({score:.2f})"}

    def _simulate_domain(self, d):
        score = (sum(bytearray(d.encode())) % 90) / 100
        if score > 0.75:
            return {"severity": "high", "confidence": 0.88, "tags": ["phishing"], "explain": f"Domain risk high ({score:.2f})"}
        elif score > 0.45:
            return {"severity": "medium", "confidence": 0.7, "tags": ["suspicious"], "explain": f"Domain medium ({score:.2f})"}
        else:
            return {"severity": "low", "confidence": 0.4, "tags": ["benign"], "explain": f"Domain benign ({score:.2f})"}

    def _simulate_hash(self, h):
        score = (len(h) % 10) / 10
        if score > 0.6:
            return {"severity": "high", "confidence": 0.9, "tags": ["malware-hash"], "explain": f"Hash high ({score:.2f})"}
        else:
            return {"severity": "low", "confidence": 0.5, "tags": ["unknown"], "explain": f"Hash benign ({score:.2f})"}


# ---------------------------
# Data Processing
# ---------------------------

def run_enrichment(df, mcp_server):
    """Iterates over all IOC records and enriches them with severity and confidence."""
    enriched = []
    for _, row in df.iterrows():
        indicator, ioc_type = row["indicator"], row.get("type", guess_ioc_type(row["indicator"]))
        enr = mcp_server.enrich_ioc(indicator, ioc_type)
        enriched.append({
            **row,
            "severity": enr["severity"],
            "confidence": enr["confidence"],
            "related_tags": ",".join(enr["related_tags"]),
            "first_seen_enrich": enr["first_seen"],
            "explain": enr["explain"]
        })
    return pd.DataFrame(enriched)


# ---------------------------
# Main App GUI
# ---------------------------

st.title("🧠 Model Context Protocol (MCP) — Cyber IOC Enricher")
st.markdown("Upload or generate IOCs, enrich them with AI-driven reasoning, and visualize the results.")

num = st.sidebar.slider("Number of sample records", 5, 100, 25)
uploaded_file = st.sidebar.file_uploader("📂 Upload CSV (optional)", type=["csv"])
refresh = st.sidebar.button("🔄 Refresh / Generate Data")

if uploaded_file:
    df_in = pd.read_csv(uploaded_file).head(100)
else:
    df_in = make_sample_iocs(num)

if refresh:
    st.experimental_rerun()

mcp_server = MCPDemoServer(df_in)
if st.button("🚀 Run Enrichment", type="primary", use_container_width=True):
    enriched_df = run_enrichment(df_in, mcp_server)
    st.success("MCP enrichment completed successfully!")

    # --- Charts ---
    st.subheader("📊 Visualization Dashboard")

    # Severity Bar
    sev_counts = enriched_df["severity"].value_counts().reset_index(names=["count"]).rename(columns={"index": "severity"})
    fig_bar = px.bar(sev_counts, x="severity", y="count", color="severity",
                     color_discrete_map={"low": "#6EE7B7", "medium": "#FBBF24", "high": "#EF4444"},
                     title="🔍 Severity Distribution", text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

    # Type Pie
    type_counts = enriched_df["type"].value_counts().reset_index(names=["count"]).rename(columns={"index": "type"})
    fig_pie = px.pie(type_counts, names="type", values="count", title="🌐 IOC Type Breakdown",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

    # Tags Chart
    tags = Counter([t.strip() for sub in enriched_df["related_tags"].dropna() for t in sub.split(",") if t.strip()])
    tag_df = pd.DataFrame(tags.most_common(15), columns=["Tag", "Count"])
    fig_tags = px.bar(tag_df, x="Tag", y="Count", color="Count",
                      color_continuous_scale="Viridis", title="🏷️ Top 15 Related Tags", text_auto=True)
    st.plotly_chart(fig_tags, use_container_width=True)

    # --- Export Options ---
    csv_buf = io.StringIO()
    enriched_df.to_csv(csv_buf, index=False)

    st.download_button("📥 Download Enriched CSV", csv_buf.getvalue(), "enriched_iocs.csv", "text/csv")

    # --- Export PDF Charts ---
    pdf_buf = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buf, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    story.append(Paragraph("MCP Cyber IOC Enrichment Report", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("This report summarizes the enriched indicators and charts for severity and IOC types.", styles["BodyText"]))
    story.append(Spacer(1, 12))
    for fig, name in [(fig_bar, "severity_chart.png"), (fig_pie, "type_chart.png"), (fig_tags, "tags_chart.png")]:
        img_buf = io.BytesIO()
        fig.write_image(img_buf, format="png")
        img_buf.seek(0)
        story.append(Image(img_buf, width=450, height=300))
        story.append(Spacer(1, 20))
    doc.build(story)
    st.download_button("📄 Download PDF Report", data=pdf_buf.getvalue(), file_name="MCP_Report.pdf", mime="application/pdf")

else:
    st.info("Click **Run Enrichment** to process and visualize data.")
