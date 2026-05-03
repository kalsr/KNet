# ==========================================================
# KALSNET – REAL AGENTIC LLM ORCHESTRATION SYSTEM
# ==========================================================

import streamlit as st
import json
import datetime
import io
import requests

from openai import OpenAI
from groq import Groq
import anthropic

try:
    from tavily import TavilyClient
except:
    TavilyClient = None

# ==========================================================
# CONFIG
# ==========================================================
st.set_page_config(page_title="KNet Agentic AI", layout="wide")

st.title("🧠 KALSNET – Agentic AI Orchestration System")
st.markdown("---")

# ==========================================================
# SIDEBAR KEYS
# ==========================================================
st.sidebar.title("🔐 API Keys")

openai_key = st.sidebar.text_input("OpenAI Key", type="password")
groq_key = st.sidebar.text_input("Groq Key", type="password")
claude_key = st.sidebar.text_input("Claude Key", type="password")
tavily_key = st.sidebar.text_input("Tavily Search Key", type="password")

st.sidebar.markdown("### How to get keys")
st.sidebar.markdown("""
- OpenAI: https://platform.openai.com/api-keys  
- Groq: https://console.groq.com/keys  
- Claude: https://console.anthropic.com  
- Tavily: https://tavily.com  
""")

# ==========================================================
# INPUT
# ==========================================================
query = st.text_area("💬 Enter your query", height=150)

# ==========================================================
# LLM CLIENTS
# ==========================================================
def call_openai(q):
    client = OpenAI(api_key=openai_key)
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q}]
    )
    return r.choices[0].message.content


def call_groq(q):
    client = Groq(api_key=groq_key)
    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": q}]
    )
    return r.choices[0].message.content


def call_claude(q):
    client = anthropic.Anthropic(api_key=claude_key)
    r = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": q}]
    )
    return r.content[0].text

# ==========================================================
# WEB SEARCH AGENT (PERPLEXITY STYLE)
# ==========================================================
def search_web(q):
    if not tavily_key:
        return "❌ Missing Tavily API key for web search"

    client = TavilyClient(api_key=tavily_key)
    result = client.search(query=q, max_results=5)

    snippets = []
    for r in result.get("results", []):
        snippets.append(r["content"])

    return "\n".join(snippets)

# ==========================================================
# AGENT ROUTER (CORE LOGIC)
# ==========================================================
def route_query(q):

    q_lower = q.lower()

    # 🔍 Research mode
    if any(x in q_lower for x in ["latest", "news", "current", "who", "what is", "search"]):
        context = search_web(q)
        return call_openai(f"Answer using this context:\n{context}\n\nQuestion: {q}")

    # ⚡ Fast reasoning
    elif len(q.split()) < 20:
        return call_groq(q)

    # 🧠 Deep reasoning
    else:
        return call_openai(q)

# ==========================================================
# RUN
# ==========================================================
if st.button("🚀 Run Agent"):

    if not query.strip():
        st.warning("Enter a query")
    else:

        try:
            response = route_query(query)

        except Exception as e:
            response = f"❌ Error: {e}"

        st.success("✅ Agent Response")

        st.markdown("## 📄 Output")
        st.write(response)

        # ================= EXPORT =================
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        data = {
            "query": query,
            "response": response,
            "time": ts
        }

        st.download_button("📥 JSON", json.dumps(data, indent=4), f"{ts}.json")

        st.download_button(
            "📥 CSV",
            st.dataframe([data]).to_csv(index=False),
            f"{ts}.csv"
        )

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("---")
st.caption("KNet Agentic AI System | Real LLM + Search Orchestration")