import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.feature_extraction.text import CountVectorizer
from fpdf import FPDF
from io import BytesIO
from PIL import Image, ImageDraw
import random
import tempfile
from scipy.io.wavfile import write
import os

st.set_page_config(page_title="AI & LLM Platform", layout="wide")

# --- Initialize session state ---
if 'menu' not in st.session_state:
    st.session_state.menu = 'Home'
if 'df' not in st.session_state:
    st.session_state.df = None
if 'images' not in st.session_state:
    st.session_state.images = None
if 'n_records' not in st.session_state:
    st.session_state.n_records = 50

# --- Slider for number of records ---
st.sidebar.markdown("### Select number of records")
st.session_state.n_records = st.sidebar.slider("Records:", 1, 100, st.session_state.n_records)

# --- Helper functions ---
def generate_classification(n=50):
    X, y = make_classification(n_samples=n, n_features=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df['Target'] = y
    return df

def generate_regression(n=50):
    X, y = make_regression(n_samples=n, n_features=5, noise=0.1, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df['Target'] = y
    return df

def generate_text(n=50):
    texts = ["AI is amazing","I love machine learning","Streamlit is powerful",
             "Data science is fun","NLP is revolutionizing industries",
             "Python programming is great","Deep learning is fascinating",
             "Speech recognition is cool","Generative AI changes the world"]
    df = pd.DataFrame({'Text':[random.choice(texts) for _ in range(n)]})
    return df

def generate_cv_images(n=50,size=64):
    imgs=[]
    for _ in range(n):
        img=Image.new('RGB',(size,size),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        draw=ImageDraw.Draw(img)
        shape=random.choice(['rectangle','ellipse','line'])
        if shape=='rectangle':
            x0,y0=random.randint(0,size//2), random.randint(0,size//2)
            x1,y1=random.randint(size//2,size), random.randint(size//2,size)
            draw.rectangle([x0,y0,x1,y1], fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        elif shape=='ellipse':
            x0,y0=random.randint(0,size//2), random.randint(0,size//2)
            x1,y1=random.randint(size//2,size), random.randint(size//2,size)
            draw.ellipse([x0,y0,x1,y1], fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        else:
            draw.line([random.randint(0,size),random.randint(0,size),random.randint(0,size),random.randint(0,size)],
                      fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), width=2)
        imgs.append(img)
    return imgs

def plot_charts(df):
    numeric_cols=df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.subheader("Distribution Pie Chart")
        fig,ax=plt.subplots()
        df[numeric_cols[0]].value_counts().plot.pie(autopct="%1.1f%%", colors=["#66b3ff","#99ff99","#ff9999"], ax=ax)
        st.pyplot(fig)
    if "Text" in df.columns:
        st.subheader("Top 10 Words Frequency")
        vec=CountVectorizer()
        X=vec.fit_transform(df['Text'])
        freq=pd.DataFrame({'Word':vec.get_feature_names_out(),'Count':np.array(X.sum(axis=0)).flatten()})
        freq=freq.sort_values(by='Count',ascending=False).head(10)
        fig,ax=plt.subplots()
        ax.bar(freq['Word'],freq['Count'],color="#17A2B8")
        st.pyplot(fig)

def download_csv(df):
    st.download_button("⬇️ CSV", df.to_csv(index=False).encode(), "results.csv", "text/csv")

def download_excel(df):
    output = BytesIO()
    df.to_excel(output,index=False)
    st.download_button("⬇️ Excel", output.getvalue(),"results.xlsx","application/vnd.ms-excel")

def download_json(df):
    st.download_button("⬇️ JSON", df.to_json(orient="records"),"results.json","application/json")

def download_pdf(df):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial","",10)
    pdf.cell(200,10,txt="AI Demo Results",ln=True,align="C")
    pdf.ln(10)
    for i in range(len(df)):
        pdf.multi_cell(0,8,str(df.iloc[i].to_dict()))
    st.download_button("📄 PDF", BytesIO(pdf.output(dest='S').encode('latin1')),"results.pdf","application/pdf")

# --- Top colored menu buttons ---
menu_labels=["ML & DL","NLP & LLMs","Computer Vision","Speech & Audio","Reinforcement",
             "Data & Preprocessing","Model Optimization","Agentic AI","MLOps"]
menu_colors=["#007BFF","#28A745","#17A2B8","#FFC107","#6F42C1","#FD7E14","#20C997","#DC3545","#6610F2"]

cols=st.columns(9)
for i,label in enumerate(menu_labels):
    if cols[i].button(label):
        st.session_state.menu=label
        st.session_state.df=None
        st.session_state.images=None
        n=st.session_state.n_records
        # Generate data immediately
        if label=="ML & DL": st.session_state.df=generate_classification(n)
        elif label=="NLP & LLMs": st.session_state.df=generate_text(n)
        elif label=="Data & Preprocessing": st.session_state.df=generate_regression(n)
        elif label=="Computer Vision": 
            st.session_state.images=generate_cv_images(n)
            st.session_state.df=pd.DataFrame({"Image_Index":list(range(len(st.session_state.images)))})
        elif label=="Reinforcement": 
            st.session_state.df=pd.DataFrame({"Step":range(n),"Reward":np.cumsum(np.random.randn(n))})
        elif label=="Model Optimization":
            st.session_state.df=pd.DataFrame({"Compression (%)": np.linspace(0,90,n),
                                             "Accuracy": np.linspace(98,70,n)+np.random.randn(n),
                                             "Latency (ms)": np.linspace(10,200,n)})
        elif label=="Agentic AI":
            steps=["Collect Data","Analyze Input","Call Model","Generate Output","Refine Result"]
            st.session_state.df=pd.DataFrame({"Step":steps,"Execution Time (s)":np.random.uniform(0.1,1.5,len(steps))})
        elif label=="MLOps":
            st.session_state.df=pd.DataFrame({"Metric":["Accuracy","Precision","Recall","F1 Score"],
                                             "Value":[round(random.uniform(0.7,0.99),2) for _ in range(4)]})
        elif label=="Speech & Audio":
            rate=44100
            t=np.linspace(0,1,n*441)
            amplitude=np.sin(2*np.pi*220*t)+np.random.normal(0,0.1,len(t))
            st.session_state.df=pd.DataFrame({"Time":t[:n*10],"Amplitude":amplitude[:n*10]})

st.markdown(f"### Selected Menu: {st.session_state.menu}")

# --- Reset button ---
if st.button("🔄 Reset All Data"):
    st.session_state.df=None
    st.session_state.images=None

# --- Display data ---
if st.session_state.df is not None:
    st.subheader("Dataset Preview")
    st.dataframe(st.session_state.df.head(100))
    plot_charts(st.session_state.df)
    download_csv(st.session_state.df)
    download_excel(st.session_state.df)
    download_json(st.session_state.df)
    download_pdf(st.session_state.df)

# --- Display CV images ---
if st.session_state.images is not None:
    st.subheader("Sample Images")
    img_cols=st.columns(5)
    for i,img in enumerate(st.session_state.images[:25]):
        img_cols[i%5].image(img,width=64)

# --- Play Audio for Speech & Audio ---
if st.session_state.menu=="Speech & Audio" and st.session_state.df is not None:
    st.subheader("🔊 Play Synthetic Audio")
    samples=(st.session_state.df['Amplitude'].values*32767).astype(np.int16)
    tmp_file=tempfile.NamedTemporaryFile(delete=False,suffix=".wav")
    write(tmp_file.name,44100,samples)
    st.audio(tmp_file.name)
    os.unlink(tmp_file.name)
