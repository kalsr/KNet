

# python
# streamlit_10_llm_demo_v1.py

# Streamlit LLM Demo App v1
# Top 10 LLM buttons with logos/colors
# Real API-call adapters (OpenAI, HuggingFace) — requires keys via env vars
# Chat UI with history (session + persisted DB via SQLAlchemy)
# Simple auth/login (env var USERS_JSON or default demo user)
# File upload, sample data generator, Reset (fixed)
# Professional header with your attribution

import os
import json
import time
from datetime import datetime
import hashlib
import requests
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, MetaData, Table
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select

# ----------------------------
# CONFIG / ENV
# ----------------------------
DEFAULT_USER = {"demo": "demo"}  # fallback
USERS_JSON = os.getenv("USERS_JSON")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
HF_KEY = os.getenv("HF_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///llm_logs.db")  # default to local sqlite file

# ----------------------------
# Helper: users
# ----------------------------
def load_users():
    try:
        if USERS_JSON:
            return json.loads(USERS_JSON)
    except Exception:
        pass
    return DEFAULT_USER

USERS = load_users()

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

# store hashed passwords in memory for comparison
USERS_HASHED = {u: hash_password(p) for u, p in USERS.items()}

# ----------------------------
# DB Setup (SQLAlchemy)
# ----------------------------
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
metadata = MetaData()

chats_table = Table(
    "llm_chats",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(128)),
    Column("llm", String(128)),
    Column("prompt", Text),
    Column("response", Text),
    Column("created_at", DateTime, default=datetime.utcnow)
)

try:
    metadata.create_all(engine)
except Exception as e:
    st.warning(f"Warning creating DB tables: {e}")

def log_chat_to_db(username, llm, prompt, response):
    try:
        with engine.connect() as conn:
            stmt = chats_table.insert().values(
                username=username, llm=llm, prompt=prompt, response=response, created_at=datetime.utcnow()
            )
            conn.execute(stmt)
    except SQLAlchemyError as e:
        st.error(f"DB logging failed: {e}")

def fetch_chats_from_db(username=None, llm=None, limit=200):
    try:
        with engine.connect() as conn:
            stmt = select([chats_table]).order_by(chats_table.c.created_at.desc()).limit(limit)
            if username:
                stmt = stmt.where(chats_table.c.username == username)
            if llm:
                stmt = stmt.where(chats_table.c.llm == llm)
            rows = conn.execute(stmt).fetchall()
            return [dict(r) for r in rows]
    except Exception as e:
        st.error(f"DB fetch failed: {e}")
        return []

# ----------------------------
# LLM Config: list, logos, mapping
# ----------------------------
LLMS = [
    {"id": "GPT4All", "label": "GPT4All", "logo": "https://gpt4all.io/img/logo.png", "provider": "local"},
    {"id": "LLaMA", "label": "LLaMA", "logo": "https://huggingface.co/front/assets/huggingface_logo-noborder.svg", "provider": "hf"},
    {"id": "MPT", "label": "MPT", "logo": "https://www.mosaicml.com/favicon.ico", "provider": "hf"},
    {"id": "Falcon", "label": "Falcon", "logo": "https://huggingface.co/front/assets/huggingface_logo-noborder.svg", "provider": "hf"},
    {"id": "BLOOM", "label": "BLOOM", "logo": "https://huggingface.co/front/assets/huggingface_logo-noborder.svg", "provider": "hf"},
    {"id": "Dolly", "label": "Dolly", "logo": "https://raw.githubusercontent.com/databricks/dolly/main/docs/docs/img/dolly_logo.png", "provider": "hf"},
    {"id": "Vicuna", "label": "Vicuna", "logo": "https://vicuna.lmsys.org/favicon.ico", "provider": "hf"},
    {"id": "OpenAssistant", "label": "OpenAssistant", "logo": "https://open-assistant.io/static/favicon.png", "provider": "hf"},
    {"id": "RWKV", "label": "RWKV", "logo": "https://raw.githubusercontent.com/BlinkDL/RWKV-LM/master/logo.png", "provider": "hf"},
    {"id": "Alpaca", "label": "Alpaca", "logo": "https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/main/banner.png", "provider": "hf"},
]

BUTTON_COLORS = [
    "#FF5733", "#33A1FF", "#9D33FF", "#33FF57", "#FFC300",
    "#FF33A8", "#33FFF0", "#F0FF33", "#FF8F33", "#7DFF33"
]

# ----------------------------
# API Adapters
# - call_llm(llm_id, prompt) -> response (string)
# ----------------------------
def call_openai(prompt, model="gpt-3.5-turbo"):
    if not OPENAI_KEY:
        return "[OpenAI API key not provided in OPENAI_API_KEY env var]"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": 512}
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[OpenAI call failed: {e}]"

def call_hf_inference(prompt, model_repo="facebook/opt-350m"):
    if not HF_KEY:
        return "[Hugging Face API key not provided in HF_API_KEY env var]"
    # Using Hugging Face Inference API (text-generation)
    url = f"https://api-inference.huggingface.co/models/{model_repo}"
    headers = {"Authorization": f"Bearer {HF_KEY}"}
    payload = {"inputs": prompt, "options": {"wait_for_model": True, "use_cache": False}}
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        # HF returns a list of outputs
        out = r.json()
        if isinstance(out, list) and "generated_text" in out[0]:
            return out[0]["generated_text"]
        # other formats
        return str(out)
    except Exception as e:
        return f"[Hugging Face call failed: {e}]"

def call_local_dummy(prompt):
    # placeholder for local runs like GPT4All: implement your local runner here
    return f"[Local/demo executor] Echo: {prompt[:1000]}"

def call_llm(llm_id, prompt):
    """
    Simple routing: for many LLMs we map to HF inference or OpenAI.
    You should replace 'model_repo' with the real repo you want to call.
    """
    mapping = {
        "GPT4All": lambda p: call_local_dummy(p),
        "LLaMA": lambda p: call_hf_inference(p, model_repo="meta-llama/Llama-2-7b-chat"),  # example
        "MPT": lambda p: call_hf_inference(p, model_repo="mosaicml/mpt-7b-instruct"),
        "Falcon": lambda p: call_hf_inference(p, model_repo="tiiuae/falcon-7b-instruct"),
        "BLOOM": lambda p: call_hf_inference(p, model_repo="bigscience/bloom"),
        "Dolly": lambda p: call_hf_inference(p, model_repo="databricks/dolly-v2-3b"),
        "Vicuna": lambda p: call_hf_inference(p, model_repo="lmsys/vicuna-13b-delta-v1.1"),
        "OpenAssistant": lambda p: call_hf_inference(p, model_repo="OpenAssistant/retrained-openassistant-3b"),
        "RWKV": lambda p: call_hf_inference(p, model_repo="rwkv/rwkv-4-169m"),
        "Alpaca": lambda p: call_hf_inference(p, model_repo="chavinlo/alpaca-native"),
    }
    fn = mapping.get(llm_id, lambda p: "[No mapping for that LLM]")
    return fn(prompt)

# ----------------------------
# Streamlit UI: auth
# ----------------------------
st.set_page_config(page_title="LLM Demo App - Pro", layout="wide")

# Header (Professional Title)
st.markdown(
    """
    <div style='background-color:#111;padding:16px;border-radius:8px;margin-bottom:10px;'>
      <h1 style='color:#fff;text-align:center;font-weight:800;margin:0;'>
        This Application Is Designed By Randy Singh — KNet Consulting Group
      </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Authentication: simple username/password
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user = None

if not st.session_state.authenticated:
    st.markdown("### 🔒 Login")
    col1, col2 = st.columns([1, 2])
    with col1:
        username = st.text_input("Username")
    with col2:
        password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in USERS_HASHED and USERS_HASHED[username] == hash_password(password):
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("Logged in")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password. Set USERS_JSON env var or use demo:demo")

    st.stop()  # stop until logged in

# User is authenticated — main layout
username = st.session_state.user or "demo"

# Layout: top LLM buttons (10) with logos/colors
st.markdown("### Select an LLM to open")
cols = st.columns(5)
for idx, llm in enumerate(LLMS):
    col = cols[idx % 5]
    color = BUTTON_COLORS[idx]
    with col:
        # use markdown for colored rectangle + logo + label
        btn_html = f"""
        <div style='background:{color};padding:8px;border-radius:8px;display:flex;align-items:center;cursor:pointer'>
          <img src="{llm['logo']}" style='height:38px;margin-right:8px;object-fit:contain'/>
          <div style='font-weight:700;color:#111'>{llm['label']}</div>
        </div>
        """
        st.markdown(btn_html, unsafe_allow_html=True)
        if st.button(f"open_{llm['id']}", key=f"open_{llm['id']}", help=f"Open {llm['label']}"):
            st.session_state.active_llm = llm['id']
            st.experimental_rerun()

# show top-row actions (generate, upload, reset)
st.markdown("---")
left, right = st.columns([2, 1])
with left:
    st.subheader("Demo Controls & Data")
    # Sample generator
    sample_size = st.slider("Sample size for quick demo dataset", min_value=1, max_value=200, value=10)
    if st.button("Generate Sample Data"):
        df = pd.DataFrame({"id": range(1, sample_size + 1), "value": [round(x * 0.75 + 10, 2) for x in range(sample_size)]})
        st.session_state.sample_data = df
        st.success(f"Generated {len(df)} rows")
        st.dataframe(df)

    # Upload
    uploaded_file = st.file_uploader("Upload CSV / XLSX / JSON", type=["csv", "xlsx", "json"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                df = pd.read_json(uploaded_file)
            st.session_state.uploaded_data = df
            st.success(f"Uploaded {uploaded_file.name}")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Upload failed: {e}")

    st.markdown("")

    if st.button("Reset Data & Session (full reset)"):
        # clear session_state keys but preserve auth
        preserved = {"authenticated": st.session_state.get("authenticated"), "user": st.session_state.get("user")}
        st.session_state.clear()
        st.session_state.update(preserved)
        st.success("Session reset")
        st.experimental_rerun()

with right:
    st.subheader("User")
    st.write(f"**Logged in as:** {username}")
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.active_llm = None
        st.experimental_rerun()

# If an LLM is active, show LLM screen
active_llm = st.session_state.get("active_llm")
if active_llm:
    st.markdown("---")
    st.markdown(f"## 🧠 {active_llm} — Interactive Demo")
    st.markdown(f"**Instructions:** Use the prompt box below to send a request to {active_llm}. If you want real responses, make sure appropriate API keys are set as environment variables.")
    st.markdown("")

    # show quick instructions & model mapping
    st.info("Model mapping & providers: some LLMs are served via Hugging Face Inference API (HF_KEY required). GPT4All is configured as a local/dummy executor by default — replace with your local runner.")

    # Chat UI: prompt + run
    prompt = st.text_area("Enter prompt for the LLM", height=250, key=f"prompt_{active_llm}")

    run_col, exit_col = st.columns([1, 1])
    with run_col:
        if st.button("Run LLM", key=f"run_{active_llm}"):
            if not prompt.strip():
                st.warning("Please enter a prompt.")
            else:
                with st.spinner("Calling LLM..."):
                    response = call_llm(active_llm, prompt)
                    # Save to session chat history
                    if "chat_history" not in st.session_state:
                        st.session_state.chat_history = []
                    entry = {"ts": datetime.utcnow().isoformat(), "user": username, "llm": active_llm, "prompt": prompt, "response": response}
                    st.session_state.chat_history.insert(0, entry)  # newest first
                    # Log to DB (best effort)
                    try:
                        log_chat_to_db(username, active_llm, prompt, response)
                    except Exception as e:
                        st.warning(f"Unable to log to DB: {e}")
                    st.success("LLM returned a response (demo). Scroll to see chat history.")
    with exit_col:
        if st.button("Exit LLM & Return to Menu", key=f"exit_{active_llm}"):
            st.session_state.active_llm = None
            st.experimental_rerun()

    st.markdown("---")
    st.markdown("### 💬 Chat History (session & persisted)")
    # Render chat history from session state first
    if "chat_history" in st.session_state and st.session_state.chat_history:
        for i, msg in enumerate(st.session_state.chat_history[:50]):
            st.markdown(f"**{msg['llm']}** • {msg['ts']} • **{msg['user']}**")
            st.markdown(f"> **Prompt:** {msg['prompt']}")
            st.markdown(f"> **Response:** {msg['response']}")
            st.markdown("---")
    else:
        st.info("No session chat history yet. Interactions will be recorded here and persisted to DB.")

    # Also show persisted logs (live fetch)
    if st.button("Load persisted logs (DB)", key="load_db"):
        rows = fetch_chats_from_db(username=username, llm=active_llm, limit=100)
        if rows:
            for r in rows:
                st.markdown(f"**{r['llm']}** • {r['created_at']} • **{r['username']}**")
                st.markdown(f"> **Prompt:** {r['prompt']}")
                st.markdown(f"> **Response:** {r['response']}")
                st.markdown("---")
        else:
            st.info("No persisted logs found for this user/LLM.")

    if st.button("Clear session chat history", key=f"clear_{active_llm}"):
        st.session_state.pop("chat_history", None)
        st.success("Cleared session chat history")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center;color:gray;font-size:13px;padding-bottom:20px;'>
      Demo & integration playground — Developed by Randy Singh, KNet Consulting Group.
    </div>
    """,
    unsafe_allow_html=True
)
