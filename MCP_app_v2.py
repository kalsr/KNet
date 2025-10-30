

#  MCP_app_v2.py

import streamlit as st

import pandas as pd

import plotly.express as px

import random

import datetime

from dateutil.relativedelta import relativedelta

import io

import json



st.set_page_config(page_title="MCP Cyber Demo — IOC Enricher", layout="wide")



# ---------------------------

# Small MCP-style server shim

# ---------------------------

# This is a minimal, in-process MCP-like server implementation for demo purposes.

# It exposes one tool: "enrich_ioc(indicator: str, type: str) -> dict"

# Replace this shim with the real MCP Python SDK server implementation if desired.

# (See comments below and MCP SDK docs.)

class MCPDemoServer:

    def __init__(self, dataset_df=None):

        self.dataset_df = dataset_df.copy() if dataset_df is not None else pd.DataFrame()

        # small built-in threat intel for enrichment

        self.known_malicious = {

            "1.2.3.4": {"severity":"high","confidence":0.94,"tags":["botnet","malicious-ip"], "first_seen":"2025-01-10"},

            "bad.example[.]com": {"severity":"medium","confidence":0.7,"tags":["phishing"], "first_seen":"2024-11-01"},

            "abcdef1234567890": {"severity":"high","confidence":0.98,"tags":["malware-hash"], "first_seen":"2025-03-02"},

        }



    def enrich_ioc(self, indicator: str, ioc_type: str):

        """

        Simulates an MCP tool call returning structured JSON context.

        """

        indicator = str(indicator).strip()

        # match from dataset or known_malicious

        base = None

        # direct known_malicious lookup

        if indicator in self.known_malicious:

            base = self.known_malicious[indicator]

        else:

            # heuristic: IP-like, domain-like, hex-like

            if ioc_type.lower() == "ip" or (ioc_type=="" and self._looks_like_ip(indicator)):

                base = self._simulate_ip_enrichment(indicator)

            elif ioc_type.lower() == "domain" or (ioc_type=="" and "." in indicator):

                base = self._simulate_domain_enrichment(indicator)

            else:

                base = self._simulate_hash_enrichment(indicator)



        # build structured response similar to MCP tool response

        response = {

            "indicator": indicator,

            "type": ioc_type or guess_ioc_type(indicator),

            "severity": base["severity"],

            "confidence": round(float(base["confidence"]), 2),

            "related_tags": base["tags"],

            "first_seen": base.get("first_seen", datetime.date.today().isoformat()),

            "explain": base.get("explain", f"Enrichment via local MCP demo rules for {indicator}.")

        }

        return response



    def _looks_like_ip(self, s):

        parts = s.split(".")

        if len(parts) == 4 and all(p.isdigit() and 0<=int(p)<=255 for p in parts):

            return True

        return False



    def _simulate_ip_enrichment(self, ip):

        # randomly simulate scores but deterministic-ish using hash

        r = (sum(bytearray(ip.encode("utf8"))) % 100) / 100

        if r > 0.85:

            sev = "high"

            tags = ["botnet","scanner"]

        elif r > 0.5:

            sev = "medium"

            tags = ["suspicious"]

        else:

            sev = "low"

            tags = ["benign"]

        return {"severity": sev, "confidence": 0.5 + r*0.5, "tags": tags,

                "explain": f"IP heuristic analysis: score {r:.2f}"}



    def _simulate_domain_enrichment(self, d):

        r = (sum(bytearray(d.encode("utf8"))) % 80) / 100

        if "phish" in d or r>0.75:

            sev = "high"

            tags = ["phishing"]

        elif r>0.45:

            sev = "medium"

            tags = ["suspicious","typosquat"]

        else:

            sev = "low"

            tags = ["benign"]

        return {"severity": sev, "confidence": 0.45 + r*0.55, "tags": tags,

                "explain": f"Domain lookups + heuristics: score {r:.2f}"}



    def _simulate_hash_enrichment(self, h):

        r = (len(h) % 10) / 10

        if r>0.6:

            sev = "high"

            tags = ["malware-hash"]

        else:

            sev = "low"

            tags = ["unknown"]

        return {"severity": sev, "confidence": 0.4 + r*0.6, "tags": tags,

                "explain": f"Hash heuristic length-score {r:.2f}"}





# ---------------------------

# Helpers

# ---------------------------

def guess_ioc_type(indicator: str):

    if indicator.count(".") == 3 and all(p.isdigit() for p in indicator.split(".")):

        return "ip"

    if "/" in indicator or "." in indicator:

        if "." in indicator:

            return "domain"

    # default

    return "hash"



def make_sample_iocs(n=25):

    # generate a mixed set of IPs, domains, and hashes

    n = min(max(1, int(n)), 100)

    samples = []

    base_date = datetime.date.today() - relativedelta(months=6)

    for i in range(n):

        kind = random.choices(["ip","domain","hash"], weights=[0.4,0.4,0.2])[0]

        if kind == "ip":

            ip = ".".join(str(random.randint(1,250)) for _ in range(4))

            samples.append({

                "id": i+1,

                "indicator": ip,

                "type": "ip",

                "source": random.choice(["internal-sensor","talos","user-report","honeypot"]),

                "first_seen": (base_date + datetime.timedelta(days=random.randint(0,180))).isoformat(),

                "notes": ""

            })

        elif kind == "domain":

            d = random.choice(["example","login","secure","update","bank","paypal","office"])

            tld = random.choice(["com","net","org","info"])

            dom = f"{d}{random.randint(1,99)}.{tld}"

            samples.append({

                "id": i+1,

                "indicator": dom,

                "type": "domain",

                "source": random.choice(["passive-dns","user-report","redirector"]),

                "first_seen": (base_date + datetime.timedelta(days=random.randint(0,180))).isoformat(),

                "notes": ""

            })

        else:

            h = ''.join(random.choice("abcdef0123456789") for _ in range(32))

            samples.append({

                "id": i+1,

                "indicator": h,

                "type": "hash",

                "source": random.choice(["scan","AV","sandbox"]),

                "first_seen": (base_date + datetime.timedelta(days=random.randint(0,180))).isoformat(),

                "notes": ""

            })

    df = pd.DataFrame(samples)

    return df



# ---------------------------

# Streamlit UI

# ---------------------------



# Left panel: controls

st.sidebar.header("MCP Cyber demo controls")

num = st.sidebar.slider("Number of sample records", min_value=5, max_value=100, value=25, step=1)

show_avatar = st.sidebar.checkbox("Show friendly avatar", value=True)

upload = st.sidebar.file_uploader("Upload CSV (optional) — will replace sample dataset", type=["csv"])

use_mcp_sdk = st.sidebar.checkbox("(Optional) Use official MCP SDK if available", value=False)

run_demo = st.sidebar.button("(Re)load dataset & run enrichment")



st.title("Model Context Protocol (MCP) — Cyber IOC Enricher (Demo)")



# avatar / mascot

if show_avatar:

    st.markdown(

        """

        <div style="display:flex; align-items:center; gap:16px;">

          <div style="width:140px; height:140px; border-radius:20px; background: linear-gradient(135deg,#6EE7B7,#3B82F6); padding:12px; box-shadow: 0 6px 18px rgba(0,0,0,0.12);">

            <!-- SVG "colored guy" -->

            <svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:100%;">

              <circle cx="60" cy="40" r="22" fill="#fff6" />

              <circle cx="60" cy="40" r="18" fill="#fff" />

              <circle cx="50" cy="36" r="3" fill="#333" />

              <circle cx="70" cy="36" r="3" fill="#333" />

              <path d="M48 50c6 6 18 6 24 0" stroke="#333" stroke-width="2" fill="none" stroke-linecap="round"/>

              <rect x="26" y="72" rx="8" width="68" height="30" fill="#ffffff33"/>

              <text x="60" y="92" text-anchor="middle" font-size="10" fill="#fff">MCP Agent</text>

            </svg>

          </div>

          <div>

            <h3 style="margin:0">MCP IOC Enricher</h3>

            <div style="color: #666; margin-top:6px">A friendly MCP-style tool to enrich indicators of compromise.</div>

            <div style="margin-top:8px"><small style="color:#333">Features: up to 100 sample records, CSV upload, MCP-style tool calls, graphs.</small></div>

          </div>

        </div>

        """,

        unsafe_allow_html=True

    )



# load dataset (samples or uploaded)

if upload is not None:

    try:

        df_in = pd.read_csv(upload)

        # enforce max 100 rows

        if len(df_in) > 100:

            df_in = df_in.head(100)

            st.warning("Only first 100 rows are used.")

        # attempt to detect columns

        if "indicator" not in df_in.columns:

            # try to accept first column as indicator

            df_in = df_in.rename(columns={df_in.columns[0]:"indicator"})

        if "type" not in df_in.columns:

            df_in["type"] = df_in["indicator"].apply(guess_ioc_type)

    except Exception as e:

        st.error(f"Failed to parse uploaded CSV: {e}")

        df_in = make_sample_iocs(num)

else:

    df_in = make_sample_iocs(num)



# show dataset preview

st.subheader("Dataset (preview)")

st.dataframe(df_in.head(50))



# create MCP server shim instance using current dataset (optional: real SDK)

mcp_server = MCPDemoServer(dataset_df=df_in)



# Enrichment run: call enrich_ioc for each row

def run_enrichment(df):

    records = []

    for _, row in df.iterrows():

        indicator = row.get("indicator")

        itype = row.get("type", "") or guess_ioc_type(str(indicator))

        # MCP-style client call to server tool

        enr = mcp_server.enrich_ioc(indicator, itype)

        # combine

        rec = row.to_dict()

        rec.update({

            "severity": enr["severity"],

            "confidence": enr["confidence"],

            "related_tags": ",".join(enr["related_tags"]),

            "first_seen_enrich": enr["first_seen"],

            "explain": enr["explain"]

        })

        records.append(rec)

    return pd.DataFrame(records)



if run_demo:

    enriched_df = run_enrichment(df_in)

    st.success("MCP enrichment completed (demo).")

else:

    # default: do not auto-run heavy ops until user clicks

    enriched_df = None

    st.info("Click the button in the left sidebar to run MCP enrichment.")



if enriched_df is not None:

    st.subheader("Enrichment results (first 100 rows)")

    st.dataframe(enriched_df)



    # Summary of outputs + explanation (user requested)

    st.markdown("### Summary of results — how the MCP tool produced them")

    # explain algorithm in text

    st.markdown(

        """

        This demo MCP tool (`enrich_ioc`) returns **structured context** for each indicator:

        - `severity` — heuristic label (low/medium/high) from rule-based or lookup heuristics.

        - `confidence` — numeric confidence (0..1) synthesized from simple heuristics and known matches.

        - `related_tags` — short tags (e.g., `phishing`, `malware-hash`) to let downstream models filter.

        - `first_seen` — earliest date recorded or simulated.

        - `explain` — short human-readable rationale for the enrichment.



        **How results are produced (demo):**

        1. Known IOCs are matched against a small built-in list (deterministic high-confidence matches).

        2. Otherwise, the server runs light heuristics based on indicator shape (IP / domain / hash).

        3. Scores are computed deterministically from indicator bytes/length so results are repeatable.

        4. The client (this UI) then receives structured JSON from the MCP tool and displays it.

        """

    )



    # Charts

    st.subheader("Charts")



    # Severity counts bar

    fig_bar = px.bar(enriched_df["severity"].value_counts().reset_index().rename(columns={"index":"severity", "severity":"count"}),

                     x="severity", y="count", title="Severity distribution")

    st.plotly_chart(fig_bar, use_container_width=True)



    # Pie chart of indicator types

    types = enriched_df["type"].fillna("unknown").value_counts().reset_index().rename(columns={"index":"type", "type":"count"})

    fig_pie = px.pie(types, names="type", values="count", title="Indicator type breakdown")

    st.plotly_chart(fig_pie, use_container_width=True)



    # Show top tags

    st.subheader("Top related tags")

    # collect tags

    tag_series = enriched_df["related_tags"].dropna().apply(lambda s: [x.strip() for x in s.split(",") if x.strip()])

    from collections import Counter

    c = Counter()

    for row in tag_series:

        c.update(row)

    top_tags = pd.DataFrame(c.most_common(), columns=["tag","count"])

    if not top_tags.empty:

        st.table(top_tags.head(20))

    else:

        st.write("No tags found.")



    # Export enriched data

    buf = io.StringIO()

    enriched_df.to_csv(buf, index=False)

    st.download_button("Download enriched CSV", data=buf.getvalue(), file_name="enriched_iocs.csv", mime="text/csv")



# Small note about replacing shim with official MCP server

st.markdown("---")

st.markdown(

    """

    **Notes & next steps (MCP-focused):**

    - This demo uses an in-process MCP-style *shim* to keep everything self-contained and runnable in Streamlit.

    - To convert to a real MCP server:

      1. Install the official `mcp` Python SDK (`pip install mcp`).

      2. Implement the `enrich_ioc` tool using `mcp.server.*` constructs and run a proper MCP transport (stdio/HTTP/SSE).

      3. Replace the `MCPDemoServer.enrich_ioc` calls with real MCP client calls from your LLM host.

    - Official MCP docs & Python SDK: see the Model Context Protocol specification and Python SDK pages.

    """

)



st.markdown("### MCP references")

st.markdown("- Model Context Protocol specification & docs (overview + how-to).")

st.markdown("- Official MCP Python SDK (optional) if you want a true server implementation.")