#*********************
# Details
#*********+******

# This builds five Kalsnet engines (Reasoning, Search, Graph, Fast, Private) plus an Overview tab, matching the router architecture in your document. To run it:


# Each tab includes: the primary, backup, and local models used; a benefits list; a graphviz workflow diagram; a bar chart of sample usage volume; a latency line chart; and a checkbox to # # reveal the entire sample dataset instead of just a preview. The left sidebar holds engine navigation plus expandable API key instructions for OpenAI, Anthropic, Google, DeepSeek, Qwen, # #Llama, and three free-tier options (Groq, OpenRouter, Hugging Face). The title and subtitle render in large bold blue as requested, and no emoji or the word sample-as-demo appear in the #code (I used "sample" instead of "demo" throughout).

#One note on the source document: it contains a lot of very specific claims about models and rankings dated September 2026 (GPT-6 Astra, Claude Fable 5.1 topping benchmarks, Qwen3.8 Max, # #etc.). I built the app's structure and model-role mapping from that document as given, but I can't verify those specific rankings independently, so treat the model names and star ratings # as the document's claims rather than confirmed facts.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalsnet LLM Hub", layout="wide")

st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        font-weight: 800;
        color: #1a4fd6;
        margin-bottom: 0px;
        line-height: 1.1;
    }
    .sub-title {
        font-size: 26px;
        font-weight: 700;
        color: #1a4fd6;
        margin-top: 4px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">Kalsnet LLM Hub</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Developed by Randy Singh from Kalsnet (KNet) Consulting Group</div>',
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------
# Reference data for the five Kalsnet engines
# -----------------------------------------------------------------------

ENGINES = {
    "Overview": {
        "explanation": (
            "The Kalsnet Hub does not send every request to a single language model. "
            "Instead a routing layer looks at each request and forwards it to one of five "
            "logical engines. Each engine wraps a small group of large language models that "
            "are strong at a particular kind of work. This keeps cost under control while "
            "still giving access to the strongest reasoning models when they are actually needed."
        ),
        "primary": "Router",
        "backup": "Router",
        "local": "Router",
        "benefits": [
            "Requests are matched to the cheapest model that can still do the job well",
            "Expensive frontier models are reserved for genuinely difficult requests",
            "New models can be added behind an engine without changing the applications on top",
            "Customers see one Kalsnet assistant while the underlying models can change over time",
        ],
        "diagram": """
digraph Overview {
    rankdir=TB;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Hub [label="Kalsnet Hub"];
    Router [label="LLM Router"];
    Reasoning [label="Reasoning Engine"];
    Search [label="Search Engine"];
    Graph [label="Graph Engine"];
    Fast [label="Fast Engine"];
    Private [label="Private Engine"];
    Result [label="Combined Result"];

    Hub -> Router;
    Router -> Reasoning;
    Router -> Search;
    Router -> Graph;
    Router -> Fast;
    Router -> Private;
    Reasoning -> Result;
    Search -> Result;
    Graph -> Result;
    Fast -> Result;
    Private -> Result;
}
""",
        "categories": ["Reasoning", "Search", "Graph", "Fast", "Private"],
        "seed": 1,
        "unit": "Requests routed last month",
    },
    "Reasoning Engine": {
        "explanation": (
            "The Reasoning Engine is used for complicated decisions where the request needs "
            "careful step by step thinking, for example reviewing a security incident or "
            "producing a written recommendation. It is built around the strongest general "
            "purpose reasoning models available."
        ),
        "primary": "Claude Fable",
        "backup": "GPT Astra",
        "local": "DeepSeek",
        "benefits": [
            "Highest accuracy on multi step reasoning and analysis tasks",
            "Good at combining several pieces of evidence into one recommendation",
            "Strong coding and code review ability",
            "Handles long and detailed instructions reliably",
        ],
        "diagram": """
digraph Reasoning {
    rankdir=LR;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Request -> ComplexityCheck [label="analyze"];
    ComplexityCheck -> ReasoningModel [label="complex"];
    ComplexityCheck -> FastModel [label="simple"];
    ReasoningModel -> Answer;
    FastModel -> Answer;
}
""",
        "categories": ["Incident review", "Written recommendation", "Code review", "Policy analysis", "Risk scoring"],
        "seed": 2,
        "unit": "Requests handled this month",
    },
    "Search Engine": {
        "explanation": (
            "The Search Engine combines keyword search, vector search and retrieval augmented "
            "generation. It is used whenever an answer needs to be grounded in a specific set "
            "of documents rather than general knowledge, for example searching a policy manual "
            "or a set of contracts."
        ),
        "primary": "GPT Astra",
        "backup": "Gemini",
        "local": "Qwen",
        "benefits": [
            "Answers are grounded in the customer own documents",
            "Reduces incorrect or made up answers by citing retrieved passages",
            "Works across large document collections without retraining a model",
            "Can mix keyword search and vector search for better recall",
        ],
        "diagram": """
digraph Search {
    rankdir=LR;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Query -> KeywordSearch;
    Query -> VectorSearch;
    KeywordSearch -> Merge;
    VectorSearch -> Merge;
    Merge -> RAGModel [label="retrieved passages"];
    RAGModel -> Answer;
}
""",
        "categories": ["Policy lookup", "Contract search", "Knowledge base query", "FAQ answer", "Document summary"],
        "seed": 3,
        "unit": "Searches performed this month",
    },
    "Graph Engine": {
        "explanation": (
            "The Graph Engine represents entities and relationships as a knowledge graph, for "
            "example users, systems, and the connections between them. It is used to trace "
            "relationships and paths, such as an attack path in a cybersecurity investigation "
            "or a chain of ownership in a financial review."
        ),
        "primary": "GPT Astra",
        "backup": "Claude Fable",
        "local": "Qwen",
        "benefits": [
            "Makes hidden relationships between entities visible",
            "Supports multi hop questions that a plain search cannot answer",
            "Useful for attack path analysis and fraud investigation",
            "Can be combined with the Reasoning Engine for a written explanation",
        ],
        "diagram": """
digraph Graph {
    rankdir=LR;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Data -> EntityExtraction;
    EntityExtraction -> KnowledgeGraph;
    KnowledgeGraph -> GraphModel [label="graph query"];
    GraphModel -> Answer;
}
""",
        "categories": ["Attack path", "Ownership chain", "Dependency map", "Fraud ring", "Relationship query"],
        "seed": 4,
        "unit": "Graph queries this month",
    },
    "Fast Engine": {
        "explanation": (
            "The Fast Engine is used for simple, high volume operations where speed and low "
            "cost matter more than deep reasoning, for example classifying a support ticket or "
            "summarizing a short email."
        ),
        "primary": "GPT Luna",
        "backup": "Gemini Flash",
        "local": "Llama",
        "benefits": [
            "Very low cost per request compared to a frontier reasoning model",
            "Fast response time suitable for interactive applications",
            "Handles the large majority of simple day to day requests",
            "Frees the Reasoning Engine to focus on genuinely hard problems",
        ],
        "diagram": """
digraph Fast {
    rankdir=LR;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Request -> FastModel;
    FastModel -> Confident [label="check confidence"];
    Confident -> Answer [label="yes"];
    Confident -> ReasoningEngine [label="no"];
    ReasoningEngine -> Answer;
}
""",
        "categories": ["Ticket classification", "Email summary", "Short reply draft", "Tag suggestion", "Simple lookup"],
        "seed": 5,
        "unit": "Requests handled this month",
    },
    "Private Engine": {
        "explanation": (
            "The Private Engine runs open weight models inside the customer own environment "
            "so that sensitive data never leaves their infrastructure. This is important for "
            "defense, healthcare and financial customers with strict data residency rules."
        ),
        "primary": "Qwen",
        "backup": "Llama",
        "local": "DeepSeek",
        "benefits": [
            "Data stays inside the customer environment at all times",
            "Supports strict compliance and data residency requirements",
            "No dependency on an external vendor for uptime",
            "Cost is predictable since the customer owns the hardware",
        ],
        "diagram": """
digraph Private {
    rankdir=LR;
    node [shape=box style=filled fillcolor="#dce6ff" fontname="Helvetica"];
    Request -> LocalModel [label="inside customer environment"];
    LocalModel -> Answer;
}
""",
        "categories": ["Sensitive record review", "Local coding assistant", "Private RAG", "On site classification", "Offline analysis"],
        "seed": 6,
        "unit": "Local requests this month",
    },
}

API_KEY_INFO = {
    "OpenAI (GPT family)": {
        "url": "https://platform.openai.com/api-keys",
        "note": "Sign in, open API keys, create a new secret key. A small free credit is usually given to new accounts.",
    },
    "Anthropic (Claude family)": {
        "url": "https://console.anthropic.com/",
        "note": "Create a console account, open API keys, create a new key. Claude ai also offers a separate free chat tier.",
    },
    "Google (Gemini family)": {
        "url": "https://aistudio.google.com/app/apikey",
        "note": "Sign in with a Google account and generate a key in Google AI Studio. This tier is free with rate limits.",
    },
    "DeepSeek": {
        "url": "https://platform.deepseek.com/",
        "note": "Create an account and generate an API key from the platform dashboard. Pricing is low cost per token.",
    },
    "Qwen (Alibaba Cloud)": {
        "url": "https://bailian.console.aliyun.com/",
        "note": "Create an Alibaba Cloud account and generate a key in the Model Studio console. Open weight Qwen models can also be downloaded and run locally at no cost.",
    },
    "Llama (Meta)": {
        "url": "https://huggingface.co/meta-llama",
        "note": "Llama models are open weight. Download them from Hugging Face, or call a hosted free tier through a provider such as Groq.",
    },
    "Groq (free hosted open models)": {
        "url": "https://console.groq.com/keys",
        "note": "Free API key with a generous rate limit for open weight models such as Llama and Qwen, useful for quick testing.",
    },
    "OpenRouter (many models, one key)": {
        "url": "https://openrouter.ai/keys",
        "note": "One key gives access to many providers including several free open weight models.",
    },
    "Hugging Face": {
        "url": "https://huggingface.co/settings/tokens",
        "note": "Free account token, useful for downloading open weight models and calling the free inference endpoints.",
    },
}


def make_sample_data(engine_key):
    engine = ENGINES[engine_key]
    rng = np.random.default_rng(engine["seed"])
    categories = engine["categories"]
    values = rng.integers(low=40, high=500, size=len(categories))
    cost = rng.uniform(low=0.001, high=0.08, size=len(categories)).round(4)
    latency = rng.uniform(low=0.3, high=4.5, size=len(categories)).round(2)
    df = pd.DataFrame(
        {
            "Category": categories,
            "Volume": values,
            "Average Cost Per Request": cost,
            "Average Latency Seconds": latency,
        }
    )
    return df


def render_engine_page(engine_key):
    engine = ENGINES[engine_key]

    st.header(engine_key)
    st.write(engine["explanation"])

    st.subheader("Models used")
    model_table = pd.DataFrame(
        {
            "Role": ["Primary model", "Backup model", "Local or private model"],
            "Model": [engine["primary"], engine["backup"], engine["local"]],
        }
    )
    st.table(model_table)

    st.subheader("Benefits")
    for item in engine["benefits"]:
        st.write("- " + item)

    st.subheader("Workflow diagram")
    st.graphviz_chart(engine["diagram"])

    st.subheader("Sample usage data")
    st.caption(engine["unit"])
    df = make_sample_data(engine_key)

    st.bar_chart(df.set_index("Category")["Volume"])

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(df["Category"], df["Average Latency Seconds"], marker="o", color="#1a4fd6")
    ax.set_ylabel("Average latency seconds")
    ax.set_xlabel("Category")
    ax.set_title("Average latency by category")
    plt.xticks(rotation=20, ha="right")
    st.pyplot(fig)

    show_all = st.checkbox("Show entire selected data", key="show_all_" + engine_key)
    if show_all:
        st.dataframe(df, use_container_width=True)
    else:
        st.dataframe(df.head(3), use_container_width=True)


# -----------------------------------------------------------------------
# Sidebar navigation and key access instructions
# -----------------------------------------------------------------------

st.sidebar.title("Kalsnet Navigation")
selected_engine = st.sidebar.radio("Select an engine", list(ENGINES.keys()))

st.sidebar.markdown("---")
st.sidebar.header("LLM key access instructions")
st.sidebar.write(
    "Expand a provider below for a direct link and short setup note. "
    "Several providers listed offer a free tier suitable for testing this application."
)

for provider, info in API_KEY_INFO.items():
    with st.sidebar.expander(provider):
        st.write(info["note"])
        st.write(info["url"])

st.sidebar.markdown("---")
st.sidebar.caption(
    "All usage data shown in this application is randomly generated sample data for "
    "illustration only and does not reflect real account activity."
)

# -----------------------------------------------------------------------
# Main content
# -----------------------------------------------------------------------

render_engine_page(selected_engine)
