import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
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
.stButton>button {border-radius:10px; padding:0.6em 1.2em; font-weight:bold; font-size:16px; margin-right:5px;}
.generate-btn {background-color: #17a2b8; color: white;}
.download-csv {background-color: #28a745; color: white;}
.download-pdf {background-color: #ffc107; color: white;}
.reset-btn {background-color: #dc3545; color: white;}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">AI & LLM Demo Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Randy Singh — KNet Consulting Group</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Session state initialization ---
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = 'home'
if 'df' not in st.session_state:
    st.session_state.df = None
if 'images' not in st.session_state:
    st.session_state.images = None

# --- Menu buttons ---
menu_items = [
    ("🏁 Home", "home"),
    ("1️⃣ Machine Learning & Deep Learning", "ml"),
    ("2️⃣ NLP & LLMs", "nlp"),
    ("3️⃣ Computer Vision", "cv"),
    ("4️⃣ Speech & Audio AI", "speech"),
    ("5️⃣ Reinforcement Learning", "rl"),
    ("6️⃣ Data & Preprocessing", "data"),
    ("7️⃣ Model Optimization & Serving", "opt"),
    ("8️⃣ Agentic AI & Workflow Orchestration", "agentic"),
    ("9️⃣ MLOps & Evaluation", "mlops")
]

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
cols = [col1,col2,col3,col4,col5,col6,col7,col8,col9]

for i,(label,key) in enumerate(menu_items):
    if cols[i].button(label):
        st.session_state.selected_menu = key
        st.session_state.df = None
        st.session_state.images = None
        st.experimental_rerun()

menu = st.session_state.selected_menu

# --- Helper functions ---
def generate_classification(n=50):
    X, y = make_classification(n_samples=n, n_features=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df["Target"] = y
    return df

def generate_text(n=50):
    texts = ["AI is amazing","I love machine learning","Streamlit is powerful",
             "Data science is fun","NLP is revolutionizing industries"]
    return pd.DataFrame({"Text":[random.choice(texts) for _ in range(n)]})

def generate_regression(n=50):
    X, y = make_regression(n_samples=n, n_features=5, noise=0.1, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df["Target"] = y
    return df

def generate_cv_images(n=50, size=64):
    images=[]
    for _ in range(n):
        img = Image.new('RGB',(size,size),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        shape = random.choice(['rectangle','ellipse','line'])
        if shape=='rectangle':
            draw.rectangle([random.randint(0,size//2), random.randint(0,size//2), 
                            random.randint(size//2,size), random.randint(0,size//2)], 
                           fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        elif shape=='ellipse':
            draw.ellipse([random.randint(0,size//2), random.randint(0,size//2), 
                          random.randint(size//2,size), random.randint(0,size//2)], 
                         fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        else:
            draw.line([random.randint(0,size), random.randint(0,size), 
                       random.randint(0,size), random.randint(0,size)], 
                      fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), width=2)
        images.append(img)
    return images

def download_csv(df):
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "results.csv","text/csv")

def download_pdf(df):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",10)
    pdf.cell(200,10,txt="AI Demo Results",ln=True,align="C")
    pdf.ln(10)
    for i in range(len(df)):
        pdf.multi_cell(0,8,str(df.iloc[i].to_dict()))
    st.download_button("📄 Download PDF", BytesIO(pdf.output(dest='S').encode('latin1')), "results.pdf","application/pdf")

def plot_charts(df):
    numeric_cols=df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.subheader("Distribution Pie Chart")
        fig,ax=plt.subplots()
        df[numeric_cols[0]].value_counts().plot.pie(autopct="%1.1f%%",colors=["#66b3ff","#99ff99","#ff9999"],ax=ax)
        st.pyplot(fig)

# --- Reset button ---
if st.button("🔄 Reset All Data"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

# --- Main logic ---
st.subheader(f"Selected Menu: {menu.upper()}")

n_records = st.slider("Number of sample records", 1, 100, 50)
uploaded = st.file_uploader("Upload CSV/Excel/JSON", type=["csv","xlsx","json"])

if uploaded:
    if uploaded.name.endswith(".csv"): st.session_state.df=pd.read_csv(uploaded)
    elif uploaded.name.endswith(".xlsx"): st.session_state.df=pd.read_excel(uploaded)
    else: st.session_state.df=pd.read_json(uploaded)

if st.button("Generate Synthetic Data"):
    if menu=="ml": st.session_state.df = generate_classification(n_records)
    elif menu=="nlp": st.session_state.df = generate_text(n_records)
    elif menu=="data": st.session_state.df = generate_regression(n_records)
    elif menu=="cv": 
        st.session_state.images = generate_cv_images(n_records)
        st.subheader("Sample Images")
        cols_img = st.columns(5)
        for i,img in enumerate(st.session_state.images[:25]):
            cols_img[i%5].image(img,width=64)
        st.session_state.df = pd.DataFrame({"Image_Index": list(range(len(st.session_state.images)))})

if st.session_state.df is not None:
    st.subheader("Dataset Preview")
    st.dataframe(st.session_state.df.head(50))
    plot_charts(st.session_state.df)
