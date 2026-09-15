# Kalsnet Universal Search and Reasoning Engine
# Developed By Randy Singh from Kalsnet (KNet) Consulting Group

# This Streamlit application implements thirteen categories of search
# techniques, covering roughly ninety individual algorithms, applied to
# synthetic or uploaded enterprise and security data.


import io
import re
import math
import bisect
import random
import heapq
import datetime

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
from reportlab.lib import colors as rl_colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch


def _default_seed():
    """Return a fresh random default for a Random seed widget.

    Every Random seed number_input below used to default to the fixed value
    42, which meant every category and every algorithm generated the exact
    same synthetic data unless a person manually typed a different seed. A
    Streamlit widget's `value` argument only takes effect the first time
    that widget's key is created in a session, so calling this on every
    script rerun still lets each seed widget keep whatever the person set
    once it exists, while giving every category, sub search, and fresh
    session a genuinely different starting seed instead of always the same
    identical looking synthetic data.
    """
    return random.randint(1, 9999)


# ---------------------------------------------------------------------------
# Reference lists
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
TABLE_CATEGORIES = ["Finance", "HR", "IT", "Sales", "Legal", "Operations"]
EVENT_TYPES = ["Login", "FileAccess", "NetworkConnection", "Alert", "ConfigChange"]
COUNTRIES = ["USA", "UK", "Canada", "Germany", "India", "Australia"]
TEXT_TOPICS = ["firewall", "database", "server", "employee", "vulnerability",
               "network", "application", "incident", "credential", "vendor"]
TEXT_VERBS = ["accessed", "scanned", "updated", "reviewed", "detected",
              "isolated", "patched", "monitored", "flagged", "restored"]

NODE_SCHEMA = pd.DataFrame([
    {"Field": "ID", "Type": "String", "Description": "Unique identifier for the node",
     "How Calculated": "Assigned in generation order as N1, N2, N3 and so on, one per node created."},
    {"Field": "Type", "Type": "String", "Description": "Category of the node, for example Endpoint, Server, Database",
     "How Calculated": "Chosen at random, uniformly, from the fixed NODE_TYPES reference list using the node generator's seeded random number generator."},
    {"Field": "Risk", "Type": "Integer 0 to 10", "Description": "Risk score assigned to the node",
     "How Calculated": "A random integer drawn uniformly from 0 to 10 inclusive using the seeded random number generator."},
    {"Field": "Criticality", "Type": "Integer 0 to 10", "Description": "Business criticality of the node",
     "How Calculated": "A random integer drawn uniformly from 0 to 10 inclusive, independent of Risk, using the seeded random number generator."},
    {"Field": "Owner", "Type": "String", "Description": "Team responsible for the node",
     "How Calculated": "Chosen at random, uniformly, from the fixed OWNERS reference list."},
    {"Field": "Security_Score", "Type": "Integer 0 to 100", "Description": "Overall security posture score",
     "How Calculated": "A random integer drawn uniformly from 0 to 100 inclusive, independent of Risk and Criticality."},
    {"Field": "X", "Type": "Float", "Description": "Synthetic coordinate used by heuristic search techniques",
     "How Calculated": "A random value drawn uniformly from 0 to 100 and rounded to one decimal place, used only to compute straight line distance heuristics for A Star and related techniques."},
    {"Field": "Y", "Type": "Float", "Description": "Synthetic coordinate used by heuristic search techniques",
     "How Calculated": "A random value drawn uniformly from 0 to 100 and rounded to one decimal place, paired with X to place the node in a synthetic two dimensional plane."},
])

EDGE_SCHEMA = pd.DataFrame([
    {"Field": "Source", "Type": "String", "Description": "ID of the source node",
     "How Calculated": "For the first pass of edges, each node from the second one onward is connected back to a randomly chosen earlier node, guaranteeing the graph is reachable from the start; extra edges then pick two random existing node IDs."},
    {"Field": "Target", "Type": "String", "Description": "ID of the target node",
     "How Calculated": "The node being connected to, either the next node in generation order for the guaranteed connectivity pass, or a second randomly chosen node for extra edges."},
    {"Field": "Relationship", "Type": "String", "Description": "Type of relationship between the nodes",
     "How Calculated": "Chosen at random, uniformly, from the fixed RELATIONSHIP_TYPES reference list."},
    {"Field": "Cost", "Type": "Float", "Description": "Cost of traversing this relationship",
     "How Calculated": "A random value drawn uniformly from 1 to 50 and rounded to two decimals; when negative costs are enabled for an algorithm, roughly 15 percent of edges instead get a negative cost drawn uniformly from -1 to -10."},
    {"Field": "Risk", "Type": "Integer 0 to 10", "Description": "Risk score of this relationship",
     "How Calculated": "A random integer drawn uniformly from 0 to 10 inclusive, independent of the node level Risk field."},
    {"Field": "Probability", "Type": "Float 0 to 1", "Description": "Estimated probability of exploit",
     "How Calculated": "A random value drawn uniformly from 0 to 1 and rounded to two decimals."},
    {"Field": "Time", "Type": "Float", "Description": "Estimated time in hours to traverse this relationship",
     "How Calculated": "A random value drawn uniformly from 1 to 20 and rounded to two decimals."},
])

TEXT_SCHEMA = pd.DataFrame([
    {"Field": "DocID", "Type": "String", "Description": "Unique identifier for the document",
     "How Calculated": "Assigned in generation order as D1, D2, D3 and so on, one per document created."},
    {"Field": "Title", "Type": "String", "Description": "Document title",
     "How Calculated": "Built automatically as the literal text Document followed by the document's sequence number."},
    {"Field": "Text", "Type": "String", "Description": "Full text content of the document",
     "How Calculated": "Built by randomly choosing three words from the TEXT_TOPICS list and two words from the TEXT_VERBS list, shuffling all five words into a random order, and appending the literal text report number followed by the document's sequence number."},
])

TABLE_SCHEMA = pd.DataFrame([
    {"Field": "RecordID", "Type": "Integer", "Description": "Unique identifier for the record",
     "How Calculated": "Assigned in generation order starting at 1, one per record created."},
    {"Field": "Key", "Type": "String", "Description": "Business key used for lookups",
     "How Calculated": "The letter K followed by a random four digit integer drawn uniformly from 1000 to 9999."},
    {"Field": "Category", "Type": "String", "Description": "Business category of the record",
     "How Calculated": "Chosen at random, uniformly, from the fixed TABLE_CATEGORIES reference list."},
    {"Field": "Amount", "Type": "Float", "Description": "Monetary amount associated with the record",
     "How Calculated": "A random value drawn uniformly from 10 to 10000 and rounded to two decimals."},
    {"Field": "Risk_Score", "Type": "Integer 0 to 100", "Description": "Risk score of the record",
     "How Calculated": "A random integer drawn uniformly from 0 to 100 inclusive."},
    {"Field": "Country", "Type": "String", "Description": "Country associated with the record",
     "How Calculated": "Chosen at random, uniformly, from the fixed COUNTRIES reference list."},
    {"Field": "Probability", "Type": "Float 0 to 1", "Description": "Estimated probability used by probabilistic search",
     "How Calculated": "A random value drawn uniformly from 0 to 1 and rounded to three decimals."},
    {"Field": "IP_Address", "Type": "String", "Description": "Source IP address, used by cybersecurity search",
     "How Calculated": "Four random integers, each drawn uniformly from 1 to 255, joined with periods into a dotted quad address."},
    {"Field": "File_Hash", "Type": "String", "Description": "File hash, used by cybersecurity search",
     "How Calculated": "Sixteen characters chosen at random from the hexadecimal digits 0 through 9 and a through f, concatenated together."},
    {"Field": "Event_Type", "Type": "String", "Description": "Type of security or business event",
     "How Calculated": "Chosen at random, uniformly, from the fixed EVENT_TYPES reference list."},
    {"Field": "Hour", "Type": "Integer 0 to 23", "Description": "Hour of day the event occurred",
     "How Calculated": "A random integer drawn uniformly from 0 to 23 inclusive, representing a 24 hour clock hour."},
])

CITIES_SCHEMA = pd.DataFrame([
    {"Field": "CityID", "Type": "String", "Description": "Unique identifier for the city or stop",
     "How Calculated": "Assigned in generation order as C1, C2, C3 and so on, one per stop created."},
    {"Field": "Name", "Type": "String", "Description": "Display name of the city or stop",
     "How Calculated": "Built automatically as the literal text City followed by the stop's sequence number."},
    {"Field": "X", "Type": "Float", "Description": "Horizontal coordinate",
     "How Calculated": "A random value drawn uniformly from 0 to 100 and rounded to one decimal place."},
    {"Field": "Y", "Type": "Float", "Description": "Vertical coordinate",
     "How Calculated": "A random value drawn uniformly from 0 to 100 and rounded to one decimal place, independent of X."},
])

CSP_SCHEMA = pd.DataFrame([
    {"Field": "RegionID", "Type": "String", "Description": "Unique identifier for the region or variable",
     "How Calculated": "Assigned in generation order as R1, R2, R3 and so on, one per region created."},
    {"Field": "Name", "Type": "String", "Description": "Display name of the region",
     "How Calculated": "Built automatically as the literal text Region followed by the region's sequence number."},
    {"Field": "RegionA, RegionB", "Type": "String pair", "Description": "Adjacency constraint between two regions",
     "How Calculated": "Built in two passes: first, each region from the second one onward is paired with a randomly chosen earlier region, guaranteeing every region has at least one neighbor; then extra adjacency pairs, about 30 percent of the region count, connect two randomly chosen distinct regions."},
])


# ---------------------------------------------------------------------------
# Graph domain
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
            "X": round(rng.uniform(0, 100), 1),
            "Y": round(rng.uniform(0, 100), 1),
        })
    return pd.DataFrame(rows)


def generate_synthetic_edges(nodes_df, extra_edge_ratio=0.4, seed=42, allow_negative=False, force_dag=False):
    rng = random.Random(seed)
    node_ids = list(nodes_df["ID"])
    rows = []
    for i in range(1, len(node_ids)):
        source = rng.choice(node_ids[:i])
        target = node_ids[i]
        rows.append(_make_edge_row(rng, source, target, allow_negative))
    if not force_dag:
        num_extra = int(len(node_ids) * extra_edge_ratio)
        for _ in range(num_extra):
            source, target = rng.sample(node_ids, 2)
            rows.append(_make_edge_row(rng, source, target, allow_negative))
    return pd.DataFrame(rows)


def _make_edge_row(rng, source, target, allow_negative=False):
    cost = round(rng.uniform(1, 50), 2)
    if allow_negative and rng.random() < 0.15:
        cost = -round(rng.uniform(1, 10), 2)
    return {
        "Source": source,
        "Target": target,
        "Relationship": rng.choice(RELATIONSHIP_TYPES),
        "Cost": cost,
        "Risk": rng.randint(0, 10),
        "Probability": round(rng.uniform(0, 1), 2),
        "Time": round(rng.uniform(1, 20), 2),
    }


def build_graph(nodes_df, edges_df):
    graph = nx.DiGraph()
    for _, row in nodes_df.iterrows():
        graph.add_node(row["ID"], **row.drop(labels=["ID"]).to_dict())
    for _, row in edges_df.iterrows():
        graph.add_edge(row["Source"], row["Target"], **row.drop(labels=["Source", "Target"]).to_dict())
    return graph


# ---------------------------------------------------------------------------
# Text domain
# ---------------------------------------------------------------------------

def build_synthetic_corpus(num_docs, seed=42):
    rng = random.Random(seed)
    rows = []
    for i in range(1, num_docs + 1):
        words = [rng.choice(TEXT_TOPICS) for _ in range(3)] + [rng.choice(TEXT_VERBS) for _ in range(2)]
        rng.shuffle(words)
        text = " ".join(words) + " report number " + str(i)
        rows.append({"DocID": "D" + str(i), "Title": "Document " + str(i), "Text": text})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Table domain
# ---------------------------------------------------------------------------

def build_synthetic_table(num_records, seed=42):
    rng = random.Random(seed)
    rows = []
    for i in range(1, num_records + 1):
        rows.append({
            "RecordID": i,
            "Key": "K" + str(rng.randint(1000, 9999)),
            "Category": rng.choice(TABLE_CATEGORIES),
            "Amount": round(rng.uniform(10, 10000), 2),
            "Risk_Score": rng.randint(0, 100),
            "Country": rng.choice(COUNTRIES),
            "Probability": round(rng.uniform(0, 1), 3),
            "IP_Address": ".".join(str(rng.randint(1, 255)) for _ in range(4)),
            "File_Hash": "".join(rng.choice("0123456789abcdef") for _ in range(16)),
            "Event_Type": rng.choice(EVENT_TYPES),
            "Hour": rng.randint(0, 23),
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Cities domain, used for TSP style optimization search
# ---------------------------------------------------------------------------

def build_synthetic_cities(num_cities, seed=42):
    rng = random.Random(seed)
    rows = []
    for i in range(1, num_cities + 1):
        rows.append({
            "CityID": "C" + str(i),
            "Name": "City " + str(i),
            "X": round(rng.uniform(0, 100), 1),
            "Y": round(rng.uniform(0, 100), 1),
        })
    return pd.DataFrame(rows)


def tour_distance(cities_df, tour):
    coords = {row["CityID"]: (row["X"], row["Y"]) for _, row in cities_df.iterrows()}
    total = 0.0
    for i in range(len(tour)):
        a = coords[tour[i]]
        b = coords[tour[(i + 1) % len(tour)]]
        total += math.hypot(a[0] - b[0], a[1] - b[1])
    return total


# ---------------------------------------------------------------------------
# CSP domain, used for constraint based search, map coloring style problem
# ---------------------------------------------------------------------------

def build_synthetic_regions(num_regions, seed=42):
    rng = random.Random(seed)
    rows = [{"RegionID": "R" + str(i), "Name": "Region " + str(i)} for i in range(1, num_regions + 1)]
    regions_df = pd.DataFrame(rows)
    region_ids = list(regions_df["RegionID"])
    edges = []
    for i in range(1, len(region_ids)):
        a = rng.choice(region_ids[:i])
        b = region_ids[i]
        edges.append({"RegionA": a, "RegionB": b})
    extra = int(num_regions * 0.3)
    for _ in range(extra):
        a, b = rng.sample(region_ids, 2)
        if a != b:
            edges.append({"RegionA": a, "RegionB": b})
    adjacency_df = pd.DataFrame(edges)
    return regions_df, adjacency_df


def build_adjacency_map(regions_df, adjacency_df):
    adj = {r: set() for r in regions_df["RegionID"]}
    for _, row in adjacency_df.iterrows():
        if row["RegionA"] in adj and row["RegionB"] in adj:
            adj[row["RegionA"]].add(row["RegionB"])
            adj[row["RegionB"]].add(row["RegionA"])
    return adj


# ---------------------------------------------------------------------------
# Game tree domain, used for adversarial search
# ---------------------------------------------------------------------------

def build_synthetic_gametree(branching, depth, seed=42, use_chance_nodes=False):
    rng = random.Random(seed)
    counter = {"n": 0}

    def build(d):
        counter["n"] += 1
        node_id = "G" + str(counter["n"])
        if d == 0:
            return {"id": node_id, "value": rng.randint(-50, 50), "children": [], "type": "leaf"}
        children = [build(d - 1) for _ in range(branching)]
        node_type = "chance" if (use_chance_nodes and d % 2 == 0) else "internal"
        if node_type == "chance":
            probs = [rng.random() for _ in children]
            total = sum(probs)
            probs = [p / total for p in probs]
            for child, p in zip(children, probs):
                child["prob"] = round(p, 2)
        return {"id": node_id, "children": children, "type": node_type}

    root = build(depth)
    root["type"] = "root" if root.get("type") != "leaf" else "leaf"
    return root

# ---------------------------------------------------------------------------
# Category 1: Classical AI and State Space Search
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
        for neighbor in sorted(graph.successors(node), reverse=True):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None, visited_order


def bfs_search(graph, start, goal):
    visited_order = []
    visited = {start}
    queue = [(start, [start])]
    head = 0
    while head < len(queue):
        node, path = queue[head]
        head += 1
        visited_order.append(node)
        if node == goal:
            return path, visited_order
        for neighbor in sorted(graph.successors(node)):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, visited_order


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


def depth_limited_search(graph, start, goal, limit):
    stack = [(start, [start], 0)]
    visited_order = []
    while stack:
        node, path, depth = stack.pop()
        visited_order.append(node)
        if node == goal:
            return path, visited_order
        if depth < limit:
            for n in sorted(graph.successors(node), reverse=True):
                if n not in path:
                    stack.append((n, path + [n], depth + 1))
    return None, visited_order


def iddfs_search(graph, start, goal, max_limit):
    total_visited = []
    for limit in range(0, max_limit + 1):
        path, visited = depth_limited_search(graph, start, goal, limit)
        total_visited.extend(visited)
        if path:
            return path, total_visited, limit
    return None, total_visited, max_limit


def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start], [start]
    forward_frontier = {start: [start]}
    backward_frontier = {goal: [goal]}
    forward_visited = {start}
    backward_visited = {goal}
    rev_graph = graph.reverse()
    visited_order = [start, goal]
    steps = 0
    while forward_frontier and backward_frontier and steps < 500:
        steps += 1
        new_forward = {}
        for node, path in forward_frontier.items():
            for n in graph.successors(node):
                if n in backward_frontier:
                    return path + backward_frontier[n][::-1][1:], visited_order
                if n not in forward_visited:
                    forward_visited.add(n)
                    new_forward[n] = path + [n]
                    visited_order.append(n)
        forward_frontier = new_forward
        new_backward = {}
        for node, path in backward_frontier.items():
            for n in rev_graph.successors(node):
                if n in forward_frontier:
                    return forward_frontier[n] + path[::-1][1:], visited_order
                if n not in backward_visited:
                    backward_visited.add(n)
                    new_backward[n] = path + [n]
                    visited_order.append(n)
        backward_frontier = new_backward
    return None, visited_order


def tree_search_no_visited(graph, start, goal, max_depth=8, max_expansions=400):
    stack = [(start, [start])]
    visited_order = []
    count = 0
    while stack and count < max_expansions:
        node, path = stack.pop()
        visited_order.append(node)
        count += 1
        if node == goal:
            return path, visited_order
        if len(path) < max_depth:
            for n in sorted(graph.successors(node), reverse=True):
                stack.append((n, path + [n]))
    return None, visited_order


def graph_search_with_explored_set(graph, start, goal):
    return dfs_search(graph, start, goal)


# ---------------------------------------------------------------------------
# Category 2: Informed and Heuristic Search
# ---------------------------------------------------------------------------

def heuristic_distance(graph, node, goal):
    x1, y1 = graph.nodes[node]["X"], graph.nodes[node]["Y"]
    x2, y2 = graph.nodes[goal]["X"], graph.nodes[goal]["Y"]
    return math.hypot(x1 - x2, y1 - y2)


def greedy_best_first_search(graph, start, goal):
    visited = set()
    visited_order = []
    counter = 0
    frontier = [(heuristic_distance(graph, start, goal), counter, start, [start])]
    while frontier:
        h, _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)
        if node == goal:
            return path, visited_order
        for n in graph.successors(node):
            if n not in visited:
                counter += 1
                heapq.heappush(frontier, (heuristic_distance(graph, n, goal), counter, n, path + [n]))
    return None, visited_order


def astar_search(graph, start, goal, weight_field="Cost", heuristic_weight=1.0):
    visited = set()
    visited_order = []
    counter = 0
    frontier = [(heuristic_distance(graph, start, goal) * heuristic_weight, 0.0, counter, start, [start])]
    while frontier:
        f, g, _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)
        if node == goal:
            return path, g, visited_order
        for n in graph.successors(node):
            if n not in visited:
                edge_cost = graph[node][n].get(weight_field, 1.0)
                new_g = g + edge_cost
                counter += 1
                new_f = new_g + heuristic_distance(graph, n, goal) * heuristic_weight
                heapq.heappush(frontier, (new_f, new_g, counter, n, path + [n]))
    return None, None, visited_order


def ida_star_search(graph, start, goal, weight_field="Cost"):
    threshold = heuristic_distance(graph, start, goal)
    visited_order = []

    def search(path, g, bound):
        node = path[-1]
        visited_order.append(node)
        f = g + heuristic_distance(graph, node, goal)
        if f > bound:
            return f, None
        if node == goal:
            return "FOUND", path[:]
        minimum = float("inf")
        for n in graph.successors(node):
            if n not in path:
                edge_cost = graph[node][n].get(weight_field, 1.0)
                path.append(n)
                t, found_path = search(path, g + edge_cost, bound)
                if t == "FOUND":
                    return "FOUND", found_path
                if t < minimum:
                    minimum = t
                path.pop()
        return minimum, None

    for _ in range(40):
        t, found_path = search([start], 0.0, threshold)
        if t == "FOUND":
            return found_path, visited_order
        if t == float("inf"):
            return None, visited_order
        threshold = t
    return None, visited_order


def beam_search(graph, start, goal, beam_width=3, max_steps=100):
    frontier = [(heuristic_distance(graph, start, goal), start, [start])]
    visited_order = []
    for _ in range(max_steps):
        if not frontier:
            return None, visited_order
        next_candidates = []
        for h, node, path in frontier:
            visited_order.append(node)
            if node == goal:
                return path, visited_order
            for n in graph.successors(node):
                if n not in path:
                    next_candidates.append((heuristic_distance(graph, n, goal), n, path + [n]))
        next_candidates.sort(key=lambda x: x[0])
        frontier = next_candidates[:beam_width]
    return None, visited_order


def hill_climbing_search(graph, start, goal, max_steps=100):
    current = start
    path = [start]
    visited_order = [start]
    for _ in range(max_steps):
        if current == goal:
            return path, visited_order, "Reached the goal node"
        neighbors = list(graph.successors(current))
        if not neighbors:
            return None, visited_order, "Stuck, node " + current + " has no outgoing neighbors"
        neighbors.sort(key=lambda n: heuristic_distance(graph, n, goal))
        best = neighbors[0]
        if heuristic_distance(graph, best, goal) >= heuristic_distance(graph, current, goal):
            return None, visited_order, "Stuck in a local optimum at node " + current
        current = best
        path.append(current)
        visited_order.append(current)
    return None, visited_order, "Maximum number of steps reached"


def random_restart_hill_climbing(graph, start, goal, restarts=5, seed=42):
    rng = random.Random(seed)
    node_ids = list(graph.nodes)
    all_visited = []
    for i in range(restarts):
        s = start if i == 0 else rng.choice(node_ids)
        path, visited, status = hill_climbing_search(graph, s, goal)
        all_visited.extend(visited)
        if path:
            return path, all_visited, "Solution found on restart " + str(i + 1) + " starting from " + s
    return None, all_visited, "No restart reached the goal after " + str(restarts) + " attempts"


def simulated_annealing_search(graph, start, goal, seed=42, initial_temp=100.0, cooling=0.95, max_steps=300):
    rng = random.Random(seed)
    current = start
    path = [start]
    visited_order = [start]
    temp = initial_temp
    for step in range(max_steps):
        if current == goal:
            return path, visited_order, "Reached the goal at step " + str(step)
        neighbors = list(graph.successors(current))
        if not neighbors:
            break
        nxt = rng.choice(neighbors)
        delta = heuristic_distance(graph, nxt, goal) - heuristic_distance(graph, current, goal)
        if delta < 0 or rng.random() < math.exp(-delta / max(temp, 0.01)):
            current = nxt
            path.append(current)
            visited_order.append(current)
        temp *= cooling
    return None, visited_order, "Did not reach the goal, search ended near node " + current

# ---------------------------------------------------------------------------
# Category 3: Adversarial and Game Search
# ---------------------------------------------------------------------------

def minimax_search(node, maximizing=True):
    if not node["children"]:
        return node["value"], [node["id"]]
    values = []
    for child in node["children"]:
        v, path = minimax_search(child, not maximizing)
        values.append((v, path))
    best = max(values, key=lambda x: x[0]) if maximizing else min(values, key=lambda x: x[0])
    return best[0], [node["id"]] + best[1]


def alpha_beta_search(node, maximizing=True, alpha=-math.inf, beta=math.inf, counter=None):
    if counter is None:
        counter = {"nodes": 0, "pruned": 0}
    counter["nodes"] += 1
    if not node["children"]:
        return node["value"], [node["id"]], counter
    if maximizing:
        best_val = -math.inf
        best_path = []
        for idx, child in enumerate(node["children"]):
            v, path, _ = alpha_beta_search(child, False, alpha, beta, counter)
            if v > best_val:
                best_val = v
                best_path = path
            alpha = max(alpha, best_val)
            if beta <= alpha:
                counter["pruned"] += len(node["children"]) - idx - 1
                break
    else:
        best_val = math.inf
        best_path = []
        for idx, child in enumerate(node["children"]):
            v, path, _ = alpha_beta_search(child, True, alpha, beta, counter)
            if v < best_val:
                best_val = v
                best_path = path
            beta = min(beta, best_val)
            if beta <= alpha:
                counter["pruned"] += len(node["children"]) - idx - 1
                break
    return best_val, [node["id"]] + best_path, counter


def expectiminimax_search(node, maximizing=True):
    if not node["children"]:
        return node["value"], [node["id"]]
    if node.get("type") == "chance":
        total = 0.0
        for child in node["children"]:
            v, _ = expectiminimax_search(child, not maximizing)
            total += v * child.get("prob", 1.0 / len(node["children"]))
        return total, [node["id"]]
    values = [expectiminimax_search(child, not maximizing) for child in node["children"]]
    best = max(values, key=lambda x: x[0]) if maximizing else min(values, key=lambda x: x[0])
    return best[0], [node["id"]] + best[1]


def mcts_estimate(node, simulations=200, seed=42):
    rng = random.Random(seed)

    def rollout(n):
        while n["children"]:
            n = rng.choice(n["children"])
        return n["value"]

    child_scores = {}
    for child in node["children"]:
        total = 0.0
        for _ in range(simulations):
            total += rollout(child)
        child_scores[child["id"]] = round(total / simulations, 2)
    best_id = max(child_scores, key=child_scores.get)
    return best_id, child_scores


# ---------------------------------------------------------------------------
# Category 4: Optimization Search, implemented as a traveling salesman style
# route optimization problem over synthetic or uploaded city coordinates
# ---------------------------------------------------------------------------

def local_search_tsp(cities_df, seed=42, iterations=200):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])
    tour = ids[:]
    rng.shuffle(tour)
    best = tour[:]
    best_cost = tour_distance(cities_df, tour)
    history = [best_cost]
    for _ in range(iterations):
        i, j = rng.sample(range(len(tour)), 2)
        new_tour = tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        cost = tour_distance(cities_df, new_tour)
        if cost < best_cost:
            tour = new_tour
            best = new_tour[:]
            best_cost = cost
        history.append(best_cost)
    return best, best_cost, history


def genetic_algorithm_tsp(cities_df, seed=42, pop_size=30, generations=100):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])

    def make_individual():
        t = ids[:]
        rng.shuffle(t)
        return t

    population = [make_individual() for _ in range(pop_size)]
    history = []
    for _ in range(generations):
        population.sort(key=lambda ind: tour_distance(cities_df, ind))
        history.append(tour_distance(cities_df, population[0]))
        parents = population[:max(2, pop_size // 2)]
        children = []
        while len(children) < pop_size:
            p1, p2 = rng.sample(parents, 2)
            cut = rng.randint(1, len(ids) - 2)
            child = p1[:cut] + [c for c in p2 if c not in p1[:cut]]
            if rng.random() < 0.2:
                i, j = rng.sample(range(len(child)), 2)
                child[i], child[j] = child[j], child[i]
            children.append(child)
        population = children
    population.sort(key=lambda ind: tour_distance(cities_df, ind))
    return population[0], tour_distance(cities_df, population[0]), history


def evolutionary_search_tsp(cities_df, seed=42, pop_size=30, generations=100):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])

    def make_individual():
        t = ids[:]
        rng.shuffle(t)
        return t

    population = [make_individual() for _ in range(pop_size)]
    history = []
    for _ in range(generations):
        population.sort(key=lambda ind: tour_distance(cities_df, ind))
        history.append(tour_distance(cities_df, population[0]))
        survivors = population[:max(2, pop_size // 3)]
        offspring = []
        while len(offspring) < pop_size - len(survivors):
            parent = rng.choice(survivors)
            child = parent[:]
            i, j = rng.sample(range(len(child)), 2)
            child[i], child[j] = child[j], child[i]
            offspring.append(child)
        population = survivors + offspring
    population.sort(key=lambda ind: tour_distance(cities_df, ind))
    return population[0], tour_distance(cities_df, population[0]), history


def pso_tsp(cities_df, seed=42, num_particles=20, iterations=80):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])
    n = len(ids)

    def keys_to_tour(keys):
        order = sorted(range(n), key=lambda i: keys[i])
        return [ids[i] for i in order]

    particles = [[rng.random() for _ in range(n)] for _ in range(num_particles)]
    velocities = [[0.0] * n for _ in range(num_particles)]
    pbest = [p[:] for p in particles]
    pbest_cost = [tour_distance(cities_df, keys_to_tour(p)) for p in particles]
    gbest_idx = min(range(num_particles), key=lambda i: pbest_cost[i])
    gbest = pbest[gbest_idx][:]
    gbest_cost = pbest_cost[gbest_idx]
    history = [gbest_cost]
    w, c1, c2 = 0.5, 1.5, 1.5
    for _ in range(iterations):
        for i in range(num_particles):
            for d in range(n):
                r1, r2 = rng.random(), rng.random()
                velocities[i][d] = (w * velocities[i][d]
                                     + c1 * r1 * (pbest[i][d] - particles[i][d])
                                     + c2 * r2 * (gbest[d] - particles[i][d]))
                particles[i][d] += velocities[i][d]
            cost = tour_distance(cities_df, keys_to_tour(particles[i]))
            if cost < pbest_cost[i]:
                pbest[i] = particles[i][:]
                pbest_cost[i] = cost
                if cost < gbest_cost:
                    gbest = particles[i][:]
                    gbest_cost = cost
        history.append(gbest_cost)
    return keys_to_tour(gbest), gbest_cost, history


def aco_tsp(cities_df, seed=42, num_ants=15, iterations=40, evaporation=0.5):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])
    coords = {row["CityID"]: (row["X"], row["Y"]) for _, row in cities_df.iterrows()}

    def dist(a, b):
        return math.hypot(coords[a][0] - coords[b][0], coords[a][1] - coords[b][1])

    pheromone = {(a, b): 1.0 for a in ids for b in ids if a != b}
    best_tour = None
    best_cost = float("inf")
    history = []
    for _ in range(iterations):
        tours = []
        for _ in range(num_ants):
            unvisited = set(ids)
            current = rng.choice(ids)
            tour = [current]
            unvisited.remove(current)
            while unvisited:
                candidates = list(unvisited)
                weights = []
                for cand in candidates:
                    tau = pheromone[(current, cand)]
                    eta = 1.0 / (dist(current, cand) + 1e-6)
                    weights.append(tau * (eta ** 2.0))
                total_w = sum(weights) or 1.0
                probs = [wv / total_w for wv in weights]
                nxt = rng.choices(candidates, weights=probs)[0]
                tour.append(nxt)
                unvisited.remove(nxt)
                current = nxt
            cost = tour_distance(cities_df, tour)
            tours.append((tour, cost))
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
        for key in pheromone:
            pheromone[key] *= (1 - evaporation)
        for tour, cost in tours:
            for i in range(len(tour)):
                a, b = tour[i], tour[(i + 1) % len(tour)]
                pheromone[(a, b)] += 1.0 / cost
                pheromone[(b, a)] += 1.0 / cost
        history.append(best_cost)
    return best_tour, best_cost, history


def tabu_search_tsp(cities_df, seed=42, iterations=150, tabu_size=15):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])
    current = ids[:]
    rng.shuffle(current)
    best = current[:]
    best_cost = tour_distance(cities_df, current)
    tabu_list = []
    history = [best_cost]
    for _ in range(iterations):
        neighbors = []
        for _ in range(20):
            i, j = rng.sample(range(len(current)), 2)
            move = tuple(sorted((i, j)))
            if move in tabu_list:
                continue
            candidate = current[:]
            candidate[i], candidate[j] = candidate[j], candidate[i]
            neighbors.append((candidate, tour_distance(cities_df, candidate), move))
        if not neighbors:
            continue
        neighbors.sort(key=lambda x: x[1])
        current, cost, move = neighbors[0]
        tabu_list.append(move)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        if cost < best_cost:
            best = current[:]
            best_cost = cost
        history.append(best_cost)
    return best, best_cost, history


def differential_evolution_tsp(cities_df, seed=42, pop_size=20, generations=80, mutation_factor=0.5, crossover_rate=0.7):
    rng = random.Random(seed)
    ids = list(cities_df["CityID"])
    n = len(ids)

    def keys_to_tour(keys):
        order = sorted(range(n), key=lambda i: keys[i])
        return [ids[i] for i in order]

    population = [[rng.random() for _ in range(n)] for _ in range(pop_size)]
    costs = [tour_distance(cities_df, keys_to_tour(ind)) for ind in population]
    history = [min(costs)]
    for _ in range(generations):
        for i in range(pop_size):
            a, b, c = rng.sample([x for x in range(pop_size) if x != i], 3)
            mutant = [population[a][d] + mutation_factor * (population[b][d] - population[c][d]) for d in range(n)]
            trial = [mutant[d] if rng.random() < crossover_rate else population[i][d] for d in range(n)]
            trial_cost = tour_distance(cities_df, keys_to_tour(trial))
            if trial_cost < costs[i]:
                population[i] = trial
                costs[i] = trial_cost
        history.append(min(costs))
    best_idx = min(range(pop_size), key=lambda i: costs[i])
    return keys_to_tour(population[best_idx]), costs[best_idx], history

# ---------------------------------------------------------------------------
# Category 5: Constraint Based Search, implemented as a map coloring
# constraint satisfaction problem over synthetic or uploaded regions
# ---------------------------------------------------------------------------

def run_ac3(region_ids, adj, domains):
    queue = [(a, b) for a in region_ids for b in adj[a]]
    pruned = 0
    while queue:
        a, b = queue.pop(0)
        removed = False
        for ca in domains[a][:]:
            if not any(ca != cb for cb in domains[b]):
                domains[a].remove(ca)
                removed = True
                pruned += 1
        if removed:
            for neighbor in adj[a]:
                if neighbor != b:
                    queue.append((neighbor, a))
    return pruned


def backtracking_coloring(regions_df, adj, colors, use_forward_checking=False, use_arc_consistency=False):
    region_ids = list(regions_df["RegionID"])
    domains = {r: list(colors) for r in region_ids}
    assignment = {}
    stats = {"nodes_explored": 0, "backtracks": 0, "pruned": 0}

    if use_arc_consistency:
        stats["pruned"] += run_ac3(region_ids, adj, domains)
        for r in region_ids:
            if not domains[r]:
                return None, stats

    def backtrack():
        stats["nodes_explored"] += 1
        if len(assignment) == len(region_ids):
            return True
        unassigned = [r for r in region_ids if r not in assignment]
        var = unassigned[0]
        for color in domains[var]:
            if all(assignment.get(n) != color for n in adj[var]):
                assignment[var] = color
                saved_domains = None
                ok = True
                if use_forward_checking:
                    saved_domains = {n: domains[n][:] for n in adj[var] if n not in assignment}
                    for n in adj[var]:
                        if n not in assignment and color in domains[n]:
                            domains[n].remove(color)
                            stats["pruned"] += 1
                            if not domains[n]:
                                ok = False
                if ok and backtrack():
                    return True
                if use_forward_checking and saved_domains:
                    for n, d in saved_domains.items():
                        domains[n] = d
                del assignment[var]
        stats["backtracks"] += 1
        return False

    success = backtrack()
    return (dict(assignment) if success else None), stats


def branch_and_bound_coloring(regions_df, adj, color_palette):
    for k in range(1, len(color_palette) + 1):
        colors = color_palette[:k]
        assignment, stats = backtracking_coloring(regions_df, adj, colors)
        if assignment:
            return assignment, k, stats
    return None, len(color_palette), {}


# ---------------------------------------------------------------------------
# Category 6: String and Text Searching
# ---------------------------------------------------------------------------

def linear_string_search(text, pattern):
    positions = []
    if not pattern:
        return positions
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions


def naive_pattern_matching(text, pattern):
    positions = []
    comparisons = 0
    n, m = len(text), len(pattern)
    if m == 0:
        return positions, comparisons
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            positions.append(i)
    return positions, comparisons


def kmp_search(text, pattern):
    if not pattern:
        return []
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    positions = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
    return positions


def boyer_moore_search(text, pattern):
    if not pattern:
        return []
    m = len(pattern)
    n = len(text)
    last = {c: i for i, c in enumerate(pattern)}
    positions = []
    i = m - 1
    j = m - 1
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                positions.append(i)
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            l = last.get(text[i], -1)
            i += m - min(j, l + 1)
            j = m - 1
    return positions


def rabin_karp_search(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    h = pow(base, m - 1, mod)
    p_hash = 0
    t_hash = 0
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i])) % mod
    positions = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            positions.append(i)
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
    return positions


def build_trie(words):
    trie = {}
    for w in words:
        node = trie
        for ch in w:
            node = node.setdefault(ch, {})
        node["$end"] = True
    return trie


def trie_search(trie, prefix):
    node = trie
    for ch in prefix:
        if ch not in node:
            return []
        node = node[ch]
    results = []

    def collect(n, path):
        if "$end" in n:
            results.append(prefix + path)
        for ch, child in n.items():
            if ch != "$end":
                collect(child, path + ch)

    collect(node, "")
    return results


def suffix_array_search(text, pattern):
    suffixes = sorted(range(len(text)), key=lambda i: text[i:])
    lo, hi = 0, len(suffixes)
    while lo < hi:
        mid = (lo + hi) // 2
        if text[suffixes[mid]:suffixes[mid] + len(pattern)] < pattern:
            lo = mid + 1
        else:
            hi = mid
    results = []
    idx = lo
    while idx < len(suffixes) and text[suffixes[idx]:suffixes[idx] + len(pattern)] == pattern:
        results.append(suffixes[idx])
        idx += 1
    return sorted(results)


def regex_search(text, pattern):
    try:
        matches = [m.start() for m in re.finditer(pattern, text)]
        return matches, None
    except re.error as e:
        return [], str(e)

# ---------------------------------------------------------------------------
# Category 7: Database Search
# ---------------------------------------------------------------------------

def sequential_scan(table_df, field, value):
    matches = table_df[table_df[field].astype(str) == str(value)]
    return matches, len(table_df)


def index_search(table_df, field, value):
    index = {}
    for idx, row in table_df.iterrows():
        index.setdefault(str(row[field]), []).append(idx)
    rows = index.get(str(value), [])
    return table_df.loc[rows], len(index)


def btree_search(table_df, field, value):
    sorted_df = table_df.sort_values(field).reset_index(drop=True)
    keys = sorted_df[field].astype(str).tolist()
    pos = bisect.bisect_left(keys, str(value))
    matches = sorted_df[sorted_df[field].astype(str) == str(value)]
    return matches, pos


def hash_search(table_df, field, value):
    hash_index = {str(row[field]): idx for idx, row in table_df.iterrows()}
    idx = hash_index.get(str(value))
    if idx is None:
        return table_df.iloc[0:0], None
    return table_df.loc[[idx]], idx


def range_search(table_df, field, low, high):
    sorted_df = table_df.sort_values(field)
    matches = sorted_df[(sorted_df[field] >= low) & (sorted_df[field] <= high)]
    return matches


def query_optimization_search(table_df, field, value):
    n = len(table_df)
    scan_cost = n
    index_cost = (math.log2(n) + 1) if n > 0 else 1
    chosen = "Index Search" if index_cost < scan_cost else "Sequential Scan"
    if chosen == "Index Search":
        matches, _ = index_search(table_df, field, value)
    else:
        matches, _ = sequential_scan(table_df, field, value)
    return matches, chosen, scan_cost, index_cost


# ---------------------------------------------------------------------------
# Category 8: Graph Search
# ---------------------------------------------------------------------------

def dijkstra_search(graph, start, goal, weight_field="Cost"):
    dist = {start: 0.0}
    prev = {}
    visited = set()
    visited_order = []
    counter = 0
    frontier = [(0.0, counter, start)]
    while frontier:
        d, _, node = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)
        if node == goal:
            break
        for n in graph.successors(node):
            w = graph[node][n].get(weight_field, 1.0)
            nd = d + w
            if nd < dist.get(n, float("inf")):
                dist[n] = nd
                prev[n] = node
                counter += 1
                heapq.heappush(frontier, (nd, counter, n))
    if goal not in dist:
        return None, None, visited_order
    path = [goal]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    return path, dist[goal], visited_order


def bellman_ford_search(graph, start, goal, weight_field="Cost"):
    dist = {n: float("inf") for n in graph.nodes}
    dist[start] = 0.0
    prev = {}
    edges = [(u, v, graph[u][v].get(weight_field, 1.0)) for u, v in graph.edges]
    for _ in range(len(graph.nodes) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break
    negative_cycle = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            negative_cycle = True
    if goal not in prev and goal != start:
        return None, None, negative_cycle
    path = [goal]
    while path[-1] != start:
        if path[-1] not in prev:
            return None, None, negative_cycle
        path.append(prev[path[-1]])
    path.reverse()
    return path, dist[goal], negative_cycle


def floyd_warshall_search(graph, weight_field="Cost"):
    nodes = list(graph.nodes)
    dist = {a: {b: (0.0 if a == b else float("inf")) for b in nodes} for a in nodes}
    for u, v in graph.edges:
        w = graph[u][v].get(weight_field, 1.0)
        if w < dist[u][v]:
            dist[u][v] = w
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def topological_search(graph):
    try:
        order = list(nx.topological_sort(graph))
        return order, True
    except nx.NetworkXUnfeasible:
        return None, False


def connectivity_search(graph):
    return list(nx.weakly_connected_components(graph))


def community_detection_search(graph):
    undirected = graph.to_undirected()
    return list(nx.algorithms.community.greedy_modularity_communities(undirected))

# ---------------------------------------------------------------------------
# Category 9: Information Retrieval Search
# ---------------------------------------------------------------------------

def keyword_search(corpus_df, keyword):
    return corpus_df[corpus_df["Text"].str.contains(re.escape(keyword), case=False, na=False)]


def boolean_search(corpus_df, query):
    tokens = query.upper().split()
    ops = [t for t in tokens if t in ("AND", "OR", "NOT")]
    terms = [t for t in tokens if t not in ("AND", "OR", "NOT")]
    if not terms:
        return corpus_df.iloc[0:0]
    matched = {t: set(corpus_df[corpus_df["Text"].str.contains(re.escape(t), case=False, na=False)]["DocID"])
               for t in terms}
    result_set = matched[terms[0]]
    op_idx = 0
    for t in terms[1:]:
        op = ops[op_idx] if op_idx < len(ops) else "AND"
        if op == "AND":
            result_set = result_set & matched[t]
        elif op == "OR":
            result_set = result_set | matched[t]
        elif op == "NOT":
            result_set = result_set - matched[t]
        op_idx += 1
    return corpus_df[corpus_df["DocID"].isin(result_set)]


def full_text_search(corpus_df, query):
    return corpus_df[corpus_df["Text"].str.contains(re.escape(query), case=False, na=False)]


def build_inverted_index(corpus_df):
    index = {}
    for _, row in corpus_df.iterrows():
        for word in set(row["Text"].lower().split()):
            index.setdefault(word, set()).add(row["DocID"])
    return index


def inverted_index_search(corpus_df, term):
    index = build_inverted_index(corpus_df)
    doc_ids = index.get(term.lower(), set())
    return corpus_df[corpus_df["DocID"].isin(doc_ids)], len(index)


def ranked_retrieval(corpus_df, query):
    terms = query.lower().split()
    scores = []
    for _, row in corpus_df.iterrows():
        text_words = row["Text"].lower().split()
        scores.append(sum(text_words.count(t) for t in terms))
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False)


def compute_tfidf(corpus_df):
    docs = corpus_df["Text"].str.lower().tolist()
    vocab = sorted(set(word for doc in docs for word in doc.split()))
    n_docs = len(docs)
    doc_freq = {w: sum(1 for doc in docs if w in doc.split()) for w in vocab}
    matrix = []
    for doc in docs:
        words = doc.split()
        wc = len(words) or 1
        row = {}
        for w in vocab:
            tf = words.count(w) / wc
            idf = math.log((n_docs + 1) / (doc_freq[w] + 1)) + 1
            row[w] = tf * idf
        matrix.append(row)
    return vocab, matrix


def tfidf_search(corpus_df, query):
    vocab, matrix = compute_tfidf(corpus_df)
    q_terms = query.lower().split()
    scores = [sum(row.get(t, 0) for t in q_terms) for row in matrix]
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False)


def bm25_search(corpus_df, query, k1=1.5, b=0.75):
    docs = corpus_df["Text"].str.lower().tolist()
    n_docs = len(docs)
    avgdl = (sum(len(d.split()) for d in docs) / n_docs) if n_docs else 1
    q_terms = query.lower().split()
    doc_freq = {t: sum(1 for d in docs if t in d.split()) for t in q_terms}
    scores = []
    for d in docs:
        words = d.split()
        dl = len(words)
        score = 0.0
        for t in q_terms:
            f = words.count(t)
            idf = math.log((n_docs - doc_freq.get(t, 0) + 0.5) / (doc_freq.get(t, 0) + 0.5) + 1)
            score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl) + 1e-9)
        scores.append(score)
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False)


def word_overlap_similarity(a, b):
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def vector_search_tfidf(corpus_df, query):
    vocab, matrix = compute_tfidf(corpus_df)
    q_words = query.lower().split()
    q_vec = [q_words.count(w) for w in vocab]
    scores = [cosine_similarity(list(row.values()), q_vec) for row in matrix]
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False)


def hybrid_search(corpus_df, query):
    bm25_scores = bm25_search(corpus_df, query).set_index("DocID")["Score"]
    vector_scores = vector_search_tfidf(corpus_df, query).set_index("DocID")["Score"]
    combined = bm25_scores.rank(pct=True) * 0.5 + vector_scores.rank(pct=True) * 0.5
    result = corpus_df.copy().set_index("DocID")
    result["Score"] = combined
    return result.reset_index().sort_values("Score", ascending=False)


def semantic_search_wordoverlap(corpus_df, query):
    scores = [word_overlap_similarity(query, t) for t in corpus_df["Text"]]
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False)


# ---------------------------------------------------------------------------
# Category 10: Modern AI and LLM Search, with optional OpenAI, Gemini, or Grok keys
# ---------------------------------------------------------------------------

def synthetic_pseudo_embedding(text, dims=16):
    vec = [0.0] * dims
    for i, ch in enumerate(text):
        vec[i % dims] += ord(ch)
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def get_embeddings_for_texts(texts, api_provider, api_key):
    if not api_key or api_provider == "None":
        vectors = [synthetic_pseudo_embedding(t) for t in texts]
        note = ("No API key provided. Using a deterministic hash based pseudo embedding as a stand in. "
                "Provide an OpenAI or Gemini key in the sidebar for real semantic embeddings.")
        return vectors, note
    if api_provider == "Grok":
        vectors = [synthetic_pseudo_embedding(t) for t in texts]
        note = ("xAI's Grok API does not currently offer a public embeddings endpoint, so a deterministic hash "
                "based pseudo embedding was used instead. Switch the provider to OpenAI or Gemini in the sidebar "
                "for real semantic embeddings.")
        return vectors, note
    try:
        if api_provider == "OpenAI":
            resp = requests.post(
                "https://api.openai.com/v1/embeddings",
                headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
                json={"model": "text-embedding-3-small", "input": texts},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            vectors = [item["embedding"] for item in data["data"]]
            return vectors, "Embeddings generated using OpenAI text-embedding-3-small"
        if api_provider == "Gemini":
            vectors = []
            for t in texts:
                resp = requests.post(
                    "https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004:embedContent?key=" + api_key,
                    json={"content": {"parts": [{"text": t}]}},
                    timeout=30,
                )
                resp.raise_for_status()
                vectors.append(resp.json()["embedding"]["values"])
            return vectors, "Embeddings generated using Gemini text-embedding-004"
    except Exception as e:
        vectors = [synthetic_pseudo_embedding(t) for t in texts]
        return vectors, "The API call failed, so synthetic embeddings were used instead. Detail: " + str(e)
    vectors = [synthetic_pseudo_embedding(t) for t in texts]
    return vectors, "Unknown provider, used synthetic embeddings"


def call_llm_chat(prompt, api_provider, api_key, max_tokens=300):
    if not api_key or api_provider == "None":
        return None, ("No API key provided, so an AI generated answer was not created. "
                       "Provide an OpenAI, Gemini, or Grok key in the sidebar to enable this feature.")
    try:
        if api_provider == "OpenAI":
            resp = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
                json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"], "Response generated using OpenAI gpt-4o-mini"
        if api_provider == "Gemini":
            resp = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + api_key,
                json={"contents": [{"parts": [{"text": prompt}]}]},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["candidates"][0]["content"]["parts"][0]["text"], "Response generated using Gemini 1.5 Flash"
        if api_provider == "Grok":
            resp = requests.post(
                "https://api.x.ai/v1/chat/completions",
                headers={"Authorization": "Bearer " + api_key, "Content-Type": "application/json"},
                json={"model": "grok-4.6", "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"], "Response generated using xAI Grok 4.6"
    except Exception as e:
        return None, "The API call failed. Detail: " + str(e)
    return None, "Unknown provider"


def embedding_search(corpus_df, query, api_provider, api_key):
    vectors, note = get_embeddings_for_texts(corpus_df["Text"].tolist() + [query], api_provider, api_key)
    query_vec = vectors[-1]
    doc_vecs = vectors[:-1]
    scores = [cosine_similarity(query_vec, v) for v in doc_vecs]
    result = corpus_df.copy()
    result["Score"] = scores
    return result.sort_values("Score", ascending=False), note


def rag_search(corpus_df, query, api_provider, api_key, top_k=3):
    ranked, note = embedding_search(corpus_df, query, api_provider, api_key)
    context_docs = ranked.head(top_k)
    context_text = "\n".join(context_docs["Text"].tolist())
    prompt = "Answer the question using only the following context.\nContext:\n" + context_text + "\nQuestion: " + query
    answer, llm_note = call_llm_chat(prompt, api_provider, api_key)
    return context_docs, answer, note, llm_note


def knowledge_graph_search(graph, query):
    matches = []
    for n, attrs in graph.nodes(data=True):
        haystack = (str(attrs.get("Type", "")) + " " + str(attrs.get("Owner", "")) + " " + str(n)).lower()
        if query.lower() in haystack:
            matches.append(n)
    return matches


def graph_rag_search(graph, corpus_df, query, api_provider, api_key):
    kg_matches = knowledge_graph_search(graph, query)
    ranked, note = embedding_search(corpus_df, query, api_provider, api_key)
    context = "Graph entities matched: " + ", ".join(kg_matches[:10]) + "\nDocuments:\n" + "\n".join(ranked.head(3)["Text"].tolist())
    prompt = "Using the following graph and document context, answer the question.\n" + context + "\nQuestion: " + query
    answer, llm_note = call_llm_chat(prompt, api_provider, api_key)
    return kg_matches, ranked.head(3), answer, note, llm_note


def agentic_search(corpus_df, query, max_iterations=3):
    current_query = query
    trace = []
    for i in range(max_iterations):
        ranked = ranked_retrieval(corpus_df, current_query)
        best_score = ranked["Score"].iloc[0] if len(ranked) else 0
        top_doc = ranked.iloc[0]["DocID"] if len(ranked) else None
        trace.append({"Iteration": i + 1, "Query": current_query, "Top_Doc": top_doc, "Score": best_score})
        if best_score >= 3 or i == max_iterations - 1 or not len(ranked):
            break
        current_query = current_query + " " + ranked.iloc[0]["Text"].split()[0]
    return trace


def multi_step_search(corpus_df, query, steps=3):
    trace = []
    current = query
    for i in range(steps):
        result = ranked_retrieval(corpus_df, current)
        if not len(result):
            break
        top_row = result.iloc[0]
        trace.append({"Step": i + 1, "Query": current, "Top_Doc": top_row["DocID"], "Top_Text": top_row["Text"]})
        current = top_row["Text"].split()[-1]
    return trace


SYNONYM_MAP = {
    "server": ["host", "machine"], "database": ["db", "datastore"],
    "vulnerability": ["weakness", "flaw"], "employee": ["staff", "user"],
    "network": ["lan", "infrastructure"], "firewall": ["packet filter", "security gateway"],
    "incident": ["event", "occurrence"], "credential": ["login", "password"],
    "vendor": ["supplier", "third party"], "application": ["app", "software"],
}


def query_expansion_search(corpus_df, query, api_provider, api_key):
    if api_key and api_provider != "None":
        prompt = "Provide three short synonym or related terms for this search query, comma separated only, no explanation: " + query
        answer, note = call_llm_chat(prompt, api_provider, api_key)
        if answer:
            expansions = [t.strip() for t in answer.split(",") if t.strip()][:3]
        else:
            expansions = []
            for word in query.lower().split():
                expansions.extend(SYNONYM_MAP.get(word, []))
            note = note + " Falling back to a built in synonym list."
    else:
        expansions = []
        for word in query.lower().split():
            expansions.extend(SYNONYM_MAP.get(word, []))
        note = "No API key provided, used a built in synonym list."
    expanded_query = query + " " + " ".join(expansions)
    result = ranked_retrieval(corpus_df, expanded_query)
    return result, expansions, note


def semantic_reranking_search(corpus_df, query, api_provider, api_key, initial_k=8):
    keyword_ranked = ranked_retrieval(corpus_df, query).head(initial_k)
    reranked, note = embedding_search(keyword_ranked, query, api_provider, api_key)
    return reranked, note


def self_query_search(table_df, nl_query):
    filtered = table_df.copy()
    text = nl_query.lower()
    filters = []
    m = re.search(r"risk(?:_score)?\s*(above|over|greater than|below|under|less than)\s*(\d+)", text)
    if m:
        op, val = m.group(1), int(m.group(2))
        if op in ("above", "over", "greater than"):
            filtered = filtered[filtered["Risk_Score"] > val]
            filters.append("Risk_Score > " + str(val))
        else:
            filtered = filtered[filtered["Risk_Score"] < val]
            filters.append("Risk_Score < " + str(val))
    m2 = re.search(r"amount\s*(above|over|greater than|below|under|less than)\s*(\d+)", text)
    if m2:
        op, val = m2.group(1), float(m2.group(2))
        if op in ("above", "over", "greater than"):
            filtered = filtered[filtered["Amount"] > val]
            filters.append("Amount > " + str(val))
        else:
            filtered = filtered[filtered["Amount"] < val]
            filters.append("Amount < " + str(val))
    for country in COUNTRIES:
        if country.lower() in text:
            filtered = filtered[filtered["Country"] == country]
            filters.append("Country = " + country)
    return filtered, filters

# ---------------------------------------------------------------------------
# Category 11: Probabilistic Search
# ---------------------------------------------------------------------------

def probabilistic_search(table_df, threshold=0.5):
    return table_df[table_df["Probability"] >= threshold].sort_values("Probability", ascending=False)


def bayesian_search(table_df, seed=42):
    rng = random.Random(seed)
    priors = table_df["Probability"].tolist()
    likelihoods = [rng.uniform(0.5, 1.0) if p > 0.5 else rng.uniform(0.0, 0.5) for p in priors]
    posteriors = []
    for prior, like in zip(priors, likelihoods):
        num = like * prior
        denom = num + (1 - like) * (1 - prior)
        posteriors.append(num / denom if denom > 0 else prior)
    result = table_df.copy()
    result["Posterior"] = posteriors
    return result.sort_values("Posterior", ascending=False)


def monte_carlo_search(table_df, seed=42, trials=1000):
    rng = random.Random(seed)
    records = table_df.to_dict("records")
    counts = {rec["RecordID"]: 0 for rec in records}
    weights = [max(rec["Probability"], 0.001) for rec in records]
    for _ in range(trials):
        rec = rng.choices(records, weights=weights)[0]
        counts[rec["RecordID"]] += 1
    result = table_df.copy()
    result["Simulated_Frequency"] = result["RecordID"].map(counts)
    return result.sort_values("Simulated_Frequency", ascending=False)


def particle_filtering_search(table_df, seed=42, iterations=5):
    rng = random.Random(seed)
    records = table_df.to_dict("records")
    weights = [1.0 / len(records)] * len(records)
    for _ in range(iterations):
        new_weights = []
        for rec, w in zip(records, weights):
            noise = rng.uniform(-0.05, 0.05)
            new_weights.append(max(0.0001, w * (rec["Probability"] + noise)))
        total = sum(new_weights)
        weights = [w / total for w in new_weights]
    result = table_df.copy()
    result["Particle_Weight"] = weights
    return result.sort_values("Particle_Weight", ascending=False)


# ---------------------------------------------------------------------------
# Category 12: Distributed and Large Scale Search
# ---------------------------------------------------------------------------

def split_dataframe(df, n):
    n = max(1, n)
    size = max(1, math.ceil(len(df) / n))
    return [df.iloc[i * size:(i + 1) * size] for i in range(n) if len(df.iloc[i * size:(i + 1) * size]) > 0]


def distributed_search(table_df, field, value, num_workers=4):
    parts = split_dataframe(table_df, num_workers)
    results = []
    matched_parts = []
    for i, part in enumerate(parts):
        matches = part[part[field].astype(str) == str(value)]
        matched_parts.append(matches)
        results.append({"Worker": "Worker " + str(i + 1), "Records_Scanned": len(part), "Matches_Found": len(matches)})
    combined = pd.concat(matched_parts) if matched_parts else table_df.iloc[0:0]
    return combined, pd.DataFrame(results)


def parallel_search(table_df, field, value, num_workers=4, seed=42):
    rng = random.Random(seed)
    parts = split_dataframe(table_df, num_workers)
    timings = []
    matched_parts = []
    for i, part in enumerate(parts):
        t = round(rng.uniform(0.1, 1.0) * len(part) / 10 + 0.05, 3)
        matches = part[part[field].astype(str) == str(value)]
        matched_parts.append(matches)
        timings.append({"Worker": "Worker " + str(i + 1), "Records": len(part), "Matches": len(matches), "Simulated_Time_Seconds": t})
    parallel_time = max(t["Simulated_Time_Seconds"] for t in timings) if timings else 0
    sequential_time = sum(t["Simulated_Time_Seconds"] for t in timings)
    combined = pd.concat(matched_parts) if matched_parts else table_df.iloc[0:0]
    return combined, pd.DataFrame(timings), parallel_time, sequential_time


def federated_search(table_df, field, value, num_sources=3):
    sources = split_dataframe(table_df, num_sources)
    results = []
    for i, src in enumerate(sources):
        matches = src[src[field].astype(str) == str(value)].copy()
        matches["Source"] = "Source " + str(i + 1)
        results.append(matches)
    merged = pd.concat(results) if results else table_df.iloc[0:0]
    return merged


def mapreduce_search(table_df, category_field="Category", num_workers=4):
    parts = split_dataframe(table_df, num_workers)
    map_rows = []
    reduced = {}
    for i, part in enumerate(parts):
        counts = part[category_field].value_counts().to_dict()
        for k, v in counts.items():
            map_rows.append({"Worker": "Worker " + str(i + 1), "Category": k, "Count": v})
            reduced[k] = reduced.get(k, 0) + v
    map_df = pd.DataFrame(map_rows)
    reduce_df = pd.DataFrame(sorted(reduced.items(), key=lambda x: -x[1]), columns=["Category", "Total_Count"])
    return map_df, reduce_df


def distributed_graph_search(graph, start, goal, num_workers=3, seed=42):
    rng = random.Random(seed)
    nodes = list(graph.nodes)
    rng.shuffle(nodes)
    parts = split_dataframe(pd.DataFrame({"ID": nodes}), num_workers)
    partition_of = {}
    for i, part in enumerate(parts):
        for nid in part["ID"]:
            partition_of[nid] = "Worker " + str(i + 1)
    path, visited_order = dfs_search(graph, start, goal)
    cross_partition_hops = 0
    if path:
        for i in range(len(path) - 1):
            if partition_of.get(path[i]) != partition_of.get(path[i + 1]):
                cross_partition_hops += 1
    worker_counts = pd.Series(partition_of).value_counts().rename_axis("Worker").reset_index(name="Node_Count")
    return path, cross_partition_hops, worker_counts, visited_order


# ---------------------------------------------------------------------------
# Category 13: Cybersecurity Search
# ---------------------------------------------------------------------------

def ioc_search(table_df, ioc_type, ioc_value):
    field_map = {"IP Address": "IP_Address", "File Hash": "File_Hash"}
    field = field_map.get(ioc_type, "IP_Address")
    return table_df[table_df[field] == ioc_value]


def threat_hunting_search(table_df, risk_threshold=70, odd_hour_start=0, odd_hour_end=5):
    return table_df[(table_df["Risk_Score"] >= risk_threshold) &
                     (table_df["Hour"] >= odd_hour_start) & (table_df["Hour"] <= odd_hour_end)]


def attack_path_search(graph, start, goal):
    return dfs_search(graph, start, goal)


def graph_based_threat_search(graph, start, risk_threshold=6, max_hops=3):
    visited = {start: 0}
    queue = [start]
    head = 0
    flagged = []
    while head < len(queue):
        node = queue[head]
        head += 1
        depth = visited[node]
        if graph.nodes[node].get("Risk", 0) >= risk_threshold:
            flagged.append((node, depth))
        if depth < max_hops:
            for n in graph.successors(node):
                if n not in visited:
                    visited[n] = depth + 1
                    queue.append(n)
    return flagged, list(visited.keys())


def anomaly_search(table_df, field="Amount", z_threshold=2.0):
    mean = table_df[field].mean()
    std = table_df[field].std() or 1.0
    result = table_df.copy()
    result["Z_Score"] = (result[field] - mean) / std
    anomalies = result[result["Z_Score"].abs() >= z_threshold]
    return anomalies.sort_values("Z_Score", key=abs, ascending=False), mean, std


def vulnerability_search(nodes_df, score_threshold=40):
    return nodes_df[nodes_df["Security_Score"] < score_threshold].sort_values("Security_Score")


def siem_query_search(table_df, query):
    filtered = table_df.copy()
    clauses = re.split(r"\s+AND\s+", query, flags=re.IGNORECASE)
    applied = []
    for clause in clauses:
        m = re.match(r"\s*(\w+)\s*(=|>=|<=|>|<)\s*(.+)\s*", clause.strip())
        if not m:
            continue
        field, op, value = m.group(1), m.group(2), m.group(3).strip()
        if field not in filtered.columns:
            continue
        applied.append(clause.strip())
        try:
            val_num = float(value)
            if op == "=":
                filtered = filtered[filtered[field] == val_num]
            elif op == ">":
                filtered = filtered[filtered[field] > val_num]
            elif op == "<":
                filtered = filtered[filtered[field] < val_num]
            elif op == ">=":
                filtered = filtered[filtered[field] >= val_num]
            elif op == "<=":
                filtered = filtered[filtered[field] <= val_num]
        except ValueError:
            if op == "=":
                filtered = filtered[filtered[field].astype(str).str.lower() == value.lower()]
    return filtered, applied


SOAR_PLAYBOOKS = [
    {"Name": "Patch Server", "Cost": 10000, "Risk": 10, "Time": 5},
    {"Name": "Replace API", "Cost": 5000, "Risk": 4, "Time": 3},
    {"Name": "Isolate Network", "Cost": 2000, "Risk": 7, "Time": 10},
    {"Name": "Revoke Credentials", "Cost": 500, "Risk": 3, "Time": 1},
    {"Name": "Full System Rebuild", "Cost": 20000, "Risk": 1, "Time": 20},
]


def soar_playbook_search(weight_cost=1.0, weight_risk=1.0, weight_time=1.0):
    scored = []
    for pb in SOAR_PLAYBOOKS:
        score = pb["Cost"] * weight_cost * 0.001 + pb["Risk"] * weight_risk + pb["Time"] * weight_time
        scored.append({**pb, "Combined_Score": round(score, 2)})
    return pd.DataFrame(scored).sort_values("Combined_Score")

# ---------------------------------------------------------------------------
# Generic plotting helpers
# ---------------------------------------------------------------------------

def plot_graph(graph, path=None, title="Graph"):
    fig, ax = plt.subplots(figsize=(8, 5))
    layout = {n: (graph.nodes[n].get("X", 0), graph.nodes[n].get("Y", 0)) for n in graph.nodes}
    if not any(graph.nodes[n].get("X") is not None for n in graph.nodes):
        layout = nx.spring_layout(graph, seed=7)
    nx.draw_networkx_nodes(graph, layout, node_color="#A9C6E8", node_size=600, ax=ax)
    nx.draw_networkx_labels(graph, layout, font_size=8, ax=ax)
    nx.draw_networkx_edges(graph, layout, edge_color="#B0B0B0", arrows=True, ax=ax)
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_nodes(graph, layout, nodelist=path, node_color="#FF9900", node_size=700, ax=ax)
        nx.draw_networkx_edges(graph, layout, edgelist=path_edges, edge_color="#CC0000", width=2.5, ax=ax)
        nx.draw_networkx_nodes(graph, layout, nodelist=[path[0]], node_color="#2E8B57", node_size=750, ax=ax)
        nx.draw_networkx_nodes(graph, layout, nodelist=[path[-1]], node_color="#B22222", node_size=750, ax=ax)
    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    ax.axis("off")
    fig.tight_layout()
    return fig


def plot_bar(labels, values, title, xlabel="", ylabel=""):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([str(l) for l in labels], values, color="#378ADD")
    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()
    return fig


def plot_line(x, y, title, xlabel="", ylabel=""):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x, y, color="#0000CC", marker="o", markersize=3)
    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.tight_layout()
    return fig


def plot_tour(cities_df, tour, title="Route"):
    fig, ax = plt.subplots(figsize=(8, 5))
    coords = {row["CityID"]: (row["X"], row["Y"]) for _, row in cities_df.iterrows()}
    xs = [coords[c][0] for c in tour] + [coords[tour[0]][0]]
    ys = [coords[c][1] for c in tour] + [coords[tour[0]][1]]
    ax.plot(xs, ys, color="#CC0000", marker="o", markersize=6, linewidth=1.5)
    for c in tour:
        ax.annotate(c, coords[c], fontsize=8)
    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    fig.tight_layout()
    return fig


def plot_tree(node, highlight_ids=None, title="Game Tree"):
    highlight_ids = highlight_ids or []
    graph = nx.DiGraph()
    labels = {}

    def walk(n, parent=None):
        label = n["id"] + ("\n" + str(n.get("value")) if not n["children"] else "")
        labels[n["id"]] = label
        graph.add_node(n["id"])
        if parent:
            graph.add_edge(parent, n["id"])
        for c in n["children"]:
            walk(c, n["id"])

    walk(node)
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = _hierarchy_layout(node)
    node_colors = ["#FF9900" if n in highlight_ids else "#A9C6E8" for n in graph.nodes]
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500, ax=ax)
    nx.draw_networkx_edges(graph, pos, edge_color="#B0B0B0", ax=ax)
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=7, ax=ax)
    ax.set_title(title, fontsize=13, fontweight="bold", color="#0000CC")
    ax.axis("off")
    fig.tight_layout()
    return fig


def _hierarchy_layout(root):
    positions = {}
    leaf_counter = [0]

    def assign(n, depth):
        if not n["children"]:
            x = leaf_counter[0]
            leaf_counter[0] += 1
            positions[n["id"]] = (x, -depth)
            return x
        xs = [assign(c, depth + 1) for c in n["children"]]
        avg = sum(xs) / len(xs)
        positions[n["id"]] = (avg, -depth)
        return avg

    assign(root, 0)
    return positions


# ---------------------------------------------------------------------------
# Generic export helpers, produce PDF, Word, CSV and plain text files
# ---------------------------------------------------------------------------

def build_summary(category_name, algo_name, explanation, params, status, result_text, details, table_df=None):
    return {
        "category": category_name,
        "algo_name": algo_name,
        "explanation": explanation,
        "params": params,
        "status": status,
        "result_text": result_text,
        "details": details or [],
        "table": table_df,
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def export_text_bytes(summary):
    lines = []
    lines.append("KALSNET UNIVERSAL SEARCH AND REASONING ENGINE")
    lines.append("Developed By Randy Singh from Kalsnet (KNet) Consulting Group")
    lines.append("")
    lines.append("Category: " + summary["category"])
    lines.append("Technique: " + summary["algo_name"])
    lines.append("Generated: " + summary["generated_at"])
    lines.append("")
    lines.append("Explanation")
    lines.append(summary["explanation"])
    lines.append("")
    lines.append("Parameters")
    for k, v in summary["params"].items():
        lines.append(str(k) + ": " + str(v))
    lines.append("")
    lines.append("Result")
    lines.append("Status: " + summary["status"])
    lines.append(summary["result_text"])
    for d in summary["details"]:
        lines.append(str(d))
    return "\n".join(lines).encode("utf-8")


def export_word_bytes(summary):
    document = Document()
    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run("Kalsnet Universal Search and Reasoning Engine")
    run.bold = True
    run.font.size = Pt(20)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0xCC)

    subtitle = document.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = subtitle.add_run("Developed By Randy Singh from Kalsnet (KNet) Consulting Group")
    run2.bold = True
    run2.font.size = Pt(13)
    run2.font.color.rgb = RGBColor(0x00, 0x00, 0xCC)

    document.add_heading(summary["category"] + " -- " + summary["algo_name"], level=1)
    document.add_paragraph("Generated: " + summary["generated_at"])

    document.add_heading("Explanation", level=2)
    document.add_paragraph(summary["explanation"])

    document.add_heading("Parameters", level=2)
    if summary["params"]:
        param_table = document.add_table(rows=len(summary["params"]), cols=2)
        param_table.style = "Light Grid Accent 1"
        for i, (k, v) in enumerate(summary["params"].items()):
            param_table.cell(i, 0).text = str(k)
            param_table.cell(i, 1).text = str(v)
    else:
        document.add_paragraph("No parameters were required for this run.")

    document.add_heading("Result", level=2)
    document.add_paragraph("Status: " + summary["status"])
    document.add_paragraph(summary["result_text"])
    for d in summary["details"]:
        document.add_paragraph(str(d))

    if summary["table"] is not None and len(summary["table"]) > 0:
        document.add_heading("Result Table", level=2)
        df = summary["table"].head(50)
        t = document.add_table(rows=1, cols=len(df.columns))
        t.style = "Light Grid Accent 1"
        for i, col in enumerate(df.columns):
            t.cell(0, i).text = str(col)
        for _, row in df.iterrows():
            cells = t.add_row().cells
            for i, col in enumerate(df.columns):
                cells[i].text = str(row[col])

    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def export_pdf_bytes(summary):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.6 * inch, bottomMargin=0.6 * inch)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("TitleBlue", parent=styles["Title"], textColor=rl_colors.HexColor("#0000CC"), fontSize=19)
    subtitle_style = ParagraphStyle("SubtitleBlue", parent=styles["Normal"], textColor=rl_colors.HexColor("#0000CC"),
                                     fontSize=12, alignment=1, spaceAfter=14)
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    elements = []
    elements.append(Paragraph("Kalsnet Universal Search and Reasoning Engine", title_style))
    elements.append(Paragraph("Developed By Randy Singh from Kalsnet (KNet) Consulting Group", subtitle_style))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(summary["category"] + " -- " + summary["algo_name"], heading_style))
    elements.append(Paragraph("Generated: " + summary["generated_at"], body_style))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph("Explanation", heading_style))
    elements.append(Paragraph(summary["explanation"], body_style))
    elements.append(Spacer(1, 8))

    if summary["params"]:
        elements.append(Paragraph("Parameters", heading_style))
        param_data = [["Field", "Value"]] + [[str(k), str(v)] for k, v in summary["params"].items()]
        param_table = Table(param_data, colWidths=[2.5 * inch, 3.5 * inch])
        param_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), rl_colors.HexColor("#0000CC")),
            ("TEXTCOLOR", (0, 0), (-1, 0), rl_colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, rl_colors.grey),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [rl_colors.white, rl_colors.HexColor("#EEF2FA")]),
        ]))
        elements.append(param_table)
        elements.append(Spacer(1, 8))

    elements.append(Paragraph("Result", heading_style))
    elements.append(Paragraph("Status: " + summary["status"], body_style))
    elements.append(Paragraph(summary["result_text"], body_style))
    for d in summary["details"]:
        elements.append(Paragraph(str(d), body_style))

    if summary["table"] is not None and len(summary["table"]) > 0:
        elements.append(Spacer(1, 8))
        elements.append(Paragraph("Result Table", heading_style))
        df = summary["table"].head(30)
        table_data = [list(df.columns)] + df.astype(str).values.tolist()
        result_table = Table(table_data, repeatRows=1)
        result_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), rl_colors.HexColor("#0000CC")),
            ("TEXTCOLOR", (0, 0), (-1, 0), rl_colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, rl_colors.grey),
            ("FONTSIZE", (0, 0), (-1, -1), 7),
        ]))
        elements.append(result_table)

    doc.build(elements)
    return buffer.getvalue()


def export_csv_bytes(summary):
    buffer = io.StringIO()
    if summary["table"] is not None and len(summary["table"]) > 0:
        summary["table"].to_csv(buffer, index=False)
    else:
        pd.DataFrame([{
            "Category": summary["category"],
            "Technique": summary["algo_name"],
            "Status": summary["status"],
            "Result": summary["result_text"],
        }]).to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")

# ---------------------------------------------------------------------------
# Page style
# ---------------------------------------------------------------------------

def apply_page_style():
    st.set_page_config(page_title="Kalsnet Universal Search and Reasoning Engine", layout="wide")
    st.markdown(
        """
        <style>
        .kalsnet-title {
            color: #0000CC;
            font-size: 40px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0px;
        }
        .kalsnet-subtitle {
            color: #0000CC;
            font-size: 20px;
            font-weight: 700;
            text-align: center;
            margin-top: 4px;
            margin-bottom: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="kalsnet-title">Kalsnet Universal Search and Reasoning Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="kalsnet-subtitle">Developed By Randy Singh from Kalsnet (KNet) Consulting Group</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Sidebar, category navigation and API key configuration
# ---------------------------------------------------------------------------

CATEGORY_LIST = [
    "1. Classical AI and State Space Search",
    "2. Informed and Heuristic Search",
    "3. Adversarial and Game Search",
    "4. Optimization Search",
    "5. Constraint Based Search",
    "6. String and Text Searching",
    "7. Database Search",
    "8. Graph Search",
    "9. Information Retrieval Search",
    "10. Modern AI and LLM Search",
    "11. Probabilistic Search",
    "12. Distributed and Large Scale Search",
    "13. Cybersecurity Search",
]


def render_sidebar():
    st.sidebar.markdown("## Search Category")
    category = st.sidebar.radio("Choose a category", CATEGORY_LIST, key="category_nav", label_visibility="collapsed")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## AI Provider Settings")
    st.sidebar.write("Optional. Used only by the Modern AI and LLM Search category for real embeddings and generated answers. Every other category works fully without a key.")
    api_provider = st.sidebar.selectbox("Provider", ["None", "OpenAI", "Gemini", "Grok"], key="api_provider")
    api_key = ""
    if api_provider != "None":
        api_key = st.sidebar.text_input("API key for " + api_provider, type="password", key="api_key_input")

    with st.sidebar.expander("How to get a free API key"):
        st.markdown(
            "**Gemini, from Google AI Studio**\n\n"
            "1. Go to aistudio.google.com/app/apikey\n"
            "2. Sign in with a Google account\n"
            "3. Click Create API key\n"
            "4. Copy the key and paste it above\n\n"
            "Google AI Studio currently offers a free tier for Gemini models, useful for testing this application. "
            "Check Google's current pricing page for up to date limits.\n\n"
            "**OpenAI**\n\n"
            "1. Go to platform.openai.com/api-keys\n"
            "2. Sign in or create an account\n"
            "3. Click Create new secret key\n"
            "4. Copy the key and paste it above\n\n"
            "New OpenAI accounts sometimes receive limited free trial credit. Check OpenAI's current pricing page, "
            "since embeddings and chat completions are billed once trial credit is used.\n\n"
            "**Grok, from xAI**\n\n"
            "1. Go to console.x.ai and sign in or create an account\n"
            "2. Open the API Keys section and click Create API Key\n"
            "3. Copy the key and paste it above\n\n"
            "xAI's Grok API is used here for generated chat answers. It does not currently offer a public embeddings "
            "endpoint, so Grok is used only for the generated answer, not for embeddings, and check xAI's current "
            "pricing page for up to date free credit and billing details."
        )

    return category, api_provider, api_key


# ---------------------------------------------------------------------------
# Generic domain loader widgets, each returns the domain data or None
# ---------------------------------------------------------------------------

def graph_domain_ui(prefix, allow_negative=False, force_dag=False):
    st.markdown("#### Provide graph data")
    source = st.radio("Data source", ["Generate Synthetic Data", "Upload Real Data"], key=prefix + "_src", horizontal=True)

    if source == "Generate Synthetic Data":
        c1, c2, c3 = st.columns(3)
        with c1:
            num_nodes = st.slider("Number of nodes", 5, 60, 14, key=prefix + "_n")
        with c2:
            seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
        with c3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=prefix + "_showall")
        if st.button("Generate Synthetic Data Now", key=prefix + "_gen"):
            nodes_df = generate_synthetic_nodes(num_nodes, seed=seed)
            edges_df = generate_synthetic_edges(nodes_df, seed=seed, allow_negative=allow_negative, force_dag=force_dag)
            st.session_state[prefix + "_nodes"] = nodes_df
            st.session_state[prefix + "_edges"] = edges_df
        if prefix + "_nodes" in st.session_state:
            nodes_df = st.session_state[prefix + "_nodes"]
            edges_df = st.session_state[prefix + "_edges"]
            if show_all:
                st.write("Complete synthetic node data, " + str(len(nodes_df)) + " rows")
                st.dataframe(nodes_df, use_container_width=True, hide_index=True)
                st.write("Complete synthetic edge data, " + str(len(edges_df)) + " rows")
                st.dataframe(edges_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of node data, first 5 rows")
                st.dataframe(nodes_df.head(5), use_container_width=True, hide_index=True)
                st.write("Preview of edge data, first 5 rows")
                st.dataframe(edges_df.head(5), use_container_width=True, hide_index=True)
            return nodes_df, edges_df, build_graph(nodes_df, edges_df)
        return None, None, None
    else:
        node_file = st.file_uploader("Upload Node CSV File", type=["csv"], key=prefix + "_nf")
        edge_file = st.file_uploader("Upload Edge CSV File", type=["csv"], key=prefix + "_ef")
        if node_file is not None and edge_file is not None:
            nodes_df = pd.read_csv(node_file)
            edges_df = pd.read_csv(edge_file)
            if "X" not in nodes_df.columns:
                rng = random.Random(1)
                nodes_df["X"] = [round(rng.uniform(0, 100), 1) for _ in range(len(nodes_df))]
                nodes_df["Y"] = [round(rng.uniform(0, 100), 1) for _ in range(len(nodes_df))]
            st.session_state[prefix + "_nodes"] = nodes_df
            st.session_state[prefix + "_edges"] = edges_df
        if prefix + "_nodes" in st.session_state:
            nodes_df = st.session_state[prefix + "_nodes"]
            edges_df = st.session_state[prefix + "_edges"]
            st.write("Uploaded node data")
            st.dataframe(nodes_df, use_container_width=True, hide_index=True)
            st.write("Uploaded edge data")
            st.dataframe(edges_df, use_container_width=True, hide_index=True)
            return nodes_df, edges_df, build_graph(nodes_df, edges_df)
        return None, None, None


def text_domain_ui(prefix):
    st.markdown("#### Provide document data")
    source = st.radio("Data source", ["Generate Synthetic Data", "Upload Real Data"], key=prefix + "_src", horizontal=True)
    if source == "Generate Synthetic Data":
        c1, c2, c3 = st.columns(3)
        with c1:
            num_docs = st.slider("Number of documents", 5, 60, 15, key=prefix + "_n")
        with c2:
            seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
        with c3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=prefix + "_showall")
        if st.button("Generate Synthetic Data Now", key=prefix + "_gen"):
            st.session_state[prefix + "_corpus"] = build_synthetic_corpus(num_docs, seed=seed)
        if prefix + "_corpus" in st.session_state:
            corpus_df = st.session_state[prefix + "_corpus"]
            if show_all:
                st.write("Complete synthetic document data, " + str(len(corpus_df)) + " rows")
                st.dataframe(corpus_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of document data, first 5 rows")
                st.dataframe(corpus_df.head(5), use_container_width=True, hide_index=True)
            return corpus_df
        return None
    else:
        doc_file = st.file_uploader("Upload Document CSV File, columns DocID Title Text", type=["csv"], key=prefix + "_df")
        if doc_file is not None:
            st.session_state[prefix + "_corpus"] = pd.read_csv(doc_file)
        if prefix + "_corpus" in st.session_state:
            corpus_df = st.session_state[prefix + "_corpus"]
            st.write("Uploaded document data")
            st.dataframe(corpus_df, use_container_width=True, hide_index=True)
            return corpus_df
        return None


def table_domain_ui(prefix):
    st.markdown("#### Provide record data")
    source = st.radio("Data source", ["Generate Synthetic Data", "Upload Real Data"], key=prefix + "_src", horizontal=True)
    if source == "Generate Synthetic Data":
        c1, c2, c3 = st.columns(3)
        with c1:
            num_records = st.slider("Number of records", 10, 300, 60, key=prefix + "_n")
        with c2:
            seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
        with c3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=prefix + "_showall")
        if st.button("Generate Synthetic Data Now", key=prefix + "_gen"):
            st.session_state[prefix + "_table"] = build_synthetic_table(num_records, seed=seed)
        if prefix + "_table" in st.session_state:
            table_df = st.session_state[prefix + "_table"]
            if show_all:
                st.write("Complete synthetic record data, " + str(len(table_df)) + " rows")
                st.dataframe(table_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of record data, first 5 rows")
                st.dataframe(table_df.head(5), use_container_width=True, hide_index=True)
            return table_df
        return None
    else:
        tfile = st.file_uploader("Upload Record CSV File", type=["csv"], key=prefix + "_tf")
        if tfile is not None:
            st.session_state[prefix + "_table"] = pd.read_csv(tfile)
        if prefix + "_table" in st.session_state:
            table_df = st.session_state[prefix + "_table"]
            st.write("Uploaded record data")
            st.dataframe(table_df, use_container_width=True, hide_index=True)
            return table_df
        return None


def cities_domain_ui(prefix):
    st.markdown("#### Provide route stop data")
    source = st.radio("Data source", ["Generate Synthetic Data", "Upload Real Data"], key=prefix + "_src", horizontal=True)
    if source == "Generate Synthetic Data":
        c1, c2, c3 = st.columns(3)
        with c1:
            num_cities = st.slider("Number of stops", 4, 25, 10, key=prefix + "_n")
        with c2:
            seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
        with c3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=prefix + "_showall")
        if st.button("Generate Synthetic Data Now", key=prefix + "_gen"):
            st.session_state[prefix + "_cities"] = build_synthetic_cities(num_cities, seed=seed)
        if prefix + "_cities" in st.session_state:
            cities_df = st.session_state[prefix + "_cities"]
            if show_all:
                st.write("Complete synthetic stop data, " + str(len(cities_df)) + " rows")
                st.dataframe(cities_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of stop data, first 5 rows")
                st.dataframe(cities_df.head(5), use_container_width=True, hide_index=True)
            return cities_df
        return None
    else:
        cfile = st.file_uploader("Upload Stop CSV File, columns CityID Name X Y", type=["csv"], key=prefix + "_cf")
        if cfile is not None:
            st.session_state[prefix + "_cities"] = pd.read_csv(cfile)
        if prefix + "_cities" in st.session_state:
            cities_df = st.session_state[prefix + "_cities"]
            st.write("Uploaded stop data")
            st.dataframe(cities_df, use_container_width=True, hide_index=True)
            return cities_df
        return None


def csp_domain_ui(prefix):
    st.markdown("#### Provide region and adjacency data")
    source = st.radio("Data source", ["Generate Synthetic Data", "Upload Real Data"], key=prefix + "_src", horizontal=True)
    if source == "Generate Synthetic Data":
        c1, c2, c3 = st.columns(3)
        with c1:
            num_regions = st.slider("Number of regions", 4, 25, 10, key=prefix + "_n")
        with c2:
            seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
        with c3:
            show_all = st.checkbox("Display Entire Synthetic Data", key=prefix + "_showall")
        if st.button("Generate Synthetic Data Now", key=prefix + "_gen"):
            regions_df, adjacency_df = build_synthetic_regions(num_regions, seed=seed)
            st.session_state[prefix + "_regions"] = regions_df
            st.session_state[prefix + "_adjacency"] = adjacency_df
        if prefix + "_regions" in st.session_state:
            regions_df = st.session_state[prefix + "_regions"]
            adjacency_df = st.session_state[prefix + "_adjacency"]
            if show_all:
                st.write("Complete region data, " + str(len(regions_df)) + " rows")
                st.dataframe(regions_df, use_container_width=True, hide_index=True)
                st.write("Complete adjacency data, " + str(len(adjacency_df)) + " rows")
                st.dataframe(adjacency_df, use_container_width=True, hide_index=True)
            else:
                st.write("Preview of region data, first 5 rows")
                st.dataframe(regions_df.head(5), use_container_width=True, hide_index=True)
                st.write("Preview of adjacency data, first 5 rows")
                st.dataframe(adjacency_df.head(5), use_container_width=True, hide_index=True)
            return regions_df, adjacency_df, build_adjacency_map(regions_df, adjacency_df)
        return None, None, None
    else:
        rfile = st.file_uploader("Upload Region CSV File, columns RegionID Name", type=["csv"], key=prefix + "_rf")
        afile = st.file_uploader("Upload Adjacency CSV File, columns RegionA RegionB", type=["csv"], key=prefix + "_af")
        if rfile is not None and afile is not None:
            st.session_state[prefix + "_regions"] = pd.read_csv(rfile)
            st.session_state[prefix + "_adjacency"] = pd.read_csv(afile)
        if prefix + "_regions" in st.session_state:
            regions_df = st.session_state[prefix + "_regions"]
            adjacency_df = st.session_state[prefix + "_adjacency"]
            st.write("Uploaded region data")
            st.dataframe(regions_df, use_container_width=True, hide_index=True)
            st.write("Uploaded adjacency data")
            st.dataframe(adjacency_df, use_container_width=True, hide_index=True)
            return regions_df, adjacency_df, build_adjacency_map(regions_df, adjacency_df)
        return None, None, None


def gametree_domain_ui(prefix, use_chance_nodes=False):
    st.markdown("#### Configure the game tree")
    st.write("Game trees are generated synthetically since they represent algorithmic decision structures rather than uploadable records.")
    c1, c2, c3 = st.columns(3)
    with c1:
        branching = st.slider("Branching factor", 2, 4, 2, key=prefix + "_b")
    with c2:
        depth = st.slider("Tree depth", 2, 5, 3, key=prefix + "_d")
    with c3:
        seed = st.number_input("Random seed", 1, 9999, _default_seed(), key=prefix + "_seed")
    if st.button("Generate Game Tree Now", key=prefix + "_gen"):
        st.session_state[prefix + "_tree"] = build_synthetic_gametree(branching, depth, seed=seed, use_chance_nodes=use_chance_nodes)
    if prefix + "_tree" in st.session_state:
        tree = st.session_state[prefix + "_tree"]
        leaf_count = branching ** depth
        st.write("Generated a game tree with branching factor " + str(branching) + ", depth " + str(depth) +
                  ", and " + str(leaf_count) + " leaf nodes.")
        return tree
    return None

# ---------------------------------------------------------------------------
# Generic result display and export section, used by every algorithm
# ---------------------------------------------------------------------------

def render_result_and_export(prefix, category_name, algo_name, explanation, params, status, result_text, details=None, table_df=None, chart_fig=None):
    st.markdown("#### Result")
    st.write("Status: " + status)
    st.write(result_text)
    for d in (details or []):
        st.write(d)

    if chart_fig is not None:
        st.markdown("#### Visualization")
        st.pyplot(chart_fig)

    if table_df is not None and len(table_df) > 0:
        st.markdown("#### Result Table")
        st.dataframe(table_df, use_container_width=True, hide_index=True)

    summary = build_summary(category_name, algo_name, explanation, params, status, result_text, details, table_df)

    st.markdown("#### Export Results")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.download_button("Download PDF", data=export_pdf_bytes(summary), file_name=prefix + "_result.pdf",
                            mime="application/pdf", key=prefix + "_pdf")
    with c2:
        st.download_button("Download Word", data=export_word_bytes(summary), file_name=prefix + "_result.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=prefix + "_word")
    with c3:
        st.download_button("Download CSV", data=export_csv_bytes(summary), file_name=prefix + "_result.csv",
                            mime="text/csv", key=prefix + "_csv")
    with c4:
        st.download_button("Download Text", data=export_text_bytes(summary), file_name=prefix + "_result.txt",
                            mime="text/plain", key=prefix + "_text")


def render_schema_section(schema_frames):
    with st.expander("View Data Schema"):
        for label, frame in schema_frames:
            st.subheader(label)
            st.dataframe(frame, use_container_width=True, hide_index=True)

def render_category_1():
    st.header("1. Classical AI and State Space Search")
    st.write("These are the foundational uninformed search techniques used to move through a knowledge graph from a start condition to a goal, without any heuristic guidance.")
    algo = st.selectbox("Choose a technique", [
        "Breadth First Search", "Depth First Search", "Depth Limited Search",
        "Iterative Deepening DFS", "Uniform Cost Search", "Bidirectional Search",
        "Tree Search", "Graph Search",
    ], key="cat1_algo")

    explanations = {
        "Breadth First Search": (
            "Explores nodes level by level outward from the start node. Finds the shortest path in terms of number of relationships when all edges are treated as equal cost.\n\n"
            "**When to use:** Use it when every relationship should count equally, no edge has a meaningful cost, and you need the fewest possible hops between two points, for example the shortest chain of logins between two accounts.\n\n"
            "**Benefits:** Guarantees the shortest hop count, is simple to implement and reason about, and explores the graph in a predictable, level by level order that is easy to visualize.\n\n"
            "**Important use-cases:** Finding the shortest reporting or access chain in an org or asset graph, computing degrees of separation in a social or vendor network, and broadcasting or reachability checks in unweighted networks."
        ),
        "Depth First Search": (
            "Follows one path as deeply as possible before backtracking. Uses relatively little memory, approximately O(b times m) for branching factor b and depth m.\n\n"
            "**When to use:** Use it when memory is limited, any valid path will do rather than the shortest one, or you need to explore deep chains such as long dependency or attack sequences before trying alternatives.\n\n"
            "**Benefits:** Very low memory footprint compared to breadth first exploration, straightforward to implement recursively or with a stack, and well suited to problems where a full path must be built before it can be evaluated.\n\n"
            "**Important use-cases:** Detecting cycles in dependency graphs, exploring deep attack or exploit chains, maze and puzzle solving, and topological style traversals where depth matters more than breadth."
        ),
        "Depth Limited Search": (
            "Performs Depth First Search but stops expanding once a maximum depth limit is reached, preventing an indefinite search.\n\n"
            "**When to use:** Use it when the graph may contain cycles or be effectively infinite and you only care about solutions within a known maximum number of hops.\n\n"
            "**Benefits:** Prevents runaway searches on cyclic or very deep graphs, keeps memory bounded like plain DFS, and gives predictable worst case run time based on the chosen limit.\n\n"
            "**Important use-cases:** Bounding how many hops an attacker could realistically pivot through, enforcing a maximum approval chain length, and any policy check where only nearby relationships matter."
        ),
        "Iterative Deepening DFS": (
            "Repeatedly runs Depth Limited Search with an increasing depth limit until a solution is found, combining the low memory use of DFS with the completeness of BFS.\n\n"
            "**When to use:** Use it when you want the shortest-path guarantee of BFS but cannot afford the memory BFS needs, particularly on large or unknown-depth graphs.\n\n"
            "**Benefits:** Combines low memory use with completeness and optimality in hop count, and does not require knowing the depth of the solution in advance.\n\n"
            "**Important use-cases:** Large scale dependency or access graphs where memory is constrained, exploratory investigations where the distance to the answer is unknown, and puzzle or game state search."
        ),
        "Uniform Cost Search": (
            "Expands the lowest cumulative cost path first, useful when relationships between nodes have different costs such as risk, time, or money.\n\n"
            "**When to use:** Use it whenever edges carry a real cost, such as risk, time, or dollars, and you need the cheapest path rather than the one with the fewest hops.\n\n"
            "**Benefits:** Guarantees the lowest total cost path for non negative edge weights, and generalizes breadth first search naturally to weighted graphs.\n\n"
            "**Important use-cases:** Finding the lowest risk path an attacker could take through a network, cheapest routing decisions, and prioritizing remediation paths by cumulative effort or cost."
        ),
        "Bidirectional Search": (
            "Runs two simultaneous searches, one forward from the start node and one backward from the goal node, meeting in the middle to reduce the search space.\n\n"
            "**When to use:** Use it when both the start and the goal are known in advance and the graph is large, so that searching from both ends cuts the explored space dramatically.\n\n"
            "**Benefits:** Can reduce the number of nodes explored roughly from b^d to 2 times b^(d/2), which is a large saving on large graphs, while still finding a shortest path.\n\n"
            "**Important use-cases:** Large scale connectivity checks between two specific assets, shortest relationship path lookups in big enterprise graphs, and any point to point search where both endpoints are fixed."
        ),
        "Tree Search": (
            "Treats every generated path as a new node even if the same state has already been seen, which can revisit states but is simple to implement.\n\n"
            "**When to use:** Use it for teaching or illustrating the basic search mechanism, or in problems where the state space is genuinely a tree and duplicate states cannot occur.\n\n"
            "**Benefits:** Very simple to implement and understand, and requires no bookkeeping of an explored set.\n\n"
            "**Important use-cases:** Educational demonstrations of search fundamentals, and small acyclic decision trees where revisiting is not a concern."
        ),
        "Graph Search": (
            "Maintains an explored set of visited states so that the same state is never expanded twice, avoiding redundant work in cyclic graphs.\n\n"
            "**When to use:** Use it whenever the underlying graph can contain cycles or shared sub-paths, which is the normal case for enterprise, network, and organizational graphs.\n\n"
            "**Benefits:** Avoids repeated, wasted expansion of the same node, which keeps the search efficient and guarantees termination even on cyclic graphs.\n\n"
            "**Important use-cases:** Any production search over a real enterprise or network graph, where cycles such as mutual dependencies or bidirectional connections are common."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
    nodes_df, edges_df, graph = graph_domain_ui("cat1_" + algo.replace(" ", "_"))
    if graph is None:
        st.info("Provide data above to continue")
        return

    node_ids = list(nodes_df["ID"])
    c1, c2 = st.columns(2)
    with c1:
        start = st.selectbox("Start node", node_ids, key="cat1_start_" + algo)
    with c2:
        goal = st.selectbox("Goal node", node_ids, index=min(len(node_ids) - 1, 1), key="cat1_goal_" + algo)

    extra_params = {}
    if algo == "Depth Limited Search":
        extra_params["limit"] = st.slider("Depth limit", 1, 15, 5, key="cat1_limit")
    if algo == "Iterative Deepening DFS":
        extra_params["max_limit"] = st.slider("Maximum depth limit", 1, 15, 8, key="cat1_maxlimit")

    if st.button("Run " + algo, key="cat1_run"):
        params = {"Start node": start, "Goal node": goal, "Total nodes": len(nodes_df), "Total edges": len(edges_df)}
        params.update(extra_params)

        if algo == "Breadth First Search":
            path, visited = bfs_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Depth First Search":
            path, visited = dfs_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Depth Limited Search":
            path, visited = depth_limited_search(graph, start, goal, extra_params["limit"])
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Iterative Deepening DFS":
            path, visited, found_limit = iddfs_search(graph, start, goal, extra_params["max_limit"])
            details = ["Nodes visited across all depth iterations: " + " then ".join(visited),
                        "Solution found at depth limit: " + str(found_limit) if path else "No solution found within the maximum depth limit"]
        elif algo == "Uniform Cost Search":
            path, cost, visited = ucs_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
            if cost is not None:
                details.append("Total cumulative cost: " + str(round(cost, 2)))
        elif algo == "Bidirectional Search":
            path, visited = bidirectional_search(graph, start, goal)
            details = ["Nodes visited from both directions: " + " then ".join(visited)]
        elif algo == "Tree Search":
            path, visited = tree_search_no_visited(graph, start, goal)
            details = ["Nodes expanded, note that revisits are possible since no explored set is kept: " + str(len(visited))]
        else:
            path, visited = graph_search_with_explored_set(graph, start, goal)
            details = ["Nodes visited using an explored set: " + " then ".join(visited)]

        status = "Path found" if path else "No path found"
        result_text = ("Path: " + " then ".join(path)) if path else "No path exists between the selected start and goal nodes"
        fig = plot_graph(graph, path, title=algo + " Result")
        st.session_state["cat1_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=nodes_df[nodes_df["ID"].isin(path)] if path else None,
                                                fig=fig, params=params, explanation=explanations[algo], algo=algo)

    if "cat1_output" in st.session_state and st.session_state["cat1_output"]["algo"] == algo:
        o = st.session_state["cat1_output"]
        render_result_and_export("cat1_" + algo.replace(" ", "_"), "Classical AI and State Space Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_2():
    st.header("2. Informed and Heuristic Search")
    st.write("These techniques use a heuristic, in this case the straight line distance between synthetic node coordinates, to guide the search more efficiently toward the goal.")
    algo = st.selectbox("Choose a technique", [
        "Greedy Best First Search", "A Star", "Weighted A Star", "IDA Star",
        "Beam Search", "Hill Climbing", "Random Restart Hill Climbing", "Simulated Annealing",
    ], key="cat2_algo")

    explanations = {
        "Greedy Best First Search": (
            "Always expands the node that appears closest to the goal according to the heuristic, ignoring the cost already spent getting there.\n\n"
            "**When to use:** Use it when you need a fast, approximate path and a reasonably good heuristic exists, and you can accept a path that may not be the cheapest.\n\n"
            "**Benefits:** Often very fast in practice because it aggressively pursues the goal, and needs little bookkeeping beyond the heuristic estimate.\n\n"
            "**Important use-cases:** Quick triage of a likely attack or access path when speed matters more than optimality, and any first-pass exploration before a more rigorous search is run."
        ),
        "A Star": (
            "Combines the actual cost so far g(n) with the estimated remaining cost h(n), expanding the node with the lowest f(n) = g(n) + h(n). Guarantees an optimal path when the heuristic never overestimates.\n\n"
            "**When to use:** Use it whenever you need the guaranteed cheapest path and have an admissible heuristic available, making it the default choice over Uniform Cost Search when a good heuristic exists.\n\n"
            "**Benefits:** Optimal and complete under an admissible heuristic, and typically explores far fewer nodes than Uniform Cost Search because the heuristic focuses the search toward the goal.\n\n"
            "**Important use-cases:** Finding the lowest cost route through a network or dependency graph, route planning, and any risk or cost minimizing path search where correctness matters."
        ),
        "Weighted A Star": (
            "A variant of A Star that multiplies the heuristic by a weight greater than one, trading optimality for a faster search.\n\n"
            "**When to use:** Use it when a fast, good-enough answer is more valuable than a guaranteed optimal one, for example under time pressure during an incident.\n\n"
            "**Benefits:** Converges faster than plain A Star by expanding fewer nodes, with the weight giving a tunable dial between speed and solution quality.\n\n"
            "**Important use-cases:** Time constrained investigations, near real time path suggestions, and large graphs where full A Star would be too slow."
        ),
        "IDA Star": (
            "Iterative Deepening A Star, which repeats a depth first search bounded by an increasing f(n) threshold, achieving A Star quality solutions with much lower memory use.\n\n"
            "**When to use:** Use it when A Star would be optimal but its memory use is too high for the size of the graph.\n\n"
            "**Benefits:** Keeps the optimality guarantees of A Star while using memory proportional to the solution depth rather than the number of nodes stored.\n\n"
            "**Important use-cases:** Very large graphs or state spaces where A Star's frontier would not fit in memory, such as broad enterprise wide asset graphs."
        ),
        "Beam Search": (
            "Keeps only a limited number of the best candidate nodes at each level, discarding the rest, which keeps memory use bounded at the cost of completeness.\n\n"
            "**When to use:** Use it on very large search spaces where exploring every candidate is impractical and a bounded, approximate search is acceptable.\n\n"
            "**Benefits:** Predictable, bounded memory and time regardless of graph size, and tunable quality versus speed through the beam width.\n\n"
            "**Important use-cases:** Large scale candidate ranking such as narrowing down likely attack paths from many possibilities, and any scenario where only the top few options at each stage matter."
        ),
        "Hill Climbing": (
            "Continuously moves to the best looking neighboring node, stopping when no neighbor improves on the current node, which can get stuck in a local optimum.\n\n"
            "**When to use:** Use it for a quick, simple local improvement when an approximate answer is acceptable and the search space is reasonably smooth.\n\n"
            "**Benefits:** Extremely simple and fast, with very low memory use since it only tracks the current node.\n\n"
            "**Important use-cases:** Fast local refinement of an existing path or configuration, and as a baseline to compare against more robust techniques like Simulated Annealing."
        ),
        "Random Restart Hill Climbing": (
            "Runs Hill Climbing repeatedly from different random starting nodes to try to escape local optima.\n\n"
            "**When to use:** Use it when plain Hill Climbing keeps getting stuck in local optima and you can afford several repeated runs.\n\n"
            "**Benefits:** Much more likely to find a globally strong solution than a single Hill Climbing run, while remaining simple to implement.\n\n"
            "**Important use-cases:** Rugged, bumpy search landscapes such as irregular network topologies, and situations where a single starting point is not trustworthy."
        ),
        "Simulated Annealing": (
            "Behaves like Hill Climbing but occasionally accepts a worse move, especially early in the search when a temperature parameter is high, to escape local optima.\n\n"
            "**When to use:** Use it when the search landscape has many local optima and a single greedy climb is likely to get stuck, but you want a single continuous run rather than many restarts.\n\n"
            "**Benefits:** Balances exploration and exploitation through its cooling schedule, and can escape local optima that trap plain Hill Climbing.\n\n"
            "**Important use-cases:** Complex optimization landscapes such as risk-weighted path selection, and problems where Random Restart Hill Climbing is too expensive to run many times."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
    nodes_df, edges_df, graph = graph_domain_ui("cat2_" + algo.replace(" ", "_"))
    if graph is None:
        st.info("Provide data above to continue")
        return

    node_ids = list(nodes_df["ID"])
    c1, c2 = st.columns(2)
    with c1:
        start = st.selectbox("Start node", node_ids, key="cat2_start_" + algo)
    with c2:
        goal = st.selectbox("Goal node", node_ids, index=min(len(node_ids) - 1, 1), key="cat2_goal_" + algo)

    extra_params = {}
    if algo == "Weighted A Star":
        extra_params["weight"] = st.slider("Heuristic weight", 1.0, 5.0, 2.0, step=0.5, key="cat2_weight")
    if algo == "Beam Search":
        extra_params["beam_width"] = st.slider("Beam width", 1, 10, 3, key="cat2_beamwidth")
    if algo == "Random Restart Hill Climbing":
        extra_params["restarts"] = st.slider("Number of restarts", 2, 20, 5, key="cat2_restarts")
    if algo == "Simulated Annealing":
        extra_params["initial_temp"] = st.slider("Initial temperature", 10, 300, 100, key="cat2_temp")
        extra_params["cooling"] = st.slider("Cooling rate", 0.80, 0.99, 0.95, step=0.01, key="cat2_cooling")
    seed = st.number_input("Random seed for stochastic techniques", 1, 9999, _default_seed(), key="cat2_seed")

    if st.button("Run " + algo, key="cat2_run"):
        params = {"Start node": start, "Goal node": goal, "Total nodes": len(nodes_df)}
        params.update(extra_params)
        details = []
        table_df = None

        if algo == "Greedy Best First Search":
            path, visited = greedy_best_first_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "A Star":
            path, cost, visited = astar_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
            if cost is not None:
                details.append("Total path cost: " + str(round(cost, 2)))
        elif algo == "Weighted A Star":
            path, cost, visited = astar_search(graph, start, goal, heuristic_weight=extra_params["weight"])
            details = ["Nodes visited in order: " + " then ".join(visited)]
            if cost is not None:
                details.append("Total path cost: " + str(round(cost, 2)))
        elif algo == "IDA Star":
            path, visited = ida_star_search(graph, start, goal)
            details = ["Nodes visited across all iterations: " + str(len(visited))]
        elif algo == "Beam Search":
            path, visited = beam_search(graph, start, goal, extra_params["beam_width"])
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Hill Climbing":
            path, visited, note = hill_climbing_search(graph, start, goal)
            details = [note, "Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Random Restart Hill Climbing":
            path, visited, note = random_restart_hill_climbing(graph, start, goal, extra_params["restarts"], seed)
            details = [note]
        else:
            path, visited, note = simulated_annealing_search(graph, start, goal, seed, extra_params["initial_temp"], extra_params["cooling"])
            details = [note]

        status = "Path found" if path else "No path found"
        result_text = ("Path: " + " then ".join(path)) if path else "No path was found with this technique and these parameters"
        fig = plot_graph(graph, path, title=algo + " Result")
        if path:
            table_df = nodes_df[nodes_df["ID"].isin(path)]
        st.session_state["cat2_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=table_df, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat2_output" in st.session_state and st.session_state["cat2_output"]["algo"] == algo:
        o = st.session_state["cat2_output"]
        render_result_and_export("cat2_" + algo.replace(" ", "_"), "Informed and Heuristic Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

def render_category_3():
    st.header("3. Adversarial and Game Search")
    st.write("These techniques search a game tree where a maximizing player and a minimizing player alternate turns, or where chance nodes introduce randomness.")
    algo = st.selectbox("Choose a technique", [
        "Minimax", "Alpha Beta Pruning", "Expectiminimax", "Monte Carlo Tree Search",
    ], key="cat3_algo")

    explanations = {
        "Minimax": (
            "Explores the full game tree, assuming the maximizing player always picks the highest value move and the minimizing player always picks the lowest value move.\n\n"
            "**When to use:** Use it on small, fully known, two player adversarial trees where the entire tree can realistically be explored.\n\n"
            "**Benefits:** Guarantees the game theoretically optimal move under the assumption of a perfectly rational opponent, and is simple and easy to reason about.\n\n"
            "**Important use-cases:** Small board games, teaching adversarial reasoning, and modeling attacker versus defender decision trees where both sides play optimally."
        ),
        "Alpha Beta Pruning": (
            "Computes the same result as Minimax but skips branches that cannot possibly influence the final decision, using alpha and beta bounds to prune the tree.\n\n"
            "**When to use:** Use it any time you would use Minimax, since it returns the identical result while typically exploring far fewer nodes.\n\n"
            "**Benefits:** Same optimal guarantees as Minimax with substantially lower computation, allowing deeper or larger trees to be searched in the same time.\n\n"
            "**Important use-cases:** Larger adversarial game trees than plain Minimax can handle, and any production adversarial reasoning where efficiency matters."
        ),
        "Expectiminimax": (
            "Extends Minimax to trees that include chance nodes, where the value of a chance node is the probability weighted average of its children.\n\n"
            "**When to use:** Use it when the adversarial process includes an element of randomness or uncertainty, not just two players making deterministic choices.\n\n"
            "**Benefits:** Correctly accounts for probabilistic outcomes rather than assuming worst case or best case chance results, giving a more realistic expected value.\n\n"
            "**Important use-cases:** Games with dice or random events, and modeling attacker decisions where some steps succeed only with a certain probability, such as an exploit that only sometimes works."
        ),
        "Monte Carlo Tree Search": (
            "Estimates the value of each move using many random rollout simulations rather than exploring the full tree, useful when the tree is too large to search exhaustively.\n\n"
            "**When to use:** Use it when the game tree is far too large for Minimax or Alpha Beta Pruning to explore exhaustively, but many quick random simulations are feasible.\n\n"
            "**Benefits:** Scales to very large or even unknown-size trees, improves its estimate as more simulations are run, and does not require a full tree in memory.\n\n"
            "**Important use-cases:** Large scale strategy games, and simulating many plausible attacker or defender scenarios to estimate the value of a move without enumerating every possibility."
        ),
    }
    st.write(explanations[algo])

    with st.expander("View Data Schema"):
        st.write("Game trees use an internal structure rather than a tabular schema. Each node has an ID, a list of children, and leaf nodes carry a numeric value representing the outcome for the maximizing player. Chance nodes additionally carry a probability on each child.")

    use_chance = (algo == "Expectiminimax")
    tree = gametree_domain_ui("cat3_" + algo.replace(" ", "_"), use_chance_nodes=use_chance)
    if tree is None:
        st.info("Generate a game tree above to continue")
        return

    simulations = 200
    if algo == "Monte Carlo Tree Search":
        simulations = st.slider("Number of rollout simulations per move", 20, 1000, 200, key="cat3_sims")
    seed = st.number_input("Random seed", 1, 9999, _default_seed(), key="cat3_seed")

    if st.button("Run " + algo, key="cat3_run"):
        params = {"Branching factor and depth": "see tree configuration above", "Random seed": seed}
        details = []
        if algo == "Minimax":
            value, path = minimax_search(tree)
            details = ["Optimal path through the tree: " + " then ".join(path)]
            result_text = "Optimal game value for the maximizing player: " + str(value)
            fig = plot_tree(tree, path, title="Minimax Result")
        elif algo == "Alpha Beta Pruning":
            value, path, counter = alpha_beta_search(tree)
            details = ["Optimal path through the tree: " + " then ".join(path),
                       "Nodes visited: " + str(counter["nodes"]),
                       "Nodes pruned and skipped: " + str(counter["pruned"])]
            result_text = "Optimal game value for the maximizing player: " + str(value)
            fig = plot_tree(tree, path, title="Alpha Beta Result")
        elif algo == "Expectiminimax":
            value, path = expectiminimax_search(tree)
            details = ["Path through the tree, note chance nodes average over all children: " + " then ".join(path)]
            result_text = "Expected game value for the maximizing player: " + str(round(value, 2))
            fig = plot_tree(tree, path, title="Expectiminimax Result")
        else:
            best_id, scores = mcts_estimate(tree, simulations, seed)
            details = ["Estimated average value per top level move: " + str(scores)]
            result_text = "Recommended move based on simulation is child node: " + best_id
            fig = plot_tree(tree, [best_id], title="Monte Carlo Tree Search Result")

        status = "Search complete"
        st.session_state["cat3_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=None, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat3_output" in st.session_state and st.session_state["cat3_output"]["algo"] == algo:
        o = st.session_state["cat3_output"]
        render_result_and_export("cat3_" + algo.replace(" ", "_"), "Adversarial and Game Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_4():
    st.header("4. Optimization Search")
    st.write("These techniques are demonstrated on a route optimization problem in the style of the traveling salesman problem, where the goal is to find a low cost tour visiting every stop exactly once.")
    algo = st.selectbox("Choose a technique", [
        "Local Search", "Genetic Algorithm", "Evolutionary Search", "Particle Swarm Optimization",
        "Ant Colony Optimization", "Tabu Search", "Differential Evolution",
    ], key="cat4_algo")

    explanations = {
        "Local Search": (
            "Searches neighboring solutions by making small random changes to the current tour, keeping any change that improves the total distance.\n\n"
            "**When to use:** Use it as a fast, simple baseline for optimization problems where you need a quick improvement over a starting solution rather than a guaranteed best answer.\n\n"
            "**Benefits:** Very low implementation complexity and computational cost, and easy to apply to almost any optimization problem with a notion of neighboring solutions.\n\n"
            "**Important use-cases:** Quick route or schedule improvement, warm-starting a more sophisticated optimizer, and small to medium routing problems."
        ),
        "Genetic Algorithm": (
            "Evolves a population of candidate tours using selection of the fittest tours, crossover between pairs of tours, and occasional random mutation.\n\n"
            "**When to use:** Use it on larger, more complex optimization landscapes where local search alone gets stuck, and where a diverse population helps avoid premature convergence.\n\n"
            "**Benefits:** Explores many candidate solutions in parallel, is resistant to getting trapped in a single local optimum, and generalizes to a wide range of optimization problems beyond routing.\n\n"
            "**Important use-cases:** Route and logistics optimization, scheduling problems, and resource allocation where the search space is large and irregular."
        ),
        "Evolutionary Search": (
            "A related population based technique that keeps only a truncated set of the best performing tours as survivors each generation, then generates offspring from them.\n\n"
            "**When to use:** Use it when you want the population diversity of a Genetic Algorithm but with stronger, more deterministic selection pressure toward the current best solutions.\n\n"
            "**Benefits:** Tends to converge faster than a standard Genetic Algorithm because only the strongest survivors reproduce, while still exploring multiple candidates per generation.\n\n"
            "**Important use-cases:** Optimization problems where faster convergence is valued over maximum diversity, such as time boxed route replanning."
        ),
        "Particle Swarm Optimization": (
            "Represents each candidate tour as a particle with a position and velocity in a continuous space, where particles are pulled toward their own best position and the swarm's best position.\n\n"
            "**When to use:** Use it on optimization problems that can be represented in a continuous space and benefit from particles sharing information about the best solution found so far.\n\n"
            "**Benefits:** Simple to tune with few parameters, converges quickly by combining individual and collective memory, and works well on smooth continuous landscapes.\n\n"
            "**Important use-cases:** Continuous parameter tuning, route and layout optimization, and engineering style optimization problems adapted to a discrete tour."
        ),
        "Ant Colony Optimization": (
            "Simulates ants laying down pheromone trails on good edges, with future ants more likely to follow paths with stronger pheromone concentration.\n\n"
            "**When to use:** Use it specifically on graph and routing style optimization problems, where reinforcing good edges over many iterations naturally builds strong paths.\n\n"
            "**Benefits:** Naturally suited to edge and path based problems, balances exploration and exploitation through pheromone evaporation, and often finds high quality routes.\n\n"
            "**Important use-cases:** Vehicle routing and logistics, network path optimization, and any problem naturally expressed as finding good edges through a graph."
        ),
        "Tabu Search": (
            "Similar to Local Search, but keeps a short term memory of recently tried moves that are temporarily forbidden, encouraging the search to explore new areas.\n\n"
            "**When to use:** Use it when plain Local Search keeps cycling back to the same local optimum and you need memory of recent moves to force exploration of new areas.\n\n"
            "**Benefits:** Escapes cycles and shallow local optima more reliably than plain Local Search, while remaining computationally lightweight.\n\n"
            "**Important use-cases:** Routing and scheduling problems with many similar local optima, and refining a solution after a broader search has narrowed the candidates."
        ),
        "Differential Evolution": (
            "A population based technique that creates new candidate solutions by combining the weighted difference between two population members with a third member.\n\n"
            "**When to use:** Use it on optimization problems with continuous or continuous-like structure where combining differences between existing good solutions tends to produce better ones.\n\n"
            "**Benefits:** Few control parameters, strong performance on continuous optimization landscapes, and a good balance of exploration through mutation and exploitation through selection.\n\n"
            "**Important use-cases:** Parameter and configuration tuning, continuous route or layout optimization, and as an alternative to Genetic Algorithm and PSO on smoother landscapes."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Stop Schema", CITIES_SCHEMA)])
    cities_df = cities_domain_ui("cat4_" + algo.replace(" ", "_"))
    if cities_df is None:
        st.info("Provide data above to continue")
        return

    seed = st.number_input("Random seed", 1, 9999, _default_seed(), key="cat4_seed")
    extra_params = {}
    if algo in ("Genetic Algorithm", "Evolutionary Search"):
        extra_params["pop_size"] = st.slider("Population size", 10, 100, 30, key="cat4_pop")
        extra_params["generations"] = st.slider("Generations", 10, 300, 100, key="cat4_gen")
    if algo == "Particle Swarm Optimization":
        extra_params["num_particles"] = st.slider("Number of particles", 5, 60, 20, key="cat4_particles")
        extra_params["iterations"] = st.slider("Iterations", 10, 300, 80, key="cat4_iters")
    if algo == "Ant Colony Optimization":
        extra_params["num_ants"] = st.slider("Number of ants", 5, 40, 15, key="cat4_ants")
        extra_params["iterations"] = st.slider("Iterations", 10, 150, 40, key="cat4_aco_iters")
    if algo == "Tabu Search":
        extra_params["iterations"] = st.slider("Iterations", 20, 400, 150, key="cat4_tabu_iters")
        extra_params["tabu_size"] = st.slider("Tabu list size", 5, 50, 15, key="cat4_tabu_size")
    if algo == "Differential Evolution":
        extra_params["pop_size"] = st.slider("Population size", 10, 80, 20, key="cat4_de_pop")
        extra_params["generations"] = st.slider("Generations", 10, 300, 80, key="cat4_de_gen")
    if algo == "Local Search":
        extra_params["iterations"] = st.slider("Iterations", 20, 1000, 200, key="cat4_ls_iters")

    if st.button("Run " + algo, key="cat4_run"):
        params = {"Number of stops": len(cities_df), "Random seed": seed}
        params.update(extra_params)

        if algo == "Local Search":
            best_tour, best_cost, history = local_search_tsp(cities_df, seed, extra_params["iterations"])
        elif algo == "Genetic Algorithm":
            best_tour, best_cost, history = genetic_algorithm_tsp(cities_df, seed, extra_params["pop_size"], extra_params["generations"])
        elif algo == "Evolutionary Search":
            best_tour, best_cost, history = evolutionary_search_tsp(cities_df, seed, extra_params["pop_size"], extra_params["generations"])
        elif algo == "Particle Swarm Optimization":
            best_tour, best_cost, history = pso_tsp(cities_df, seed, extra_params["num_particles"], extra_params["iterations"])
        elif algo == "Ant Colony Optimization":
            best_tour, best_cost, history = aco_tsp(cities_df, seed, extra_params["num_ants"], extra_params["iterations"])
        elif algo == "Tabu Search":
            best_tour, best_cost, history = tabu_search_tsp(cities_df, seed, extra_params["iterations"], extra_params["tabu_size"])
        else:
            best_tour, best_cost, history = differential_evolution_tsp(cities_df, seed, extra_params["pop_size"], extra_params["generations"])

        status = "Optimization complete"
        result_text = "Best tour found: " + " then ".join(best_tour) + ". Total distance: " + str(round(best_cost, 2))
        details = ["Starting distance before optimization: " + str(round(history[0], 2)),
                    "Final distance after optimization: " + str(round(history[-1], 2))]
        fig = plot_tour(cities_df, best_tour, title=algo + " Best Route")
        table_df = pd.DataFrame({"Step": list(range(1, len(history) + 1)), "Best_Distance_So_Far": history})
        st.session_state["cat4_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=table_df, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo, history=history)

    if "cat4_output" in st.session_state and st.session_state["cat4_output"]["algo"] == algo:
        o = st.session_state["cat4_output"]
        st.markdown("#### Convergence Curve")
        conv_fig = plot_line(list(range(1, len(o["history"]) + 1)), o["history"], algo + " Convergence", "Iteration", "Best Distance")
        st.pyplot(conv_fig)
        render_result_and_export("cat4_" + algo.replace(" ", "_"), "Optimization Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

def render_category_5():
    st.header("5. Constraint Based Search")
    st.write("These techniques are demonstrated on a map coloring problem, where each region must be assigned a color so that no two adjacent regions share the same color.")
    algo = st.selectbox("Choose a technique", [
        "Backtracking Search", "CSP Search", "Forward Checking", "Arc Consistency Search", "Branch and Bound",
    ], key="cat5_algo")

    explanations = {
        "Backtracking Search": (
            "Builds a solution one region at a time, assigning a valid color and moving forward. If no valid color exists it backs up and tries a different earlier assignment.\n\n"
            "**When to use:** Use it as the standard baseline approach for any constraint satisfaction problem where solutions must be built incrementally and checked against constraints.\n\n"
            "**Benefits:** Guaranteed to find a solution if one exists, straightforward to implement, and works on any constraint structure without special preprocessing.\n\n"
            "**Important use-cases:** Resource and role assignment where conflicting entities cannot share a value, scheduling with exclusion rules, and classic map or graph coloring problems."
        ),
        "CSP Search": (
            "The general Constraint Satisfaction Problem search process, here applying the same backtracking mechanism while explicitly tracking every variable, its domain of possible colors, and the constraints between neighboring regions.\n\n"
            "**When to use:** Use it when you want full visibility into the variables, domains, and constraints driving the search, not just the final answer.\n\n"
            "**Benefits:** Makes the constraint model explicit and auditable, which helps when explaining why a particular assignment was or was not possible.\n\n"
            "**Important use-cases:** Compliance and policy modeling where every constraint must be traceable, and configuration problems with many interacting rules."
        ),
        "Forward Checking": (
            "After assigning a color to a region, immediately removes that color from the domains of its uncolored neighbors, catching failures earlier than plain backtracking.\n\n"
            "**When to use:** Use it whenever plain Backtracking Search is exploring too many dead ends, since detecting failure earlier saves significant wasted work.\n\n"
            "**Benefits:** Prunes the search tree earlier than plain backtracking, reducing wasted exploration, while remaining simple to add on top of backtracking.\n\n"
            "**Important use-cases:** Larger constraint problems such as enterprise wide access or segmentation assignments, where early failure detection meaningfully speeds up the search."
        ),
        "Arc Consistency Search": (
            "Applies the AC-3 algorithm before search begins, removing colors from a region's domain if no compatible color exists for a neighboring region, shrinking the search space in advance.\n\n"
            "**When to use:** Use it as a preprocessing step before search on problems with many tightly interconnected constraints, to shrink the space before any search begins.\n\n"
            "**Benefits:** Can eliminate large parts of the search space before search starts, often making the subsequent search dramatically faster or even trivial.\n\n"
            "**Important use-cases:** Densely connected constraint networks such as tightly coupled segmentation zones, and any CSP where a quick consistency check can rule out many options up front."
        ),
        "Branch and Bound": (
            "Tries to color the map with the fewest possible colors, starting from one color and increasing the palette size only when a smaller palette fails, bounding the search by the best known solution.\n\n"
            "**When to use:** Use it when the goal is not just any valid assignment but the smallest or cheapest number of resources needed to satisfy all constraints.\n\n"
            "**Benefits:** Finds the provably minimal resource count, and prunes branches that cannot beat the best solution found so far, avoiding wasted search.\n\n"
            "**Important use-cases:** Minimizing the number of security zones, roles, or resource pools needed while respecting separation constraints, and other minimum-resource assignment problems."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Region and Adjacency Schema", CSP_SCHEMA)])
    regions_df, adjacency_df, adj = csp_domain_ui("cat5_" + algo.replace(" ", "_"))
    if adj is None:
        st.info("Provide data above to continue")
        return

    colors_text = st.text_input("Available colors, comma separated", "Red,Green,Blue,Yellow", key="cat5_colors")
    colors = [c.strip() for c in colors_text.split(",") if c.strip()]

    if st.button("Run " + algo, key="cat5_run"):
        params = {"Number of regions": len(regions_df), "Available colors": colors_text}
        if algo == "Backtracking Search" or algo == "CSP Search":
            assignment, stats = backtracking_coloring(regions_df, adj, colors)
        elif algo == "Forward Checking":
            assignment, stats = backtracking_coloring(regions_df, adj, colors, use_forward_checking=True)
        elif algo == "Arc Consistency Search":
            assignment, stats = backtracking_coloring(regions_df, adj, colors, use_arc_consistency=True)
        else:
            assignment, k_used, stats = branch_and_bound_coloring(regions_df, adj, colors)
            params["Minimum colors needed"] = k_used

        status = "Solution found" if assignment else "No valid coloring found with the given color palette"
        if assignment:
            result_text = "Assignment: " + ", ".join(r + " = " + c for r, c in assignment.items())
            table_df = pd.DataFrame([{"Region": r, "Assigned_Color": c} for r, c in assignment.items()])
        else:
            result_text = "The search could not find a valid coloring, try adding more colors"
            table_df = None
        details = ["Nodes explored: " + str(stats.get("nodes_explored", 0)),
                   "Backtracks performed: " + str(stats.get("backtracks", 0)),
                   "Domain values pruned: " + str(stats.get("pruned", 0))]

        graph_for_plot = nx.DiGraph()
        for r in regions_df["RegionID"]:
            graph_for_plot.add_node(r, X=0, Y=0)
        color_palette_hex = ["#FF9900", "#2E8B57", "#378ADD", "#D4537E", "#A9C6E8", "#7F77DD"]
        color_lookup = {c: color_palette_hex[i % len(color_palette_hex)] for i, c in enumerate(colors)}
        for _, row in adjacency_df.iterrows():
            graph_for_plot.add_edge(row["RegionA"], row["RegionB"])
        undirected = graph_for_plot.to_undirected()
        pos = nx.spring_layout(undirected, seed=7)
        fig, ax = plt.subplots(figsize=(8, 5))
        node_colors = [color_lookup.get(assignment.get(n), "#B0B0B0") if assignment else "#B0B0B0" for n in undirected.nodes]
        nx.draw_networkx_nodes(undirected, pos, node_color=node_colors, node_size=600, ax=ax)
        nx.draw_networkx_labels(undirected, pos, font_size=8, ax=ax)
        nx.draw_networkx_edges(undirected, pos, edge_color="#888888", ax=ax)
        ax.set_title(algo + " Result", fontsize=13, fontweight="bold", color="#0000CC")
        ax.axis("off")
        fig.tight_layout()

        st.session_state["cat5_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=table_df, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat5_output" in st.session_state and st.session_state["cat5_output"]["algo"] == algo:
        o = st.session_state["cat5_output"]
        render_result_and_export("cat5_" + algo.replace(" ", "_"), "Constraint Based Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_6():
    st.header("6. String and Text Searching")
    st.write("These techniques search for an exact pattern within a body of text, each using a different strategy to reduce the number of character comparisons.")
    algo = st.selectbox("Choose a technique", [
        "Linear String Search", "Naive Pattern Matching", "KMP Search", "Boyer Moore Search",
        "Rabin Karp Search", "Trie Search", "Suffix Tree Search", "Regular Expression Search",
    ], key="cat6_algo")

    explanations = {
        "Linear String Search": (
            "Checks every position in the text sequentially, comparing the pattern directly against the text at that position.\n\n"
            "**When to use:** Use it for short texts or one-off searches where implementation simplicity matters more than raw speed.\n\n"
            "**Benefits:** Trivial to implement and understand, with no preprocessing step required before searching.\n\n"
            "**Important use-cases:** Quick ad hoc lookups in short log snippets or small text fields, and as a correctness baseline to compare faster algorithms against."
        ),
        "Naive Pattern Matching": (
            "The classic brute force approach that tries matching the pattern at every possible position in the text, one character at a time, also reporting the total number of character comparisons performed.\n\n"
            "**When to use:** Use it when you want to see or measure exactly how many character comparisons a brute force match requires, typically for teaching or benchmarking.\n\n"
            "**Benefits:** Simple, predictable, and useful as a reference point for demonstrating why smarter algorithms like KMP or Boyer Moore are faster.\n\n"
            "**Important use-cases:** Educational comparisons of string matching efficiency, and small texts where the overhead of a smarter algorithm is not worth it."
        ),
        "KMP Search": (
            "Knuth Morris Pratt search precomputes a failure function from the pattern itself, allowing it to skip re-examining characters it has already matched, giving linear time performance.\n\n"
            "**When to use:** Use it when searching for a pattern in a large text and you need a guaranteed linear time worst case, especially with repetitive patterns.\n\n"
            "**Benefits:** Guaranteed O(n plus m) time with no backtracking in the text, which makes it reliable even in adversarial or highly repetitive inputs.\n\n"
            "**Important use-cases:** Scanning large log files or documents for a fixed signature, and streaming text search where the text cannot be re-read."
        ),
        "Boyer Moore Search": (
            "Compares the pattern against the text from right to left and uses a bad character rule to skip ahead in the text when a mismatch occurs, often skipping many positions at once.\n\n"
            "**When to use:** Use it on long texts with a moderately long pattern, where large skips on mismatch give a real world speed advantage.\n\n"
            "**Benefits:** Often the fastest practical exact string matcher on natural language or long alphabets, since it can skip multiple characters per mismatch.\n\n"
            "**Important use-cases:** Searching large documents or log corpora for known signatures, and text editor or IDE style find operations on big files."
        ),
        "Rabin Karp Search": (
            "Uses a rolling hash to quickly compare a hash of the pattern against a hash of each substring of the text, only doing a full character comparison when the hashes match.\n\n"
            "**When to use:** Use it when you need to search for many patterns at once, or search the same text for multiple different patterns efficiently.\n\n"
            "**Benefits:** The rolling hash makes it easy to extend to multiple pattern search, and average case performance is very good on typical text.\n\n"
            "**Important use-cases:** Plagiarism and duplicate content detection, multi-pattern indicator of compromise scanning, and DNA or sequence matching style problems."
        ),
        "Trie Search": (
            "Builds a prefix tree from a list of words, enabling very fast lookup of all words that share a given prefix.\n\n"
            "**When to use:** Use it when you repeatedly need prefix based lookups, such as autocomplete, over a fixed or slowly changing vocabulary of words.\n\n"
            "**Benefits:** Extremely fast prefix queries after the tree is built, and naturally supports autocomplete and prefix enumeration.\n\n"
            "**Important use-cases:** Autocomplete and typeahead search, dictionary and vocabulary lookups, and matching against a known list of terms or identifiers by prefix."
        ),
        "Suffix Tree Search": (
            "Represents all suffixes of a text using a sorted suffix array with binary search, enabling fast substring lookup, here implemented as a suffix array based approximation of a suffix tree.\n\n"
            "**When to use:** Use it when the same text will be searched for many different substrings repeatedly, so the upfront indexing cost pays off.\n\n"
            "**Benefits:** Very fast repeated substring queries once built, at the cost of a one time preprocessing step to build the suffix structure.\n\n"
            "**Important use-cases:** Repeated substring or pattern queries against a fixed large document, bioinformatics style sequence analysis, and full text indexing."
        ),
        "Regular Expression Search": (
            "Uses the standard regular expression engine to find all positions in the text matching a pattern that may include wildcards and special characters.\n\n"
            "**When to use:** Use it when the search pattern is not a fixed literal string but a flexible pattern involving wildcards, character classes, or repetition.\n\n"
            "**Benefits:** Enormous flexibility to express complex matching rules in a compact syntax, supporting far more than exact string matches.\n\n"
            "**Important use-cases:** Validating and extracting structured fields such as IP addresses or file hashes from log text, and flexible pattern based log or alert filtering."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Document Schema", TEXT_SCHEMA)])
    corpus_df = text_domain_ui("cat6_" + algo.replace(" ", "_"))
    if corpus_df is None:
        st.info("Provide data above to continue")
        return

    doc_id = st.selectbox("Document to search within", list(corpus_df["DocID"]), key="cat6_doc")
    text = corpus_df[corpus_df["DocID"] == doc_id]["Text"].iloc[0]
    st.write("Selected document text: " + text)

    default_pattern = text.split()[0] if text.split() else "report"
    if algo == "Trie Search":
        pattern = st.text_input("Prefix to search for", default_pattern[:3], key="cat6_pattern")
    elif algo == "Regular Expression Search":
        pattern = st.text_input("Regular expression pattern", default_pattern, key="cat6_pattern")
    else:
        pattern = st.text_input("Pattern to search for", default_pattern, key="cat6_pattern")

    if st.button("Run " + algo, key="cat6_run"):
        params = {"Document": doc_id, "Pattern": pattern}
        details = []
        table_df = None

        if algo == "Linear String Search":
            positions = linear_string_search(text, pattern)
        elif algo == "Naive Pattern Matching":
            positions, comparisons = naive_pattern_matching(text, pattern)
            details.append("Total character comparisons performed: " + str(comparisons))
        elif algo == "KMP Search":
            positions = kmp_search(text, pattern)
        elif algo == "Boyer Moore Search":
            positions = boyer_moore_search(text, pattern)
        elif algo == "Rabin Karp Search":
            positions = rabin_karp_search(text, pattern)
        elif algo == "Trie Search":
            trie = build_trie(text.split())
            matches = trie_search(trie, pattern)
            positions = None
            details.append("Words matching this prefix: " + (", ".join(matches) if matches else "none"))
            table_df = pd.DataFrame({"Matched_Word": matches}) if matches else None
        elif algo == "Suffix Tree Search":
            positions = suffix_array_search(text, pattern)
        else:
            positions, error = regex_search(text, pattern)
            if error:
                details.append("Regular expression error: " + error)

        if algo != "Trie Search":
            status = "Pattern found" if positions else "Pattern not found"
            result_text = ("Pattern found at character positions: " + str(positions)) if positions else "The pattern was not found in the selected document"
            if positions:
                table_df = pd.DataFrame({"Match_Position": positions})
        else:
            status = "Search complete"
            result_text = "Trie prefix search complete for prefix " + pattern

        fig = plot_bar(["Document length", "Pattern length"], [len(text), len(pattern)], "Text and Pattern Length", "", "Characters")
        st.session_state["cat6_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=table_df, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat6_output" in st.session_state and st.session_state["cat6_output"]["algo"] == algo:
        o = st.session_state["cat6_output"]
        render_result_and_export("cat6_" + algo.replace(" ", "_"), "String and Text Searching", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

def render_category_7():
    st.header("7. Database Search")
    st.write("These techniques search a table of business records using strategies similar to those used inside a real database engine.")
    algo = st.selectbox("Choose a technique", [
        "Sequential Table Scan", "Index Search", "B Tree Search", "Hash Search",
        "Range Search", "Query Optimization Search",
    ], key="cat7_algo")

    explanations = {
        "Sequential Table Scan": (
            "Examines every record one at a time, comparing the target field against the search value. Simple but slow on large tables.\n\n"
            "**When to use:** Use it on small tables, one-off queries, or when no index exists and building one is not worth the cost.\n\n"
            "**Benefits:** Requires no preprocessing or index maintenance, always works regardless of query pattern, and is trivial to reason about.\n\n"
            "**Important use-cases:** Ad hoc exploration of small record sets, and as a correctness baseline when validating that an indexed search returns the right results."
        ),
        "Index Search": (
            "Builds a dictionary style index that maps each field value to the matching record positions, giving very fast lookup after the index is built.\n\n"
            "**When to use:** Use it when the same field will be queried repeatedly for exact matches, so the one time cost of building the index is repaid many times over.\n\n"
            "**Benefits:** Near constant time equality lookups after the index is built, dramatically faster than scanning for repeated queries.\n\n"
            "**Important use-cases:** Repeated lookups by a business key such as employee ID or account number, and any field queried frequently in a dashboard or application."
        ),
        "B Tree Search": (
            "Sorts the table on the search field and uses binary search to locate the target value, similar to how a balanced B tree index narrows down a search range.\n\n"
            "**When to use:** Use it when queries need both exact match and range or ordering support, which a pure hash index cannot provide.\n\n"
            "**Benefits:** Logarithmic time lookup while also preserving sort order, enabling efficient range queries in addition to exact matches.\n\n"
            "**Important use-cases:** Fields queried both for exact values and ranges, such as amounts or risk scores, and any scenario mirroring a real relational database B tree index."
        ),
        "Hash Search": (
            "Builds a hash based index for exact equality lookups, giving close to constant time lookup regardless of table size.\n\n"
            "**When to use:** Use it when only exact equality lookups are needed on a field, not ranges or ordering, and lookup speed is the top priority.\n\n"
            "**Benefits:** Close to constant time lookup regardless of table size, generally the fastest option for pure equality queries.\n\n"
            "**Important use-cases:** High volume equality lookups such as looking up a record by a unique key, hash, or identifier during real time processing."
        ),
        "Range Search": (
            "Finds all records whose value in a numeric field falls between a lower and upper bound, after sorting the table on that field.\n\n"
            "**When to use:** Use it whenever the query is a range condition rather than an exact match, such as records above a threshold or within a window.\n\n"
            "**Benefits:** Efficiently narrows down to a contiguous block of sorted records rather than scanning the whole table.\n\n"
            "**Important use-cases:** Finding records with a risk score above a threshold, amounts within a budget range, or events within a time window."
        ),
        "Query Optimization Search": (
            "Estimates the cost of a full table scan versus an index based lookup and automatically chooses the cheaper strategy, similar to a database query optimizer choosing an execution plan.\n\n"
            "**When to use:** Use it when you want the system to automatically pick the most efficient strategy rather than committing to one approach manually.\n\n"
            "**Benefits:** Adapts automatically to table size and selectivity, avoiding the cost of a full scan when an index based approach would be cheaper, and vice versa.\n\n"
            "**Important use-cases:** Production style query execution where workload characteristics vary, and demonstrating how a real database optimizer chooses between plans."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Record Schema", TABLE_SCHEMA)])
    table_df = table_domain_ui("cat7_" + algo.replace(" ", "_"))
    if table_df is None:
        st.info("Provide data above to continue")
        return

    numeric_fields = [c for c in table_df.columns if pd.api.types.is_numeric_dtype(table_df[c])]
    all_fields = list(table_df.columns)

    if algo == "Range Search":
        field = st.selectbox("Numeric field", numeric_fields, key="cat7_field")
        low = st.number_input("Lower bound", value=float(table_df[field].min()), key="cat7_low")
        high = st.number_input("Upper bound", value=float(table_df[field].max()), key="cat7_high")
    else:
        field = st.selectbox("Field to search", all_fields, key="cat7_field")
        default_value = str(table_df[field].iloc[0])
        value = st.text_input("Value to search for", default_value, key="cat7_value")

    if st.button("Run " + algo, key="cat7_run"):
        details = []
        if algo == "Sequential Table Scan":
            params = {"Field": field, "Value": value}
            matches, scanned = sequential_scan(table_df, field, value)
            details.append("Records scanned: " + str(scanned))
        elif algo == "Index Search":
            params = {"Field": field, "Value": value}
            matches, index_size = index_search(table_df, field, value)
            details.append("Distinct index keys built: " + str(index_size))
        elif algo == "B Tree Search":
            params = {"Field": field, "Value": value}
            matches, position = btree_search(table_df, field, value)
            details.append("Position located by binary search: " + str(position))
        elif algo == "Hash Search":
            params = {"Field": field, "Value": value}
            matches, idx = hash_search(table_df, field, value)
            details.append("Row index located: " + str(idx))
        elif algo == "Range Search":
            params = {"Field": field, "Lower bound": low, "Upper bound": high}
            matches = range_search(table_df, field, low, high)
        else:
            params = {"Field": field, "Value": value}
            matches, chosen, scan_cost, index_cost = query_optimization_search(table_df, field, value)
            details.append("Chosen execution plan: " + chosen)
            details.append("Estimated sequential scan cost: " + str(round(scan_cost, 2)))
            details.append("Estimated index search cost: " + str(round(index_cost, 2)))

        status = "Records found" if len(matches) > 0 else "No matching records found"
        result_text = "Number of matching records: " + str(len(matches))
        fig = plot_bar(["Total records", "Matched records"], [len(table_df), len(matches)], algo + " Result", "", "Record count")
        st.session_state["cat7_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=matches, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat7_output" in st.session_state and st.session_state["cat7_output"]["algo"] == algo:
        o = st.session_state["cat7_output"]
        render_result_and_export("cat7_" + algo.replace(" ", "_"), "Database Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_8():
    st.header("8. Graph Search")
    st.write("Graph search underpins much of the Kalsnet Hub Knowledge Graph, letting the system find paths, distances, and structure across enterprise and security data.")
    algo = st.selectbox("Choose a technique", [
        "Breadth First Search", "Depth First Search", "Shortest Path Search", "Dijkstra Algorithm",
        "Bellman Ford Algorithm", "Floyd Warshall Algorithm", "A Star Graph Search",
        "Topological Search", "Connectivity Search", "Community Detection",
    ], key="cat8_algo")

    explanations = {
        "Breadth First Search": (
            "Finds nodes by increasing number of relationships, or hops, away from a starting node.\n\n"
            "**When to use:** Use it to explore an enterprise or network graph outward from an asset when hop distance, not weighted cost, is what matters.\n\n"
            "**Benefits:** Simple, predictable, and guarantees the fewest hops to any reachable node.\n\n"
            "**Important use-cases:** Mapping how far an asset is from a compromised node in hops, and general graph reachability exploration."
        ),
        "Depth First Search": (
            "Explores a graph as deeply as possible along each branch before backtracking.\n\n"
            "**When to use:** Use it when you need to trace a single deep chain of relationships, such as following one dependency path to its end, rather than exploring broadly.\n\n"
            "**Benefits:** Low memory use and naturally suited to exploring deep chains of relationships one at a time.\n\n"
            "**Important use-cases:** Tracing a dependency or ownership chain to its root, and exploring deep relationship structures in the Knowledge Graph."
        ),
        "Shortest Path Search": (
            "Finds the least cost path between two nodes. Implemented here using Dijkstra's algorithm, which is optimal when all edge costs are non negative.\n\n"
            "**When to use:** Use it as the general purpose, go-to shortest path tool whenever edge costs are non negative and you need the single lowest cost path between two specific nodes.\n\n"
            "**Benefits:** Optimal and efficient for the common case of non negative weights, and directly answers the practical question of the cheapest way between two points.\n\n"
            "**Important use-cases:** Lowest cost or lowest risk path between two enterprise assets, and general purpose point to point routing in the Knowledge Graph."
        ),
        "Dijkstra Algorithm": (
            "Finds the shortest path from a start node to every other node using a priority queue, guaranteed correct when all edge weights are non negative.\n\n"
            "**When to use:** Use it when you need shortest paths from one start node to many or all other nodes at once, not just a single destination.\n\n"
            "**Benefits:** Computes shortest paths to every reachable node in a single run, which is more efficient than repeating a single-target search for each destination.\n\n"
            "**Important use-cases:** Computing the shortest or lowest risk distance from a compromised asset to every other asset, and building distance tables for further analysis."
        ),
        "Bellman Ford Algorithm": (
            "Finds shortest paths even when some edge weights are negative, by relaxing every edge repeatedly, and can also detect negative cost cycles.\n\n"
            "**When to use:** Use it specifically when the graph can contain negative edge weights, which Dijkstra cannot handle correctly, or when you need to detect negative cycles.\n\n"
            "**Benefits:** Correctly handles negative weights and can explicitly detect negative cost cycles that would otherwise be silently mishandled by other algorithms.\n\n"
            "**Important use-cases:** Graphs where a relationship can represent a net benefit or discount modeled as a negative cost, and detecting inconsistent or cyclic risk scoring."
        ),
        "Floyd Warshall Algorithm": (
            "Computes the shortest path between every pair of nodes in the graph simultaneously using dynamic programming.\n\n"
            "**When to use:** Use it on smaller to medium graphs when you need the complete matrix of shortest distances between every pair of nodes, not just from one source.\n\n"
            "**Benefits:** Produces the full all pairs shortest path matrix in one computation, and naturally handles negative edges without negative cycles.\n\n"
            "**Important use-cases:** Building a complete distance or risk matrix across all assets for further analysis, and dense graphs where many pairwise queries are expected."
        ),
        "A Star Graph Search": (
            "Uses a straight line distance heuristic between synthetic coordinates to accelerate the search for the lowest cost path.\n\n"
            "**When to use:** Use it, as in Category 2, whenever a good heuristic is available and you want the optimal path found faster than Dijkstra alone.\n\n"
            "**Benefits:** Same optimality guarantee as Dijkstra for a single target, but typically explores far fewer nodes thanks to heuristic guidance.\n\n"
            "**Important use-cases:** Fast point to point shortest path queries on large graphs where a spatial or estimated distance heuristic is available."
        ),
        "Topological Search": (
            "Orders the nodes of a directed acyclic graph so that every edge points from an earlier node to a later node, useful for dependency ordering.\n\n"
            "**When to use:** Use it whenever you need a valid processing or build order that respects dependency relationships, and the graph has no cycles.\n\n"
            "**Benefits:** Produces a correct dependency respecting order in linear time, and can reveal whether the graph actually is acyclic.\n\n"
            "**Important use-cases:** Determining a safe order to patch or update interdependent systems, and sequencing tasks that must respect prerequisite relationships."
        ),
        "Connectivity Search": (
            "Determines which groups of nodes are connected to each other, useful for identifying isolated segments of an enterprise network.\n\n"
            "**When to use:** Use it to check whether the graph is a single connected structure or splits into isolated islands, which matters for both reachability and isolation analysis.\n\n"
            "**Benefits:** Quickly reveals isolated or segmented parts of the network without needing to compute full path distances.\n\n"
            "**Important use-cases:** Verifying that network segmentation is working as intended, and identifying orphaned or disconnected assets in the environment."
        ),
        "Community Detection": (
            "Groups nodes into clusters that are more densely connected internally than to the rest of the graph, using a greedy modularity optimization approach.\n\n"
            "**When to use:** Use it when you want to discover natural groupings or clusters in the graph without predefining categories, based purely on connection density.\n\n"
            "**Benefits:** Surfaces organizational or functional groupings that may not be obvious from metadata alone, purely from the relationship structure.\n\n"
            "**Important use-cases:** Discovering natural asset or team clusters for segmentation planning, and identifying tightly coupled groups of systems that behave as a unit."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
    allow_negative = algo == "Bellman Ford Algorithm"
    force_dag = algo == "Topological Search"
    nodes_df, edges_df, graph = graph_domain_ui("cat8_" + algo.replace(" ", "_"), allow_negative=allow_negative, force_dag=force_dag)
    if graph is None:
        st.info("Provide data above to continue")
        return

    node_ids = list(nodes_df["ID"])
    needs_start_goal = algo not in ("Floyd Warshall Algorithm", "Topological Search", "Connectivity Search", "Community Detection")
    start, goal = node_ids[0], node_ids[min(len(node_ids) - 1, 1)]
    if needs_start_goal:
        c1, c2 = st.columns(2)
        with c1:
            start = st.selectbox("Start node", node_ids, key="cat8_start_" + algo)
        with c2:
            goal = st.selectbox("Goal node", node_ids, index=min(len(node_ids) - 1, 1), key="cat8_goal_" + algo)

    if st.button("Run " + algo, key="cat8_run"):
        params = {"Total nodes": len(nodes_df), "Total edges": len(edges_df)}
        if needs_start_goal:
            params["Start node"] = start
            params["Goal node"] = goal
        details = []
        table_df = None
        fig = None

        if algo == "Breadth First Search":
            path, visited = bfs_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo == "Depth First Search":
            path, visited = dfs_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
        elif algo in ("Shortest Path Search", "Dijkstra Algorithm"):
            path, cost, visited = dijkstra_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
            if cost is not None:
                details.append("Total path cost: " + str(round(cost, 2)))
        elif algo == "Bellman Ford Algorithm":
            path, cost, negative_cycle = bellman_ford_search(graph, start, goal)
            details = ["Negative cost cycle detected: " + str(negative_cycle)]
            if cost is not None:
                details.append("Total path cost: " + str(round(cost, 2)))
        elif algo == "Floyd Warshall Algorithm":
            dist_matrix = floyd_warshall_search(graph)
            table_df = pd.DataFrame(dist_matrix).replace(float("inf"), None)
            table_df.insert(0, "From_Node", table_df.index)
            path = None
        elif algo == "A Star Graph Search":
            path, cost, visited = astar_search(graph, start, goal)
            details = ["Nodes visited in order: " + " then ".join(visited)]
            if cost is not None:
                details.append("Total path cost: " + str(round(cost, 2)))
        elif algo == "Topological Search":
            order, is_dag = topological_search(graph)
            path = None
            details = ["Graph is a directed acyclic graph: " + str(is_dag)]
            if order:
                table_df = pd.DataFrame({"Topological_Order": order})
        elif algo == "Connectivity Search":
            components = connectivity_search(graph)
            path = None
            table_df = pd.DataFrame([{"Component": i + 1, "Nodes": ", ".join(sorted(c)), "Size": len(c)} for i, c in enumerate(components)])
            details = ["Number of weakly connected components: " + str(len(components))]
        else:
            communities = community_detection_search(graph)
            path = None
            table_df = pd.DataFrame([{"Community": i + 1, "Nodes": ", ".join(sorted(c)), "Size": len(c)} for i, c in enumerate(communities)])
            details = ["Number of communities detected: " + str(len(communities))]

        if algo in ("Breadth First Search", "Depth First Search", "Shortest Path Search", "Dijkstra Algorithm",
                    "Bellman Ford Algorithm", "A Star Graph Search"):
            status = "Path found" if path else "No path found"
            result_text = ("Path: " + " then ".join(path)) if path else "No path exists between the selected start and goal nodes"
            fig = plot_graph(graph, path, title=algo + " Result")
            if path:
                table_df = nodes_df[nodes_df["ID"].isin(path)]
        else:
            status = "Search complete"
            result_text = "See details and result table below"
            fig = plot_graph(graph, None, title=algo + " Result")

        st.session_state["cat8_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=table_df, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat8_output" in st.session_state and st.session_state["cat8_output"]["algo"] == algo:
        o = st.session_state["cat8_output"]
        render_result_and_export("cat8_" + algo.replace(" ", "_"), "Graph Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

def render_category_9():
    st.header("9. Information Retrieval Search")
    st.write("These techniques search a collection of documents and rank them by relevance to a query, the same foundational operations used inside search engines.")
    algo = st.selectbox("Choose a technique", [
        "Keyword Search", "Boolean Search", "Full Text Search", "Inverted Index Search",
        "Ranked Retrieval", "TF-IDF Search", "BM25 Search", "Semantic Search", "Vector Search", "Hybrid Search",
    ], key="cat9_algo")

    explanations = {
        "Keyword Search": (
            "Finds documents whose text contains the given keyword, treated as a simple substring match.\n\n"
            "**When to use:** Use it for the simplest possible lookup, when you just need to know which documents mention a specific word or phrase.\n\n"
            "**Benefits:** Extremely simple, fast to implement, and requires no indexing or ranking machinery.\n\n"
            "**Important use-cases:** Quick presence checks such as finding every document that mentions a specific vendor or system name."
        ),
        "Boolean Search": (
            "Supports AND, OR, and NOT operators between terms, letting the person build more precise queries.\n\n"
            "**When to use:** Use it when a single keyword is too broad or too narrow and you need to combine multiple conditions precisely.\n\n"
            "**Benefits:** Gives precise, explicit control over which combinations of terms must, may, or must not appear.\n\n"
            "**Important use-cases:** Precise compliance or legal style document searches, and narrowing large result sets with explicit include and exclude terms."
        ),
        "Full Text Search": (
            "Searches the complete content of every document for the query text, case insensitive.\n\n"
            "**When to use:** Use it for a straightforward, case-insensitive search of complete document content when exact substring matching is enough.\n\n"
            "**Benefits:** Simple and comprehensive, checking the entire document body rather than just titles or metadata.\n\n"
            "**Important use-cases:** General purpose document search across incident reports, policies, or notes."
        ),
        "Inverted Index Search": (
            "Builds an index mapping every word to the list of documents containing it, which is the foundational data structure behind most search engines.\n\n"
            "**When to use:** Use it when the same corpus will be searched repeatedly, since the one time cost of building the index makes every subsequent query fast.\n\n"
            "**Benefits:** Very fast repeated term lookups after the index is built, and forms the foundation that ranked and scored search techniques build on.\n\n"
            "**Important use-cases:** Backing a searchable document repository or knowledge base where users issue many queries over time."
        ),
        "Ranked Retrieval": (
            "Counts how many times each query term appears in each document and ranks documents by that raw term frequency count.\n\n"
            "**When to use:** Use it as a simple relevance ranking when a more sophisticated weighting scheme like TF-IDF or BM25 is not needed.\n\n"
            "**Benefits:** Easy to understand and compute, giving a basic sense of relevance ordering beyond simple presence or absence.\n\n"
            "**Important use-cases:** Quick relevance ordering of search results when document collections are small and term frequency alone is informative enough."
        ),
        "TF-IDF Search": (
            "Ranks documents using term frequency, how often a word appears in a document, combined with inverse document frequency, which down weights words that appear in many documents.\n\n"
            "**When to use:** Use it when common words should be down-weighted automatically so that distinctive, rarer terms drive the ranking.\n\n"
            "**Benefits:** Automatically balances term frequency against how distinctive a term is across the whole corpus, giving better relevance than raw counts.\n\n"
            "**Important use-cases:** Ranking documents by relevance in a general purpose search tool, and as the foundation for the Vector Search technique below."
        ),
        "BM25 Search": (
            "A widely used probabilistic ranking function that improves on TF-IDF by accounting for document length and saturating the effect of very frequent terms.\n\n"
            "**When to use:** Use it as a stronger default than TF-IDF for production style relevance ranking, especially when documents vary a lot in length.\n\n"
            "**Benefits:** Handles document length variation and term frequency saturation better than plain TF-IDF, which is why it is the default ranking function in many real search engines.\n\n"
            "**Important use-cases:** Production grade document ranking, and as the keyword-based half of Hybrid Search."
        ),
        "Semantic Search": (
            "Ranks documents by meaning rather than exact words. Without an API key this falls back to a word overlap similarity measure, described in the Modern AI and LLM Search category for full embedding based semantics.\n\n"
            "**When to use:** Use it when the right documents may not share exact keywords with the query, so meaning based matching is needed instead of literal term matching.\n\n"
            "**Benefits:** Can surface relevant documents that use different wording than the query, which keyword based methods would miss entirely.\n\n"
            "**Important use-cases:** Natural language questions over a document set, and finding conceptually related material that does not share exact vocabulary."
        ),
        "Vector Search": (
            "Represents documents and the query as numeric vectors, here built from TF-IDF weights, and ranks by cosine similarity between vectors.\n\n"
            "**When to use:** Use it when you want a mathematically grounded similarity ranking based on vector representations rather than raw term overlap.\n\n"
            "**Benefits:** Provides a general, reusable similarity framework that also underlies embedding based semantic search in Category 10.\n\n"
            "**Important use-cases:** Similarity ranking and nearest-document lookups, and as a conceptual bridge to full embedding based vector search."
        ),
        "Hybrid Search": (
            "Combines a keyword based ranking, BM25, with a vector based ranking, blending both scores into a single combined rank.\n\n"
            "**When to use:** Use it when neither pure keyword search nor pure vector search alone gives consistently strong results, and you want the strengths of both.\n\n"
            "**Benefits:** Balances exact keyword precision with vector based conceptual relevance, generally outperforming either approach used alone.\n\n"
            "**Important use-cases:** Production search systems that need to handle both precise keyword queries and broader conceptual questions well."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Document Schema", TEXT_SCHEMA)])
    corpus_df = text_domain_ui("cat9_" + algo.replace(" ", "_"))
    if corpus_df is None:
        st.info("Provide data above to continue")
        return

    default_query = "server database"
    if algo == "Boolean Search":
        query = st.text_input("Query, use AND OR NOT between terms", "server AND database", key="cat9_query")
    else:
        query = st.text_input("Search query", default_query, key="cat9_query")

    if st.button("Run " + algo, key="cat9_run"):
        params = {"Query": query, "Total documents": len(corpus_df)}
        details = []
        if algo == "Keyword Search":
            result = keyword_search(corpus_df, query)
        elif algo == "Boolean Search":
            result = boolean_search(corpus_df, query)
        elif algo == "Full Text Search":
            result = full_text_search(corpus_df, query)
        elif algo == "Inverted Index Search":
            result, index_size = inverted_index_search(corpus_df, query)
            details.append("Distinct terms in the inverted index: " + str(index_size))
        elif algo == "Ranked Retrieval":
            result = ranked_retrieval(corpus_df, query)
        elif algo == "TF-IDF Search":
            result = tfidf_search(corpus_df, query)
        elif algo == "BM25 Search":
            result = bm25_search(corpus_df, query)
        elif algo == "Semantic Search":
            result = semantic_search_wordoverlap(corpus_df, query)
            details.append("This uses a built in word overlap similarity measure. See Modern AI and LLM Search for real embedding based semantic search.")
        elif algo == "Vector Search":
            result = vector_search_tfidf(corpus_df, query)
        else:
            result = hybrid_search(corpus_df, query)

        status = "Results found" if len(result) > 0 else "No matching documents found"
        result_text = "Number of matching or ranked documents: " + str(len(result))
        top_labels = result["DocID"].head(8).tolist()
        top_values = result["Score"].head(8).tolist() if "Score" in result.columns else [1] * len(top_labels)
        fig = plot_bar(top_labels, top_values, algo + " Top Results", "Document", "Score") if top_labels else None
        st.session_state["cat9_output"] = dict(status=status, result_text=result_text, details=details,
                                                table_df=result, fig=fig, params=params,
                                                explanation=explanations[algo], algo=algo)

    if "cat9_output" in st.session_state and st.session_state["cat9_output"]["algo"] == algo:
        o = st.session_state["cat9_output"]
        render_result_and_export("cat9_" + algo.replace(" ", "_"), "Information Retrieval Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_10(api_provider, api_key):
    st.header("10. Modern AI and LLM Search")
    st.write("These techniques reflect how modern AI systems, including large language models, search over information. Several can use a real OpenAI, Gemini, or Grok API key configured in the sidebar for true generated answers, real embeddings from OpenAI or Gemini, and otherwise fall back to a transparent synthetic substitute.")
    algo = st.selectbox("Choose a technique", [
        "Embedding Search", "Vector Similarity Search", "RAG Search", "Knowledge Graph Search",
        "Graph RAG", "Agentic Search", "Multi Step Search", "Query Expansion",
        "Semantic Reranking", "Self Query Search",
    ], key="cat10_algo")

    explanations = {
        "Embedding Search": (
            "Converts every document and the query into a numeric embedding vector and ranks documents by cosine similarity to the query vector.\n\n"
            "**When to use:** Use it when the right answer may be phrased very differently from the query, so meaning based similarity is needed rather than exact keyword overlap. Configure an OpenAI or Gemini key for real embeddings.\n\n"
            "**Benefits:** Captures conceptual similarity that keyword search misses entirely, and provides the foundation for RAG and other AI search techniques.\n\n"
            "**Important use-cases:** Finding conceptually related incident reports or policies that use different terminology, and general semantic document lookup."
        ),
        "Vector Similarity Search": (
            "The same underlying mechanism as Embedding Search, presented as the general technique of comparing vector representations using a distance measure such as cosine similarity.\n\n"
            "**When to use:** Use it whenever you already have vector representations of items and need to compare or rank them by similarity, beyond just documents.\n\n"
            "**Benefits:** A general purpose similarity framework applicable to any vectorized data, not limited to text.\n\n"
            "**Important use-cases:** Nearest neighbor lookups across embedded records, and as the mathematical basis behind recommendation and clustering features."
        ),
        "RAG Search": (
            "Retrieval Augmented Generation, which retrieves the most relevant documents for a query and then, if an API key is configured, asks a language model to answer using only that retrieved context.\n\n"
            "**When to use:** Use it when you want a natural language answer grounded in your own documents rather than the model's general knowledge, reducing the risk of an unsupported answer. Requires an OpenAI, Gemini, or Grok key for the generated answer, and OpenAI or Gemini for real retrieval embeddings.\n\n"
            "**Benefits:** Answers are grounded in retrieved source material, which reduces fabricated or unsupported claims compared to asking a language model with no context.\n\n"
            "**Important use-cases:** Answering questions about internal policies or incident history in natural language, and building an internal assistant grounded in enterprise documents."
        ),
        "Knowledge Graph Search": (
            "Searches entities and relationships in the enterprise Knowledge Graph for nodes whose type, owner, or name matches the query.\n\n"
            "**When to use:** Use it when the answer depends on structured entities and their relationships rather than free text, such as who owns what or how systems relate.\n\n"
            "**Benefits:** Leverages the explicit structure of the graph, giving precise, structured answers rather than approximate text matches.\n\n"
            "**Important use-cases:** Looking up ownership or relationship facts about specific assets, and grounding AI answers in verified structured data."
        ),
        "Graph RAG": (
            "Combines Knowledge Graph Search with document retrieval, giving a language model both graph context and document context to generate a grounded answer.\n\n"
            "**When to use:** Use it when a good answer needs both structured relationship facts and narrative document context together, more than either alone provides. Requires an OpenAI, Gemini, or Grok key for the generated answer.\n\n"
            "**Benefits:** Produces richer, more complete grounded answers by combining two complementary sources of truth, structure and narrative.\n\n"
            "**Important use-cases:** Investigative questions that need both relationship context, such as which systems are connected, and document context, such as what happened."
        ),
        "Agentic Search": (
            "Simulates an AI agent that runs a search, evaluates the result, and automatically refines its own query across several iterations until a strong match is found.\n\n"
            "**When to use:** Use it when a single search query is unlikely to find the best answer immediately and iterative refinement would help.\n\n"
            "**Benefits:** Automatically improves the query over multiple attempts without manual intervention, often surfacing better results than a single static query.\n\n"
            "**Important use-cases:** Exploratory investigations where the right search terms are not known up front, and automating iterative research tasks."
        ),
        "Multi Step Search": (
            "Chains together a sequence of searches, where each step's top result feeds into the query used for the next step.\n\n"
            "**When to use:** Use it when answering the real question requires following a chain of related lookups rather than a single search.\n\n"
            "**Benefits:** Supports multi-hop reasoning by carrying context from one search step into the next, something a single query cannot do.\n\n"
            "**Important use-cases:** Multi-hop investigative questions such as tracing from an initial alert to a related system to that system's owner."
        ),
        "Query Expansion": (
            "Expands the original query with related terms, either from a language model if a key is configured or from a small built in synonym list, before searching.\n\n"
            "**When to use:** Use it when users may search with different words than the documents use, so broadening the query improves recall. An OpenAI, Gemini, or Grok key gives richer, model generated expansions.\n\n"
            "**Benefits:** Improves recall by catching relevant documents that use synonyms or related terms rather than the exact query wording.\n\n"
            "**Important use-cases:** Improving search recall for users unfamiliar with exact internal terminology, and reducing missed results from narrow keyword queries."
        ),
        "Semantic Reranking": (
            "First retrieves a broader set of candidates using keyword ranking, then reorders that smaller set using embedding based semantic similarity.\n\n"
            "**When to use:** Use it when you want the speed of keyword retrieval combined with the relevance quality of semantic ranking, without running semantic search over the whole corpus.\n\n"
            "**Benefits:** Cheaper than running semantic search over an entire large corpus, while still improving final ranking quality using meaning based similarity.\n\n"
            "**Important use-cases:** Improving top result quality in large document collections without the cost of full corpus embedding search."
        ),
        "Self Query Search": (
            "Parses a natural language question into structured filters, for example turning risk above fifty into a numeric filter, and applies them to a table of records.\n\n"
            "**When to use:** Use it when users want to query structured tabular data using plain language instead of learning a formal query syntax.\n\n"
            "**Benefits:** Makes structured data accessible through natural language, lowering the barrier for non-technical users to filter records precisely.\n\n"
            "**Important use-cases:** Letting analysts ask plain language questions like risk above fifty in the USA, and building natural language front ends over enterprise tables."
        ),
    }
    st.write(explanations[algo])

    if api_key and api_provider != "None":
        st.success("An API key is configured for " + api_provider + ". This technique will use real AI calls where applicable.")
    else:
        st.warning("No API key is configured. This technique will use a transparent synthetic fallback. Configure a free key in the sidebar for real AI behavior.")

    if algo == "Self Query Search":
        render_schema_section([("Record Schema", TABLE_SCHEMA)])
        table_df = table_domain_ui("cat10_" + algo.replace(" ", "_"))
        if table_df is None:
            st.info("Provide data above to continue")
            return
        nl_query = st.text_input("Natural language question", "records with risk above 50 and country USA", key="cat10_nlq")
        if st.button("Run " + algo, key="cat10_run"):
            filtered, filters = self_query_search(table_df, nl_query)
            params = {"Natural language question": nl_query}
            status = "Filters applied" if filters else "No structured filters were recognized"
            result_text = "Parsed filters: " + (", ".join(filters) if filters else "none") + ". Matching records: " + str(len(filtered))
            fig = plot_bar(["Total records", "Matching records"], [len(table_df), len(filtered)], algo + " Result", "", "Record count")
            st.session_state["cat10_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=filtered, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
        if "cat10_output" in st.session_state and st.session_state["cat10_output"]["algo"] == algo:
            o = st.session_state["cat10_output"]
            render_result_and_export("cat10_" + algo.replace(" ", "_"), "Modern AI and LLM Search", algo,
                                      o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                      o["table_df"], o["fig"])
        return

    render_schema_section([("Document Schema", TEXT_SCHEMA), ("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
    corpus_df = text_domain_ui("cat10_" + algo.replace(" ", "_"))
    if corpus_df is None:
        st.info("Provide data above to continue")
        return

    graph = None
    if algo in ("Knowledge Graph Search", "Graph RAG"):
        st.markdown("#### Provide graph data for the knowledge graph portion")
        nodes_df, edges_df, graph = graph_domain_ui("cat10_graph_" + algo.replace(" ", "_"))
        if graph is None:
            st.info("Provide graph data above to continue")
            return

    query = st.text_input("Search query", "server database", key="cat10_query")

    if st.button("Run " + algo, key="cat10_run"):
        params = {"Query": query, "Total documents": len(corpus_df)}
        details = []
        table_df = None
        fig = None

        if algo == "Embedding Search" or algo == "Vector Similarity Search":
            result, note = embedding_search(corpus_df, query, api_provider, api_key)
            details.append(note)
            table_df = result
            status = "Search complete"
            result_text = "Top document: " + (result.iloc[0]["DocID"] if len(result) else "none")
            fig = plot_bar(result["DocID"].head(8).tolist(), result["Score"].head(8).tolist(), algo + " Result", "Document", "Similarity") if len(result) else None
        elif algo == "RAG Search":
            context_docs, answer, note, llm_note = rag_search(corpus_df, query, api_provider, api_key)
            details = [note, llm_note]
            table_df = context_docs
            status = "Answer generated" if answer else "Context retrieved, no AI answer available"
            result_text = answer if answer else "Retrieved context documents are shown below, but no answer was generated"
        elif algo == "Knowledge Graph Search":
            matches = knowledge_graph_search(graph, query)
            status = "Entities found" if matches else "No matching entities found"
            result_text = "Matched graph entities: " + (", ".join(matches) if matches else "none")
            table_df = pd.DataFrame({"Matched_Node": matches}) if matches else None
            fig = plot_graph(graph, matches if matches else None, title="Knowledge Graph Search Result")
        elif algo == "Graph RAG":
            kg_matches, doc_context, answer, note, llm_note = graph_rag_search(graph, corpus_df, query, api_provider, api_key)
            details = ["Matched graph entities: " + (", ".join(kg_matches) if kg_matches else "none"), note, llm_note]
            table_df = doc_context
            status = "Answer generated" if answer else "Context retrieved, no AI answer available"
            result_text = answer if answer else "Retrieved graph and document context is shown below"
            fig = plot_graph(graph, kg_matches if kg_matches else None, title="Graph RAG Result")
        elif algo == "Agentic Search":
            trace = agentic_search(corpus_df, query)
            table_df = pd.DataFrame(trace)
            status = "Agent finished searching"
            result_text = "The agent ran " + str(len(trace)) + " search iterations, refining its query each time"
            fig = plot_bar([str(t["Iteration"]) for t in trace], [t["Score"] for t in trace], "Agentic Search Score by Iteration", "Iteration", "Top score")
        elif algo == "Multi Step Search":
            trace = multi_step_search(corpus_df, query)
            table_df = pd.DataFrame(trace)
            status = "Multi step search finished"
            result_text = "The search chained through " + str(len(trace)) + " steps"
            fig = None
        elif algo == "Query Expansion":
            result, expansions, note = query_expansion_search(corpus_df, query, api_provider, api_key)
            details = [note, "Expansion terms used: " + (", ".join(expansions) if expansions else "none")]
            table_df = result
            status = "Search complete"
            result_text = "Top document after expansion: " + (result.iloc[0]["DocID"] if len(result) else "none")
        else:
            result, note = semantic_reranking_search(corpus_df, query, api_provider, api_key)
            details = [note]
            table_df = result
            status = "Reranking complete"
            result_text = "Top document after reranking: " + (result.iloc[0]["DocID"] if len(result) else "none")

        st.session_state["cat10_output"] = dict(status=status, result_text=result_text, details=details,
                                                 table_df=table_df, fig=fig, params=params,
                                                 explanation=explanations[algo], algo=algo)

    if "cat10_output" in st.session_state and st.session_state["cat10_output"]["algo"] == algo:
        o = st.session_state["cat10_output"]
        render_result_and_export("cat10_" + algo.replace(" ", "_"), "Modern AI and LLM Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

def render_category_11():
    st.header("11. Probabilistic Search")
    st.write("These techniques rank or sample records according to probability, useful when information is uncertain rather than exact.")
    algo = st.selectbox("Choose a technique", [
        "Probabilistic Search", "Bayesian Search", "Monte Carlo Search", "Particle Filtering",
    ], key="cat11_algo")

    explanations = {
        "Probabilistic Search": (
            "Ranks records by a precomputed probability field, returning only those above a chosen threshold.\n\n"
            "**When to use:** Use it when each record already carries a meaningful probability estimate and you simply need to filter or rank by it.\n\n"
            "**Benefits:** Very fast and simple since it only requires filtering and sorting, no modeling step needed.\n\n"
            "**Important use-cases:** Filtering alerts or records to only those above a confidence or likelihood threshold, such as high probability exploit records."
        ),
        "Bayesian Search": (
            "Starts from a prior probability for each record, combines it with a simulated likelihood based on new evidence, and computes an updated posterior probability using Bayes rule.\n\n"
            "**When to use:** Use it when new evidence should update an existing belief rather than replace it outright, formally combining prior knowledge with new observations.\n\n"
            "**Benefits:** Provides a principled, mathematically grounded way to combine prior knowledge with new evidence, rather than treating each new fact in isolation.\n\n"
            "**Important use-cases:** Updating the likelihood that a record represents a true incident as new evidence arrives, and any belief revision task with prior knowledge."
        ),
        "Monte Carlo Search": (
            "Repeatedly samples records at random, weighted by their probability, and counts how often each record is drawn to build an estimate of its true relative importance.\n\n"
            "**When to use:** Use it when you want to empirically estimate relative importance or likelihood through repeated random sampling rather than closed form computation.\n\n"
            "**Benefits:** Works even when an exact analytical computation is difficult, and the estimate improves as more trials are run.\n\n"
            "**Important use-cases:** Estimating the relative importance of risk factors through simulation, and validating a probability model by empirical sampling."
        ),
        "Particle Filtering": (
            "Maintains a population of weighted particles representing possible states, and repeatedly reweights and normalizes them as new noisy evidence arrives.\n\n"
            "**When to use:** Use it when tracking a state that evolves over time under noisy or uncertain observations, and a single point estimate is not enough.\n\n"
            "**Benefits:** Naturally represents a whole distribution of possible states rather than a single guess, and adapts as new noisy evidence arrives.\n\n"
            "**Important use-cases:** Tracking the evolving likelihood of a security state under a stream of uncertain signals, and other sequential state estimation problems."
        ),
    }
    st.write(explanations[algo])

    render_schema_section([("Record Schema", TABLE_SCHEMA)])
    table_df = table_domain_ui("cat11_" + algo.replace(" ", "_"))
    if table_df is None:
        st.info("Provide data above to continue")
        return

    seed = st.number_input("Random seed", 1, 9999, _default_seed(), key="cat11_seed")
    extra_params = {}
    if algo == "Probabilistic Search":
        extra_params["threshold"] = st.slider("Probability threshold", 0.0, 1.0, 0.5, step=0.05, key="cat11_threshold")
    if algo == "Monte Carlo Search":
        extra_params["trials"] = st.slider("Number of simulation trials", 100, 5000, 1000, step=100, key="cat11_trials")
    if algo == "Particle Filtering":
        extra_params["iterations"] = st.slider("Number of update iterations", 1, 20, 5, key="cat11_iters")

    if st.button("Run " + algo, key="cat11_run"):
        params = {"Total records": len(table_df), "Random seed": seed}
        params.update(extra_params)
        if algo == "Probabilistic Search":
            result = probabilistic_search(table_df, extra_params["threshold"])
            score_col = "Probability"
        elif algo == "Bayesian Search":
            result = bayesian_search(table_df, seed)
            score_col = "Posterior"
        elif algo == "Monte Carlo Search":
            result = monte_carlo_search(table_df, seed, extra_params["trials"])
            score_col = "Simulated_Frequency"
        else:
            result = particle_filtering_search(table_df, seed, extra_params["iterations"])
            score_col = "Particle_Weight"

        status = "Search complete"
        result_text = "Top ranked record has " + score_col + " of " + str(round(float(result.iloc[0][score_col]), 4)) if len(result) else "No records available"
        top = result.head(10)
        fig = plot_bar(top["RecordID"].astype(str).tolist(), top[score_col].tolist(), algo + " Top Records", "Record ID", score_col) if len(result) else None
        st.session_state["cat11_output"] = dict(status=status, result_text=result_text, details=[],
                                                 table_df=result, fig=fig, params=params,
                                                 explanation=explanations[algo], algo=algo)

    if "cat11_output" in st.session_state and st.session_state["cat11_output"]["algo"] == algo:
        o = st.session_state["cat11_output"]
        render_result_and_export("cat11_" + algo.replace(" ", "_"), "Probabilistic Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_12():
    st.header("12. Distributed and Large Scale Search")
    st.write("These techniques simulate splitting a search problem across multiple workers or sources, the way a large scale enterprise system would.")
    algo = st.selectbox("Choose a technique", [
        "Distributed Search", "Parallel Search", "Federated Search", "MapReduce Search", "Distributed Graph Search",
    ], key="cat12_algo")

    explanations = {
        "Distributed Search": (
            "Splits the record table into partitions, one per simulated worker, and each worker searches only its own partition before results are combined.\n\n"
            "**When to use:** Use it when a table is too large for a single sequential scan to be efficient and can be naturally divided among workers.\n\n"
            "**Benefits:** Reduces the work any single worker must do by dividing the table, illustrating how horizontal scaling speeds up search.\n\n"
            "**Important use-cases:** Searching very large record sets that are naturally partitioned, such as by region or business unit, across multiple nodes."
        ),
        "Parallel Search": (
            "Similar to Distributed Search, but also simulates a processing time for each worker, showing how the total completion time under parallel execution compares to running everything sequentially.\n\n"
            "**When to use:** Use it when you need to reason about or demonstrate the time savings of parallel execution, not just the logical partitioning.\n\n"
            "**Benefits:** Makes the real world speed benefit of parallelism visible and measurable, not just conceptual.\n\n"
            "**Important use-cases:** Capacity planning and demonstrating expected speedup from adding more parallel workers to a search workload."
        ),
        "Federated Search": (
            "Treats each partition as an independent data source with its own identity, searching all sources and merging the results while keeping track of which source each result came from.\n\n"
            "**When to use:** Use it when data genuinely lives in separate, independently owned systems and provenance of each result must be preserved.\n\n"
            "**Benefits:** Preserves source identity and ownership boundaries while still providing a single unified search experience.\n\n"
            "**Important use-cases:** Searching across independently owned business unit systems or vendor data sources while tracking where each result originated."
        ),
        "MapReduce Search": (
            "Applies a map phase that counts values per partition, then a reduce phase that aggregates those partial counts into a single combined total, mirroring the MapReduce programming model.\n\n"
            "**When to use:** Use it for aggregation style questions, such as totals or counts, over very large partitioned datasets, rather than simple record retrieval.\n\n"
            "**Benefits:** Scales aggregation computations naturally across many partitions, following a well understood, proven programming model.\n\n"
            "**Important use-cases:** Computing enterprise wide totals or counts across many partitioned data sources, such as total events per category."
        ),
        "Distributed Graph Search": (
            "Partitions the nodes of a graph across simulated workers and runs a search, counting how many times the path has to cross from one worker's partition to another.\n\n"
            "**When to use:** Use it when the graph itself is too large for one machine and understanding cross-partition traversal cost matters.\n\n"
            "**Benefits:** Surfaces the hidden cost of cross-partition edges, which is a key consideration when designing large scale distributed graph systems.\n\n"
            "**Important use-cases:** Planning how to partition a very large enterprise graph across systems, and understanding the overhead of cross-partition relationship traversal."
        ),
    }
    st.write(explanations[algo])

    if algo == "Distributed Graph Search":
        render_schema_section([("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
        nodes_df, edges_df, graph = graph_domain_ui("cat12_" + algo.replace(" ", "_"))
        if graph is None:
            st.info("Provide data above to continue")
            return
        node_ids = list(nodes_df["ID"])
        c1, c2, c3 = st.columns(3)
        with c1:
            start = st.selectbox("Start node", node_ids, key="cat12_start")
        with c2:
            goal = st.selectbox("Goal node", node_ids, index=min(len(node_ids) - 1, 1), key="cat12_goal")
        with c3:
            num_workers = st.slider("Number of workers", 2, 8, 3, key="cat12_workers")
        seed = st.number_input("Random seed", 1, 9999, _default_seed(), key="cat12_seed")

        if st.button("Run " + algo, key="cat12_run"):
            path, hops, worker_counts, visited = distributed_graph_search(graph, start, goal, num_workers, seed)
            params = {"Start node": start, "Goal node": goal, "Number of workers": num_workers}
            status = "Path found" if path else "No path found"
            result_text = ("Path: " + " then ".join(path) + ". Cross partition hops: " + str(hops)) if path else "No path exists"
            fig = plot_graph(graph, path, title=algo + " Result")
            st.session_state["cat12_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=worker_counts, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
        if "cat12_output" in st.session_state and st.session_state["cat12_output"]["algo"] == algo:
            o = st.session_state["cat12_output"]
            render_result_and_export("cat12_" + algo.replace(" ", "_"), "Distributed and Large Scale Search", algo,
                                      o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                      o["table_df"], o["fig"])
        return

    render_schema_section([("Record Schema", TABLE_SCHEMA)])
    table_df = table_domain_ui("cat12_" + algo.replace(" ", "_"))
    if table_df is None:
        st.info("Provide data above to continue")
        return

    all_fields = list(table_df.columns)
    if algo == "MapReduce Search":
        field = st.selectbox("Category field to aggregate", [c for c in all_fields if table_df[c].dtype == object], key="cat12_field")
        num_workers = st.slider("Number of workers", 2, 10, 4, key="cat12_workers")
    else:
        field = st.selectbox("Field to search", all_fields, key="cat12_field")
        value = st.text_input("Value to search for", str(table_df[field].iloc[0]), key="cat12_value")
        num_workers = st.slider("Number of workers or sources", 2, 10, 4, key="cat12_workers")
    seed = st.number_input("Random seed", 1, 9999, _default_seed(), key="cat12_seed")

    if st.button("Run " + algo, key="cat12_run"):
        details = []
        if algo == "Distributed Search":
            params = {"Field": field, "Value": value, "Number of workers": num_workers}
            combined, worker_stats = distributed_search(table_df, field, value, num_workers)
            table_df_out = worker_stats
            result_text = "Total matches across all workers: " + str(len(combined))
        elif algo == "Parallel Search":
            params = {"Field": field, "Value": value, "Number of workers": num_workers}
            combined, timings, ptime, stime = parallel_search(table_df, field, value, num_workers, seed)
            table_df_out = timings
            result_text = ("Total matches: " + str(len(combined)) + ". Simulated parallel completion time: " +
                            str(round(ptime, 3)) + " seconds versus sequential time of " + str(round(stime, 3)) + " seconds")
        elif algo == "Federated Search":
            params = {"Field": field, "Value": value, "Number of sources": num_workers}
            merged = federated_search(table_df, field, value, num_workers)
            table_df_out = merged
            result_text = "Total matches merged across all sources: " + str(len(merged))
        else:
            params = {"Category field": field, "Number of workers": num_workers}
            map_df, reduce_df = mapreduce_search(table_df, field, num_workers)
            table_df_out = reduce_df
            result_text = "Reduce phase produced " + str(len(reduce_df)) + " aggregated category totals"
            details.append("Map phase produced " + str(len(map_df)) + " partial counts across all workers")

        status = "Search complete"
        fig = plot_bar(table_df_out.iloc[:, 0].astype(str).tolist()[:10], table_df_out.iloc[:, -1].tolist()[:10], algo + " Result", "", "") if len(table_df_out) else None
        st.session_state["cat12_output"] = dict(status=status, result_text=result_text, details=details,
                                                 table_df=table_df_out, fig=fig, params=params,
                                                 explanation=explanations[algo], algo=algo)

    if "cat12_output" in st.session_state and st.session_state["cat12_output"]["algo"] == algo:
        o = st.session_state["cat12_output"]
        render_result_and_export("cat12_" + algo.replace(" ", "_"), "Distributed and Large Scale Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])


def render_category_13():
    st.header("13. Cybersecurity Search")
    st.write("These techniques apply search directly to security use cases inside the Kalsnet Hub, from indicator lookups to attack path tracing.")
    algo = st.selectbox("Choose a technique", [
        "IOC Search", "Threat Hunting Search", "Attack Path Search", "Graph Based Threat Search",
        "Anomaly Search", "Vulnerability Search", "SIEM Query Search", "SOAR Playbook Search",
    ], key="cat13_algo")

    explanations = {
        "IOC Search": (
            "Searches event records for a known indicator of compromise, such as a specific IP address or file hash.\n\n"
            "**When to use:** Use it when you already have a specific known-bad indicator, such as a malicious IP or file hash from a threat feed, and need to check for it in your own event data.\n\n"
            "**Benefits:** Fast, precise, and directly actionable, since a match against a known indicator is high confidence evidence.\n\n"
            "**Important use-cases:** Checking newly published threat intelligence indicators against historical event logs, and confirming whether a known-bad artifact touched the environment."
        ),
        "Threat Hunting Search": (
            "Proactively searches event records for a suspicious combination of attributes, such as a high risk score occurring during an unusual hour of the day.\n\n"
            "**When to use:** Use it proactively, before any specific alert exists, to look for suspicious patterns that automated rules might not catch.\n\n"
            "**Benefits:** Surfaces suspicious activity that does not match any known indicator, catching novel or previously unseen threats.\n\n"
            "**Important use-cases:** Proactive hunting for insider threats or novel attacker behavior, and validating that monitoring coverage catches unusual combinations of activity."
        ),
        "Attack Path Search": (
            "Traces a possible attack chain from a compromised endpoint to a sensitive target by performing a depth first search across the enterprise Knowledge Graph.\n\n"
            "**When to use:** Use it after identifying a compromised or at-risk starting point, to understand how far an attacker could reach and what they could reach it through.\n\n"
            "**Benefits:** Reveals a concrete, traceable chain of relationships an attacker could exploit, turning an abstract risk into a specific actionable path.\n\n"
            "**Important use-cases:** Incident response scoping from a known compromised endpoint, and red team or tabletop exercises tracing plausible attack chains."
        ),
        "Graph Based Threat Search": (
            "Performs a bounded breadth first search from a starting node, flagging every node reached within a limited number of hops whose risk score meets or exceeds a threshold.\n\n"
            "**When to use:** Use it to find every risky asset within a bounded blast radius of a starting point, rather than tracing a single path.\n\n"
            "**Benefits:** Efficiently surfaces every at-risk asset within a defined proximity, giving a fuller picture than a single attack path alone.\n\n"
            "**Important use-cases:** Assessing blast radius around a compromised or high risk asset, and prioritizing containment around the riskiest nearby nodes."
        ),
        "Anomaly Search": (
            "Computes a z-score for each record relative to the mean and standard deviation of a numeric field, flagging records that deviate significantly from normal behavior.\n\n"
            "**When to use:** Use it when there is no known indicator to search for, but a numeric field's typical range is well understood and outliers are suspicious.\n\n"
            "**Benefits:** Statistically grounded and catches unusual behavior automatically, without needing predefined rules or known indicators.\n\n"
            "**Important use-cases:** Flagging unusually large transactions or unusual access counts, and general purpose outlier detection across numeric security metrics."
        ),
        "Vulnerability Search": (
            "Searches the Knowledge Graph nodes for assets whose security score falls below an acceptable threshold.\n\n"
            "**When to use:** Use it to proactively identify weak points in the environment before they are exploited, based on an existing security posture score.\n\n"
            "**Benefits:** Directly surfaces the weakest assets by score, making prioritization of remediation straightforward.\n\n"
            "**Important use-cases:** Prioritizing patching and hardening efforts, and periodic posture reviews to catch assets that have drifted below acceptable standards."
        ),
        "SIEM Query Search": (
            "Parses a simple query language, similar to a SIEM search query, with field comparisons joined by AND, and applies it to event records.\n\n"
            "**When to use:** Use it when analysts need to build custom, precise, multi-condition queries against event data, similar to querying a real SIEM.\n\n"
            "**Benefits:** Flexible and precise, letting analysts combine multiple conditions in one query rather than being limited to a single fixed search.\n\n"
            "**Important use-cases:** Ad hoc security investigations with multiple conditions, and mimicking real SIEM query workflows for training or demonstration."
        ),
        "SOAR Playbook Search": (
            "Scores a set of predefined remediation playbooks by a weighted combination of cost, risk, and time, and recommends the lowest combined score playbook, similar to automated SOAR playbook selection.\n\n"
            "**When to use:** Use it once a threat or incident is identified and you need to decide which remediation playbook to execute, balancing multiple competing factors.\n\n"
            "**Benefits:** Provides a consistent, explainable, weighted basis for choosing a remediation action instead of an ad hoc decision.\n\n"
            "**Important use-cases:** Automated or semi-automated incident response playbook selection, and comparing remediation options by cost, risk, and time trade-offs."
        ),
    }
    st.write(explanations[algo])

    if algo in ("Attack Path Search", "Graph Based Threat Search", "Vulnerability Search"):
        render_schema_section([("Node Schema", NODE_SCHEMA), ("Edge Schema", EDGE_SCHEMA)])
        nodes_df, edges_df, graph = graph_domain_ui("cat13_" + algo.replace(" ", "_"))
        if graph is None:
            st.info("Provide data above to continue")
            return

        if algo == "Attack Path Search":
            node_ids = list(nodes_df["ID"])
            c1, c2 = st.columns(2)
            with c1:
                start = st.selectbox("Compromised endpoint (start)", node_ids, key="cat13_start")
            with c2:
                goal = st.selectbox("Sensitive target (goal)", node_ids, index=min(len(node_ids) - 1, 1), key="cat13_goal")
            if st.button("Run " + algo, key="cat13_run"):
                path, visited = attack_path_search(graph, start, goal)
                params = {"Start node": start, "Goal node": goal}
                status = "Attack path found" if path else "No attack path found"
                result_text = ("Possible attack path: " + " then ".join(path)) if path else "No path exists between the selected nodes"
                fig = plot_graph(graph, path, title="Attack Path Search Result")
                table_df = nodes_df[nodes_df["ID"].isin(path)] if path else None
                st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                         table_df=table_df, fig=fig, params=params,
                                                         explanation=explanations[algo], algo=algo)
        elif algo == "Graph Based Threat Search":
            node_ids = list(nodes_df["ID"])
            c1, c2, c3 = st.columns(3)
            with c1:
                start = st.selectbox("Starting node", node_ids, key="cat13_start2")
            with c2:
                risk_threshold = st.slider("Risk threshold", 0, 10, 6, key="cat13_risk")
            with c3:
                max_hops = st.slider("Maximum hops", 1, 6, 3, key="cat13_hops")
            if st.button("Run " + algo, key="cat13_run"):
                flagged, visited = graph_based_threat_search(graph, start, risk_threshold, max_hops)
                params = {"Start node": start, "Risk threshold": risk_threshold, "Max hops": max_hops}
                status = "Flagged nodes found" if flagged else "No nodes met the risk threshold within range"
                result_text = "Nodes flagged: " + str(len(flagged))
                table_df = pd.DataFrame(flagged, columns=["Node", "Hops_From_Start"]) if flagged else None
                fig = plot_graph(graph, [f[0] for f in flagged] if flagged else None, title="Graph Based Threat Search Result")
                st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                         table_df=table_df, fig=fig, params=params,
                                                         explanation=explanations[algo], algo=algo)
        else:
            score_threshold = st.slider("Security score threshold", 0, 100, 40, key="cat13_score")
            if st.button("Run " + algo, key="cat13_run"):
                result = vulnerability_search(nodes_df, score_threshold)
                params = {"Security score threshold": score_threshold}
                status = "Vulnerable assets found" if len(result) else "No vulnerable assets found"
                result_text = "Assets below the security score threshold: " + str(len(result))
                fig = plot_bar(["Total assets", "Vulnerable assets"], [len(nodes_df), len(result)], "Vulnerability Search Result", "", "Asset count")
                st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                         table_df=result, fig=fig, params=params,
                                                         explanation=explanations[algo], algo=algo)

        if "cat13_output" in st.session_state and st.session_state["cat13_output"]["algo"] == algo:
            o = st.session_state["cat13_output"]
            render_result_and_export("cat13_" + algo.replace(" ", "_"), "Cybersecurity Search", algo,
                                      o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                      o["table_df"], o["fig"])
        return

    if algo == "SOAR Playbook Search":
        with st.expander("View Data Schema"):
            st.write("This technique uses a fixed set of predefined remediation playbooks, each with a Cost, Risk, and Time estimate, rather than uploaded or generated records.")
        c1, c2, c3 = st.columns(3)
        with c1:
            wc = st.slider("Cost weight", 0.0, 3.0, 1.0, step=0.1, key="cat13_wc")
        with c2:
            wr = st.slider("Risk weight", 0.0, 3.0, 1.0, step=0.1, key="cat13_wr")
        with c3:
            wt = st.slider("Time weight", 0.0, 3.0, 1.0, step=0.1, key="cat13_wt")
        if st.button("Run " + algo, key="cat13_run"):
            result = soar_playbook_search(wc, wr, wt)
            params = {"Cost weight": wc, "Risk weight": wr, "Time weight": wt}
            status = "Recommendation ready"
            result_text = "Recommended playbook: " + result.iloc[0]["Name"] + " with combined score " + str(result.iloc[0]["Combined_Score"])
            fig = plot_bar(result["Name"].tolist(), result["Combined_Score"].tolist(), "SOAR Playbook Combined Score", "Playbook", "Combined score")
            st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=result, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
        if "cat13_output" in st.session_state and st.session_state["cat13_output"]["algo"] == algo:
            o = st.session_state["cat13_output"]
            render_result_and_export("cat13_" + algo.replace(" ", "_"), "Cybersecurity Search", algo,
                                      o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                      o["table_df"], o["fig"])
        return

    render_schema_section([("Record Schema", TABLE_SCHEMA)])
    table_df = table_domain_ui("cat13_" + algo.replace(" ", "_"))
    if table_df is None:
        st.info("Provide data above to continue")
        return

    if algo == "IOC Search":
        ioc_type = st.selectbox("Indicator type", ["IP Address", "File Hash"], key="cat13_ioctype")
        field = "IP_Address" if ioc_type == "IP Address" else "File_Hash"
        ioc_value = st.selectbox("Indicator value", list(table_df[field].unique()), key="cat13_iocvalue")
        if st.button("Run " + algo, key="cat13_run"):
            result = ioc_search(table_df, ioc_type, ioc_value)
            params = {"Indicator type": ioc_type, "Indicator value": ioc_value}
            status = "Matches found" if len(result) else "No matches found"
            result_text = "Records matching this indicator: " + str(len(result))
            fig = plot_bar(["Total records", "Matches"], [len(table_df), len(result)], algo + " Result", "", "Record count")
            st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=result, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
    elif algo == "Threat Hunting Search":
        c1, c2, c3 = st.columns(3)
        with c1:
            risk_threshold = st.slider("Risk score threshold", 0, 100, 70, key="cat13_thrisk")
        with c2:
            hour_start = st.slider("Odd hour range start", 0, 23, 0, key="cat13_hs")
        with c3:
            hour_end = st.slider("Odd hour range end", 0, 23, 5, key="cat13_he")
        if st.button("Run " + algo, key="cat13_run"):
            result = threat_hunting_search(table_df, risk_threshold, hour_start, hour_end)
            params = {"Risk threshold": risk_threshold, "Hour range": str(hour_start) + " to " + str(hour_end)}
            status = "Suspicious records found" if len(result) else "No suspicious records found"
            result_text = "Suspicious records identified: " + str(len(result))
            fig = plot_bar(["Total records", "Suspicious"], [len(table_df), len(result)], algo + " Result", "", "Record count")
            st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=result, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
    elif algo == "Anomaly Search":
        numeric_fields = [c for c in table_df.columns if pd.api.types.is_numeric_dtype(table_df[c])]
        field = st.selectbox("Numeric field to analyze", numeric_fields, key="cat13_anomfield")
        z_threshold = st.slider("Z-score threshold", 1.0, 4.0, 2.0, step=0.1, key="cat13_z")
        if st.button("Run " + algo, key="cat13_run"):
            result, mean, std = anomaly_search(table_df, field, z_threshold)
            params = {"Field": field, "Z-score threshold": z_threshold}
            status = "Anomalies found" if len(result) else "No anomalies found"
            result_text = "Anomalies detected: " + str(len(result)) + ". Field mean: " + str(round(mean, 2)) + ", standard deviation: " + str(round(std, 2))
            fig = plot_bar(["Total records", "Anomalies"], [len(table_df), len(result)], algo + " Result", "", "Record count")
            st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=result, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)
    else:
        query = st.text_input("SIEM style query, example Risk_Score > 50 AND Country = USA",
                               "Risk_Score > 50 AND Country = USA", key="cat13_siemq")
        if st.button("Run " + algo, key="cat13_run"):
            result, applied = siem_query_search(table_df, query)
            params = {"Query": query}
            status = "Query executed"
            result_text = "Filters applied: " + (", ".join(applied) if applied else "none") + ". Matching records: " + str(len(result))
            fig = plot_bar(["Total records", "Matches"], [len(table_df), len(result)], algo + " Result", "", "Record count")
            st.session_state["cat13_output"] = dict(status=status, result_text=result_text, details=[],
                                                     table_df=result, fig=fig, params=params,
                                                     explanation=explanations[algo], algo=algo)

    if "cat13_output" in st.session_state and st.session_state["cat13_output"]["algo"] == algo:
        o = st.session_state["cat13_output"]
        render_result_and_export("cat13_" + algo.replace(" ", "_"), "Cybersecurity Search", algo,
                                  o["explanation"], o["params"], o["status"], o["result_text"], o["details"],
                                  o["table_df"], o["fig"])

# ---------------------------------------------------------------------------
# Main application entry point
# ---------------------------------------------------------------------------

def main():
    apply_page_style()
    category, api_provider, api_key = render_sidebar()

    if category.startswith("1."):
        render_category_1()
    elif category.startswith("2."):
        render_category_2()
    elif category.startswith("3."):
        render_category_3()
    elif category.startswith("4."):
        render_category_4()
    elif category.startswith("5."):
        render_category_5()
    elif category.startswith("6."):
        render_category_6()
    elif category.startswith("7."):
        render_category_7()
    elif category.startswith("8."):
        render_category_8()
    elif category.startswith("9."):
        render_category_9()
    elif category.startswith("10."):
        render_category_10(api_provider, api_key)
    elif category.startswith("11."):
        render_category_11()
    elif category.startswith("12."):
        render_category_12()
    else:
        render_category_13()


if __name__ == "__main__":
    main()
