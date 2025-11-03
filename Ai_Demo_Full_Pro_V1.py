

# mcp_ai_realdata_v1.py
# Real-data enhanced MCP AI demo with Titanic, Digits, Books, Stocks, etc.
# Run: streamlit run mcp_ai_realdata_v1.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random, tempfile, os, io
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.feature_extraction.text import CountVectorizer
from scipy.io.wavfile import write
from PIL import Image, ImageDraw

# try yfinance for stock data (optional)
try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except Exception:
    YFINANCE_AVAILABLE = False

# ---------------- Page config & CSS ----------------
st.set_page_config(page_title="MCP AI — Real Data Demo", layout="wide")
st.markdown("""
<style>
body {background:#f6fbff;}
.title {text-align:center; color:#003366; font-size:28px; font-weight:700;}
.subtitle {text-align:center; color:#666; font-size:14px; margin-bottom:12px;}
.nav {display:flex; justify-content:center; gap:8px; flex-wrap:wrap; margin-bottom:10px;}
.btn {padding:8px 14px; border-radius:8px; color:white; font-weight:700; border:none; cursor:pointer;}
.ml{background:#0d6efd;} .nlp{background:#198754;} .cv{background:#0dcaf0;} .sp{background:#ffc107;}
.rl{background:#6f42c1;} .dp{background:#20c997;} .mo{background:#d63384;} .ag{background:#fd7e14;} .mlops{background:#343a40;} .home{background:#0b5ed7;}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="title">MCP Agentic AI — Real Data Demo</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real world datasets (Titanic, Digits, Books, Stocks) + upload, charts, PDF/CSV export</div>', unsafe_allow_html=True)

# ---------------- Navigation buttons (top) ----------------
buttons = {
    "🏠 Home": "home",
    "1️⃣ Machine Learning (Iris/Titanic)": "ml",
    "2️⃣ NLP & LLM (Reviews/Books)": "nlp",
    "3️⃣ Computer Vision (Digits 8x8)": "cv",
    "4️⃣ Speech & Audio (Tone demo)": "sp",
    "5️⃣ Reinforcement Learning (Rewards sim)": "rl",
    "6️⃣ Data & Preprocessing (Wine)": "dp",
    "7️⃣ Model Optimization (Compression vs Acc)": "mo",
    "8️⃣ Agentic AI (Workflow steps)": "ag",
    "9️⃣ MLOps (Metrics)": "mlops"
}
nav_html = "<div class='nav'>" + "".join(
    [f"<form action='?app={v}' method='get' style='display:inline'><button class='btn {v}'>{k}</button></form>"
     for k, v in buttons.items()]) + "</div>"
st.markdown(nav_html, unsafe_allow_html=True)

# detect which app selected via query param
app_key = st.experimental_get_query_params().get("app", ["home"])[0]

# ---------------- Utilities & data loaders ----------------

TITANIC_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
BOOKS_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
# small fallback stock CSV (public sample)
SAMPLE_STOCK_CSV = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv"

def fetch_csv_url(url, nrows=None):
    try:
        df = pd.read_csv(url)
        if nrows:
            return df.head(nrows)
        return df
    except Exception:
        return None

def load_ml_data(n):
    # prefer Titanic (for tabular real data) and Iris (classification)
    tit = fetch_csv_url(TITANIC_URL, nrows=n)
    iris = load_iris(as_frame=True).frame.head(n)
    return iris, tit

def load_nlp_data(n):
    books = fetch_csv_url(BOOKS_URL)
    sample_reviews = [
        "A thrilling and emotional story.",
        "A slow plot but well acted.",
        "Completely engaging from start to finish.",
        "Not for me - predictable and long."
    ]
    if books is not None:
        # create a short reviews column if none
        if "description" in books.columns:
            df = books.head(n)[["title", "authors", "description"]].rename(columns={"description":"Review"})
        elif "title" in books.columns:
            df = books.head(n)[["title", "authors"]]
            df["Review"] = [random.choice(sample_reviews) for _ in range(len(df))]
        else:
            df = pd.DataFrame({"Review": [random.choice(sample_reviews) for _ in range(n)]})
    else:
        df = pd.DataFrame({"Review": [random.choice(sample_reviews) for _ in range(n)]})
    return df.head(n)

def load_cv_digits(n):
    digits = load_digits()
    imgs = digits.images[:n]
    targets = digits.target[:n]
    # produce a dataframe with flattened pixels + label for plotting/exam
    df = pd.DataFrame(digits.data[:n])
    df["label"] = targets
    return imgs, df

def load_stock(ticker="AAPL", period_days=365, n=100):
    # try yfinance if available
    if YFINANCE_AVAILABLE:
        try:
            import datetime as dt
            end = dt.date.today()
            start = end - dt.timedelta(days=period_days)
            hist = yf.download(ticker, start=start, end=end, progress=False)
            if hist is None or hist.empty:
                return None
            return hist.reset_index().head(n)
        except Exception:
            return None
    # fallback: try public sample CSV listing constituents, return small synthetic series
    df = fetch_csv_url(SAMPLE_STOCK_CSV)
    if df is not None:
        # generate synthetic prices for n rows
        dates = pd.date_range(end=pd.Timestamp.today(), periods=n)
        prices = (np.cumsum(np.random.randn(n)) + 100).round(2)
        return pd.DataFrame({"Date": dates, "Close": prices})
    # final fallback synthetic
    dates = pd.date_range(end=pd.Timestamp.today(), periods=n)
    prices = (np.cumsum(np.random.randn(n)) + 100).round(2)
    return pd.DataFrame({"Date": dates, "Close": prices})

# ---------------- Plot helpers ----------------
def show_scatter(df):
    numcols = df.select_dtypes(include="number").columns.tolist()
    if len(numcols) >= 2:
        x = st.selectbox("X-axis", numcols, key="x")
        y = st.selectbox("Y-axis", numcols, key="y")
        fig, ax = plt.subplots()
        ax.scatter(df[x], df[y], c="#1f77b4", edgecolors="k")
        ax.set_xlabel(x); ax.set_ylabel(y); ax.set_title(f"{x} vs {y}")
        st.pyplot(fig)

def show_pie_for_col(df, col):
    fig, ax = plt.subplots()
    df[col].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

def text_top_words(df, text_col="Review", top_n=10):
    vec = CountVectorizer(stop_words="english")
    X = vec.fit_transform(df[text_col].astype(str))
    freq = pd.DataFrame({"word": vec.get_feature_names_out(), "count": np.array(X.sum(axis=0)).flatten()})
    freq = freq.sort_values("count", ascending=False).head(top_n)
    fig, ax = plt.subplots()
    ax.bar(freq["word"], freq["count"], color="#17a2b8")
    ax.set_title("Top words")
    st.pyplot(fig)

# ---------------- Export helpers ----------------
def download_csv(df, name="results.csv"):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", data=csv, file_name=name, mime="text/csv")

def download_pdf(df, title="MCP AI Report"):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)
    styles = getSampleStyleSheet()
    elems = []
    elems.append(Paragraph(f"<para align='center'><font color='blue' size=14><b>{title}</b></font></para>", styles["Normal"]))
    elems.append(Spacer(1, 8))
    # table header + up to 100 rows
    data = [list(df.columns)] + df.head(100).astype(str).values.tolist()
    tbl = Table(data)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#cfe8ff")),
        ("GRID", (0,0), (-1,-1), 0.25, colors.gray),
        ("ALIGN", (0,0), (-1,-1), "CENTER")
    ]))
    elems.append(tbl)
    doc.build(elems)
    st.download_button("📄 Download PDF", data=buf.getvalue(), file_name="mcp_report.pdf", mime="application/pdf")

# ---------------- Main UI logic per domain ----------------
st.write("")  # spacing
if app_key == "home":
    st.header("Welcome — select a domain using the top buttons")
    st.info("This demo uses real public datasets where possible (Titanic, Digits, Books, Stocks). You may also upload CSV/Excel/JSON files (up to 100 rows).")
else:
    st.header(f"Domain: {app_key.upper()}")
    st.markdown("---")

    # controls: record count, upload
    cols = st.columns([2, 2, 2, 2])
    n = cols[0].slider("Sample size (0-100)", min_value=0, max_value=100, value=50)
    upload = cols[1].file_uploader("Upload CSV / XLSX / JSON", type=["csv","xlsx","json"])
    if cols[2].button("🔁 Refresh"): st.experimental_rerun()
    if cols[3].button("🧹 Reset"): st.session_state.clear(); st.experimental_rerun()

    df = None  # main dataframe for display
    # domain-specific processing
    if app_key == "ml":
        iris, titanic = load_ml_data(n if n>0 else 50)
        # let user choose which dataset to view
        choice = st.selectbox("Select dataset", ["Iris (classification)", "Titanic (passengers)"])
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded file: {upload.name}")
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = iris.head(n)
        else:
            df = iris.head(n) if choice.startswith("Iris") else (titanic.head(n) if titanic is not None else iris.head(n))
        st.subheader("Dataset preview")
        st.dataframe(df.head(100))
        # charts
        show_scatter(df)
        if "Species" in df.columns:
            show_pie_for_col(df, "Species")
        # exports
        download_csv(df, name="ml_results.csv")
        download_pdf(df, title="ML Domain Report")

    elif app_key == "nlp":
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded {upload.name}")
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = load_nlp_data(n)
        else:
            df = load_nlp_data(n)
        st.subheader("Text dataset preview")
        st.dataframe(df.head(100))
        if "Review" in df.columns or "description" in df.columns or "Text" in df.columns:
            text_col = "Review" if "Review" in df.columns else ("Text" if "Text" in df.columns else df.columns[-1])
            text_top_words(df, text_col)
        download_csv(df, name="nlp_results.csv")
        download_pdf(df, title="NLP Domain Report")

    elif app_key == "cv":
        if upload:
            # uploaded CSV describing images (or zipped not supported) — accept CSV of image ids/labels
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded {upload.name}")
            except Exception as e:
                st.error(f"Upload failed: {e}")
                imgs, df = load_cv_digits(n)
        else:
            imgs, df = load_cv_digits(n if n>0 else 25)
            # show sample grid
            st.subheader("Digits sample (8x8) — first 16")
            cols_grid = st.columns(8)
            for i, img in enumerate(imgs[:16]):
                cols_grid[i % 8].image(img, width=64)
        st.dataframe(df.head(100))
        download_csv(df, name="cv_results.csv")
        download_pdf(df, title="CV Domain Report")

    elif app_key == "sp":
        if upload:
            # allow user to upload audio csv or wav? We'll accept CSV of amplitude/time
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded {upload.name}")
                # if audio-like structure, attempt playback
                if {"Amplitude","Time"}.issubset(df.columns):
                    arr = (df["Amplitude"].values * 32767).astype(np.int16)
                    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
                    write(tmp.name, 44100, arr)
                    st.audio(tmp.name)
                    os.unlink(tmp.name)
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = generate_real_data_if_needed = pd.DataFrame({"Note":["Upload failed; using demo tone"]})
        else:
            # demo tone: short sine wave
            rate = 44100
            duration = 1  # seconds
            t = np.linspace(0, duration, int(rate*duration), False)
            tone = np.sin(2*np.pi*440*t) * 0.3
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            write(tmp.name, rate, (tone * 32767).astype(np.int16))
            st.audio(tmp.name)
            os.unlink(tmp.name)
            df = pd.DataFrame({"Time": t[:100], "Amplitude": tone[:100]})
        st.dataframe(df.head(100))
        download_csv(df, name="speech_results.csv")
        download_pdf(df, title="Speech Domain Report")

    elif app_key == "rl":
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded {upload.name}")
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = generate_real_data("rl", n)
        else:
            df = generate_real_data("rl", n)
        st.dataframe(df.head(100))
        show_scatter(df)
        download_csv(df, name="rl_results.csv")
        download_pdf(df, title="RL Domain Report")

    elif app_key == "dp":
        # Wine dataset
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
                st.success(f"Loaded {upload.name}")
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = load_wine(as_frame=True).frame.head(n)
        else:
            df = load_wine(as_frame=True).frame.head(n)
        st.dataframe(df.head(100))
        show_scatter(df)
        download_csv(df, name="dp_results.csv")
        download_pdf(df, title="DataPrep Domain Report")

    elif app_key == "mo":
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = generate_real_data("mo", n)
        else:
            df = generate_real_data("mo", n)
        st.dataframe(df.head(100))
        show_scatter(df)
        download_csv(df, name="mo_results.csv")
        download_pdf(df, title="ModelOpt Domain Report")

    elif app_key == "ag":
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = generate_real_data("ag", n)
        else:
            df = generate_real_data("ag", n)
        st.dataframe(df.head(100))
        download_csv(df, name="agentic_results.csv")
        download_pdf(df, title="Agentic AI Domain Report")

    elif app_key == "mlops":
        if upload:
            try:
                if upload.name.endswith(".csv"): df = pd.read_csv(upload)
                elif upload.name.endswith(".xlsx"): df = pd.read_excel(upload)
                else: df = pd.read_json(upload)
            except Exception as e:
                st.error(f"Upload failed: {e}")
                df = generate_real_data("mlops", n)
        else:
            df = generate_real_data("mlops", n)
        st.dataframe(df.head(100))
        download_csv(df, name="mlops_results.csv")
        download_pdf(df, title="MLOps Domain Report")

    else:
        st.write("Unknown domain key")

# ---------------- Helper: generate_real_data used above ----------------
def generate_real_data(domain, n=50):
    """Used as fallback generator for some domains when not using special loaders above."""
    if domain == "rl":
        return pd.DataFrame({"Episode": np.arange(1, n+1), "Reward": np.cumsum(np.random.randn(n)*2 + 5)})
    if domain == "mo":
        return pd.DataFrame({"Compression (%)": np.linspace(0, 90, n),
                             "Accuracy": np.linspace(99, 70, n) + np.random.randn(n),
                             "Latency (ms)": np.linspace(10, 250, n)})
    if domain == "ag":
        steps = ["Collect","Analyze","CallModel","Output","Refine"]
        rows = []
        for i in range(n):
            rows.append({"Step": random.choice(steps), "ExecTime(s)": round(random.uniform(0.05, 2.0),3)})
        return pd.DataFrame(rows)
    if domain == "mlops":
        metrics = ["Accuracy","Precision","Recall","F1"]
        return pd.DataFrame({"Metric": metrics, "Value":[round(random.uniform(0.7,0.99),2) for _ in metrics]})
    return pd.DataFrame({"note":["No generator configured"]})

# ---------------- End of script ----------------
