# ==========================================================
# KALSNET (KNet) – LLM SELECTOR STUDIO (ENTERPRISE GUI)
# Developed by Randy Singh
# ==========================================================

import streamlit as st
import pandas as pd
import json
import datetime
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="KNet LLM Selector Studio", layout="wide")

# -------------------------------
# HEADER (PROFESSIONAL BLUE STYLE)
# -------------------------------
st.markdown(
    """
    <h1 style='color:#0B3D91; text-align:center; font-weight:bold;'>
    KALSNET (KNet) – Large Language Model (LLM) Platform
    </h1>
    <h3 style='color:#0B3D91; text-align:center; font-weight:bold;'>
    Developed by Randy Singh – Kalsnet (KNet) Consulting Group
    </h3>
    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# LLM LINKS (FROM YOUR JAVA CODE)
# -------------------------------
llm_links = {
    "GPT-3": "https://chat.openai.com/",
    "Google-Bard": "https://cloud.google.com/natural-language#section-2",
    "T5": "https://heidloff.net/article/running-llm-flan-t5-locally/",
    "GPT-3.5": "https://chat.openai.com/",
    "GPT-4": "https://chat.openai.com/",
    "LLaMA": "https://replicate.com/blog/run-llama-2-with-an-api",
    "LaMDA": "https://blog.google/technology/ai/lamda/",
    "Bing-ChatGPT": "https://portal.azure.us/#home",
    "GPT-2": "https://chat.openai.com/",
    "XLM-R": "https://huggingface.co/docs/transformers/model_doc/xlm-roberta"
}

# -------------------------------
# USER INPUT
# -------------------------------
st.subheader("💡 Enter Your Prompt / Task")
user_input = st.text_area("Type your request here...", height=150)

# -------------------------------
# LLM BUTTON GRID (COLORED)
# -------------------------------
st.subheader("🚀 Select LLM Platform")

cols = st.columns(5)

selected_llm = None

for i, (llm, url) in enumerate(llm_links.items()):
    if cols[i % 5].button(f"🔷 {llm}"):
        selected_llm = llm
        st.markdown(f"### 🌐 Launching [{llm}]({url})")

# -------------------------------
# SIMULATED LLM RESPONSE
# -------------------------------
st.subheader("🤖 LLM Response")

response = ""
if selected_llm and user_input:
    response = f"[{selected_llm}] Response:\n\nProcessed Task: {user_input}\n\nGenerated Insight: This is a simulated AI response for demonstration purposes."
    st.success(response)

# -------------------------------
# EXPORT OPTIONS
# -------------------------------
st.subheader("📤 Export Results")

if response:

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # JSON EXPORT
    json_data = {
        "llm": selected_llm,
        "input": user_input,
        "response": response,
        "timestamp": timestamp
    }

    st.download_button(
        label="⬇️ Download JSON",
        data=json.dumps(json_data, indent=4),
        file_name=f"llm_output_{timestamp}.json",
        mime="application/json"
    )

    # CSV EXPORT
    df = pd.DataFrame([json_data])
    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name=f"llm_output_{timestamp}.csv",
        mime="text/csv"
    )

    # PDF EXPORT
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph("KALSNET LLM OUTPUT REPORT", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"LLM: {selected_llm}", styles['Normal']))
    story.append(Paragraph(f"Input: {user_input}", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Response: {response}", styles['Normal']))

    doc.build(story)

    st.download_button(
        label="⬇️ Download PDF",
        data=buffer.getvalue(),
        file_name=f"llm_output_{timestamp}.pdf",
        mime="application/pdf"
    )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray;'>
    Enterprise Agentic-AI Interface | Multi-LLM Orchestration | Kalsnet (KNet)
    </p>
    """,
    unsafe_allow_html=True
)