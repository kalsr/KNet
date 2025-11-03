

# ------------------------------------------------------------
# KNet Consulting | AI & LLM Demo Platform (v2)
# Includes 9 AI domains, charts, downloads, speech & image demo
# Synthetic data generation and user upload
# Graphs and pie charts for every applicable domain
# NLP: Top words frequency visualization
# Computer Vision: Synthetic images display
# Speech/Audio: Playable synthetic audio
# SV and PDF downloads
# Professional branding & GUI
# Continuous menu selection without quitting – user can switch domains freely
# Reset/Refresh functionality
#THIS APPLICATION IS DESIGNED BY RANDY SINGH FROM KNet CONSULTING GROUP.
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.feature_extraction.text import CountVectorizer
from io import BytesIO
import random
from scipy.io.wavfile import write
import tempfile
import os
from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# ------------------- PAGE CONFIG -------------------
st.set_page_config(page_title="AI & LLM Platform | KNet Consulting", layout="wide")

st.markdown("""
<style>
.main-title {text-align: center; color: #004AAD; font-size: 32px; font-weight: 700;}
.sub-title {text-align: center; color: #6c757d; font-size: 18px;}
.stButton>button {
  background: linear-gradient(135deg,#004AAD,#007BFF);
  color:white; border-radius:10px; border:none; padding:0.6em 1.2em;
  font-size:16px; font-weight:600; transition:0.3s;
}
.stButton>button:hover {background:linear-gradient(135deg,#007BFF,#00B4D8);}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">AI & LLM Demo Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Randy Singh — KNet Consulting Group</div>', unsafe_allow_html=True)
st.markdown("---")

# ------------------- SIDEBAR -------------------
menu = st.sidebar.radio(
    "Select an AI Application (Quit by closing sidebar)",
    [
        "🏁 Home",
        "1️⃣ Machine Learning & Deep Learning",
        "2️⃣ NLP & LLMs",
        "3️⃣ Computer Vision",
        "4️⃣ Speech & Audio AI",
        "5️⃣ Reinforcement Learning",
        "6️⃣ Data & Preprocessing",
        "7️⃣ Model Optimization & Serving",
        "8️⃣ Agentic AI & Workflow Orchestration",
        "9️⃣ MLOps & Evaluation"
    ]
)

# ------------------- HELPER FUNCTIONS -------------------
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
    sample_texts = [
        "AI is amazing", "I love machine learning", "Streamlit is powerful",
        "Data science is fun", "NLP is revolutionizing industries"
    ]
    df = pd.DataFrame({"Text": [random.choice(sample_texts) for _ in range(n)]})
    return df

def generate_cv_images(n=50, size=64):
    images = []
    for _ in range(n):
        img = Image.new('RGB', (size, size), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        shape_type = random.choice(['rectangle', 'ellipse', 'line'])
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
    """Generate a color-themed PDF report"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # --- Title Section (Blue Banner) ---
    title_data = [[title]]
    title_table = Table(title_data, colWidths=[480])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#004AAD")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12)
    ]))
    elements.append(title_table)
    elements.append(Spacer(1, 12))

    # --- Data Section ---
    elements.append(Paragraph("Dataset Summary", styles["Heading2"]))
    elements.append(Spacer(1, 6))
    data_head = [df.columns.tolist()] + df.head(15).values.tolist()
    table = Table(data_head)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E3EFFF")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("End of Report — Generated via KNet AI & LLM Platform", styles["Italic"]))

    doc.build(elements)
    pdf_data = buffer.getvalue()
    buffer.close()
    st.download_button("📄 Download PDF", data=pdf_data, file_name="results.pdf", mime="application/pdf")

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

    target_col = "Target" if "Target" in df.columns else (numeric_cols[0] if numeric_cols else None)
    if target_col:
        st.subheader("Distribution Pie Chart")
        fig2, ax2 = plt.subplots()
        df[target_col].value_counts().plot.pie(autopct="%1.1f%%",
                                               colors=["#66b3ff","#99ff99","#ff9999"],
                                               ax=ax2)
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

# ------------------- HOME -------------------
if menu == "🏁 Home":
    st.markdown("### 🌐 Welcome to AI & LLM Demo Platform")
    st.info("""
Explore 9 AI/LLM domains with:
- Generate up to **109 synthetic records**
- **Upload** CSV/Excel/JSON data
- **Visualize** with scatter, bar, and pie charts
- **Download** results as CSV or PDF
- Each application is fully interactive and branded
- Continue selecting menu items without restarting
""")

# ------------------- APPLICATIONS -------------------
else:
    app_name = menu.split(' ',1)[1]
    st.header(f"🚀 {app_name}")
    st.caption("Developed by Randy Singh — KNet Consulting Group")
    st.markdown("---")

    n_records = st.slider("Select number of synthetic records (max 109):", 10, 109, 50)
    uploaded = st.file_uploader("Upload your dataset (CSV, Excel, JSON)", type=["csv","xlsx","json"])
    df = None
    images = None

    if uploaded:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        elif uploaded.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded)
        else:
            df = pd.read_json(uploaded)
        st.success(f"Loaded {uploaded.name}")

    if df is None or st.button("🔁 Generate Synthetic Data"):
        if "Machine Learning" in app_name or "Deep Learning" in app_name:
            df = generate_classification(n_records)
        elif "NLP" in app_name or "LLMs" in app_name:
            df = generate_text(n_records)
        elif "Computer Vision" in app_name:
            images = generate_cv_images(n_records)
            st.subheader("Sample Synthetic Images")
            for img in images[:9]:
                st.image(img, width=100)
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
        st.dataframe(df.head(), use_container_width=True)
        plot_charts(df)

    if "Speech" in app_name and df is not None:
        st.subheader("🔊 Play Synthetic Audio")
        samples = (df["Amplitude"].values * 32767).astype(np.int16)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(tmp_file.name, 44100, samples)
        st.audio(tmp_file.name)
        os.unlink(tmp_file.name)

    if df is not None:
        st.markdown("### 💾 Download Results")
        download_csv(df)
        download_pdf(df, title=f"{app_name} Results - KNet Consulting Group")

    if st.button("🔄 Reset Data"):
        st.experimental_rerun()
