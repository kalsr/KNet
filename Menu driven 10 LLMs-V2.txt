

# python
# streamlit_10_llm_demo_fixed.py

import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="LLM Demo App", layout="wide")

# -----------------------
# Title Bar (Bold Black)
# -----------------------
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

# -----------------------
# LLM List + Colors + Logos (optional)
# -----------------------
LLMS = [
    "GPT4All", "LLaMA", "MPT", "Falcon", "BLOOM",
    "Dolly", "Vicuna", "OpenAssistant", "RWKV", "Alpaca"
]

# 10 distinct pleasant colors
BUTTON_COLORS = [
    "#FF6B6B", "#4D96FF", "#9B5DE5", "#38C172", "#FFB703",
    "#FF6FCF", "#00D1B2", "#FFD166", "#FF8A65", "#7EE7C5"
]

# session init
if "active_llm" not in st.session_state:
    st.session_state.active_llm = None
if "chat_history" not in st.session_state:
    # chat_history keyed by llm name -> list of {ts, prompt, response}
    st.session_state.chat_history = {llm: [] for llm in LLMS}
if "sample_data" not in st.session_state:
    st.session_state.sample_data = None
if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = None

# -----------------------
# Functions
# -----------------------
def go_to_llm(llm_name):
    st.session_state.active_llm = llm_name
    # safe rerun only inside handler
    st.experimental_rerun()

def exit_llm():
    st.session_state.active_llm = None
    st.experimental_rerun()

def reset_all_data():
    # preserve nothing except UI state defaults
    preserved = {}
    st.session_state.clear()
    # reinitialize minimal keys
    st.session_state.active_llm = None
    st.session_state.chat_history = {llm: [] for llm in LLMS}
    st.session_state.sample_data = None
    st.session_state.uploaded_data = None
    st.experimental_rerun()

def dummy_llm_execute(llm_name, prompt_text):
    # Replace this with a real API call later.
    ts = datetime.datetime.utcnow().isoformat(sep=' ', timespec='seconds')
    # Simple deterministic echo + metadata
    resp = f"(Demo response from {llm_name} at {ts})\n\n" \
           f"Prompt received ({len(prompt_text)} chars):\n{prompt_text}\n\n" \
           f"Tip: Replace dummy_llm_execute with real API integration."
    return resp

# -----------------------
# Top: LLM Buttons (two rows of 5)
# -----------------------
st.markdown("### Select an LLM to demo")
# produce 2 rows of 5 cols for visual balance
for row in range(2):
    cols = st.columns(5, gap="medium")
    for i in range(5):
        idx = row * 5 + i
        llm_name = LLMS[idx]
        color = BUTTON_COLORS[idx]
        with cols[i]:
            # rectangle card with label and a hidden button below
            st.markdown(
                f"""
                <div style="background:{color};padding:10px;border-radius:8px;min-height:68px;display:flex;
                            align-items:center;justify-content:center;">
                  <div style="font-weight:800;color:#111;text-align:center;font-size:15px;">
                    {llm_name}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            # place the actionable button (visually separate, but aligned)
            if st.button(f"Open {llm_name}", key=f"open_{llm_name}"):
                go_to_llm(llm_name)

st.markdown("---")

# -----------------------
# If no LLM selected -> show main menu features
# -----------------------
if st.session_state.active_llm is None:
    st.subheader("Main Menu / Demo Controls")

    # Show quick instructions for each LLM in expander
    with st.expander("Instructions for all LLMs (click to open)"):
        st.write("This demo shows how to connect to many open-source LLMs. For real responses, integrate "
                 "each model's API or run a local inference server and replace the `dummy_llm_execute` function.")

        for idx, llm in enumerate(LLMS, start=1):
            st.markdown(f"**{idx}. {llm}** — See vendor pages or Hugging Face for downloads/configuration.")

    # Sample data generator
    st.subheader("Sample Data Generator")
    sample_size = st.slider("Select number of sample data points:", min_value=1, max_value=500, value=10)
    if st.button("Generate Sample Data", key="generate_sample"):
        df = pd.DataFrame({
            "id": list(range(1, sample_size + 1)),
            "value": [round(x * 0.75 + 10, 2) for x in range(sample_size)]
        })
        st.session_state.sample_data = df
        st.success(f"{sample_size} rows generated.")
        st.dataframe(df)

    if st.session_state.sample_data is not None:
        st.markdown("**Existing sample data:**")
        st.dataframe(st.session_state.sample_data)

    st.markdown("---")

    # Upload your own data
    st.subheader("Upload Your Own Data")
    uploaded_file = st.file_uploader("Upload CSV, Excel or JSON", type=["csv", "xlsx", "json"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.lower().endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.lower().endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                df = pd.read_json(uploaded_file)
            st.session_state.uploaded_data = df
            st.success(f"Uploaded {uploaded_file.name} successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading file: {e}")

    if st.session_state.uploaded_data is not None:
        st.markdown("**Uploaded data (most recent):**")
        st.dataframe(st.session_state.uploaded_data)

    st.markdown("---")

    # Reset button: fixed and safe
    st.markdown("### Session Controls")
    c1, c2 = st.columns([1, 2])
    with c1:
        if st.button("Reset Data (clear generated & uploaded & chats)", key="reset_all"):
            reset_all_data()

    with c2:
        st.markdown(
            "Use the colored LLM buttons above to open a demonstration 'environment' for that LLM. "
            "Inside each LLM environment you can enter a prompt, 'Run' it (demo response), view session chat history, and Exit back to the menu."
        )

    st.markdown("---")
    st.info("Demo ready. Click any LLM button above to open its prompt screen.")

# -----------------------
# If an LLM is active -> show LLM environment
# -----------------------
else:
    llm = st.session_state.active_llm
    st.subheader(f"LLM: {llm}")
    st.markdown(
        "<div style='padding:8px;border-left:4px solid #4CAF50;background:#fafafa;border-radius:4px'>"
        "<b>Account / Setup Instructions:</b> For real usage you may need to create an account (Hugging Face, vendor etc.) "
        "or download the model to run locally. This demo only shows UI + chat flow. Replace the dummy executor with real API/local-runner."
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("### Enter prompt for the selected LLM")
    prompt = st.text_area("Prompt", height=240, key=f"prompt_{llm}")

    run_col, exit_col = st.columns([1, 1])
    with run_col:
        if st.button("Run LLM", key=f"run_{llm}"):
            if not prompt or str(prompt).strip() == "":
                st.warning("Please enter a prompt before running.")
            else:
                # execute (dummy) and save to session chat history
                resp = dummy_llm_execute(llm, prompt)
                entry = {
                    "ts": datetime.datetime.utcnow().isoformat(sep=' ', timespec='seconds'),
                    "prompt": prompt,
                    "response": resp
                }
                st.session_state.chat_history.setdefault(llm, [])
                # prepend newest
                st.session_state.chat_history[llm].insert(0, entry)
                st.success("LLM (demo) responded — see Chat History below.")
                # show response immediately
                st.markdown("**Response:**")
                st.code(resp, language=None)

    with exit_col:
        if st.button("Exit LLM & Return to Menu", key=f"exit_{llm}"):
            # leave active_llm and return
            exit_llm()

    st.markdown("---")
    # Chat history
    st.markdown("### Chat History (session only)")
    hist = st.session_state.chat_history.get(llm, [])
    if not hist:
        st.info("No chat history yet for this LLM in this session.")
    else:
        for i, rec in enumerate(hist):
            st.markdown(f"**[{rec['ts']}] Prompt:**")
            st.write(rec["prompt"])
            st.markdown(f"**Response:**")
            st.code(rec["response"], language=None)
            st.markdown("---")

    # provide option to clear chat history for this LLM
    c1, c2 = st.columns([1, 3])
    with c1:
        if st.button("Clear chat history for this LLM", key=f"clearhist_{llm}"):
            st.session_state.chat_history[llm] = []
            st.success(f"Cleared chat history for {llm}.")
    with c2:
        st.write("You can clear chat history above. Chat history is session-only (stored in memory) and will be lost on full reset or page reload.")

    st.markdown("---")
    # show quick link back to main menu as alternative to Exit
    st.markdown("Tip: use 'Exit LLM & Return to Menu' to go back to the top menu and select another LLM.")

# -----------------------
# Footer
# -----------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;font-size:12px;'>"
    "Demo application for showcasing open-source LLMs. Developed by Randy Singh, KNet Consulting Group."
    "</p>",
    unsafe_allow_html=True,
)
