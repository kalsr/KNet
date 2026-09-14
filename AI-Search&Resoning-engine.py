# Search & Resoning engine app

# Message. For JAWS, turn virtual PC Cursor on if needed.

# Kalsnet Graph Search and Reasoning Engine
# Developed By Randy Singh from Kalsnet (KNet) Consulting Group

# This Streamlit application demonstrates Uninformed Search techniques
# (Depth First Search, Breadth First Search, and Uniform Cost Search)
# applied to a security and enterprise Knowledge Graph.

# The application allows the user to:
# 1. Read an explanation of each search technique and its schema
# 2. Upload real data or generate synthetic data for each case
# 3. Display the entire synthetic dataset on request
# 4. Run the search algorithm and view a graph visualization of the result
# 5. Export the results as PDF, Word, CSV, and plain text files
# 6. Optionally generate an AI-powered plain-English explanation of the
#    result using a free Groq or Google Gemini LLM (user supplies their own
#    API key, entered in the sidebar)


import io
import random
import string
import heapq
import datetime
import json

import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import requests

import streamlit as st

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch


# ---------------------------------------------------------------------------
# Static reference data
# ---------------------------------------------------------------------------

NODE_TYPES = [
    "Endpoint", "Employee", "Laptop", "VPN", "API", "Gateway",
    "Application", "Server", "Database", "Sensitive Data",
    "Vendor", "Software", "Library"
]

OWNERS = [
    "IT Security", "Network Team", "Application Team",
    "Database Team", "Cloud Team", "Vendor Management"
]

RELATIONSHIP_TYPES = [
    "connects_to", "accesses", "uses", "depends_on",
    "communicates_with", "hosts"
]

NODE_SCHEMA = pd.DataFrame([
    {"Field": "ID", "Type": "String", "Description": "Unique identifier for the node"},
    {"Field": "Type", "Type": "String", "Description": "Category of the node, for example Endpoint, Server, Database, Application"},
    {"Field": "Risk", "Type": "Integer 0 to 10", "Description": "Risk score assigned to the node"},
    {"Field": "Criticality", "Type": "Integer 0 to 10", "Description": "Business criticality of the node"},
    {"Field": "Owner", "Type": "String", "Description": "Team or individual responsible for the node"},
    {"Field": "Security_Score", "Type": "Integer 0 to 100", "Description": "Overall security posture score of the node"},
])

EDGE_SCHEMA = pd.DataFrame([
    {"Field": "Source", "Type": "String", "Description": "ID of the source node"},
    {"Field": "Target", "Type": "String", "Description": "ID of the target node"},
    {"Field": "Relationship", "Type": "String", "Description": "Type of relationship, for example connects_to, accesses, uses"},
    {"Field": "Cost", "Type": "Float", "Description": "Cost of traversing this relationship, used by Uniform Cost Search"},
    {"Field": "Risk", "Type": "Integer 0 to 10", "Description": "Risk score of this relationship"},
    {"Field": "Probability", "Type": "Float 0 to 1", "Description": "Estimated probability of exploit along this relationship"},
    {"Field": "Time", "Type": "Float", "Description": "Estimated time in hours required to traverse this relationship"},
])

CASE_INFO = {
    "DFS": {
        "full_name": "Depth First Search",
        "purpose": "Attack Chain Exploration",
        "explanation": (
            "Depth First Search follows one path as deeply as possible before backtracking. "
            "Inside Kalsnet Hub this is used to trace a full attack chain from a compromised "
            "endpoint all the way to a sensitive target, for example moving from a compromised "
            "PC to a user account, then to an API, then to an application server, then to a "
            "database, and finally to sensitive data. "
            "The typical space complexity of a stack based Depth First Search is approximately "
            "O(b times m), where b is the branching factor and m is the maximum depth, rather "
            "than O(b to the power m), because only the current path is kept in memory rather "
            "than the entire tree."
        ),
        "use_cases": [
            "Tracing a cyber attack path from a compromised device to a sensitive asset",
            "Following a chain of dependencies as deeply as possible",
            "Root cause analysis that requires exploring one branch fully before trying another"
        ],
    },
    "BFS": {
        "full_name": "Breadth First Search",
        "purpose": "Blast Radius and Impact Analysis",
        "explanation": (
            "Breadth First Search explores a graph level by level, expanding all neighbors of "
            "the current node before moving further out. Inside Kalsnet Hub this is used to "
            "answer questions such as which systems are within three network relationships of "
            "a compromised server. "
            "This is extremely useful for cyber blast radius analysis, dependency analysis, "
            "incident response, network topology mapping, API dependency analysis, application "
            "dependency analysis, and Zero Trust analysis. "
            "The space requirement of Breadth First Search can reach approximately O(b to the "
            "power s), where b is the branching factor and s is the solution depth, because it "
            "must retain an entire frontier level in memory at once."
        ),
        "use_cases": [
            "Finding the shortest number of relationships between two systems",
            "Blast radius analysis after a compromise",
            "Mapping all assets connected to an incident within a limited number of hops"
        ],
    },
    "UCS": {
        "full_name": "Uniform Cost Search",
        "purpose": "Least Cost Remediation Path",
        "explanation": (
            "Uniform Cost Search finds the path with the lowest cumulative cost between a start "
            "node and a goal node, where cost can represent risk, financial cost, time, or "
            "operational impact, or a combination of these factors. Inside Kalsnet Hub this "
            "becomes a basic form of decision optimization, for example comparing patch server, "
            "replace API, and isolate network as three different remediation paths and selecting "
            "the one with the lowest overall combined cost. "
            "Uniform Cost Search always expands the node with the lowest cumulative cost so far, "
            "which guarantees an optimal solution when all edge costs are non negative."
        ),
        "use_cases": [
            "Selecting the lowest risk and lowest cost remediation path",
            "SOAR playbook selection based on operational cost",
            "Recovery sequencing based on cost, time, risk, and business priority"
        ],
    },
}


# ---------------------------------------------------------------------------
# Synthetic data generation
# ---------------------------------------------------------------------------

def generate_synthetic_nodes(num_nodes, seed=42):
    rng = random.Random(seed)
    rows = []
    for i in range(1, num_nodes + 1):
        rows.append({
            "ID": "N" + str(i),
            "Type": rng.choice(NODE_TYPES),
            "Risk": rng.randint(0, 10),
            "Criticality": rng.randint(0, 10),
            "Owner": rng.choice(OWNERS),
            "Security_Score": rng.randint(0, 100),
        })
    return pd.DataFrame(rows)


def generate_synthetic_edges(nodes_df, extra_edge_ratio=0.4, seed=42):
    rng = random.Random(seed)
    node_ids = list(nodes_df["ID"])
    rows = []

    # build a spanning tree first so the graph stays connected
    for i in range(1, len(node_ids)):
        source = rng.choice(node_ids[:i])
        target = node_ids[i]
        rows.append(_make_edge_row(rng, source, target))

    # add extra random edges for additional complexity
    num_extra = int(len(node_ids) * extra_edge_ratio)
    for _ in range(num_extra):
        source, target = rng.sample(node_ids, 2)
        rows.append(_make_edge_row(rng, source, target))

    return pd.DataFrame(rows)


def _make_edge_row(rng, source, target):
    return {
        "Source": source,
        "Target": target,
        "Relationship": rng.choice(RELATIONSHIP_TYPES),
        "Cost": round(rng.uniform(1, 50), 2),
        "Risk": rng.randint(0, 10),
        "Probability": round(rng.uniform(0, 1), 2),
        "Time": round(rng.uniform(1, 20), 2),
    }


# ---------------------------------------------------------------------------
# Graph construction
# ---------------------------------------------------------------------------

def build_graph(nodes_df, edges_df):
    graph = nx.DiGraph()
    for _, row in nodes_df.iterrows():
        graph.add_node(row["ID"], **row.drop(labels=["ID"]).to_dict())
    for _, row in edges_df.iterrows():
        graph.add_edge(row["Source"], row["Target"], **row.drop(labels=["Source", "Target"]).to_dict())
    return graph


# ---------------------------------------------------------------------------
# Search algorithms
# ---------------------------------------------------------------------------

def dfs_search(graph, start, goal):
    visited_order = []
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)

        if node == goal:
            return path, visited_order

        neighbors = sorted(graph.successors(node), reverse=True)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None, visited_order


def bfs_search(graph, start, goal):
    visited_order = []
    visited = {start}
    queue = [(start, [start], 0)]
    levels = {start: 0}
    head = 0

    while head < len(queue):
        node, path, depth = queue[head]
        head += 1
        visited_order.append(node)

        if node == goal:
            return path, visited_order, levels

        for neighbor in sorted(graph.successors(node)):
            if neighbor not in visited:
                visited.add(neighbor)
                levels[neighbor] = depth + 1
                queue.append((neighbor, path + [neighbor], depth + 1))

    return None, visited_order, levels


def ucs_search(graph, start, goal, weight_field="Cost"):
    visited_order = []
    visited = set()
    counter = 0
    frontier = [(0.0, counter, start, [start])]

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)

        if node == goal:
            return path, cost, visited_order

        for neighbor in sorted(graph.successors(node)):
            if neighbor not in visited:
                edge_cost = graph[node][neighbor].get(weight_field, 1.0)
                counter += 1
                heapq.heappush(frontier, (cost + edge_cost, counter, neighbor, path + [neighbor]))

    return None, None, visited_order


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

def plot_graph(graph, path=None, title="Knowledge Graph"):
    fig, ax = plt.subplots(figsize=(9, 6))
    layout = nx.spring_layout(graph, seed=7)

    nx.draw_networkx_nodes(graph, layout, node_color="#A9C6E8", node_size=650, ax=ax)
    nx.draw_networkx_labels(graph, layout, font_size=8, ax=ax)
    nx.draw_networkx_edges(graph, layout, edge_color="#B0B0B0", arrows=True, ax=ax)

    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_nodes(graph, layout, nodelist=path, node_color="#FF9900", node_size=750, ax=ax)
        nx.draw_networkx_edges(graph, layout, edgelist=path_edges, edge_color="#CC0000", width=2.5, arrows=True, ax=ax)
        nx.draw_networkx_nodes(graph, layout, nodelist=[path[0]], node_color="#2E8B57", node_size=800, ax=ax)
        nx.draw_networkx_nodes(graph, layout, nodelist=[path[-1]], node_color="#B22222", node_size=800, ax=ax)

    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    ax.axis("off")
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Export helpers
# ---------------------------------------------------------------------------

def build_result_summary(case_key, start, goal, path, cost_or_extra, nodes_df, edges_df, visited_order):
    info = CASE_INFO[case_key]
    generated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if path:
        path_text = " then ".join(path)
        status = "Path found"
    else:
        path_text = "No path was found between the selected start and goal nodes"
        status = "No path found"

    summary = {
        "case_key": case_key,
        "case_name": info["full_name"],
        "purpose": info["purpose"],
        "explanation": info["explanation"],
        "generated_at": generated_at,
        "start": start,
        "goal": goal,
        "status": status,
        "path": path,
        "path_text": path_text,
        "extra": cost_or_extra,
        "node_count": len(nodes_df),
        "edge_count": len(edges_df),
        "visited_order": visited_order,
    }
    return summary


def export_csv_bytes(path, nodes_df):
    if path:
        result_df = nodes_df[nodes_df["ID"].isin(path)].copy()
        result_df["Order_In_Path"] = result_df["ID"].apply(lambda x: path.index(x) + 1)
        result_df = result_df.sort_values("Order_In_Path")
    else:
        result_df = pd.DataFrame(columns=list(nodes_df.columns) + ["Order_In_Path"])
    buffer = io.StringIO()
    result_df.to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")


def export_text_bytes(summary):
    lines = []
    lines.append("KALSNET GRAPH SEARCH AND REASONING ENGINE")
    lines.append("Developed By Randy Singh from Kalsnet (KNet) Consulting Group")
    lines.append("")
    lines.append("Case: " + summary["case_name"] + " -- " + summary["purpose"])
    lines.append("Generated: " + summary["generated_at"])
    lines.append("")
    lines.append("Explanation")
    lines.append(summary["explanation"])
    lines.append("")
    lines.append("Search Parameters")
    lines.append("Start node: " + str(summary["start"]))
    lines.append("Goal node: " + str(summary["goal"]))
    lines.append("Total nodes in graph: " + str(summary["node_count"]))
    lines.append("Total edges in graph: " + str(summary["edge_count"]))
    lines.append("")
    lines.append("Result")
    lines.append("Status: " + summary["status"])
    lines.append("Path: " + summary["path_text"])
    if summary["extra"] is not None:
        lines.append("Additional detail: " + str(summary["extra"]))
    lines.append("")
    lines.append("Visited Order")
    lines.append(" then ".join(summary["visited_order"]))
    if summary.get("ai_explanation"):
        lines.append("")
        lines.append("AI Generated Explanation (" + str(summary.get("ai_provider", "")) + ")")
        lines.append(summary["ai_explanation"])
    return "\n".join(lines).encode("utf-8")


def export_word_bytes(summary):
    document = Document()

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("Kalsnet Graph Search and Reasoning Engine")
    run.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0xCC)

    subtitle = document.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = subtitle.add_run("Developed By Randy Singh from Kalsnet (KNet) Consulting Group")
    run2.bold = True
    run2.font.size = Pt(13)
    run2.font.color.rgb = RGBColor(0x00, 0x00, 0xCC)

    document.add_heading(summary["case_name"] + " -- " + summary["purpose"], level=1)
    document.add_paragraph("Generated: " + summary["generated_at"])

    document.add_heading("Explanation", level=2)
    document.add_paragraph(summary["explanation"])

    document.add_heading("Search Parameters", level=2)
    param_table = document.add_table(rows=4, cols=2)
    param_table.style = "Light Grid Accent 1"
    param_rows = [
        ("Start node", str(summary["start"])),
        ("Goal node", str(summary["goal"])),
        ("Total nodes in graph", str(summary["node_count"])),
        ("Total edges in graph", str(summary["edge_count"])),
    ]
    for i, (label, value) in enumerate(param_rows):
        param_table.cell(i, 0).text = label
        param_table.cell(i, 1).text = value

    document.add_heading("Result", level=2)
    document.add_paragraph("Status: " + summary["status"])
    document.add_paragraph("Path: " + summary["path_text"])
    if summary["extra"] is not None:
        document.add_paragraph("Additional detail: " + str(summary["extra"]))

    document.add_heading("Visited Order", level=2)
    document.add_paragraph(" then ".join(summary["visited_order"]))

    if summary.get("ai_explanation"):
        document.add_heading("AI Generated Explanation (" + str(summary.get("ai_provider", "")) + ")", level=2)
        document.add_paragraph(summary["ai_explanation"])

    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def export_pdf_bytes(summary):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.6 * inch, bottomMargin=0.6 * inch)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleBlue", parent=styles["Title"], textColor=colors.HexColor("#0000CC"), fontSize=20
    )
    subtitle_style = ParagraphStyle(
        "SubtitleBlue", parent=styles["Normal"], textColor=colors.HexColor("#0000CC"),
        fontSize=12, alignment=1, spaceAfter=14
    )
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    elements = []
    elements.append(Paragraph("Kalsnet Graph Search and Reasoning Engine", title_style))
    elements.append(Paragraph("Developed By Randy Singh from Kalsnet (KNet) Consulting Group", subtitle_style))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(summary["case_name"] + " -- " + summary["purpose"], heading_style))
    elements.append(Paragraph("Generated: " + summary["generated_at"], body_style))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Explanation", heading_style))
    elements.append(Paragraph(summary["explanation"], body_style))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Search Parameters", heading_style))
    param_data = [
        ["Field", "Value"],
        ["Start node", str(summary["start"])],
        ["Goal node", str(summary["goal"])],
        ["Total nodes in graph", str(summary["node_count"])],
        ["Total edges in graph", str(summary["edge_count"])],
    ]
    param_table = Table(param_data, colWidths=[2.5 * inch, 3.5 * inch])
    param_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0000CC")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EEF2FA")]),
    ]))
    elements.append(param_table)
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Result", heading_style))
    elements.append(Paragraph("Status: " + summary["status"], body_style))
    elements.append(Paragraph("Path: " + summary["path_text"], body_style))
    if summary["extra"] is not None:
        elements.append(Paragraph("Additional detail: " + str(summary["extra"]), body_style))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph("Visited Order", heading_style))
    elements.append(Paragraph(" then ".join(summary["visited_order"]), body_style))

    if summary.get("ai_explanation"):
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("AI Generated Explanation (" + str(summary.get("ai_provider", "")) + ")", heading_style))
        elements.append(Paragraph(summary["ai_explanation"], body_style))

    doc.build(elements)
    return buffer.getvalue()


# ---------------------------------------------------------------------------
# AI integration -- Groq and Google Gemini
# ---------------------------------------------------------------------------
# These helpers call the user's own Groq or Gemini account using a key the
# user pastes into the sidebar at runtime. No key is ever hard coded here,
# and nothing is sent anywhere except directly to Groq's or Google's API.

# These are ONLY an offline fallback, used if the live model list can't be
# fetched from the provider (for example no internet reachability to the
# provider's /models endpoint). Both Groq and Google retire and rename
# models fairly often, so hard coding "the current models" is exactly what
# broke this app twice before. Whenever a key is entered, the app now asks
# the provider directly which models that key can use right now, and uses
# that live list instead. Keep these as rough placeholders only.
GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
]

GEMINI_MODELS = [
    "gemini-flash-latest",
    "gemini-2.5-flash",
]

# If one of these IDs shows up in the live list fetched from the provider,
# it is preselected as the default choice in the dropdown. If none of them
# match (for example because the provider has renamed things again), a
# scoring heuristic (_default_model_score below) picks a sensible default
# instead of just taking whatever happens to sort first alphabetically.
PREFERRED_GROQ_DEFAULTS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
]

# Deliberately favors small/flash models over "pro" tier ones: Gemini "pro"
# models frequently have a free-tier quota of exactly zero, so defaulting to
# one just produces an immediate 429 quota-exceeded error for anyone on a
# free API key. Pro models are still selectable by hand.
PREFERRED_GEMINI_DEFAULTS = [
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
]


def build_ai_prompt(summary):
    prompt = (
        "You are a cybersecurity analyst assistant. Explain the following graph "
        "search result from a security knowledge graph in clear, plain English "
        "for a mixed audience of technical and non technical stakeholders. "
        "Describe what the path means in practice, why it matters, and suggest "
        "two or three concrete next steps or remediation actions. Keep the answer "
        "under 250 words.\n\n"
        "Search technique: " + summary["case_name"] + " (" + summary["purpose"] + ")\n"
        "Start node: " + str(summary["start"]) + "\n"
        "Goal node: " + str(summary["goal"]) + "\n"
        "Status: " + summary["status"] + "\n"
        "Path: " + summary["path_text"] + "\n"
    )
    if summary["extra"] is not None:
        prompt += "Additional detail: " + str(summary["extra"]) + "\n"
    return prompt


def _raise_with_api_detail(response, provider_label):
    """Raise an error that includes the API's own explanation, not just the
    bare HTTP status. Groq and Gemini both return a JSON body describing
    exactly what was wrong (bad model name, bad key, rate limit, etc.), but
    response.raise_for_status() alone discards that body, which is why past
    errors only ever showed '400 Client Error' with no explanation."""
    if response.ok:
        return
    detail = ""
    try:
        body = response.json()
        if isinstance(body, dict):
            err = body.get("error", body)
            if isinstance(err, dict):
                detail = err.get("message") or err.get("code") or str(err)
            else:
                detail = str(err)
        else:
            detail = str(body)
    except ValueError:
        detail = response.text[:500]

    detail = detail or "no additional detail returned"

    # A 429 with "limit: 0" for a specific model means that model has NO
    # free-tier quota at all on this key's project, no matter how long you
    # wait or retry -- this happens on Pro-tier and image-generation Gemini
    # models in particular. Make that distinction obvious instead of letting
    # it look like an ordinary rate limit that will clear up on its own.
    lowered = detail.lower()
    if response.status_code == 429 and "free_tier" in lowered and "limit: 0" in lowered:
        detail += (
            " | This model has ZERO free-tier quota on your API key's project, so retrying "
            "will not help. This is common for Pro-tier and image-generation models. Pick a "
            "Flash or Flash-Lite model in the sidebar instead, or enable billing on the "
            "Google Cloud project behind this key."
        )

    message = provider_label + " API error " + str(response.status_code) + ": " + detail
    raise requests.exceptions.HTTPError(message, response=response)


def call_groq_api(api_key, model, prompt, max_tokens=500, json_mode=False):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful cybersecurity analyst assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
        "max_tokens": max_tokens,
    }
    if json_mode:
        payload["response_format"] = {"type": "json_object"}

    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)

    # Not every model on Groq supports response_format / JSON mode. If that is
    # why the request failed, quietly retry once without it rather than
    # surfacing a confusing error for something the caller did not ask about.
    if json_mode and response.status_code == 400 and "response_format" in response.text.lower():
        payload.pop("response_format", None)
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)

    _raise_with_api_detail(response, "Groq")
    data = response.json()
    choice = data["choices"][0]
    content = choice["message"]["content"].strip()

    # If the response was cut off because it hit max_tokens, say so plainly
    # instead of letting the caller fail later with a cryptic JSON parse
    # error that gives no hint about why the JSON is incomplete.
    if choice.get("finish_reason") == "length":
        raise ValueError(
            "The model's response was cut off before it finished (hit the " +
            str(max_tokens) + " token output limit). Try a smaller number of "
            "nodes, or pick a different model."
        )

    return content


def call_gemini_api(api_key, model, prompt, max_tokens=500, json_mode=False):
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        + model + ":generateContent?key=" + api_key
    )
    headers = {"Content-Type": "application/json"}
    generation_config = {
        "temperature": 0.4,
        "maxOutputTokens": max_tokens,
    }
    if json_mode:
        generation_config["responseMimeType"] = "application/json"

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ],
        "generationConfig": generation_config,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)

    # Older or more restricted Gemini models can reject responseMimeType.
    # Retry once in plain text mode rather than failing outright.
    if json_mode and response.status_code == 400 and "mimetype" in response.text.lower():
        generation_config.pop("responseMimeType", None)
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)

    _raise_with_api_detail(response, "Gemini")
    data = response.json()

    candidates = data.get("candidates") or []
    if not candidates:
        block_reason = (data.get("promptFeedback") or {}).get("blockReason")
        if block_reason:
            raise ValueError("Gemini blocked this request (reason: " + str(block_reason) + ").")
        raise ValueError("Gemini returned no candidates for this request.")

    candidate = candidates[0]
    finish_reason = candidate.get("finishReason")
    parts = (candidate.get("content") or {}).get("parts") or []
    text = "".join(part.get("text", "") for part in parts).strip()

    if finish_reason == "MAX_TOKENS" and not text:
        raise ValueError(
            "The model's response was cut off before it produced any output (hit the " +
            str(max_tokens) + " token output limit). Try a smaller number of "
            "nodes, or pick a different model."
        )

    return text


def list_groq_models(api_key):
    """Ask Groq directly which chat models this API key can currently use.
    Model availability on Groq changes over time (models get retired or
    renamed), so this is queried live instead of trusting a hard coded list."""
    url = "https://api.groq.com/openai/v1/models"
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.get(url, headers=headers, timeout=15)
    _raise_with_api_detail(response, "Groq")
    data = response.json()

    # Groq's /models endpoint lists every model it hosts, not just text chat
    # models: speech-to-text (whisper), text-to-speech (tts, playai, orpheus /
    # canopylabs voices), and safety classifiers (guard / prompt-guard /
    # moderation) all show up here too, but none of them work with the
    # /chat/completions JSON-generation prompts this app sends. Some of the
    # TTS voice models also require separate terms acceptance per voice,
    # which otherwise shows up as a confusing 400 error after the user picks
    # one from the dropdown. Filter all of these out up front.
    exclude_markers = (
        "whisper", "distil-whisper", "tts", "playai", "orpheus", "canopylabs",
        "guard", "prompt-guard", "moderation", "transcribe", "safety",
    )
    model_ids = []
    for entry in data.get("data", []):
        model_id = entry.get("id", "")
        if not model_id:
            continue
        if entry.get("active") is False:
            continue
        if any(marker in model_id.lower() for marker in exclude_markers):
            continue
        model_ids.append(model_id)

    return sorted(model_ids)


def list_gemini_models(api_key):
    """Ask Google directly which models this API key can currently use with
    generateContent. Gemini model names change fairly often (for example
    gemini-1.5-flash and gemini-2.5-flash were both later retired for new
    users), so this is queried live instead of trusting a hard coded list.

    Filtering on 'generateContent' support alone is not enough: Google's
    image-generation models (gemini-3-pro-image, gemini-2.5-flash-image, ...),
    text-to-speech models, and a few other specialty families all answer
    generateContent too, but they either return image/audio parts this app
    can't use for JSON, or sit on a paid-only quota tier (free-tier limit of
    0 requests), which is exactly the 429 error this app kept hitting. Both
    problems are avoided by excluding these non-text-chat families by name."""
    url = "https://generativelanguage.googleapis.com/v1beta/models?key=" + api_key
    response = requests.get(url, timeout=15)
    _raise_with_api_detail(response, "Gemini")
    data = response.json()

    exclude_markers = (
        "image", "imagen", "tts", "veo", "embedding", "aqa", "-live",
        "robotics", "computer-use", "video",
    )
    model_ids = []
    for entry in data.get("models", []):
        methods = entry.get("supportedGenerationMethods", [])
        if "generateContent" not in methods:
            continue
        name = entry.get("name", "")
        if name.startswith("models/"):
            name = name[len("models/"):]
        if not name:
            continue
        if any(marker in name.lower() for marker in exclude_markers):
            continue
        model_ids.append(name)

    return sorted(model_ids)


def _default_model_score(model_id):
    """Heuristic used only to choose which model is preselected in the
    dropdown, favoring smaller / lighter chat models that are far more
    likely to be usable on a free API key. 'Pro' tier models in particular
    often have a free-tier quota of zero (a 429 quota-exceeded error, not a
    bug in this app), so they are never auto-selected, only selectable by
    hand. Higher score wins."""
    low = model_id.lower()
    score = 0
    if "flash-lite" in low:
        score += 4
    elif "flash" in low:
        score += 3
    elif "instant" in low or "8b" in low or "-mini" in low or "small" in low:
        score += 2
    if "latest" in low:
        score += 1
    if "-pro" in low or low.endswith("pro"):
        score -= 5
    if any(tag in low for tag in ("preview", "exp", "image", "vision", "embedding", "live")):
        score -= 2
    return score


def _pick_default_index(models, preferred_ids):
    if not models:
        return 0
    for preferred in preferred_ids:
        if preferred in models:
            return models.index(preferred)
    ranked = sorted(range(len(models)), key=lambda i: (-_default_model_score(models[i]), models[i]))
    return ranked[0]


def get_selectable_models(provider, api_key, static_fallback, force_refresh=False):
    """Return (models, is_live) for the given provider and key. Results are
    cached in session state per API key so the provider is not re-queried on
    every Streamlit rerun. Falls back to the static offline list, tagged as
    not-live, if the key is missing or the live lookup fails."""
    if not api_key:
        return static_fallback, False

    cache_key = "_model_cache_" + provider
    cached = st.session_state.get(cache_key)
    if not force_refresh and cached and cached.get("api_key") == api_key and cached.get("models"):
        return cached["models"], True

    try:
        if provider == "Groq":
            models = list_groq_models(api_key)
        elif provider == "Google Gemini":
            models = list_gemini_models(api_key)
        else:
            models = []
        if not models:
            raise ValueError("The provider returned no usable chat models for this key")
        st.session_state[cache_key] = {"api_key": api_key, "models": models}
        return models, True
    except Exception:
        return static_fallback, False


def generate_ai_explanation(provider, api_key, model, summary):
    prompt = build_ai_prompt(summary)
    if provider == "Groq":
        return call_groq_api(api_key, model, prompt)
    elif provider == "Google Gemini":
        return call_gemini_api(api_key, model, prompt)
    else:
        raise ValueError("Unknown AI provider selected")


# ---------------------------------------------------------------------------
# AI-driven reasoning -- the LLM performs the search itself, replacing the
# classical DFS / BFS / UCS algorithms below as the primary reasoning engine.
# The classical functions are kept only as an automatic fallback in case an
# AI call fails or returns an unusable result, so the app never breaks.
# ---------------------------------------------------------------------------

def serialize_graph_for_llm(nodes_df, edges_df):
    lines = ["NODES:"]
    for _, row in nodes_df.iterrows():
        lines.append(
            str(row["ID"]) + " (Type=" + str(row["Type"]) +
            ", Risk=" + str(row["Risk"]) +
            ", Criticality=" + str(row["Criticality"]) +
            ", Security_Score=" + str(row["Security_Score"]) + ")"
        )
    lines.append("")
    lines.append("DIRECTED EDGES (Source -> Target):")
    for _, row in edges_df.iterrows():
        lines.append(
            str(row["Source"]) + " -> " + str(row["Target"]) +
            " [Relationship=" + str(row["Relationship"]) +
            ", Cost=" + str(row["Cost"]) +
            ", Risk=" + str(row["Risk"]) +
            ", Probability=" + str(row["Probability"]) +
            ", Time=" + str(row["Time"]) + "]"
        )
    return "\n".join(lines)


def build_search_reasoning_prompt(case_key, graph_text, start, goal, weight_field="Cost"):
    base = (
        "You are a graph search reasoning engine. Simulate the exact algorithm "
        "named below over the directed graph provided, step by step, exactly as "
        "a computer program would. Return ONLY a single JSON object as your "
        "entire response, with no markdown code fences, no commentary, and no "
        "extra text before or after the JSON.\n\n"
        "Graph:\n" + graph_text + "\n\n"
        "Start node: " + str(start) + "\n"
        "Goal node: " + str(goal) + "\n\n"
    )
    if case_key == "DFS":
        base += (
            "Algorithm: Depth First Search using a stack. At each node, consider "
            "unvisited successor nodes in sorted alphabetical order and explore "
            "the smallest ID first. Stop as soon as the goal node is visited.\n"
            "Return strictly this JSON shape and nothing else:\n"
            "{\"found\": true or false, \"path\": [\"start\", \"...\", \"goal\"], "
            "\"visited_order\": [\"...\"]}"
        )
    elif case_key == "BFS":
        base += (
            "Algorithm: Breadth First Search using a FIFO queue. At each node, "
            "enqueue unvisited successor nodes in sorted alphabetical order. "
            "Track the depth, meaning the number of edges from the start node, "
            "at which each node is first discovered. Stop as soon as the goal "
            "node is dequeued.\n"
            "Return strictly this JSON shape and nothing else:\n"
            "{\"found\": true or false, \"path\": [\"start\", \"...\", \"goal\"], "
            "\"visited_order\": [\"...\"], \"levels\": {\"node_id\": depth_integer}}"
        )
    else:
        base += (
            "Algorithm: Uniform Cost Search using a min priority queue ordered "
            "by cumulative edge weight, using the edge attribute '" + weight_field +
            "' as the per edge weight. Always expand the unvisited node with the "
            "lowest cumulative weight so far, breaking ties by alphabetical node "
            "ID. Stop as soon as the goal node is popped as the current minimum.\n"
            "Return strictly this JSON shape and nothing else:\n"
            "{\"found\": true or false, \"path\": [\"start\", \"...\", \"goal\"], "
            "\"visited_order\": [\"...\"], \"cost\": cumulative_weight_number}"
        )
    return base


def extract_json_object(text):
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:]
    start_idx = cleaned.find("{")
    end_idx = cleaned.rfind("}")
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise ValueError("No JSON object found in the model response")
    return json.loads(cleaned[start_idx:end_idx + 1])


def validate_path_against_graph(graph, path):
    if not path:
        return True
    for a, b in zip(path[:-1], path[1:]):
        if not graph.has_edge(a, b):
            return False
    return True


def run_llm_reasoning(case_key, graph, nodes_df, edges_df, start, goal, weight_field, provider, api_key, model):
    graph_text = serialize_graph_for_llm(nodes_df, edges_df)
    prompt = build_search_reasoning_prompt(case_key, graph_text, start, goal, weight_field)

    # 3000 tokens comfortably covers path + visited_order + levels/cost for
    # graphs up to the app's 60 node maximum; the earlier hard coded 500
    # token limit silently truncated the JSON on anything but tiny graphs,
    # which is what produced "Expecting ',' delimiter" style parse errors.
    reasoning_max_tokens = 3000

    if provider == "Groq":
        raw = call_groq_api(api_key, model, prompt, max_tokens=reasoning_max_tokens, json_mode=True)
    elif provider == "Google Gemini":
        raw = call_gemini_api(api_key, model, prompt, max_tokens=reasoning_max_tokens, json_mode=True)
    else:
        raise ValueError("Unknown AI provider selected")

    result = extract_json_object(raw)

    found = bool(result.get("found", False))
    path = result.get("path") if found else None
    visited_order = result.get("visited_order") or (path if path else [start])

    if path and not validate_path_against_graph(graph, path):
        raise ValueError("The model returned a path that does not match the actual graph edges")

    if case_key == "BFS":
        levels = result.get("levels", {}) or {}
        return path, visited_order, levels
    elif case_key == "UCS":
        cost = result.get("cost")
        return path, cost, visited_order
    else:
        return path, visited_order


# ---------------------------------------------------------------------------
# AI-driven synthetic data generation -- the LLM invents the node and edge
# data instead of Python's random module. The classical random generator
# functions above are kept only as an automatic fallback if the AI call is
# unavailable or fails, so the app never breaks.
# ---------------------------------------------------------------------------

def build_data_generation_prompt(num_nodes, seed):
    approx_extra_edges = max(1, int(num_nodes * 0.4))
    return (
        "You are a synthetic data generator for a cybersecurity and enterprise "
        "knowledge graph used in a graph search demo. Generate a directed graph "
        "with exactly " + str(num_nodes) + " nodes, using node IDs N1 through "
        "N" + str(num_nodes) + ".\n\n"
        "Use this random seed only as inspiration for variety, you do not need "
        "to reproduce it exactly: " + str(seed) + "\n\n"
        "Each node object must have exactly these fields:\n"
        "  ID (string, e.g. 'N1')\n"
        "  Type (string, one of: " + ", ".join(NODE_TYPES) + ")\n"
        "  Risk (integer 0 to 10)\n"
        "  Criticality (integer 0 to 10)\n"
        "  Owner (string, one of: " + ", ".join(OWNERS) + ")\n"
        "  Security_Score (integer 0 to 100)\n\n"
        "Each edge object must have exactly these fields:\n"
        "  Source (string, must be an existing node ID)\n"
        "  Target (string, must be an existing node ID, different from Source)\n"
        "  Relationship (string, one of: " + ", ".join(RELATIONSHIP_TYPES) + ")\n"
        "  Cost (number between 1 and 50)\n"
        "  Risk (integer 0 to 10)\n"
        "  Probability (number between 0 and 1)\n"
        "  Time (number between 1 and 20)\n\n"
        "Important: the edges must form a connected structure so that, treating "
        "edges as undirected, every node is reachable from every other node. "
        "Include a spanning tree of edges radiating out from N1, plus roughly " +
        str(approx_extra_edges) + " additional edges for complexity.\n\n"
        "Return ONLY a single JSON object, no markdown fences, no commentary, "
        "in exactly this shape:\n"
        "{\"nodes\": [ {\"ID\": \"N1\", \"Type\": \"...\", \"Risk\": 0, "
        "\"Criticality\": 0, \"Owner\": \"...\", \"Security_Score\": 0}, ... ], "
        "\"edges\": [ {\"Source\": \"N1\", \"Target\": \"N2\", "
        "\"Relationship\": \"...\", \"Cost\": 1.0, \"Risk\": 0, "
        "\"Probability\": 0.5, \"Time\": 1.0}, ... ]}"
    )


def compute_data_gen_max_tokens(num_nodes):
    """The synthetic dataset's JSON grows with the node count (each node
    plus its share of the spanning tree and extra edges), so a single fixed
    token budget either wastes tokens on small graphs or truncates large
    ones mid-JSON -- the latter is exactly what produced the earlier
    'Expecting , delimiter' parse errors on anything but a tiny graph.
    Scale the budget with num_nodes and cap it comfortably under what every
    live-discovered chat model on Groq/Gemini supports as a completion limit."""
    return min(8000, 1200 + num_nodes * 130)


def generate_synthetic_data_llm(num_nodes, seed, provider, api_key, model):
    prompt = build_data_generation_prompt(num_nodes, seed)
    data_gen_max_tokens = compute_data_gen_max_tokens(num_nodes)

    if provider == "Groq":
        raw = call_groq_api(api_key, model, prompt, max_tokens=data_gen_max_tokens, json_mode=True)
    elif provider == "Google Gemini":
        raw = call_gemini_api(api_key, model, prompt, max_tokens=data_gen_max_tokens, json_mode=True)
    else:
        raise ValueError("Unknown AI provider selected")

    result = extract_json_object(raw)
    nodes_list = result.get("nodes", [])
    edges_list = result.get("edges", [])

    if not nodes_list or not edges_list:
        raise ValueError("The model did not return usable node or edge data")

    nodes_df = pd.DataFrame(nodes_list)
    edges_df = pd.DataFrame(edges_list)

    required_node_cols = ["ID", "Type", "Risk", "Criticality", "Owner", "Security_Score"]
    required_edge_cols = ["Source", "Target", "Relationship", "Cost", "Risk", "Probability", "Time"]

    if not set(required_node_cols).issubset(set(nodes_df.columns)):
        raise ValueError("The model's node data is missing required fields")
    if not set(required_edge_cols).issubset(set(edges_df.columns)):
        raise ValueError("The model's edge data is missing required fields")

    nodes_df = nodes_df[required_node_cols].copy()
    edges_df = edges_df[required_edge_cols].copy()

    nodes_df["Risk"] = pd.to_numeric(nodes_df["Risk"], errors="coerce").fillna(0).astype(int)
    nodes_df["Criticality"] = pd.to_numeric(nodes_df["Criticality"], errors="coerce").fillna(0).astype(int)
    nodes_df["Security_Score"] = pd.to_numeric(nodes_df["Security_Score"], errors="coerce").fillna(0).astype(int)
    edges_df["Cost"] = pd.to_numeric(edges_df["Cost"], errors="coerce").fillna(1.0)
    edges_df["Risk"] = pd.to_numeric(edges_df["Risk"], errors="coerce").fillna(0).astype(int)
    edges_df["Probability"] = pd.to_numeric(edges_df["Probability"], errors="coerce").fillna(0.0)
    edges_df["Time"] = pd.to_numeric(edges_df["Time"], errors="coerce").fillna(1.0)

    nodes_df = nodes_df.drop_duplicates(subset="ID").reset_index(drop=True)
    valid_ids = set(nodes_df["ID"])
    edges_df = edges_df[edges_df["Source"].isin(valid_ids) & edges_df["Target"].isin(valid_ids)]
    edges_df = edges_df[edges_df["Source"] != edges_df["Target"]].reset_index(drop=True)

    if edges_df.empty:
        raise ValueError("The model's edges did not reference any valid node IDs")

    return nodes_df, edges_df


# ---------------------------------------------------------------------------
# Streamlit UI helpers
# ---------------------------------------------------------------------------

def apply_page_style():
    st.set_page_config(page_title="Kalsnet Graph Search and Reasoning Engine", layout="wide")
    st.markdown(
        """
        <style>
        .kalsnet-title {
            color: #0000CC;
            font-size: 44px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0px;
        }
        .kalsnet-subtitle {
            color: #0000CC;
            font-size: 22px;
            font-weight: 700;
            text-align: center;
            margin-top: 4px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="kalsnet-title">Kalsnet Graph Search and Reasoning Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="kalsnet-subtitle">Developed By Randy Singh from Kalsnet (KNet) Consulting Group</div>', unsafe_allow_html=True)


def render_ai_sidebar():
    st.sidebar.header("AI Setup (Required)")
    st.sidebar.write(
        "Connect a free Groq or Google Gemini account. This app now uses your "
        "chosen LLM to generate the synthetic graph data, perform the DFS, "
        "BFS, and UCS search reasoning itself, and write the plain English "
        "explanation of each result. Your key is only stored for this "
        "browser session and is sent directly to Groq or Google, never to "
        "Kalsnet. Without a key, each step falls back to the original "
        "classical algorithm so the app still runs."
    )

    with st.sidebar.expander("How to get a free Groq API key"):
        st.markdown(
            "1. Go to **console.groq.com** and sign up or log in (free).\n"
            "2. Open the **API Keys** section in the left menu.\n"
            "3. Click **Create API Key**, name it, and copy the key shown.\n"
            "4. Paste it into the *Groq API Key* box below.\n"
            "5. Groq's free tier includes generous rate limits on models "
            "such as Llama 3.3 70B, so no payment is required to try this."
        )

    with st.sidebar.expander("How to get a free Google Gemini API key"):
        st.markdown(
            "1. Go to **aistudio.google.com** and sign in with a Google account.\n"
            "2. Click **Get API key** (top left or in the left menu).\n"
            "3. Click **Create API key**, choose or create a Google Cloud "
            "project when prompted, and copy the key shown.\n"
            "4. Paste it into the *Gemini API Key* box below.\n"
            "5. Google AI Studio's free tier allows a limited number of "
            "requests per minute at no cost, which is enough for this app."
        )

    provider = st.sidebar.selectbox("AI Provider", ["None", "Groq", "Google Gemini"], key="ai_provider")

    api_key = ""
    model = None

    if provider == "Groq":
        api_key = st.sidebar.text_input("Groq API Key", type="password", key="groq_api_key")
        refresh = st.sidebar.button("Refresh Groq model list", key="groq_refresh_models")
        models, is_live = get_selectable_models("Groq", api_key, GROQ_MODELS, force_refresh=refresh)
        default_index = _pick_default_index(models, PREFERRED_GROQ_DEFAULTS)
        widget_key = "groq_model_" + str(abs(hash(tuple(models))))
        model = st.sidebar.selectbox("Groq Model", models, index=default_index, key=widget_key)
        if not api_key:
            st.sidebar.caption("Enter your Groq API key to load the live list of models it can use.")
        elif is_live:
            st.sidebar.caption("Model list fetched live from your Groq account just now.")
        else:
            st.sidebar.caption(
                "Could not fetch the live model list from Groq (bad key, no network, or a temporary "
                "Groq error). Showing an offline fallback list, which may include retired model names."
            )
    elif provider == "Google Gemini":
        api_key = st.sidebar.text_input("Gemini API Key", type="password", key="gemini_api_key")
        refresh = st.sidebar.button("Refresh Gemini model list", key="gemini_refresh_models")
        models, is_live = get_selectable_models("Google Gemini", api_key, GEMINI_MODELS, force_refresh=refresh)
        default_index = _pick_default_index(models, PREFERRED_GEMINI_DEFAULTS)
        widget_key = "gemini_model_" + str(abs(hash(tuple(models))))
        model = st.sidebar.selectbox("Gemini Model", models, index=default_index, key=widget_key)
        if not api_key:
            st.sidebar.caption("Enter your Gemini API key to load the live list of models it can use.")
        elif is_live:
            st.sidebar.caption("Model list fetched live from your Gemini account just now.")
        else:
            st.sidebar.caption(
                "Could not fetch the live model list from Gemini (bad key, no network, or a temporary "
                "Google error). Showing an offline fallback list, which may include retired model names."
            )
        if api_key and "-pro" in model.lower():
            st.sidebar.caption(
                "Note: Gemini 'Pro' models usually have a free-tier quota of zero and need a billing "
                "account enabled on the Google Cloud project behind this key. If you see a 429 quota "
                "error, switch to a Flash or Flash-Lite model instead."
            )

    st.session_state["ai_settings"] = {
        "provider": provider,
        "api_key": api_key,
        "model": model,
    }


def render_schema_section():
    with st.expander("View Node and Edge Schema"):
        st.subheader("Node Schema")
        st.dataframe(NODE_SCHEMA, use_container_width=True, hide_index=True)
        st.subheader("Edge Schema")
        st.dataframe(EDGE_SCHEMA, use_container_width=True, hide_index=True)


def render_data_section(case_key):
    st.subheader("Step 1: Provide Data")
    source = st.radio(
        "Choose a data source",
        ["Generate Synthetic Data", "Upload Real Data"],
        key=case_key + "_source",
        horizontal=True,
    )

    nodes_df = None
    edges_df = None

    if source == "Generate Synthetic Data":
        col1, col2, col3 = st.columns(3)
        with col1:
            num_nodes = st.slider("Number of nodes", min_value=5, max_value=60, value=15, key=case_key + "_numnodes")
        with col2:
            seed = st.number_input("Random seed", min_value=1, max_value=9999, value=42, key=case_key + "_seed")
        with col3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=case_key + "_showall")

        if st.button("Generate Synthetic Data Now", key=case_key + "_gen_button"):
            ai_settings = st.session_state.get("ai_settings", {"provider": "None", "api_key": "", "model": None})
            provider = ai_settings.get("provider", "None")
            api_key = ai_settings.get("api_key", "")
            model = ai_settings.get("model")

            if provider == "None" or not api_key:
                st.warning(
                    "Data generation is now performed by an LLM. Select Groq or "
                    "Google Gemini and paste a free API key in the sidebar for "
                    "AI-generated data. Using the classical random generator for "
                    "this run instead."
                )
                nodes_df = generate_synthetic_nodes(num_nodes, seed=seed)
                edges_df = generate_synthetic_edges(nodes_df, seed=seed)
            else:
                try:
                    with st.spinner("Generating synthetic data with " + provider + " ..."):
                        nodes_df, edges_df = generate_synthetic_data_llm(num_nodes, seed, provider, api_key, model)
                except Exception as exc:
                    st.error(
                        "AI data generation failed (" + str(exc) + "). Falling "
                        "back to the classical random generator for this run."
                    )
                    nodes_df = generate_synthetic_nodes(num_nodes, seed=seed)
                    edges_df = generate_synthetic_edges(nodes_df, seed=seed)

            st.session_state[case_key + "_nodes"] = nodes_df
            st.session_state[case_key + "_edges"] = edges_df

        if case_key + "_nodes" in st.session_state:
            nodes_df = st.session_state[case_key + "_nodes"]
            edges_df = st.session_state[case_key + "_edges"]
            if show_all:
                st.write("Complete synthetic node data, " + str(len(nodes_df)) + " rows")
                st.dataframe(nodes_df, use_container_width=True, hide_index=True)
                st.write("Complete synthetic edge data, " + str(len(edges_df)) + " rows")
                st.dataframe(edges_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of synthetic node data, first 5 rows")
                st.dataframe(nodes_df.head(5), use_container_width=True, hide_index=True)
                st.write("Preview of synthetic edge data, first 5 rows")
                st.dataframe(edges_df.head(5), use_container_width=True, hide_index=True)

    else:
        node_file = st.file_uploader("Upload Node CSV File", type=["csv"], key=case_key + "_nodefile")
        edge_file = st.file_uploader("Upload Edge CSV File", type=["csv"], key=case_key + "_edgefile")

        if node_file is not None and edge_file is not None:
            nodes_df = pd.read_csv(node_file)
            edges_df = pd.read_csv(edge_file)
            st.session_state[case_key + "_nodes"] = nodes_df
            st.session_state[case_key + "_edges"] = edges_df

        if case_key + "_nodes" in st.session_state:
            nodes_df = st.session_state[case_key + "_nodes"]
            edges_df = st.session_state[case_key + "_edges"]
            st.write("Uploaded node data")
            st.dataframe(nodes_df, use_container_width=True, hide_index=True)
            st.write("Uploaded edge data")
            st.dataframe(edges_df, use_container_width=True, hide_index=True)

    return nodes_df, edges_df


def render_ai_insights_section(case_key, summary):
    st.subheader("Step 5: AI-Powered Insights (Optional)")

    ai_settings = st.session_state.get("ai_settings", {"provider": "None", "api_key": "", "model": None})
    provider = ai_settings.get("provider", "None")
    api_key = ai_settings.get("api_key", "")
    model = ai_settings.get("model")

    if provider == "None":
        st.info(
            "Select a provider (Groq or Google Gemini) and paste a free API key "
            "in the sidebar to generate a plain English explanation of this result."
        )
        return

    if not api_key:
        st.warning("Enter your " + provider + " API key in the sidebar to enable this feature.")
        return

    st.write("Provider selected: " + provider + " | Model: " + str(model))

    if st.button("Generate AI Explanation", key=case_key + "_ai_button"):
        with st.spinner("Contacting " + provider + " ..."):
            try:
                explanation = generate_ai_explanation(provider, api_key, model, summary)
                summary["ai_explanation"] = explanation
                summary["ai_provider"] = provider + " (" + str(model) + ")"
                st.session_state[case_key + "_summary"] = summary
            except Exception as exc:
                st.error("AI request failed: " + str(exc))

    if summary.get("ai_explanation"):
        st.markdown("**AI Explanation (" + str(summary.get("ai_provider", "")) + "):**")
        st.write(summary["ai_explanation"])


def render_case(case_key):
    info = CASE_INFO[case_key]
    st.header(info["full_name"] + " -- " + info["purpose"])
    st.write(info["explanation"])

    st.subheader("Typical Use Cases")
    for item in info["use_cases"]:
        st.write("- " + item)

    render_schema_section()

    nodes_df, edges_df = render_data_section(case_key)

    if nodes_df is None or edges_df is None:
        st.info("Provide data above to continue with this case")
        return

    graph = build_graph(nodes_df, edges_df)
    node_ids = list(nodes_df["ID"])

    st.subheader("Step 2: Choose Start and Goal Nodes")
    col1, col2 = st.columns(2)
    with col1:
        start = st.selectbox("Start node", node_ids, key=case_key + "_start")
    with col2:
        goal = st.selectbox("Goal node", node_ids, index=min(len(node_ids) - 1, 1), key=case_key + "_goal")

    weight_field = "Cost"
    if case_key == "UCS":
        weight_field = st.selectbox(
            "Cost field used by Uniform Cost Search",
            ["Cost", "Risk", "Time", "Probability"],
            key=case_key + "_weightfield",
        )

    if st.button("Run " + info["full_name"], key=case_key + "_run"):
        ai_settings = st.session_state.get("ai_settings", {"provider": "None", "api_key": "", "model": None})
        provider = ai_settings.get("provider", "None")
        api_key = ai_settings.get("api_key", "")
        model = ai_settings.get("model")

        if provider == "None" or not api_key:
            st.warning(
                "Reasoning for this app is now performed by an LLM. Select Groq "
                "or Google Gemini and paste a free API key in the sidebar, then "
                "click Run again."
            )
        else:
            reasoning_note = "Reasoning performed by " + provider + " (" + str(model) + ")"
            try:
                with st.spinner("Reasoning with " + provider + " ..."):
                    if case_key == "DFS":
                        path, visited_order = run_llm_reasoning(
                            case_key, graph, nodes_df, edges_df, start, goal, weight_field, provider, api_key, model
                        )
                        extra = reasoning_note
                    elif case_key == "BFS":
                        path, visited_order, levels = run_llm_reasoning(
                            case_key, graph, nodes_df, edges_df, start, goal, weight_field, provider, api_key, model
                        )
                        extra = "Depth level of goal node: " + str(levels.get(goal, "not reached")) + " | " + reasoning_note
                    else:
                        path, cost, visited_order = run_llm_reasoning(
                            case_key, graph, nodes_df, edges_df, start, goal, weight_field, provider, api_key, model
                        )
                        extra = "Total cumulative " + weight_field.lower() + " of path: " + \
                            (str(cost) if cost is not None else "not applicable") + " | " + reasoning_note
            except Exception as exc:
                st.error(
                    "AI reasoning failed (" + str(exc) + "). Falling back to the "
                    "classical algorithm for this run only."
                )
                if case_key == "DFS":
                    path, visited_order = dfs_search(graph, start, goal)
                    extra = "Fallback: classical algorithm used because AI reasoning failed"
                elif case_key == "BFS":
                    path, visited_order, levels = bfs_search(graph, start, goal)
                    extra = "Depth level of goal node: " + str(levels.get(goal, "not reached")) + \
                        " | Fallback: classical algorithm used because AI reasoning failed"
                else:
                    path, cost, visited_order = ucs_search(graph, start, goal, weight_field=weight_field)
                    extra = "Total cumulative " + weight_field.lower() + " of path: " + \
                        (str(round(cost, 2)) if cost is not None else "not applicable") + \
                        " | Fallback: classical algorithm used because AI reasoning failed"

            summary = build_result_summary(case_key, start, goal, path, extra, nodes_df, edges_df, visited_order)
            st.session_state[case_key + "_summary"] = summary

    if case_key + "_summary" in st.session_state:
        summary = st.session_state[case_key + "_summary"]

        st.subheader("Step 3: Results")
        st.write("Status: " + summary["status"])
        st.write("Path: " + summary["path_text"])
        if summary["extra"] is not None:
            st.write(summary["extra"])
        st.write("Nodes visited during search, in order:")
        st.write(" then ".join(summary["visited_order"]))

        st.subheader("Graph Visualization")
        fig = plot_graph(graph, path=summary["path"], title=info["full_name"] + " Result")
        st.pyplot(fig)

        render_ai_insights_section(case_key, summary)

        st.subheader("Step 4: Export Results")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.download_button(
                "Download PDF",
                data=export_pdf_bytes(summary),
                file_name=case_key + "_result.pdf",
                mime="application/pdf",
                key=case_key + "_pdf",
            )
        with col2:
            st.download_button(
                "Download Word",
                data=export_word_bytes(summary),
                file_name=case_key + "_result.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                key=case_key + "_word",
            )
        with col3:
            st.download_button(
                "Download CSV",
                data=export_csv_bytes(summary["path"], nodes_df),
                file_name=case_key + "_result.csv",
                mime="text/csv",
                key=case_key + "_csv",
            )
        with col4:
            st.download_button(
                "Download Text",
                data=export_text_bytes(summary),
                file_name=case_key + "_result.txt",
                mime="text/plain",
                key=case_key + "_text",
            )


# ---------------------------------------------------------------------------
# Main application
# ---------------------------------------------------------------------------

def main():
    apply_page_style()
    render_ai_sidebar()

    st.write(
        "This application demonstrates three Uninformed Search techniques, Depth First Search, "
        "Breadth First Search, and Uniform Cost Search, applied to a security and enterprise "
        "Knowledge Graph. Select a tab below to explore each technique. Connect a free Groq or "
        "Google Gemini API key in the sidebar so the LLM generates the synthetic data, performs "
        "the search reasoning itself, and writes a plain English explanation of each result."
    )

    tab_dfs, tab_bfs, tab_ucs = st.tabs([
        "DFS -- Attack Chain Exploration",
        "BFS -- Blast Radius and Impact Analysis",
        "UCS -- Least Cost Remediation Path",
    ])

    with tab_dfs:
        render_case("DFS")

    with tab_bfs:
        render_case("BFS")

    with tab_ucs:
        render_case("UCS")

    st.markdown("---")
    st.caption("Kalsnet Graph Search and Reasoning Engine, Developed By Randy Singh from Kalsnet (KNet) Consulting Group")


if __name__ == "__main__":
    main()
