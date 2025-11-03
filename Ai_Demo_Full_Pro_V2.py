

# Ai_Demo_Full_Fixed.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression, load_digits
from sklearn.feature_extraction.text import CountVectorizer
from fpdf import FPDF
from io import BytesIO
import random
from scipy.io.wavfile import write
import tempfile
import os
from PIL import Image, ImageDraw

st.set_page_config(page_title="AI & LLM Platform | KNet Consulting", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.main-title {text-align: center; color: #004AAD; font-size: 32px; font-weight: 700;}
.sub-title {text-align: center; color: #6c757d; font-size: 18px;}
.stButton>button {background-color: #007BFF; color: white; border-radius: 10px; border: none; padding: 0.6em 1.2em; font-size: 16px; transition: 0.3s;}
.stButton>button:hover {background-color: #0056b3;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">AI & LLM Demo Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Randy Singh — KNet Consulting Group</div>', unsafe_allow_html=True)
st.markdown("---")

# --- MENU ---
menu_items = ["🏁 Home",
              "1️⃣ Machine Learning & Deep Learning",
              "2️⃣ NLP & LLMs",
              "3️⃣ Computer Vision",
              "4️⃣ Speech & Audio AI",
              "5️⃣ Reinforcement Learning",
              "6️⃣ Data & Preprocessing",
              "7️⃣ Model Optimization & Serving",
              "8️⃣ Agentic AI & Workflow Orchestration",
              "9️⃣ MLOps & Evaluation"]

menu = st.sidebar.radio("Select an AI Application", menu_items)

# --- HELPER FUNCTIONS ---
def generate_classification(n=50):
    X, y = make_classification(n_samples=n, n_features=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df["Target"] = y
    return df

def generate_regression(n=50):
    X, y = make_regression(n_samples=n, n_features=5, noise=0.1, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df["Target"] = y
    return df

def generate_text(n=50):
    sample_texts = ["AI is amazing", "I love machine learning", "Streamlit is powerful",
                    "Data science is fun", "NLP is revolutionizing industries",
                    "Python programming is great", "Deep learning is fascinating",
                    "Generative AI is changing the world", "LLMs can write code"]
    df = pd.DataFrame({"Text": [random.choice(sample_texts) for _ in range(n)]})
    return df

def generate_cv_images(n=50, size=64):
    images = []
    for _ in range(n):
        img = Image.new('RGB', (size, size), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        shape_type = random.choice(['rectangle','ellipse','line'])
        if shape_type == 'rectangle':
            draw.rectangle([random.randint(0,size//2), random.randint(0,size//2),
                            random.randint(size//2,size), random.randint(size//2,size)],
                           fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        elif shape_type == 'ellipse':
            draw.ellipse([random.randint(0,size//2), random.randint(0,size//2),
                          random.randint(size//2,size), random.randint(size//2,size)],
                         fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        else:
            draw.line([random.randint(0,size), random.randint(0,size), random.randint(0,size), random.randint(0,size)],
                      fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)), width=2)
        images.append(img)
    return images

def download_csv(df):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download CSV", data=csv, file_name="results.csv", mime="text/csv")

def download_pdf(df, title="AI Application Results"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(200,10, txt=title, ln=True, align="C")
    pdf.ln(10)
    for i in range(len(df)):
        pdf.multi_cell(0,8, txt=str(df.iloc[i].to_dict()))
    pdf_output = BytesIO(pdf.output(dest='S').encode('latin1'))
    st.download_button("📄 Download PDF", data=pdf_output, file_name="results.pdf", mime="application/pdf")

def plot_charts(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            col_x = st.selectbox("X-axis", numeric_cols, key="x_axis")
        with col2:
            col_y = st.selectbox("Y-axis", numeric_cols, key="y_axis")
        fig, ax = plt.subplots()
        ax.scatter(df[col_x], df[col_y], c='skyblue', edgecolor='black')
        ax.set_title(f"Scatter: {col_x} vs {col_y}")
        st.pyplot(fig)
    if numeric_cols:
        target_col = "Target" if "Target" in df.columns else numeric_cols[0]
        st.subheader("Distribution Pie Chart")
        fig2, ax2 = plt.subplots()
        df[target_col].value_counts().plot.pie(autopct="%1.1f%%", colors=["#66b3ff","#99ff99","#ff9999"], ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)
    if "Text" in df.columns:
        st.subheader("Top 10 Words Frequency")
        vec = CountVectorizer()
        X = vec.fit_transform(df["Text"])
        freq = pd.DataFrame({'Word': vec.get_feature_names_out(), 'Count': np.array(X.sum(axis=0)).flatten()})
        freq = freq.sort_values(by="Count", ascending=False).head(10)
        fig3, ax3 = plt.subplots()
        ax3.bar(freq["Word"], freq["Count"], color="#66b3ff")
        ax3.set_title("Top 10 Words")
        st.pyplot(fig3)

# --- HOME PAGE ---
if menu == "🏁 Home":
    st.markdown("### 🌐 Welcome to AI & LLM Demo Platform")
    st.info("Explore 9 AI/LLM domains. Generate 1–100 synthetic records, upload CSV/Excel/JSON, visualize charts, download CSV/PDF, and reset/refresh anytime.")
else:
    app_name = menu.split(' ',1)[1]
    st.header(f"🚀 {app_name}")
    st.caption("Developed by Randy Singh — KNet Consulting Group")
    st.markdown("---")
    n_records = st.slider("Select number of sample records", 1, 100, 50)
    uploaded = st.file_uploader("Upload your dataset (CSV, Excel, JSON)", type=["csv","xlsx","json"])
    df = None
    images = None
    if uploaded:
        if uploaded.name.endswith(".csv"): df = pd.read_csv(uploaded)
        elif uploaded.name.endswith(".xlsx"): df = pd.read_excel(uploaded)
        else: df = pd.read_json(uploaded)
        st.success(f"Loaded {uploaded.name}")

    # --- Generate / Demo Data ---
    if df is None or st.button("🔁 Generate Synthetic Data"):
        if "Machine Learning" in app_name:
            df = generate_classification(n_records)
        elif "NLP" in app_name:
            df = generate_text(n_records)
        elif "Computer Vision" in app_name:
            images = generate_cv_images(n_records)
            st.subheader("Sample Synthetic Images")
            grid_cols = st.columns(5)
            for i, img in enumerate(images[:25]):
                grid_cols[i % 5].image(img, width=64)
            df = pd.DataFrame({"Image_Index": list(range(len(images)))})
        elif "Speech" in app_name:
            rate = 44100
            t = np.linspace(0,1,n_records*441)
            amplitude = np.sin(2*np.pi*220*t) + np.random.normal(0,0.1,len(t))
            df = pd.DataFrame({"Time": t[:n_records*10], "Amplitude": amplitude[:n_records*10]})
        elif "Reinforcement" in app_name:
            df = pd.DataFrame({"Step": np.arange(n_records), "Reward": np.cumsum(np.random.randn(n_records))})
        elif "Data & Preprocessing" in app_name:
            df = generate_regression(n_records)
        elif "Model Optimization" in app_name:
            df = pd.DataFrame({"Compression (%)": np.linspace(0,90,n_records),
                               "Accuracy": np.linspace(98,70,n_records)+np.random.randn(n_records),
                               "Latency (ms)": np.linspace(10,200,n_records)})
        elif "Agentic AI" in app_name:
            steps = ["Collect Data","Analyze Input","Call Model","Generate Output","Refine Result"]
            df = pd.DataFrame({"Step": steps, "Execution Time (s)": np.random.uniform(0.1,1.5,len(steps))})
        elif "MLOps" in app_name:
            df = pd.DataFrame({"Metric":["Accuracy","Precision","Recall","F1 Score"],
                               "Value":[round(random.uniform(0.7,0.99),2) for _ in range(4)]})

    if df is not None:
        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(50), use_container_width=True)
        plot_charts(df)

    # --- Speech Playback ---
    if "Speech" in app_name and df is not None:
        st.subheader("🔊 Play Synthetic Audio")
        samples = (df["Amplitude"].values * 32767).astype(np.int16)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(tmp_file.name, 44100, samples)
        st.audio(tmp_file.name)
        os.unlink(tmp_file.name)

    # --- Download Options ---
    if df is not None:
        st.markdown("### 💾 Download Results")
        download_csv(df)
        download_pdf(df, title=f"{app_name} Results - KNet Consulting Group")

    # --- Reset Button ---
    if st.button("🔄 Reset Data"):
        st.experimental_rerun()
