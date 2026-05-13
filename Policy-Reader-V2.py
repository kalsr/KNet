

# Policy_Intelligence_QA_Enhanced.py

#```python
import streamlit as st
import json
import re
import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.fonts import addMapping

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Policy Intelligence Q&A System", layout="wide")

# ===============================
# HEADER / BRANDING
# ===============================
st.markdown(
    """
    <div style="background-color:#0f172a;padding:15px;border-radius:10px">
        <h2 style="color:white;text-align:center; margin-bottom:5px;">
            Policy Intelligence Q&amp;A System
        </h2>
        <h4 style="color:#cbd5e1;text-align:center; margin-top:0;">
            Developed by Randy Singh from Kalsnet (KNet) Consulting Group
        </h4>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ===============================
# SESSION STATE INIT
# ===============================
if "policy_text" not in st.session_state:
    st.session_state.policy_text = ""

if "policy_name" not in st.session_state:
    st.session_state.policy_name = ""

if "qa_results" not in st.session_state:
    st.session_state.qa_results = []

# ===============================
# STOP WORDS
# ===============================
STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "what", "when",
    "where", "who", "why", "how", "is", "are", "was", "were", "be", "been",
    "being", "to", "of", "in", "on", "for", "with", "by", "at", "from",
    "this", "that", "these", "those", "do", "does", "did", "can", "could",
    "should", "would", "will", "must", "about", "say", "says", "policy",
    "under", "into", "it", "its", "as", "than", "please"
}

# ===============================
# HELPER FUNCTIONS
# ===============================
def normalize_text(text):
    return re.sub(r"\\s+", " ", text).strip()


def extract_keywords(question):
    words = re.findall(r"[A-Za-z0-9_-]+", question.lower())
    return [w for w in words if w not in STOP_WORDS and len(w) > 2]



def parse_policy(policy_text):
    """
    Break policy into paragraphs separated by blank lines.
    Track paragraph number and line number range.
    """
    lines = policy_text.splitlines()
    paragraphs = []

    current_lines = []
    start_line = 1
    paragraph_number = 1

    for i, line in enumerate(lines, start=1):
        if line.strip():  # non-empty line
            if not current_lines:
                start_line = i
            current_lines.append(line.rstrip())
        else:
            if current_lines:
                text = " ".join(current_lines)
                paragraphs.append({
                    "paragraph": paragraph_number,
                    "start_line": start_line,
                    "end_line": i - 1,
                    "text": normalize_text(text),  # searchable version
                    "raw_text": "\n".join(current_lines),  # display version
                })
                paragraph_number += 1
                current_lines = []

    # Add last paragraph if present
    if current_lines:
        text = " ".join(current_lines)
        paragraphs.append({
            "paragraph": paragraph_number,
            "start_line": start_line,
            "end_line": len(lines),
            "text": normalize_text(text),
            "raw_text": "\n".join(current_lines),
        })

    return paragraphs



def score_paragraph(paragraph_text, keywords, full_question):
    """
    Score paragraph relevance.
    - Exact question phrase gets a large boost.
    - Each keyword occurrence adds to score.
    - Numbered requirements get slight boost.
    """
    text_lower = paragraph_text.lower()
    score = 0
    matched_keywords = []  # unique list

    # Exact question boost
    question_phrase = normalize_text(full_question.lower())
    if question_phrase and question_phrase in text_lower:
        score += 50

    # Keyword scoring
    seen = set()
    for kw in keywords:
        occurrences = text_lower.count(kw)
        if occurrences > 0:
            score += occurrences * 10
            if kw not in seen:
                matched_keywords.append(kw)
                seen.add(kw)

    # Bonus for numbered requirements
    if re.search(r"\\b\\d+\\.", paragraph_text):  # 1. 2. 3.
        score += 5

    return score, matched_keywords



def build_summary(matches):
    if not matches:
        return "No relevant information was found in the uploaded policy."

    best = matches[0]
    return (
        f"Based on the uploaded policy, the most relevant information appears in "
        f"Paragraph {best['paragraph']} (Lines {best['start_line']}-{best['end_line']}). "
        f"The policy states: {best['raw_text']}"
    )



def get_policy_answer(policy, question):
    keywords = extract_keywords(question)

    if not keywords:
        return {
            "answer": "Please enter a more specific question containing meaningful keywords.",
            "details": []
        }

    paragraphs = parse_policy(policy)
    matches = []  # list of dicts with score + metadata

    for p in paragraphs:
        score, matched_keywords = score_paragraph(p["text"], keywords, question)
        if score > 0:
            matches.append({
                **p,
                "score": score,
                "matched_keywords": matched_keywords,
            })

    # Sort by highest score first, then earliest paragraph
    matches.sort(key=lambda x: (-x["score"], x["paragraph"]))

    # Keep top 5 results
    top_matches = matches[:5]

    return {
        "answer": build_summary(top_matches),
        "details": top_matches,
    }



def export_json(data):
    return json.dumps(data, indent=4).encode("utf-8")



def export_csv(data):
    df = pd.DataFrame(data)
    return df.to_csv(index=False).encode("utf-8")



def export_pdf(data):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Policy Q&amp;A Report", styles["Title"]))
    story.append(Spacer(1, 12))

    for item in data:
        story.append(Paragraph(f"Q: {item['question']}", styles["Normal"]))
        story.append(Paragraph(f"A: {item['answer']}", styles["Normal"]))
        story.append(Spacer(1, 10))

    doc.build(story)
    buffer.seek(0)
    return buffer


# ===============================
# POLICY UPLOAD SECTION
# ===============================
st.subheader("📄 Upload Policy File (.txt)")

uploaded_file = st.file_uploader("Upload Policy File", type=["txt"])

if uploaded_file:
    st.session_state.policy_text = uploaded_file.read().decode("utf-8")
    st.session_state.policy_name = uploaded_file.name
    st.success(f"Policy loaded successfully: {uploaded_file.name}")

# Show policy preview
if st.session_state.policy_text:
    with st.expander("📖 View Loaded Policy"):
        st.text(st.session_state.policy_text)

# ===============================
# Q&A SECTION
# ===============================
st.subheader("❓ Ask Questions on Policy")

question = st.text_input("Enter your question")

if st.button("Get Answer"):
    if not st.session_state.policy_text:
        st.error("Policy does not exist so please add the policy to do any question answer.")
    elif not question.strip():
        st.error("Please enter a question")
    else:
        result_data = get_policy_answer(st.session_state.policy_text, question)
        answer = result_data["answer"]
        details = result_data["details"]

        # Save to history
        st.session_state.qa_results.append({
            "policy_file": st.session_state.policy_name,
            "question": question,
            "answer": answer,
        })

        # Display answer
        st.subheader("📌 Answer")
        st.success(answer)

        # Detailed references
        if details:
            st.subheader("📍 Supporting References")

            for item in details:
                with st.expander(
                    f"Paragraph {item['paragraph']} | Lines {item['start_line']}-{item['end_line']} | Score {item['score']}"
                ):
                    st.write(
                        f"**Matching Keywords:** {', '.join(item['matched_keywords'])}"
                    )
                    st.text(item['raw_text'])
        else:
            st.info("No specific supporting paragraphs were found.")

        st.success("Query processed successfully")

# ===============================
# RESULTS DISPLAY
# ===============================
if st.session_state.qa_results:
    st.subheader("📊 Query History")

    df = pd.DataFrame(st.session_state.qa_results)
    st.dataframe(df, use_container_width=True)

# ===============================
# DOWNLOAD SECTION
# ===============================
st.subheader("⬇️ Export Results")

if st.session_state.qa_results:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            "Download JSON",
            data=export_json(st.session_state.qa_results),
            file_name="policy_results.json",
            mime="application/json",
        )

    with col2:
        st.download_button(
            "Download CSV",
            data=export_csv(st.session_state.qa_results),
            file_name="policy_results.csv",
            mime="text/csv",
        )

    with col3:
        st.download_button(
            "Download PDF",
            data=export_pdf(st.session_state.qa_results),
            file_name="policy_results.pdf",
            mime="application/pdf",
        )

    if st.button("Clear Query History"):
        st.session_state.qa_results = []
        st.rerun()
else:
    st.info("No results available for export yet.")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("Kalsnet (KNet) Consulting Group © 2026 | Policy Intelligence Q&A System")

## Run the Application

