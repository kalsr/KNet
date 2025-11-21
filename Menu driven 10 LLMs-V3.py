

# python
# Menu driven 10 LLMs - V3 (NO experimental_rerun)

import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="10 LLM Demo", layout="wide")

# -------------------------
# Title Bar
# -------------------------
st.markdown(
    """
    <div style='background-color:#f2f2f2;padding:14px;border-radius:6px;margin-bottom:10px;'>
      <h1 style='color:#000000;text-align:center;font-weight:900;margin:0;font-size:22px;'>
        This application is designed by Randy Singh from KNet Consulting Group
      </h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Initialize session state
# -------------------------
LLMS = [
    "GPT4All", "LLaMA", "MPT", "Falcon", "BLOOM",
    "Dolly", "Vicuna", "OpenAssistant", "RWKV", "Alpaca"
]

COLORS = [
    "#FF6B6B", "#4D96FF", "#9B5DE5", "#38C172", "#FFB703",
    "#FF6FCF", "#00D1B2", "#FFD166", "#FF8A65", "#7EE7C5"
]

if "active_llm" not in st.session_state:
    st.session_state.active_llm = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {llm: [] for llm in LLMS}
if "sample_data" not in st.session_state:
    st.session_state.sample_data = None
if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = None

# -------------------------
# Dummy LLM Executor
# -------------------------
def dummy_llm_execute(llm_name, prompt_text):
    ts = datetime.datetime.utcnow().isoformat(sep=' ', timespec='seconds')
    return (
        f"(Demo response from {llm_name} at {ts})\n\n"
        f"Prompt received: {prompt_text}\n\n"
        f"Replace this with real API call."
    )

# -------------------------
# Reset All Data
# -------------------------
def reset_all():
    st.session_state.chat_history = {llm: [] for llm in LLMS}
    st.session_state.sample_data = None
    st.session_state.uploaded_data = None
    st.session_state.active_llm = None

# -------------------------
# MAIN MENU (no LLM selected)
# -------------------------
if st.session_state.active_llm is None:

    st.markdown("### Select an LLM to open")

    for row in range(2):
        cols = st.columns(5)
        for i in range(5):
            idx = row * 5 + i
            llm_name = LLMS[idx]
            color = COLORS[idx]

            with cols[i]:
                st.markdown(
                    f"""
                    <div style="background:{color};padding:10px;border-radius:8px;min-height:68px;
                                display:flex;align-items:center;justify-content:center;">
                        <div style="font-weight:800;color:#fff;text-align:center;font-size:15px;">
                            {llm_name}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(f"Open {llm_name}", key=f"open_{llm_name}"):
                    st.session_state.active_llm = llm_name

    st.markdown("---")
    st.subheader("Sample Data Generator")

    size = st.slider("Number of rows", 1, 500, 10)
    if st.button("Generate Sample Data"):
        st.session_state.sample_data = pd.DataFrame({
            "id": list(range(1, size + 1)),
            "value": [round(x * 0.75, 2) for x in range(size)]
        })
        st.success("Sample data generated!")

    if st.session_state.sample_data is not None:
        st.dataframe(st.session_state.sample_data)

    st.markdown("---")
    st.subheader("Upload Data")

    uploaded = st.file_uploader("Upload CSV/XLSX/JSON")
    if uploaded:
        try:
            if uploaded.name.endswith(".csv"):
                df = pd.read_csv(uploaded)
            elif uploaded.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded)
            else:
                df = pd.read_json(uploaded)
            st.session_state.uploaded_data = df
            st.success("Upload successful!")
            st.dataframe(df)
        except Exception as e:
            st.error(str(e))

    st.markdown("---")
    if st.button("Reset All Data"):
        reset_all()
        st.success("All data cleared!")

# -------------------------
# LLM PAGE
# -------------------------
else:
    llm = st.session_state.active_llm
    st.subheader(f"LLM: {llm}")

    st.info("This is a demo interface. Replace dummy_llm_execute() with your real LLM API.")

    prompt = st.text_area("Enter your prompt:", height=200)

    colA, colB = st.columns([1, 1])
    with colA:
        if st.button("Run"):
            if prompt.strip():
                response = dummy_llm_execute(llm, prompt)
                st.session_state.chat_history[llm].insert(0, {
                    "prompt": prompt,
                    "response": response,
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                st.warning("Enter a prompt first.")

    with colB:
        if st.button("Exit to Menu"):
            st.session_state.active_llm = None

    st.markdown("---")

    st.subheader("Chat History")

    history = st.session_state.chat_history.get(llm, [])

    if not history:
        st.write("No chats yet.")
    else:
        for msg in history:
            st.markdown(f"**[{msg['time']}] Prompt:**")
            st.write(msg["prompt"])
            st.markdown("**Response:**")
            st.code(msg["response"])
            st.markdown("---")

    if st.button("Clear History for this LLM"):
        st.session_state.chat_history[llm] = []
        st.success("Chat history cleared!")

# Footer  
st.markdown("<hr><center><small>Developed by Randy Singh, KNet Consulting Group.</small></center>", unsafe_allow_html=True)
