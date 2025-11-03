import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.feature_extraction.text import CountVectorizer
from fpdf import FPDF
from io import BytesIO
import random
from PIL import Image, ImageDraw

st.set_page_config(page_title="AI & LLM Platform", layout="wide")

# --- CSS for buttons ---
st.markdown("""
<style>
.menu-btn {border-radius:10px; padding:10px; font-weight:bold; color:white; margin-right:5px; margin-bottom:5px;}
.menu-ml{background-color:#007BFF;}
.menu-nlp{background-color:#28A745;}
.menu-cv{background-color:#17A2B8;}
.menu-speech{background-color:#FFC107;}
.menu-rl{background-color:#6F42C1;}
.menu-data{background-color:#FD7E14;}
.menu-opt{background-color:#20C997;}
.menu-agentic{background-color:#DC3545;}
.menu-mlops{background-color:#6610F2;}
.reset-btn{background-color:#343A40; color:white;}
.download-csv{background-color:#198754;color:white;}
.download-pdf{background-color:#FFC107;color:black;}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if 'menu' not in st.session_state:
    st.session_state.menu = 'home'
if 'df' not in st.session_state:
    st.session_state.df = None
if 'images' not in st.session_state:
    st.session_state.images = None

# --- Helper functions ---
def generate_classification(n):
    X, y = make_classification(n_samples=n, n_features=5, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df['Target'] = y
    return df

def generate_regression(n):
    X, y = make_regression(n_samples=n, n_features=5, noise=0.1, random_state=42)
    df = pd.DataFrame(X, columns=[f"Feature_{i}" for i in range(1,6)])
    df['Target'] = y
    return df

def generate_text(n):
    texts = ["AI is amazing", "I love machine learning", "Streamlit is powerful",
             "Data science is fun", "NLP is revolutionizing industries"]
    df = pd.DataFrame({'Text':[random.choice(texts) for _ in range(n)]})
    return df

def generate_cv_images(n, size=64):
    imgs=[]
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
            draw.line([random.randint(0,size),random.randint(0,size),random.randint(0,size),random.randint(0,size)],
                      fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), width=2)
        imgs.append(img)
    return imgs

def download_csv(df):
    st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "results.csv", "text/csv", key="csv")

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
    if "Text" in df.columns:
        st.subheader("Top 10 Words")
        vec = CountVectorizer()
        X = vec.fit_transform(df['Text'])
        freq = pd.DataFrame({'Word':vec.get_feature_names_out(),'Count':np.array(X.sum(axis=0)).flatten()})
        freq = freq.sort_values(by='Count',ascending=False).head(10)
        fig,ax=plt.subplots()
        ax.bar(freq['Word'],freq['Count'],color="#17A2B8")
        st.pyplot(fig)

# --- Top Menu ---
cols = st.columns(9)
menu_keys = ["home","ml","nlp","cv","speech","rl","data","opt","agentic","mlops"]
menu_labels = ["🏁 Home","1️⃣ ML & DL","2️⃣ NLP & LLMs","3️⃣ CV","4️⃣ Speech","5️⃣ RL","6️⃣ Data","7️⃣ Opt","8️⃣ Agentic","9️⃣ MLOps"]
colors = ["menu-ml","menu-ml","menu-nlp","menu-cv","menu-speech","menu-rl","menu-data","menu-opt","menu-agentic","menu-mlops"]

for i,col in enumerate(cols):
    if i>=len(menu_keys): break
    if col.button(menu_labels[i], key=menu_keys[i], help="Select "+menu_labels[i]):
        st.session_state.menu = menu_keys[i]
        st.session_state.df = None
        st.session_state.images = None
        st.experimental_rerun()

menu = st.session_state.menu

# --- Reset ---
if st.button("🔄 Reset All Data", key="reset", help="Reset session data"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

st.subheader(f"Selected Menu: {menu.upper()}")

n_records = st.slider("Select number of records", 1, 100, 50)
uploaded = st.file_uploader("Upload CSV/Excel/JSON", type=["csv","xlsx","json"])

if uploaded:
    if uploaded.name.endswith(".csv"): st.session_state.df=pd.read_csv(uploaded)
    elif uploaded.name.endswith(".xlsx"): st.session_state.df=pd.read_excel(uploaded)
    else: st.session_state.df=pd.read_json(uploaded)

# --- Generate Data ---
if st.button("Generate Synthetic Data"):
    if menu=="ml": st.session_state.df = generate_classification(n_records)
    elif menu=="nlp": st.session_state.df = generate_text(n_records)
    elif menu=="data": st.session_state.df = generate_regression(n_records)
    elif menu=="cv":
        st.session_state.images = generate_cv_images(n_records)
        st.subheader("Sample Images")
        img_cols=st.columns(5)
        for i,img in enumerate(st.session_state.images[:25]):
            img_cols[i%5].image(img,width=64)
        st.session_state.df=pd.DataFrame({"Image_Index": list(range(len(st.session_state.images)))})

if st.session_state.df is not None:
    st.subheader("Dataset Preview")
    st.dataframe(st.session_state.df.head(50))
    plot_charts(st.session_state.df)

# --- Downloads ---
if st.session_state.df is not None:
    download_csv(st.session_state.df)
    download_pdf(st.session_state.df)
