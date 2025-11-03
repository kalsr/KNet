

# Ai_Demo_Full_Pro_V5.py
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

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="AI & LLM Platform | KNet Consulting", layout="wide")

# -------------------- CSS --------------------
st.markdown("""
<style>
.main-title {text-align: center; color: #004AAD; font-size: 32px; font-weight: 700;}
.sub-title {text-align: center; color: #6c757d; font-size: 18px;}
.stButton>button {border-radius: 10px; border: none; padding: 0.6em 1.2em; font-size: 16px; transition: 0.3s;}
.menu-btn {color: white; padding: 0.6em 1.2em; margin-right:5px; border-radius:8px; border:none; font-weight:bold;}
.menu-ml {background-color:#007BFF;}
.menu-nlp {background-color:#6f42c1;}
.menu-cv {background-color:#e83e8c;}
.menu-speech {background-color:#fd7e14;}
.menu-rl {background-color:#20c997;}
.menu-data {background-color:#17a2b8;}
.menu-opt {background-color:#6610f2;}
.menu-agentic {background-color:#dc3545;}
.menu-mlops {background-color:#ffc107;}
.generate-btn {background-color: #17a2b8; color: white;}
.download-csv {background-color: #28a745; color: white;}
.download-pdf {background-color: #ffc107; color: white;}
.reset-btn {background-color: #dc3545; color: white;}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown('<div class="main-title">AI & LLM Demo Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Developed by Randy Singh — KNet Consulting Group</div>', unsafe_allow_html=True)
st.markdown("---")

# -------------------- MENU BUTTONS TOP --------------------
menu_names = [
    ("🏁 Home","home"), 
    ("1️⃣ Machine Learning & Deep Learning","ml"), 
    ("2️⃣ NLP & LLMs","nlp"), 
    ("3️⃣ Computer Vision","cv"), 
    ("4️⃣ Speech & Audio AI","speech"), 
    ("5️⃣ Reinforcement Learning","rl"), 
    ("6️⃣ Data & Preprocessing","data"), 
    ("7️⃣ Model Optimization & Serving","opt"), 
    ("8️⃣ Agentic AI & Workflow Orchestration","agentic"), 
    ("9️⃣ MLOps & Evaluation","mlops")
]

cols = st.columns(len(menu_names))
for i,(label,key) in enumerate(menu_names):
    if cols[i].button(label, key=f"menu_{key}", help=f"Select {label}", css_class=f"menu-{key}"):
        st.session_state.selected_menu = key

# -------------------- SESSION STATE --------------------
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = 'home'
if 'df' not in st.session_state:
    st.session_state.df = None
if 'images' not in st.session_state:
    st.session_state.images = None

menu = st.session_state.selected_menu

# -------------------- HELPER FUNCTIONS --------------------
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
    sample_texts = ["AI is amazing","I love machine learning","Streamlit is powerful",
                    "Data science is fun","NLP is revolutionizing industries",
                    "Python programming is great","Deep learning is fascinating",
                    "Generative AI is changing the world","LLMs can write code"]
    return pd.DataFrame({"Text":[random.choice(sample_texts) for _ in range(n)]})

def generate_cv_images(n=50,size=64):
    images=[]
    for _ in range(n):
        img=Image.new('RGB',(size,size), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        draw=ImageDraw.Draw(img)
        shape=random.choice(['rectangle','ellipse','line'])
        if shape=='rectangle':
            draw.rectangle([random.randint(0,size//2),random.randint(0,size//2),
                            random.randint(size//2,size),random.randint(0,size//2)],
                           fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        elif shape=='ellipse':
            draw.ellipse([random.randint(0,size//2),random.randint(0,size//2),
                          random.randint(size//2,size),random.randint(0,size//2)],
                         fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        else:
            draw.line([random.randint(0,size),random.randint(0,size),
                       random.randint(0,size),random.randint(0,size)],
                      fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),width=2)
        images.append(img)
    return images

def download_csv(df):
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "results.csv","text/csv", key="download_csv")

def download_pdf(df,title="AI Application Results"):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(200,10, txt=title, ln=True, align="C")
    pdf.ln(10)
    for i in range(len(df)):
        pdf.multi_cell(0,8, txt=str(df.iloc[i].to_dict()))
    st.download_button("📄 Download PDF", BytesIO(pdf.output(dest='S').encode('latin1')), "results.pdf","application/pdf", key="download_pdf")

def plot_charts(df):
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols)>=2:
        col1,col2=st.columns(2)
        with col1: col_x=st.selectbox("X-axis",numeric_cols,key="x_axis")
        with col2: col_y=st.selectbox("Y-axis",numeric_cols,key="y_axis")
        fig,ax=plt.subplots()
        ax.scatter(df[col_x],df[col_y],c='skyblue',edgecolor='black')
        ax.set_title(f"{col_x} vs {col_y}")
        st.pyplot(fig)
    if numeric_cols:
        target_col="Target" if "Target" in df.columns else numeric_cols[0]
        st.subheader("Distribution Pie Chart")
        fig2,ax2=plt.subplots()
        df[target_col].value_counts().plot.pie(autopct="%1.1f%%",colors=["#66b3ff","#99ff99","#ff9999"],ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)
    if "Text" in df.columns:
        st.subheader("Top 10 Words Frequency")
        vec=CountVectorizer()
        X=vec.fit_transform(df["Text"])
        freq=pd.DataFrame({'Word':vec.get_feature_names_out(),'Count':np.array(X.sum(axis=0)).flatten()})
        freq=freq.sort_values(by="Count",ascending=False).head(10)
        fig3,ax3=plt.subplots()
        ax3.bar(freq["Word"],freq["Count"],color="#66b3ff")
        ax3.set_title("Top 10 Words")
        st.pyplot(fig3)

# -------------------- RESET BUTTON --------------------
if st.button("🔄 Reset Data", key="reset_btn"):
    st.session_state.df=None
    st.session_state.images=None
    st.experimental_rerun()

# -------------------- MAIN LOGIC --------------------
if menu=="home":
    st.markdown("### 🌐 Welcome to AI & LLM Demo Platform")
    st.info("Select a menu button above to generate synthetic data, upload CSV/Excel/JSON, visualize charts, download CSV/PDF, and reset anytime.")
else:
    n_records=st.slider("Select number of sample records",1,100,50)
    uploaded=st.file_uploader("Upload dataset (CSV, Excel, JSON)",type=["csv","xlsx","json"], key="file_uploader")
    
    if uploaded:
        if uploaded.name.endswith(".csv"): st.session_state.df=pd.read_csv(uploaded)
        elif uploaded.name.endswith(".xlsx"): st.session_state.df=pd.read_excel(uploaded)
        else: st.session_state.df=pd.read_json(uploaded)

    if st.button("🔁 Generate Synthetic Data", key="gen_btn"):
        if menu=="ml": st.session_state.df=generate_classification(n_records)
        elif menu=="nlp": st.session_state.df=generate_text(n_records)
        elif menu=="cv":
            st.session_state.images=generate_cv_images(n_records)
            st.subheader("Sample Synthetic Images")
            grid_cols=st.columns(5)
            for i,img in enumerate(st.session_state.images[:25]):
                grid_cols[i%5].image(img,width=64)
            st.session_state.df=pd.DataFrame({"Image_Index":list(range(len(st.session_state.images)))})
        elif menu=="speech":
            rate=44100
            t=np.linspace(0,1,n_records*441)
            amplitude=np.sin(2*np.pi*220*t)+np.random.normal(0,0.1,len(t))
            st.session_state.df=pd.DataFrame({"Time":t[:n_records*10],"Amplitude":amplitude[:n_records*10]})
        elif menu=="rl": st.session_state.df=pd.DataFrame({"Step":np.arange(n_records),"Reward":np.cumsum(np.random.randn(n_records))})
        elif menu=="data": st.session_state.df=generate_regression(n_records)
        elif menu=="opt": st.session_state.df=pd.DataFrame({"Compression (%)":np.linspace(0,90,n_records),
                                                           "Accuracy":np.linspace(98,70,n_records)+np.random.randn(n_records),
                                                           "Latency (ms)":np.linspace(10,200,n_records)})
        elif menu=="agentic": 
            steps = ["Collect Data","Analyze Input","Call Model","Generate Output","Refine Result"]
            st.session_state.df=pd.DataFrame({"Step":steps, "Execution Time (s)":np.random.uniform(0.1,1.5,len(steps))})
        elif menu=="mlops": st.session_state.df=pd.DataFrame({"Metric":["Accuracy","Precision","Recall","F1 Score"],
                                                             "Value":[round(random.uniform(0.7,0.99),2) for _ in range(4)]})

    if st.session_state.df is not None:
        st.subheader("📋 Dataset Preview")
        st.dataframe(st.session_state.df.head(50), use_container_width=True)
        plot_charts(st.session_state.df)

    if menu=="speech" and st.session_state.df is not None:
        st.subheader("🔊 Play Synthetic Audio")
        samples=(st.session_state.df["Amplitude"].values*32767).astype(np.int16)
        tmp_file=tempfile.NamedTemporaryFile(delete=False,suffix=".wav")
        write(tmp_file.name,44100,samples)
        st.audio(tmp_file.name)
        os.unlink(tmp_file.name)

    if st.session_state.df is not None:
        st.markdown("### 💾 Download Results")
        download_csv(st.session_state.df)
        download_pdf(st.session_state.df, title=f"{menu.upper()} Results - KNet Consulting Group")
