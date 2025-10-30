# MCP_app_v3.py


# MCP_app_fixed.py
# Complete fixed & enhanced MCP Cyber IOC Enricher
# Fixes: narwhals DuplicateError, robust PDF fallback, upload limit, refresh/reset, UI polish
#
# Run: streamlit run MCP_app_fixed.py

import streamlit as st
import pandas as pd
import plotly.express as px
import random
import datetime
import io
import zipfile
from dateutil.relativedelta import relativedelta
from collections import Counter

# Optional libs for PDF generation (may not be available in all runtimes)
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
    """Guess IOC type: 'ip', 'domain', or 'hash' based on simple heuristics."""
    s = str(indicator)
    if s.count(".") == 3 and all(p.isdigit() for p in s.split(".")):
        return "ip"
    if "." in s:
        return "domain"
    return "hash"


def make_sample_iocs(n=25) -> pd.DataFrame:
    """Return a DataFrame with n sample IOC records (max 100)."""
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
    """
    Demo in-process MCP-like server that enriches one IOC at a time.
    Returns: severity, confidence, related tags, first_seen, and an explain string.
    """
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
    """
    Enrich every row of df and return a new DataFrame with added columns:
    severity, confidence, related_tags (comma-joined), first_seen_enrich, explain.
    """
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
# Session state helpers
# -------------------------
if "df_in" not in st.session_state:
    st.session_state.df_in = make_sample_iocs(25)
if "enriched_df" not in st.session_state:
    st.session_state.enriched_df = None

# -------------------------
# Controls (sidebar)
# -------------------------
with st.sidebar:
    st.header("Controls")
    num = st.slider("Number of sample records (when generating)", min_value=5, max_value=100, value=25, step=1)
    uploaded_file = st.file_uploader("Upload CSV (optional) — will replace sample dataset", type=["csv"])
    refresh_btn = st.button("🔄 Refresh / Generate Data")
    reset_btn = st.button("🧹 Reset App (clear results)")
    run_btn = st.button("🚀 Run Enrichment")

# Handle upload
if uploaded_file is not None:
    try:
        df_try = pd.read_csv(uploaded_file).head(100)
        # ensure indicator column
        if "indicator" not in df_try.columns:
            df_try = df_try.rename(columns={df_try.columns[0]: "indicator"})
        if "type" not in df_try.columns:
            df_try["type"] = df_try["indicator"].apply(guess_ioc_type)
        st.session_state.df_in = df_try
        st.success(f"Uploaded dataset loaded ({len(df_try)} rows, truncated to 100 if longer).")
    except Exception as e:
        st.error(f"Failed to parse uploaded CSV: {e}")

# Refresh -> generate new sample set
if refresh_btn:
    st.session_state.df_in = make_sample_iocs(num)
    st.session_state.enriched_df = None
    st.experimental_rerun()

# Reset -> clear enrichment results and uploaded file reference
if reset_btn:
    st.session_state.enriched_df = None
    st.experimental_rerun()

# Show dataset preview
st.subheader("Dataset (preview)")
st.dataframe(st.session_state.df_in.head(50))

# Create demo MCP server instance
mcp_server = MCPDemoServer(dataset_df=st.session_state.df_in)

# Run enrichment on button press
if run_btn:
    with st.spinner("Running enrichment..."):
        st.session_state.enriched_df = run_enrichment(st.session_state.df_in, mcp_server)
    st.success("Enrichment completed.")

# If enriched, show results & charts
if st.session_state.enriched_df is not None:
    enriched_df = st.session_state.enriched_df.copy()
    st.subheader("Enrichment results (first 100 rows)")
    st.dataframe(enriched_df.head(100))

    # Explanation of functions (visible in UI)
    st.markdown("### What each function does (short explanation)")
    st.markdown(
        """
        - `make_sample_iocs(n)`: generates sample IOCs (ips/domains/hashes) up to 100 rows.
        - `MCPDemoServer.enrich_ioc(...)`: demo enrichment logic returning severity, confidence, tags, explain.
        - `run_enrichment(df, mcp_server)`: calls the server for each row and appends enrichment columns.
        - Charts & Export: interactive visualizations and downloadable CSV/PDF/PNG.
        """
    )

    # -------------------------
    # Charts
    # -------------------------
    st.subheader("Charts")

    # --- Severity counts safe (fixes DuplicateError) ---
    # Use Series.reset_index(name='count') to get columns ['index','count'] then rename index->severity
    sev_counts = enriched_df["severity"].value_counts().reset_index(name="count").rename(columns={"index": "severity"})
    fig_bar = px.bar(
        sev_counts,
        x="severity", y="count",
        title="🔍 Severity distribution",
        color="severity",
        color_discrete_map={"low":"#6EE7B7","medium":"#FBBF24","high":"#EF4444"},
        text_auto=True
    )
    fig_bar.update_layout(template="plotly_white", title_font=dict(size=18))

    # --- Type pie (safe reset) ---
    type_counts = enriched_df["type"].fillna("unknown").value_counts().reset_index(name="count").rename(columns={"index":"type"})
    fig_pie = px.pie(type_counts, names="type", values="count", title="🌐 Indicator type breakdown",
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_pie.update_traces(textposition="inside", textinfo="percent+label")

    # --- Top tags ---
    tag_series = enriched_df["related_tags"].dropna().apply(lambda s: [x.strip() for x in s.split(",") if x.strip()])
    c = Counter()
    for row in tag_series:
        c.update(row)
    top_tags = pd.DataFrame(c.most_common(15), columns=["tag","count"])
    fig_tags = None
    if not top_tags.empty:
        fig_tags = px.bar(top_tags, x="tag", y="count", title="🏷️ Top related tags", text_auto=True)
        fig_tags.update_layout(template="plotly_white", xaxis_tickangle=-45)

    # Display Plotly charts
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_pie, use_container_width=True)
    if fig_tags is not None:
        st.plotly_chart(fig_tags, use_container_width=True)
    else:
        st.write("No tags found.")

    # -------------------------
    # Export: CSV + PDF (with fallbacks)
    # -------------------------
    st.subheader("Export")

    # CSV export
    csv_buf = io.StringIO()
    enriched_df.to_csv(csv_buf, index=False)
    st.download_button("📥 Download enriched CSV", csv_buf.getvalue(), file_name="enriched_iocs.csv", mime="text/csv")

    # Build PNG images for charts robustly (Plotly -> png, fallback to matplotlib)
    chart_images = []  # list of tuples (name, bytes)

    def fig_to_png_bytes(fig):
        """
        Try Plotly figure to_image (kaleido). If it fails, raise.
        Caller will attempt matplotlib fallback.
        """
        try:
            # plotly's to_image may require 'kaleido' or 'orca' installed in environment.
            return fig.to_image(format="png")
        except Exception:
            raise

    def matplotlib_fallback_png(df_counts, kind="bar", title=None):
        """Simple matplotlib fallback to generate PNG bytes from a small dataframe."""
        try:
            import matplotlib.pyplot as plt
            buf = io.BytesIO()
            plt.figure(figsize=(6,4))
            if kind == "bar":
                plt.bar(df_counts.iloc[:,0].astype(str), df_counts.iloc[:,1])
                plt.title(title or "")
                plt.xticks(rotation=45, ha="right")
            elif kind == "pie":
                plt.pie(df_counts.iloc[:,1], labels=df_counts.iloc[:,0], autopct="%1.1f%%")
                plt.title(title or "")
            plt.tight_layout()
            plt.savefig(buf, format="png", dpi=150)
            plt.close()
            buf.seek(0)
            return buf.read()
        except Exception:
            return None

    # severity image
    try:
        chart_images.append(("severity.png", fig_to_png_bytes(fig_bar)))
    except Exception:
        pm = matplotlib_fallback_png(sev_counts, kind="bar", title="Severity distribution")
        if pm:
            chart_images.append(("severity.png", pm))

    # type image
    try:
        chart_images.append(("types.png", fig_to_png_bytes(fig_pie)))
    except Exception:
        pm = matplotlib_fallback_png(type_counts, kind="pie", title="Indicator type breakdown")
        if pm:
            chart_images.append(("types.png", pm))

    # tags image
    if fig_tags is not None:
        try:
            chart_images.append(("tags.png", fig_to_png_bytes(fig_tags)))
        except Exception:
            if not top_tags.empty:
                pm = matplotlib_fallback_png(top_tags, kind="bar", title="Top related tags")
                if pm:
                    chart_images.append(("tags.png", pm))

    # If we couldn't make images and Pillow is available, make a placeholder
    if not chart_images:
        if PIL_AVAILABLE:
            try:
                from PIL import Image, ImageDraw, ImageFont
                img = Image.new("RGB", (800,400), color=(252,252,252))
                d = ImageDraw.Draw(img)
                text = "MCP Report — no charts available to render in this environment"
                try:
                    fnt = ImageFont.truetype("arial.ttf", 18)
                except Exception:
                    fnt = None
                d.text((20,40), text, fill=(30,30,30), font=fnt)
                b = io.BytesIO()
                img.save(b, format="PNG")
                b.seek(0)
                chart_images.append(("placeholder.png", b.read()))
            except Exception:
                pass

    # Attempt PDF generation (reportlab preferred -> Pillow fallback -> ZIP)
    pdf_bytes = None
    if chart_images:
        # ReportLab path
        if REPORTLAB_AVAILABLE:
            try:
                pdf_buf = io.BytesIO()
                doc = SimpleDocTemplate(pdf_buf, pagesize=letter)
                story = []
                styles = getSampleStyleSheet()
                story.append(Paragraph("MCP Cyber IOC Enrichment Report", styles["Title"]))
                story.append(Spacer(1, 8))
                story.append(Paragraph(f"Generated: {datetime.datetime.utcnow().isoformat()}Z", styles["Normal"]))
                story.append(Spacer(1, 12))
                for name, b in chart_images:
                    img_buf = io.BytesIO(b)
                    # width,height chosen for report layout
                    story.append(RLImage(img_buf, width=450, height=300))
                    story.append(Spacer(1, 12))
                doc.build(story)
                pdf_buf.seek(0)
                pdf_bytes = pdf_buf.read()
            except Exception:
                pdf_bytes = None

        # Pillow fallback: multi-page PDF (if PIL available)
        if pdf_bytes is None and PIL_AVAILABLE:
            try:
                pil_images = []
                for name, b in chart_images:
                    im = PILImage.open(io.BytesIO(b))
                    if im.mode in ("RGBA","LA"):
                        im = im.convert("RGB")
                    pil_images.append(im)
                out_buf = io.BytesIO()
                if len(pil_images) == 1:
                    pil_images[0].save(out_buf, format="PDF")
                else:
                    pil_images[0].save(out_buf, format="PDF", save_all=True, append_images=pil_images[1:])
                out_buf.seek(0)
                pdf_bytes = out_buf.read()
            except Exception:
                pdf_bytes = None

    # Present export option(s)
    if pdf_bytes:
        st.download_button("📄 Download PDF Report (charts)", data=pdf_bytes, file_name="MCP_Report.pdf", mime="application/pdf")
    else:
        if chart_images:
            zip_buf = io.BytesIO()
            with zipfile.ZipFile(zip_buf, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
                for name, b in chart_images:
                    zf.writestr(name, b)
            zip_buf.seek(0)
            st.download_button("🗜️ Download charts (ZIP of PNGs)", data=zip_buf.getvalue(), file_name="MCP_charts.zip", mime="application/zip")
            st.warning("PDF export not available. A ZIP of PNG charts is provided instead.")
        else:
            st.error("Unable to produce chart images for export in this runtime. CSV download above is available.")

    # show top tags table
    st.subheader("Top related tags (table)")
    if not top_tags.empty:
        st.table(top_tags)
    else:
        st.write("No tags found.")

else:
    st.info("Click **Run Enrichment** in the sidebar to enrich and visualize data.")

# -------------------------
# End of app
# -------------------------
