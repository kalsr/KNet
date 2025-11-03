# ai_demo_working.py
# Fully functional single-file Streamlit app with 9 domains,
# reliable top navigation buttons, generate 0-100 records, upload,
# charts, audio/images, refresh/reset, CSV + PDF export.
# Uses sklearn small datasets and safe fallbacks.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import tempfile, os, io
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.feature_extraction.text import CountVectorizer
from scipy.io.wavfile import write
from PIL import Image, ImageDraw

# Optional: yfinance for stock data (not required)
try:
    import yfinance as yf
    YFINANCE = True
except Exception:
    YFINANCE = False

# ---------- Page config & styling ----------
st.set_page_config(page_title="MCP Agentic AI — Working Demo", layout="wide")

st.markdown("""
<style>
.header {text-align:center; color:#0b3d91; font-size:26px; font-weight:700; margin-bottom:4px;}
.sub {text-align:center; color:#556; font-size:13px; margin-bottom:14px;}
.top-buttons {display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-bottom:12px;}
.btn {padding:8px 12px; border-radius:8px; color:white; font-weight:700; border:none; cursor:pointer;}
.ml{background:#0d6efd;} .nlp{background:#198754;} .cv{background:#0dcaf0;} .sp{background:#ffc107;}
.rl{background:#6f42c1;} .dp{background:#20c997;} .mo{background:#d63384;} .ag{background:#fd7e14;} .mlops{background:#343a40;} .home{background:#0b5ed7;}
.card {background:white;padding:12px;border-radius:10px;box-shadow:0 6px 18px rgba(0,0,0,0.06); margin-bottom:12px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">MCP Agentic AI — Working Demo</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Click a domain button, generate or upload up to 100 rows, explore charts and export results.</div>', unsafe_allow_html=True)

# ---------- Domains definition ----------
DOMAINS = [
    ("🏠 Home", "home", "Overview & instructions"),
    ("1️⃣ Machine Learning", "ml", "Iris (local) and Titanic (remote if available)."),
    ("2️⃣ NLP & LLM", "nlp", "Text reviews / book descriptions — word frequency analysis."),
    ("3️⃣ Computer Vision", "cv", "Digits 8x8 from sklearn, thumbnails shown."),
    ("4️⃣ Speech & Audio", "sp", "Generate/play a demo tone or upload Time/Amplitude CSV."),
    ("5️⃣ Reinforcement Learning", "rl", "Simulated episodes & reward curves."),
    ("6️⃣ Data & Preprocessing", "dp", "Wine dataset for preprocessing/feature work."),
    ("7️⃣ Model Optimization", "mo", "Compression vs accuracy/latency tradeoffs."),
    ("8️⃣ Agentic AI", "ag", "Agent steps and execution times (or uploaded workflows)."),
    ("9️⃣ MLOps", "mlops", "Evaluation metrics: accuracy, precision, recall, F1.")
]

# ---------- session state defaults ----------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "n_records" not in st.session_state:
    st.session_state.n_records = 50

# ---------- Top navigation (reliable) ----------
cols = st.columns((1,1,1,1,1,1,1,1,1))
for i, (label, key, _) in enumerate(DOMAINS):
    cls = key if key != "home" else "home"
    if cols[i].button(label, key=key):
        st.session_state.page = key

# ---------- Helper functions ----------
TITANIC_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
BOOKS_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"

def safe_read_csv(url, n=None):
    try:
        df = pd.read_csv(url)
        return df.head(n) if n else df
    except Exception:
        return None

def export_pdf(df, title="MCP Report"):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)
    styles = getSampleStyleSheet()
    elems = [Paragraph(f"<para align='center'><font color='blue' size=14><b>{title}</b></font></para>", styles["Normal"]), Spacer(1,8)]
    # table with header + up to 100 rows
    data = [df.columns.tolist()] + df.head(100).astype(str).values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#cfe8ff")),
        ("GRID",(0,0),(-1,-1),0.25,colors.gray),
        ("ALIGN",(0,0),(-1,-1),"CENTER")
    ]))
    elems.append(table)
    doc.build(elems)
    return buf.getvalue()

def show_scatter(df):
    numcols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numcols) >= 2:
        x = st.selectbox("X-axis", numcols, key="x_"+st.session_state.page)
        y = st.selectbox("Y-axis", numcols, index=1 if len(numcols)>1 else 0, key="y_"+st.session_state.page)
        fig, ax = plt.subplots()
        ax.scatter(df[x], df[y], c="#0d6efd", edgecolors="k")
        ax.set_xlabel(x); ax.set_ylabel(y); ax.set_title(f"{x} vs {y}")
        st.pyplot(fig)

def show_pie(df):
    catcols = df.select_dtypes(include=['object','category']).columns.tolist()
    if catcols:
        col = catcols[0]
        counts = df[col].fillna("N/A").value_counts().reset_index(name="count").rename(columns={"index":col})
        fig, ax = plt.subplots()
        counts.set_index(col)["count"].plot.pie(autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

def text_freq(df, hint=None):
    text_col = None
    if hint and hint in df.columns: text_col = hint
    else:
        for c in df.columns:
            if "review" in c.lower() or "text" in c.lower() or "description" in c.lower(): text_col = c; break
    if text_col:
        vec = CountVectorizer(stop_words="english")
        X = vec.fit_transform(df[text_col].astype(str))
        freq = pd.DataFrame({"word": vec.get_feature_names_out(), "count": np.array(X.sum(axis=0)).flatten()})
        freq = freq.sort_values("count", ascending=False).head(15)
        fig, ax = plt.subplots(figsize=(6,3))
        ax.bar(freq["word"], freq["count"], color="#198754")
        plt.xticks(rotation=45)
        ax.set_title("Top words")
        st.pyplot(fig)

# ---------- Controls common to every page ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
left, middle, right = st.columns(3)
with left:
    n = st.number_input("Generate records (0–100)", min_value=0, max_value=100, value=st.session_state.n_records, key="n_input")
    st.session_state.n_records = n
with middle:
    upload = st.file_uploader("Upload CSV / XLSX / JSON (optional)", type=["csv","xlsx","json"])
with right:
    if st.button("🔁 Refresh / Regenerate"):
        # keep same page, just rerun so generators re-run
        st.experimental_rerun()
    if st.button("🧹 Reset App (clear)"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.experimental_rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Page logic ----------
page = st.session_state.page

if page == "home":
    st.header("Welcome — how to use this demo")
    st.write("""
    * Click a colored domain button above to select a demo.
    * Generate 0–100 sample records (enter number) or upload your own CSV/XLSX/JSON.
    * Use **Refresh** to regenerate, **Reset** to clear session.
    * Each domain shows a preview, charts, and export buttons.
    """)
    st.info("This app uses sklearn small datasets and public CSVs when available, with safe offline fallbacks.")

# 1. Machine Learning
elif page == "ml":
    st.header("Machine Learning — Iris & Titanic")
    st.write("Iris: classic classification dataset (petal/sepal). Titanic: passenger records showing survival outcomes (remote fetch may fail behind firewalls).")
    df = None
    if upload:
        try:
            if upload.name.endswith(".csv"): df = pd.read_csv(upload)
            elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
            else: df = pd.read_json(upload)
            st.success(f"Loaded upload: {upload.name}")
        except Exception as e:
            st.error(f"Upload error: {e}")
    if df is None:
        iris = load_iris(as_frame=True).frame
        # try Titanic
        try:
            tit = pd.read_csv(TITANIC_URL).head(st.session_state.n_records)
        except Exception:
            tit = None
        choice = st.radio("Dataset", ("Iris (local)", "Titanic (remote/fallback)"))
        if choice.startswith("Iris"):
            df = iris.head(n if n>0 else 0)
        else:
            df = tit if tit is not None else iris.head(n if n>0 else 0)
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    show_pie(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "ml_results.csv", "text/csv")
    st.download_button("📄 Download PDF (first 100 rows)", data=export_pdf(df, "ML Domain Report"), file_name="ml_report.pdf", mime="application/pdf")

# 2. NLP
elif page == "nlp":
    st.header("NLP & LLM — Text reviews / book descriptions")
    st.write("Generates reviews or uses a books CSV (remote) to demonstrate word frequencies and simple text analytics.")
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
        try:
            books = pd.read_csv(BOOKS_URL)
            if "description" in books.columns:
                df = books[["title","authors","description"]].rename(columns={"description":"Review"}).head(n if n>0 else 0)
            else:
                df = pd.DataFrame({"Review":[ "An engaging narrative." for _ in range(n if n>0 else 0) ]})
        except Exception:
            sample_texts = ["Great movie", "Not for me", "Excellent writing", "Slow plot"]
            df = pd.DataFrame({"Review":[ random.choice(sample_texts) for _ in range(n if n>0 else 0) ]})
    st.subheader("Preview")
    st.dataframe(df.head(100))
    text_freq(df, hint="Review")
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "nlp_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "NLP Domain Report"), file_name="nlp_report.pdf", mime="application/pdf")

# 3. Computer Vision
elif page == "cv":
    st.header("Computer Vision — Digits (8x8)")
    st.write("Displays up to 100 small digit images (8x8) for basic CV demos.")
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
        # show grid
        st.subheader("Sample images (first 25)")
        cols_grid = st.columns(5)
        for i, img in enumerate(imgs[:25]):
            cols_grid[i%5].image(img, width=64)
        df = pd.DataFrame(digits.data[:n if n>0 else 0])
        df["label"] = labels
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "cv_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "CV Domain Report"), file_name="cv_report.pdf", mime="application/pdf")

# 4. Speech & Audio
elif page == "sp":
    st.header("Speech & Audio — Tone demo or uploaded audio CSV")
    st.write("Play a generated tone or upload a CSV with Time and Amplitude columns to play audio.")
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
        # create 1s sine tone and show first 100 samples
        rate = 44100
        dur = 1.0
        t = np.linspace(0, dur, int(rate*dur), False)
        tone = 0.3 * np.sin(2*np.pi*440*t)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(tmp.name, rate, (tone*32767).astype("int16"))
        st.audio(tmp.name)
        os.unlink(tmp.name)
        df = pd.DataFrame({"Time": t[:100], "Amplitude": tone[:100]})
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "speech_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "Speech Domain Report"), file_name="speech_report.pdf", mime="application/pdf")

# 5. Reinforcement Learning
elif page == "rl":
    st.header("Reinforcement Learning — Reward simulation")
    st.write("Simulated episodes and cumulative rewards.")
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
        episodes = np.arange(1, (n if n>0 else 1)+1)
        rewards = np.cumsum(np.random.randn(len(episodes))*1.5 + 5)
        df = pd.DataFrame({"Episode": episodes, "Reward": rewards})
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "rl_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "RL Domain Report"), file_name="rl_report.pdf", mime="application/pdf")

# 6. Data & Preprocessing
elif page == "dp":
    st.header("Data & Preprocessing — Wine dataset")
    st.write("Wine chemical composition dataset suitable for preprocessing demonstrations.")
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
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "dp_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "DataPrep Domain Report"), file_name="dp_report.pdf", mime="application/pdf")

# 7. Model Optimization
elif page == "mo":
    st.header("Model Optimization — Compression vs Accuracy")
    st.write("Simulated compression percent vs accuracy and latency to illustrate tradeoffs.")
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
        acc = np.clip(100 - pct*0.3 + np.random.randn(len(pct))*0.5, 50, 100)
        lat = np.linspace(10, 350, len(pct))
        df = pd.DataFrame({"Compression (%)": pct, "Accuracy": acc, "Latency (ms)": lat})
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "mo_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "ModelOpt Domain Report"), file_name="mo_report.pdf", mime="application/pdf")

# 8. Agentic AI
elif page == "ag":
    st.header("Agentic AI & Workflow Orchestration")
    st.write("Shows example multi-step agent pipelines and execution timings.")
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
        rows = [{"Step": random.choice(steps), "Execution Time (s)": round(random.uniform(0.05, 2.0),3)} for _ in range(n if n>0 else 0)]
        df = pd.DataFrame(rows)
    st.subheader("Preview")
    st.dataframe(df.head(100))
    show_scatter(df)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "ag_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "Agentic Domain Report"), file_name="ag_report.pdf", mime="application/pdf")

# 9. MLOps
elif page == "mlops":
    st.header("MLOps & Evaluation")
    st.write("Standard evaluation metrics (accuracy, precision, recall, F1) shown as a small table/plot.")
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
        metrics = ["Accuracy","Precision","Recall","F1 Score"]
        values = [round(random.uniform(0.7,0.99),3) for _ in metrics]
        df = pd.DataFrame({"Metric": metrics, "Value": values})
    st.subheader("Preview")
    st.dataframe(df.head(100))
    # simple bar chart
    fig, ax = plt.subplots()
    ax.bar(df["Metric"], df["Value"], color="#343a40")
    ax.set_ylim(0,1)
    ax.set_title("Evaluation Metrics")
    st.pyplot(fig)
    st.markdown("### Export")
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "mlops_results.csv", "text/csv")
    st.download_button("📄 Download PDF", data=export_pdf(df, "MLOps Domain Report"), file_name="mlops_report.pdf", mime="application/pdf")

else:
    st.error("Unknown page. Use top buttons to select a domain.")

# ---------- End ----------
