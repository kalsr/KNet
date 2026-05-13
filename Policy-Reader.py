# ============================================================
# POLICY READER & QUESTION ANSWERING SYSTEM
# Developed by Randy Singh, Kalsnet (KNet) Consulting Group
# ============================================================

import os
import io
import json
import time
import tempfile
from pathlib import Path
from datetime import datetime

import pandas as pd
import streamlit as st
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
from docx import Document

# PDF generation
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Optional Groq AI support
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Policy Reader & QA System",
    page_icon="📘",
    layout="wide"
)

# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
POLICY_DIR = "policies"
SUPPORTED_EXTENSIONS = [".txt", ".pdf", ".docx"]

# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------
def ensure_policy_folder():
    Path(POLICY_DIR).mkdir(exist_ok=True)


def get_policy_files():
    ensure_policy_folder()
    files = []
    for file in Path(POLICY_DIR).iterdir():
        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(file)
    return sorted(files, key=lambda x: x.name.lower())


@st.cache_data(show_spinner=False)
def load_text_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


@st.cache_data(show_spinner=False)
def load_pdf_file(path):
    reader = PdfReader(path)
    pages = []  # list of (page_number, text)
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append((i, text))
    return pages


@st.cache_data(show_spinner=False)
def load_docx_file(path):
    doc = Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text


@st.cache_data(show_spinner=False)
def build_index(file_path):
    """
    Builds a line-based index similar to the original Java program.
    Each line becomes an indexed item with page number, line number, and source.
    """
    suffix = file_path.suffix.lower()
    source_name = file_path.stem
    items = []  # list of dictionaries

    if suffix == ".txt":
        text = load_text_file(file_path)
        lines = text.splitlines()
        for line_num, line in enumerate(lines, start=1):
            if line.strip():
                items.append({
                    "source": source_name,
                    "page": 1,
                    "line": line_num,
                    "answer": line.strip(),
                })

    elif suffix == ".pdf":
        pages = load_pdf_file(file_path)
        for page_num, page_text in pages:
            lines = page_text.splitlines()
            for line_num, line in enumerate(lines, start=1):
                if line.strip():
                    items.append({
                        "source": source_name,
                        "page": page_num,
                        "line": line_num,
                        "answer": line.strip(),
                    })

    elif suffix == ".docx":
        text = load_docx_file(file_path)
        lines = text.splitlines()
        for line_num, line in enumerate(lines, start=1):
            if line.strip():
                items.append({
                    "source": source_name,
                    "page": 1,
                    "line": line_num,
                    "answer": line.strip(),
                })

    return items


def search_items(items, query):
    """
    Faithful to the Java logic:
    return items whose answer contains the query string.
    """
    query = query.lower().strip()
    if not query:
        return []

    matches = []
    for item in items:
        if query in item["answer"].lower():
            matches.append(item)
    return matches


# ------------------------------------------------------------
# Optional AI with Groq
# ------------------------------------------------------------
def get_groq_client():
    if not GROQ_AVAILABLE:
        return None

    api_key = None

    # Try Streamlit secrets
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        api_key = None

    # Try environment variable
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    try:
        return Groq(api_key=api_key)
    except Exception:
        return None



def generate_ai_answer(query, matches):
    client = get_groq_client()
    if client is None:
        return None

    context = "\n".join(
        [
            f"[{m['source']} | Page {m['page']} | Line {m['line']}] {m['answer']}"
            for m in matches[:50]
        ]
    )

    if not context.strip():
        return "No relevant policy text was found."

    prompt = f"""
You are a policy analysis assistant.
Use ONLY the provided policy excerpts.
Answer the user's question concisely and cite page and line references when relevant.

QUESTION:
{query}

POLICY EXCERPTS:
{context}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=1000,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {e}"


# ------------------------------------------------------------
# Export Functions
# ------------------------------------------------------------
def export_json(results, query):
    payload = {
        "query": query,
        "timestamp": datetime.now().isoformat(),
        "results": results,
    }
    return json.dumps(payload, indent=2)



def export_csv(results):
    df = pd.DataFrame(results)
    return df.to_csv(index=False)



def export_pdf(results, query, ai_answer=None):
    buffer = io.BytesIO()

    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    normal.fontName = "HeiseiMin-W3"

    story = []

    story.append(Paragraph("Policy Reader & Question Answering System", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Developed by Randy Singh, Kalsnet (KNet) Consulting Group", normal))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Query: {query}", normal))
    story.append(Paragraph(f"Generated: {datetime.now()}", normal))
    story.append(Spacer(1, 12))

    if ai_answer:
        story.append(Paragraph("AI Summary", styles["Heading2"]))
        story.append(Paragraph(ai_answer.replace("\n", "<br/>"), normal))
        story.append(Spacer(1, 12))

    story.append(Paragraph("Search Results", styles["Heading2"]))

    for i, row in enumerate(results, start=1):
        block = [
            Paragraph(
                f"<b>{i}.</b> {row['answer']}", normal
            ),
            Paragraph(
                f"Source: {row['source']} | Page {row['page']} | Line {row['line']}", normal
            ),
            Spacer(1, 8),
        ]
        story.append(KeepTogether(block))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.markdown(
    """
    <div style='background: linear-gradient(90deg, #0b3d91, #1e88e5);
                padding: 20px; border-radius: 12px; color: white;'>
        <h1 style='margin: 0;'>📘 Policy Reader & Question Answering System</h1>
        <p style='margin: 6px 0 0 0; font-size: 18px;'>Developed by Randy Singh, Kalsnet (KNet) Consulting Group</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("")

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
st.sidebar.header("Configuration")
use_ai = st.sidebar.checkbox("Enable AI Summary (Groq)", value=True)
show_limit = st.sidebar.slider("Maximum Results to Display", 10, 500, 100)

# ------------------------------------------------------------
# File Selection
# ------------------------------------------------------------
policy_files = get_policy_files()

if not policy_files:
    st.warning(
        "No policy files found. Create a 'policies' folder and add TXT, PDF, or DOCX files."
    )
    st.stop()

selected_files = st.multiselect(
    "Select Policy Documents",
    options=policy_files,
    default=[policy_files[0]],
    format_func=lambda p: p.name,
)

if not selected_files:
    st.info("Please select at least one policy document.")
    st.stop()

# ------------------------------------------------------------
# Build Combined Index
# ------------------------------------------------------------
with st.spinner("Loading and indexing policy documents..."):
    all_items = []
    for path in selected_files:
        all_items.extend(build_index(path))

st.success(f"Indexed {len(all_items):,} lines from {len(selected_files)} document(s).")

# ------------------------------------------------------------
# Query Input
# ------------------------------------------------------------
query = st.text_input(
    "Enter a word or question to search",
    placeholder="Example: telework, smoking, equal employment, ethical conduct",
)

if st.button("🔍 Search Policies", type="primary") and query.strip():
    start = time.time()

    results = search_items(all_items, query)
    results = results[:show_limit]

    elapsed = time.time() - start

    st.session_state["last_query"] = query
    st.session_state["last_results"] = results

    # Optional AI answer
    ai_answer = None
    if use_ai and results:
        with st.spinner("Generating AI summary using Groq..."):
            ai_answer = generate_ai_answer(query, results)

    st.session_state["last_ai_answer"] = ai_answer

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Matches Found", len(results))
    c2.metric("Documents Searched", len(selected_files))
    c3.metric("Search Time", f"{elapsed:.3f} sec")

    # AI Summary
    if ai_answer:
        st.subheader("🤖 AI Summary")
        st.write(ai_answer)

    # Results
    st.subheader("📄 Matching Results")

    if results:
        for idx, row in enumerate(results, start=1):
            with st.expander(
                f"Result {idx}: {row['source']} | Page {row['page']} | Line {row['line']}"
            ):
                st.write(row["answer"])
    else:
        st.warning("No matching items found.")

# ------------------------------------------------------------
# Export Section
# ------------------------------------------------------------
if "last_results" in st.session_state:
    results = st.session_state["last_results"]
    query = st.session_state.get("last_query", "")
    ai_answer = st.session_state.get("last_ai_answer")

    st.markdown("---")
    st.subheader("📤 Export Results")

    col1, col2, col3 = st.columns(3)

    # JSON
    json_data = export_json(results, query)
    col1.download_button(
        "Download JSON",
        data=json_data,
        file_name="policy_results.json",
        mime="application/json",
    )

    # CSV
    csv_data = export_csv(results)
    col2.download_button(
        "Download CSV",
        data=csv_data,
        file_name="policy_results.csv",
        mime="text/csv",
    )

    # PDF
    pdf_data = export_pdf(results, query, ai_answer)
    col3.download_button(
        "Download PDF",
        data=pdf_data,
        file_name="policy_results.pdf",
        mime="application/pdf",
    )

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.caption(
    "Kalsnet (KNet) Consulting Group | Policy Search, Retrieval, and AI-Assisted Analysis"
)
