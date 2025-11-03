# Ai_Demo_Full_Pro_V1.py
# -------------------------------------------------------------
# KNet Consulting | AI & LLM Real-World Demo Platform
# -------------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine
from sklearn.feature_extraction.text import CountVectorizer
from io import BytesIO
import random, os, tempfile
from scipy.io.wavfile import write
from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="AI & LLM Platform | KNet Consulting", layout="wide")

st.markdown("""
<style>
body {background-color:#f7f9fc;}
.main-title {text-align:center; color:#004AAD; font-size:32px; font-weight:700;}
.sub-title {text-align:center; color:#6c757d; font-size:18px; margin-bottom:20px;}
.nav-container {display:flex; justify-content:center; flex-wrap:wrap; gap:10px; margin-bottom:10px;}
.nav-button {border:none; padding:10px 18px; border-radius:8px; color:white; font-weight:600; cursor:pointer;}
.nav-button:hover {opacity:0.9;}
.ml{background:#007bff;} .nlp{background:#28a745;} .cv{background:#17a2b8;}
.sp{background:#ffc107;} .rl{background:#6f42c1;} .dp{background:#20c997;}
.mo{background:#e83e8c;} .ag{background:#fd7e14;} .mlops{background:#343a40;}
.home{background:#0d6efd;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">AI & LLM Demo Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Randy Singh — KNet Consulting Group</div>', unsafe_allow_html=True)


# -------------------- NAVIGATION BAR --------------------
buttons = {
    "🏁 Home": "home",
    "1️⃣ Machine Learning": "ml",
    "2️⃣ NLP & LLM": "nlp",
    "3️⃣ Computer Vision": "cv",
    "4️⃣ Speech & Audio": "sp",
    "5️⃣ Reinforcement Learning": "rl",
    "6️⃣ Data & Preprocessing": "dp",
    "7️⃣ Model Optimization": "mo",
    "8️⃣ Agentic AI": "ag",
    "9️⃣ MLOps": "mlops"
}
st.markdown('<div class="nav-container">' +
            "".join([f"<form action='?app={v}' method='get'><button class='nav-button {v}'>{k}</button></form>"
                     for k, v in buttons.items()]) +
            '</div>', unsafe_allow_html=True)

# detect selection
query_params = st.query_params
app_key = query_params.get("app", ["home"])[0]


# -------------------- DATA GENERATORS --------------------
def load_realistic_data(app, n=50):
    if app == "ml":
        data = load_iris(as_frame=True).frame.head(n)
        data.rename(columns={"target": "Species"}, inplace=True)
        return data

    elif app == "nlp":
        texts = [
            "AI is transforming industries worldwide.",
            "Natural language models understand context and emotion.",
            "Streamlit enables interactive AI dashboards.",
            "Machine learning automates decision-making.",
            "Cybersecurity benefits from agentic AI analysis.",
            "Chatbots improve user experience through LLMs."
        ]
        return pd.DataFrame({"Text": random.choices(texts, k=n)})

    elif app == "cv":
        images = []
        for _ in range(n):
            img = Image.new("RGB", (64, 64),
                            color=(random.randint(0, 255),
                                   random.randint(0, 255),
                                   random.randint(0, 255)))
            draw = ImageDraw.Draw(img)
            draw.rectangle([10, 10, 54, 54], outline="white")
            images.append(img)
        st.subheader("📸 Sample Images")
        for img in images[:10]:
            st.image(img, width=70)
        return pd.DataFrame({"Image_ID": [f"IMG_{i+1}" for i in range(n)]})

    elif app == "sp":
        rate = 44100
        t = np.linspace(0, 1, n * 441)
        amplitude = np.sin(2 * np.pi * 440 * t)
        df = pd.DataFrame({"Time": t[:n*10], "Amplitude": amplitude[:n*10]})
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(tmp.name, rate, (amplitude * 32767).astype(np.int16))
        st.subheader("🔊 Sample Audio")
        st.audio(tmp.name)
        os.unlink(tmp.name)
        return df

    elif app == "rl":
        steps = np.arange(1, n + 1)
        rewards = np.cumsum(np.random.randn(n) * 0.5)
        return pd.DataFrame({"Step": steps, "Reward": rewards})

    elif app == "dp":
        return load_wine(as_frame=True).frame.head(n)

    elif app == "mo":
        return pd.DataFrame({
            "Compression (%)": np.linspace(0, 90, n),
            "Accuracy": np.linspace(99, 70, n) + np.random.randn(n),
            "Latency (ms)": np.linspace(10, 200, n)
        })

    elif app == "ag":
        steps = ["Collect Data", "Analyze Input", "Call Model", "Generate Output", "Refine Result"]
        return pd.DataFrame({"Step": steps, "Execution Time (s)": np.random.uniform(0.1, 1.5, len(steps))})

    elif app == "mlops":
        metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
        values = [round(random.uniform(0.7, 0.99), 2) for _ in range(4)]
        return pd.DataFrame({"Metric": metrics, "Value": values})


# -------------------- UTILITIES --------------------
def plot_charts(df):
    numeric = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric) >= 2:
        c1, c2 = st.columns(2)
        with c1: x = st.selectbox("X-axis", numeric)
        with c2: y = st.selectbox("Y-axis", numeric)
        fig, ax = plt.subplots()
        ax.scatter(df[x], df[y], c="#66b3ff", edgecolor="black")
        ax.set_title(f"{x} vs {y}")
        st.pyplot(fig)

    target = "Species" if "Species" in df.columns else (numeric[0] if numeric else None)
    if target:
        st.subheader("📊 Distribution Pie Chart")
        fig2, ax2 = plt.subplots()
        df[target].value_counts().plot.pie(autopct="%1.1f%%",
                                           colors=["#66b3ff","#99ff99","#ff9999"], ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)

    if "Text" in df.columns:
        st.subheader("🧠 Top Words Frequency")
        vec = CountVectorizer()
        X = vec.fit_transform(df["Text"])
        freq = pd.DataFrame({"Word": vec.get_feature_names_out(),
                             "Count": np.array(X.sum(axis=0)).flatten()})
        freq = freq.sort_values(by="Count", ascending=False).head(10)
        fig3, ax3 = plt.subplots()
        ax3.bar(freq["Word"], freq["Count"], color="#17a2b8")
        ax3.set_title("Top 10 Words")
        st.pyplot(fig3)


def download_csv(df):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", csv, "results.csv", "text/csv")


def download_pdf(df, title="AI Application Results"):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=letter)
    styles = getSampleStyleSheet()
    elems = [Paragraph(f"<para align='center'><font color='blue' size=16><b>{title}</b></font></para>", styles["Normal"]),
             Spacer(1, 12)]
    table_data = [df.columns.tolist()] + df.head(100).astype(str).values.tolist()
    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))
    elems.append(table)
    doc.build(elems)
    st.download_button("📄 Download PDF",
                       data=buf.getvalue(),
                       file_name="results.pdf",
                       mime="application/pdf")


# -------------------- MAIN LOGIC --------------------
if app_key == "home":
    st.markdown("### 🌐 Welcome to AI & LLM Demo Platform")
    st.info("""
Explore **nine real-world AI domains**.  
Each domain loads meaningful datasets, charts, and export tools.  
Use **Refresh** to reload data or **Reset** to clear the session.
""")
else:
    st.header(f"🚀 {list(buttons.keys())[list(buttons.values()).index(app_key)]}")
    st.markdown("---")

    n_records = st.slider("Select number of sample records:", 10, 100, 50)
    uploaded = st.file_uploader("Upload dataset (CSV/XLSX/JSON)", type=["csv","xlsx","json"])

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔁 Refresh Data"): st.experimental_rerun()
    with c2:
        if st.button("🔄 Reset"): st.session_state.clear(); st.experimental_rerun()

    if uploaded:
        if uploaded.name.endswith(".csv"): df = pd.read_csv(uploaded)
        elif uploaded.name.endswith(".xlsx"): df = pd.read_excel(uploaded)
        else: df = pd.read_json(uploaded)
        st.success(f"Loaded {uploaded.name}")
    else:
        df = load_realistic_data(app_key, n_records)

    if df is not None:
        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(100), use_container_width=True)
        plot_charts(df)
        st.markdown("### 💾 Export Options")
        download_csv(df)
        download_pdf(df, title=f"{app_key.upper()} Report - KNet Consulting")
