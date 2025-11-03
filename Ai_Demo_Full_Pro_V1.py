

# ai_demo_final.py
# Complete MCP Agentic AI demo — real-data + uploads + charts + exports + refresh/reset
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random, io, tempfile, os
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.feature_extraction.text import CountVectorizer
from scipy.io.wavfile import write
from PIL import Image, ImageDraw

# ---------------- Page config & CSS ----------------
st.set_page_config(page_title="MCP Agentic AI — Demo (Final)", layout="wide")
st.markdown("""
<style>
body {background:#f6fbff;}
.header {text-align:center; color:#003366; font-size:28px; font-weight:700; margin-bottom:4px;}
.sub {text-align:center; color:#5b6b7a; font-size:13px; margin-bottom:18px;}
.nav{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-bottom:12px;}
.btn{border:none;padding:8px 14px;border-radius:8px;color:white;font-weight:700;cursor:pointer}
.ml{background:#0d6efd;} .nlp{background:#198754;} .cv{background:#0dcaf0;} .sp{background:#ffc107;}
.rl{background:#6f42c1;} .dp{background:#20c997;} .mo{background:#d63384;} .ag{background:#fd7e14;} .mlops{background:#343a40;} .home{background:#0b5ed7;}
.card {background:white;padding:10px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.06);margin-bottom:12px;}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="header">MCP Agentic AI — Demo Platform (Final)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Real-world sample data, uploads (CSV/XLSX/JSON), charts, audio/images, PDF & CSV export</div>', unsafe_allow_html=True)

# ---------------- Navigation ----------------
MENU = [
    ("🏠 Home", "home", "home"),
    ("1️⃣ Machine Learning", "ml", "Machine Learning & real-world tabular data (Iris/Titanic). Useful for classification demos."),
    ("2️⃣ NLP & LLM", "nlp", "NLP demos: review text, word frequency, and basic text analytics."),
    ("3️⃣ Computer Vision", "cv", "Computer vision demos: digits / small image thumbnails to inspect."),
    ("4️⃣ Speech & Audio", "sp", "Audio demo: generate or upload audio, play and inspect waveform samples."),
    ("5️⃣ Reinforcement Learning", "rl", "Reward-series simulations for episodic RL visualization."),
    ("6️⃣ Data & Preprocessing", "dp", "Data cleaning / preprocessing examples using Wine dataset samples."),
    ("7️⃣ Model Optimization", "mo", "Compression vs accuracy tradeoff examples (synthetic but realistic)."),
    ("8️⃣ Agentic AI", "ag", "Agentic workflow steps and execution timing examples."),
    ("9️⃣ MLOps & Evaluation", "mlops", "Common MLOps metrics (accuracy, precision, recall, F1).")
]

# top nav buttons
nav_html = "<div class='nav'>"
for label, key, _ in MENU:
    cls = key if key in ["ml","nlp","cv","sp","rl","dp","mo","ag","mlops"] else "home"
    nav_html += f"<form action='?page={key}' method='get' style='display:inline'><button class='btn {cls}'>{label}</button></form>"
nav_html += "</div>"
st.markdown(nav_html, unsafe_allow_html=True)

# detect page
query = st.experimental_get_query_params()
page = query.get("page", ["home"])[0]

# ---------------- Utilities & explanations ----------------
def get_explanation(key):
    for label, k, expl in MENU:
        if k == key:
            return expl
    return "Select a domain."

def safe_fetch_csv(url, n=None):
    try:
        df = pd.read_csv(url)
        return df.head(n) if n else df
    except Exception:
        return None

# sample external resources (may fail behind firewall)
TITANIC_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
BOOKS_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"

# ---------------- PDF export helper ----------------
def export_pdf_from_df(df, title="MCP Report"):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)
    styles = getSampleStyleSheet()
    elems = [Paragraph(f"<para align='center'><font color='blue' size=14><b>{title}</b></font></para>", styles["Normal"]), Spacer(1,10)]
    # table header + rows (first 100)
    data = [df.columns.tolist()] + df.head(100).astype(str).values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), colors.HexColor("#cfe8ff")),
        ("GRID",(0,0),(-1,-1), 0.25, colors.grey),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ]))
    elems.append(table)
    doc.build(elems)
    return buf.getvalue()

# ---------------- Page common controls ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write(f"**Selected:** {page.upper()} — {get_explanation(page)}")
col1, col2, col3 = st.columns([1,1,1])
with col1:
    n = st.number_input("Generate sample records (0–100)", min_value=0, max_value=100, value=50, step=1)
with col2:
    upload = st.file_uploader("Upload CSV / Excel / JSON (takes precedence)", type=["csv","xlsx","json"])
with col3:
    if st.button("🔁 Refresh / Regenerate"):
        st.experimental_set_query_params(page=page)
        st.rerun()
    if st.button("🧹 Reset App (clear session)"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.experimental_set_query_params(page="home")
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Page logic ----------------

def show_table_and_charts(df, text_col_hint=None):
    st.subheader("Data preview")
    st.dataframe(df.head(100), use_container_width=True)

    # numeric columns scatter
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(num_cols) >= 2:
        st.markdown("### Scatter plot")
        c1, c2 = st.columns(2)
        with c1:
            xcol = st.selectbox("X axis", num_cols, key="xcol")
        with c2:
            ycol = st.selectbox("Y axis", num_cols, index=1 if len(num_cols)>1 else 0, key="ycol")
        fig, ax = plt.subplots()
        ax.scatter(df[xcol], df[ycol], c="#0d6efd", edgecolors="k")
        ax.set_xlabel(xcol); ax.set_ylabel(ycol); ax.set_title(f"{xcol} vs {ycol}")
        st.pyplot(fig)

    # categorical pie if exists
    cat_cols = df.select_dtypes(include=['object','category']).columns.tolist()
    if cat_cols:
        st.markdown("### Distribution (first categorical column)")
        col = cat_cols[0]
        # safe counts dataframe for plotly compatibility
        counts = df[col].fillna("N/A").value_counts().reset_index(name="count").rename(columns={"index":col})
        fig2, ax2 = plt.subplots()
        counts.set_index(col)["count"].plot.pie(autopct="%1.1f%%", ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)

    # text top words
    if (text_col_hint and text_col_hint in df.columns) or ("review" in (c.lower() for c in df.columns)):
        text_col = text_col_hint if text_col_hint and text_col_hint in df.columns else next((c for c in df.columns if "review" in c.lower() or "text" in c.lower() or "description" in c.lower()), None)
        if text_col:
            st.markdown("### Top words (text analysis)")
            vec = CountVectorizer(stop_words="english")
            X = vec.fit_transform(df[text_col].astype(str))
            freq = pd.DataFrame({"word": vec.get_feature_names_out(), "count": np.array(X.sum(axis=0)).flatten()})
            freq = freq.sort_values("count", ascending=False).head(15)
            fig3, ax3 = plt.subplots(figsize=(6,3))
            ax3.bar(freq["word"], freq["count"], color="#198754")
            ax3.set_title("Top words")
            plt.xticks(rotation=45)
            st.pyplot(fig3)

# ---------------- Domain implementations ----------------
if page == "home":
    st.header("Welcome to the MCP Agentic AI Demo")
    st.write("Use the colored buttons at the top to pick a domain. Generate realistic sample rows (0-100), upload your own CSV/XLSX/JSON file, visualize, and export CSV or a color-themed PDF.")
    st.info("This demo uses small public datasets where possible and robust fallbacks so it runs offline.")

# 1. ML domain (Iris + Titanic)
elif page == "ml":
    st.header("Machine Learning — Iris & Titanic")
    st.markdown("**What this is:** Iris shows a classic classification dataset (sepal/petal measures); Titanic (when fetchable) shows passenger demographics/outcomes useful for applied modeling.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded uploaded file: {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        # load Iris always locally
        iris = load_iris(as_frame=True).frame
        # try Titanic
        tit = safe_fetch_csv(TITANIC_URL)
        choice = st.radio("Choose dataset", ("Iris (local)", "Titanic (remote if available)"))
        if choice.startswith("Iris"):
            df = iris.head(n if n>0 else 0)
        else:
            if tit is not None:
                df = tit.head(n if n>0 else 0)
            else:
                st.warning("Titanic dataset fetch failed — showing Iris instead.")
                df = iris.head(n if n>0 else 0)
    show_table_and_charts(df)
    # export
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "ml_results.csv", "text/csv")
    st.download_button("📄 Download PDF (first 100 rows)", data=export_pdf_from_df(df, "ML Domain Report"), file_name="ml_report.pdf", mime="application/pdf")

# 2. NLP & LLM
elif page == "nlp":
    st.header("NLP & LLM — Reviews / Books")
    st.markdown("**What this is:** Short review or book description text used to demonstrate token frequency, top words, and basic text analytics.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        books = safe_fetch_csv(BOOKS_URL)
        if books is not None and "description" in books.columns:
            df = books[["title","authors","description"]].rename(columns={"description":"Review"}).head(n if n>0 else 0)
        else:
            sample_texts = [
                "An exciting and moving story about hope.",
                "A technical guide to modern machine learning applications.",
                "A delightful read with strong characters and plot.",
                "Underwhelming; pacing was slow and predictable."
            ]
            df = pd.DataFrame({"Review":[random.choice(sample_texts) for _ in range(n if n>0 else 0)]})
    show_table_and_charts(df, text_col_hint="Review")
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "nlp_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "NLP Domain Report"), file_name="nlp_report.pdf", mime="application/pdf")

# 3. Computer Vision
elif page == "cv":
    st.header("Computer Vision — Digits (8x8 samples)")
    st.markdown("**What this is:** Small handwritten digits (8x8) from sklearn for quick CV demos; image thumbnails shown.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        digits = load_digits()
        imgs = digits.images[:n if n>0 else 0]
        labels = digits.target[:n if n>0 else 0]
        # show grid of up to 25
        st.subheader("Sample images (first 25)")
        cols = st.columns(5)
        for i, img in enumerate(imgs[:25]):
            cols[i%5].image(img, width=72)
        # build df with flattened features and label
        df = pd.DataFrame(digits.data[:n if n>0 else 0])
        df["label"] = labels
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "cv_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "CV Domain Report"), file_name="cv_report.pdf", mime="application/pdf")

# 4. Speech & Audio
elif page == "sp":
    st.header("Speech & Audio — Tone demo or upload audio CSV")
    st.markdown("**What this is:** Demo tone (sine) generated and playable; you may upload CSV with Time/Amplitude columns to play audio.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
            if {"Time","Amplitude"}.issubset(df.columns):
                arr = (df["Amplitude"].values * 32767).astype("int16")
                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                write(tmp.name, 44100, arr)
                st.audio(tmp.name)
                os.unlink(tmp.name)
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        duration = 1.0
        rate = 44100
        t = np.linspace(0, duration, int(rate*duration), False)
        tone = 0.3 * np.sin(2*np.pi*440*t)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(tmp.name, rate, (tone*32767).astype("int16"))
        st.audio(tmp.name)
        os.unlink(tmp.name)
        df = pd.DataFrame({"Time": t[:min(100,len(t))], "Amplitude": tone[:min(100,len(t))]})
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "speech_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "Speech Domain Report"), file_name="speech_report.pdf", mime="application/pdf")

# 5. Reinforcement Learning
elif page == "rl":
    st.header("Reinforcement Learning — Reward simulation")
    st.markdown("**What this is:** Simulated episodic rewards to demonstrate reward curves and episodic analysis.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        episodes = np.arange(1, n+1)
        rewards = np.cumsum(np.random.randn(max(1,n)) * 1.5 + 5)
        df = pd.DataFrame({"Episode": episodes[:len(rewards)], "Reward": rewards})
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "rl_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "RL Domain Report"), file_name="rl_report.pdf", mime="application/pdf")

# 6. Data & Preprocessing (Wine)
elif page == "dp":
    st.header("Data & Preprocessing — Wine dataset")
    st.markdown("**What this is:** Wine chemical composition dataset for preprocessing and feature analysis demos.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        df = load_wine(as_frame=True).frame.head(n if n>0 else 0)
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "dp_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "DataPrep Domain Report"), file_name="dp_report.pdf", mime="application/pdf")

# 7. Model Optimization
elif page == "mo":
    st.header("Model Optimization — Compression vs Accuracy")
    st.markdown("**What this is:** Simulated compression vs accuracy tradeoffs to illustrate how aggressive compression affects model accuracy/latency.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        pct = np.linspace(0, 90, n if n>0 else 0)
        acc = np.clip(100 - pct * 0.3 + np.random.randn(len(pct))*0.5, 50, 100)
        lat = np.linspace(10, 200, len(pct))
        df = pd.DataFrame({"Compression (%)": pct, "Accuracy": acc, "Latency (ms)": lat})
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "mo_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "ModelOpt Domain Report"), file_name="mo_report.pdf", mime="application/pdf")

# 8. Agentic AI
elif page == "ag":
    st.header("Agentic AI & Workflow Orchestration")
    st.markdown("**What this is:** Example agentic workflow steps and execution timings to illustrate orchestration and multi-step pipelines.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        steps = ["Collect Data", "Analyze Input", "Call Model", "Generate Output", "Refine Result"]
        rows = []
        for i in range(n if n>0 else 0):
            step = random.choice(steps)
            rows.append({"Step": step, "Execution Time (s)": round(random.uniform(0.05, 2.0), 3)})
        df = pd.DataFrame(rows)
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "agentic_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "Agentic Domain Report"), file_name="ag_report.pdf", mime="application/pdf")

# 9. MLOps
elif page == "mlops":
    st.header("MLOps & Evaluation")
    st.markdown("**What this is:** Standard MLOps metrics to inspect model evaluation summaries in dashboards.")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded {upload.name}")
        except Exception as e:
            st.error(f"Upload failed: {e}")
    if df is None:
        metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
        values = [round(random.uniform(0.7, 0.99), 3) for _ in metrics]
        df = pd.DataFrame({"Metric": metrics, "Value": values})
    show_table_and_charts(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "mlops_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf_from_df(df, "MLOps Domain Report"), file_name="mlops_report.pdf", mime="application/pdf")

else:
    st.write("Page not found — use the top buttons to choose a domain.")

# ---------------- End ----------------
