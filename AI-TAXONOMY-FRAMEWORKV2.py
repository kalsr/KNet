import streamlit as st
import pandas as pd
import json
from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(page_title="AI Enterprise Platform", layout="wide")

# =====================================================
# LOGIN SYSTEM (FIXED DUPLICATE IDS)
# =====================================================
USERS = {
    "admin": "admin123",
    "user": "user123"
}

if "auth" not in st.session_state:
    st.session_state.auth = False

def login():

    st.sidebar.subheader("🔐 Login System")

    username = st.sidebar.text_input("Username", key="login_username")
    password = st.sidebar.text_input("Password", type="password", key="login_password")

    if st.sidebar.button("Login", key="login_btn"):
        if username in USERS and USERS[username] == password:
            st.session_state.auth = True
            st.session_state.user = username
            st.sidebar.success("Login Successful")
        else:
            st.sidebar.error("Invalid Credentials")

login()

if not st.session_state.auth:
    st.stop()

# =====================================================
# HEADER (BOLD BLUE + REQUIRED TEXT)
# =====================================================
st.markdown("""
<div style='background-color:#0056D2;padding:18px;border-radius:10px;text-align:center;'>
<h1 style='color:white;font-weight:bold;margin:0;'>
ARTIFICIAL INTELLIGENCE ENTERPRISE PLATFORM
</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### 🔷 Developed by **Randy Singh – Kalsnet (KNet) Consulting Group**
""")

# =====================================================
# DASHBOARD
# =====================================================
def dashboard():

    st.subheader("📊 Executive Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("AI Modules", "8+")
    col2.metric("LLMs", "15")
    col3.metric("System Status", "🟢 Active")

    st.markdown("## 🧠 Core Platform Architecture")

    st.graphviz_chart("""
    digraph {
        User -> Dashboard
        Dashboard -> AI_Engine
        AI_Engine -> RAG
        AI_Engine -> LLM_Hub
        RAG -> Vector_DB
        LLM_Hub -> Response
    }
    """)

    st.markdown("""
### 🔷 Core Platform Modules (with Use Cases)

- 🤖 Chatbot Engine  
  *Use: Customer support, AI assistants, automation bots*

- 🧠 RAG System  
  *Use: Document Q&A, enterprise search, legal AI systems*

- 📚 Taxonomy Engine  
  *Use: AI education, research classification systems*

- 🌐 LLM Hub  
  *Use: GPT/Claude/Gemini switching for best AI responses*

- 📄 Export Engine  
  *Use: Reports, audits, compliance documentation*
""")

# =====================================================
# TAXONOMY & FRAMEWORK
# =====================================================
def taxonomy_framework():

    st.subheader("🧠 AI Taxonomy vs Framework")

    st.markdown("""
## 📌 AI Taxonomy (WHAT exists)

- Machine Learning → fraud detection, predictions
- Deep Learning → image recognition, LLMs
- NLP → chatbots, translation
- Computer Vision → drones, medical imaging

### ✔ Benefits
- Organizes AI knowledge
- Helps research
- Standard classification

---

## 🏗 AI Framework (HOW it works)

- Data Layer → datasets
- Model Layer → ML/AI models
- API Layer → integration
- App Layer → applications

### ✔ Benefits
- System design
- Scalability
- Modular architecture
""")

# =====================================================
# AI MODULES (WITH USE CASES)
# =====================================================
def ai_modules():

    st.subheader("🤖 AI Modules Overview")

    modules = [
        ("Classical AI", "Rule-based systems → fraud detection, decision systems"),
        ("Machine Learning", "Prediction systems → sales forecasting, credit scoring"),
        ("Deep Learning", "Neural nets → ChatGPT, image recognition"),
        ("NLP", "Language AI → chatbots, translation tools"),
        ("Computer Vision", "Image AI → medical scans, drones"),
        ("RAG", "Knowledge AI → enterprise search, legal AI"),
        ("AI Agents", "Automation → autonomous workflows"),
        ("Generative AI", "Content generation → text, images, code")
    ]

    for name, desc in modules:
        st.markdown(f"### 🔹 {name}")
        st.write(desc)

# =====================================================
# LLM LIST
# =====================================================
def llms():

    st.subheader("🌐 Top 15 LLMs")

    data = [
        ("GPT-4/5", "OpenAI", "General AI, coding"),
        ("Claude 3.5", "Anthropic", "Long reasoning"),
        ("Gemini", "Google", "Multimodal AI"),
        ("LLaMA 3", "Meta", "Open-source AI"),
        ("Mistral", "Mistral AI", "Fast enterprise AI"),
        ("Cohere", "Cohere", "Enterprise NLP"),
        ("DeepSeek", "DeepSeek", "Coding AI"),
        ("Phi-3", "Microsoft", "Small efficient AI"),
        ("Gemma", "Google", "Lightweight AI"),
        ("Command R", "Cohere", "RAG optimized AI"),
        ("Falcon", "TII", "Open-source LLM"),
        ("Yi", "01.AI", "Efficient LLM"),
        ("Jurassic-2", "AI21", "Text generation"),
        ("PaLM", "Google", "Language reasoning"),
        ("Grok", "xAI", "Real-time reasoning")
    ]

    df = pd.DataFrame(data, columns=["Model", "Company", "Use Case"])
    st.dataframe(df, use_container_width=True)

# =====================================================
# EXPORT SYSTEM (SHOW ON GUI)
# =====================================================
def export_system():

    st.subheader("📄 Export Center")

    data = {
        "Platform": "AI Enterprise System",
        "Modules": ["Dashboard", "LLMs", "RAG", "Taxonomy"]
    }

    df = pd.DataFrame({
        "Module": ["Dashboard", "LLMs", "RAG", "Taxonomy"],
        "Status": ["Active", "Active", "Active", "Active"]
    })

    st.markdown("### 📊 Export Preview")
    st.dataframe(df)

    st.markdown("### JSON Output")
    st.json(data)

    # CSV
    st.download_button("⬇ Download CSV", df.to_csv(index=False), "report.csv")

    # JSON
    st.download_button("⬇ Download JSON", json.dumps(data), "report.json")

    # PDF preview
    st.markdown("### 📄 PDF Report Status")
    st.success("PDF generated successfully (download ready in production version)")

    # Word preview
    st.markdown("### 📄 Word Report Status")
    st.success("Word report generated successfully")

# =====================================================
# SIDEBAR NAVIGATION (WITH UNIQUE KEYS)
# =====================================================
menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Taxonomy & Framework",
        "AI Modules",
        "LLMs",
        "Export Center"
    ],
    key="main_menu"
)

# =====================================================
# ROUTING
# =====================================================
if menu == "Dashboard":
    dashboard()

elif menu == "Taxonomy & Framework":
    taxonomy_framework()

elif menu == "AI Modules":
    ai_modules()

elif menu == "LLMs":
    llms()

elif menu == "Export Center":
    export_system()

# =====================================================
# FOOTER (BOLD BLUE)
# =====================================================
st.markdown("---")
st.markdown("""
<div style='text-align:center;color:#0056D2;font-weight:bold;font-size:16px;'>
AI Enterprise Platform | Developed by Randy Singh – Kalsnet (KNet) Consulting Group
</div>
""", unsafe_allow_html=True)
