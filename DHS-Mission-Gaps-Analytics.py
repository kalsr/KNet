


# Homeland Security Mission Gap Analytics Suite
# Developed by Randy Singh from Kalsnet (KNet) Consulting Group

# Purpose
   # One Streamlit application with eight decision support modules, each aimed at
   # a homeland security gap documented by GAO, the Intelligence Community or
   # security analysts:
   #     1  Critical infrastructure cyber risk monitor
   #     2  Counter drone incident tracker
   #     3  Disaster aid navigator
   #     4  Border security metrics quality dashboard
   #     5  Acquisition program health tracker
   #     6  Open recommendations tracker
   #     7  Deepfake and impersonation verification
   #     8  Facility insider threat and supply chain checklist

   # Every module supports synthetic data, real CSV uploads, an explained scoring
   # model, flowcharts, a field dictionary and exports to CSV, text, Word and PDF.


# Important note
#   This is a prototype. Weights, thresholds, program rules and deadlines are
#   illustrative starting points and must be validated against official policy
#   and tuned by the responsible office before operational use.


import io
import math
import datetime

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

try:
    import docx
    HAVE_DOCX = True
except ImportError:
    HAVE_DOCX = False

try:
    from pypdf import PdfReader
    HAVE_PYPDF = True
except ImportError:
    HAVE_PYPDF = False

try:
    from fpdf import FPDF
    HAVE_FPDF = True
except ImportError:
    HAVE_FPDF = False


APP_TITLE = "Homeland Security Mission Gap Analytics Suite"
APP_SUBTITLE = "Developed by Randy Singh from Kalsnet (KNet) Consulting Group"
TODAY = datetime.date.today()


# ==========================================================================
# Shared helpers
# ==========================================================================

def F(name, kind, meaning, relevance, default, options=None):
    """Describe one field. Kinds: text, cat, int, num, num01, numblank, yesno, date."""
    return {"name": name, "kind": kind, "meaning": meaning, "relevance": relevance,
            "default": default, "options": options}


def clip01(series):
    return series.astype(float).clip(lower=0.0, upper=1.0)


def is_yes(series):
    return series.astype(str).str.strip().str.lower().isin(["yes", "true", "1", "y"])


def band(series, cuts, labels):
    """Assign labels by descending cut points. cuts has one fewer item than labels."""
    out = []
    for value in series:
        label = labels[-1]
        for cut, name in zip(cuts, labels):
            if value >= cut:
                label = name
                break
        out.append(label)
    return out


def clean_upload(frame, fields):
    """Coerce an uploaded table to the module schema and fill safe defaults."""
    frame = frame.copy()
    frame.columns = [str(c).strip().lower().replace(" ", "_") for c in frame.columns]
    missing = []
    for f in fields:
        name = f["name"]
        if name not in frame.columns:
            missing.append(name)
            if f["kind"] == "text" and name.endswith("_id"):
                frame[name] = [f"ROW{i + 1}" for i in range(len(frame))]
            else:
                frame[name] = f["default"]
        kind = f["kind"]
        if kind == "int":
            frame[name] = pd.to_numeric(frame[name], errors="coerce").fillna(
                f["default"]).astype(int)
        elif kind == "num":
            frame[name] = pd.to_numeric(frame[name], errors="coerce").fillna(f["default"])
        elif kind == "numblank":
            frame[name] = pd.to_numeric(frame[name], errors="coerce")
        elif kind == "num01":
            frame[name] = clip01(pd.to_numeric(frame[name], errors="coerce").fillna(
                f["default"]))
        elif kind == "yesno":
            frame[name] = np.where(is_yes(frame[name]), "Yes", "No")
        elif kind == "cat":
            lookup = {o.lower(): o for o in f["options"]}
            frame[name] = frame[name].astype(str).str.strip().str.lower().map(
                lookup).fillna(f["default"])
        elif kind == "date":
            parsed = pd.to_datetime(frame[name], errors="coerce")
            frame[name] = parsed.dt.date.astype(str).where(parsed.notna(), str(f["default"]))
        else:
            frame[name] = frame[name].astype(str)
    return frame, missing


def read_uploaded_document(uploaded):
    name = uploaded.name.lower()
    data = uploaded.getvalue()
    if name.endswith(".csv"):
        return "table", pd.read_csv(io.BytesIO(data))
    if name.endswith(".txt"):
        return "text", data.decode("utf-8", errors="replace")
    if name.endswith(".pdf"):
        if not HAVE_PYPDF:
            return "text", "Install pypdf to read PDF files."
        reader = PdfReader(io.BytesIO(data))
        return "text", "\n\n".join(f"Page {i + 1}\n{p.extract_text() or ''}"
                                   for i, p in enumerate(reader.pages))
    if name.endswith(".docx"):
        if not HAVE_DOCX:
            return "text", "Install python-docx to read Word files."
        document = docx.Document(io.BytesIO(data))
        text = "\n".join(p.text for p in document.paragraphs if p.text.strip())
        tables = []
        for table in document.tables:
            grid = [[c.text for c in r.cells] for r in table.rows]
            if len(grid) > 1:
                tables.append(pd.DataFrame(grid[1:], columns=grid[0]))
        return "docx", (text, tables)
    return "text", "Unsupported file type."


def latin(text):
    return str(text).encode("latin-1", errors="replace").decode("latin-1")


def summary_lines(module, scored):
    lines = [APP_TITLE, APP_SUBTITLE, f"Module: {module['title']}",
             f"Report generated: {datetime.datetime.now():%Y-%m-%d %H:%M}", "",
             f"Records assessed: {len(scored)}",
             f"Average {module['score_label'].lower()}: "
             f"{scored[module['score_col']].mean():.1f}"]
    counts = scored[module["band_col"]].value_counts().to_dict()
    for label in module["band_labels"]:
        lines.append(f"{label}: {counts.get(label, 0)}")
    return lines


def export_txt(module, scored):
    lines = summary_lines(module, scored) + ["", "Records"]
    for _, r in scored.iterrows():
        lines.append(" | ".join(str(r[c]) for c in module["report_cols"]))
    return "\n".join(lines).encode("utf-8")


def export_docx(module, scored):
    document = docx.Document()
    lines = summary_lines(module, scored)
    document.add_heading(lines[0], level=0)
    document.add_paragraph(lines[1])
    document.add_heading(lines[2], level=1)
    for line in lines[3:]:
        if line:
            document.add_paragraph(line)
    document.add_heading("Records", level=1)
    cols = module["report_cols"]
    table = document.add_table(rows=1, cols=len(cols))
    table.style = "Light Grid Accent 1"
    for i, col in enumerate(cols):
        table.rows[0].cells[i].text = col.replace("_", " ").title()
    for _, r in scored.iterrows():
        cells = table.add_row().cells
        for i, col in enumerate(cols):
            cells[i].text = str(r[col])
    buffer = io.BytesIO()
    document.save(buffer)
    return buffer.getvalue()


def export_pdf(module, scored):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()
    pdf.set_text_color(13, 71, 161)
    pdf.set_font("Helvetica", "B", 17)
    pdf.cell(0, 10, latin(APP_TITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, latin(APP_SUBTITLE), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, latin(f"Module: {module['title']}"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    for line in summary_lines(module, scored)[3:]:
        pdf.cell(0, 5, latin(line), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    cols = module["report_cols"]
    width = 277.0 / len(cols)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(227, 236, 250)
    for col in cols:
        pdf.cell(width, 7, latin(col.replace("_", " ").title())[: int(width / 1.6)],
                 border=1, fill=True)
    pdf.ln()
    pdf.set_font("Helvetica", "", 7)
    limit = int(width / 1.5)
    for _, r in scored.iterrows():
        for col in cols:
            value = latin(r[col])
            if len(value) > limit:
                value = value[: limit - 2] + ".."
            pdf.cell(width, 5.5, value, border=1)
        pdf.ln()
    return bytes(pdf.output())


DOT_STYLE = """
    graph [rankdir=LR, bgcolor=transparent, fontname=Helvetica, nodesep=0.35];
    node  [shape=box, style="rounded,filled", fillcolor="#E3ECFA", color="#0D47A1",
           fontname=Helvetica, fontsize=11];
    edge  [color="#0D47A1", fontname=Helvetica, fontsize=10];
"""


def flow(*steps, highlight=None):
    """Build a left to right flowchart from a list of step labels."""
    highlight = highlight or []
    nodes = []
    for i, label in enumerate(steps):
        fill = ', fillcolor="#BBDEFB"' if i in highlight else ""
        nodes.append(f'N{i} [label="{label}"{fill}];')
    edges = " -> ".join(f"N{i}" for i in range(len(steps))) + ";"
    return "digraph G {" + DOT_STYLE + " ".join(nodes) + edges + "}"


# ==========================================================================
# Module 1  Critical infrastructure cyber risk monitor
# ==========================================================================

SECTORS = ["Energy", "Water", "Healthcare", "Communications", "Transportation"]
SECTOR_WEIGHT = {"Energy": 1.0, "Water": 1.0, "Healthcare": 0.9,
                 "Communications": 0.8, "Transportation": 0.8}

CYBER_FIELDS = [
    F("facility_id", "text", "Unique facility identifier", "Links findings to one site", "F0"),
    F("facility_name", "text", "Facility or utility name", "Readable label for reports", "Unknown"),
    F("sector", "cat", ", ".join(SECTORS), "Sets the consequence weight of an attack",
      "Energy", SECTORS),
    F("exposed_services", "int", "Internet facing services found by scanning",
      "Each exposed service is a door an attacker can try", 0),
    F("kev_vulns", "int", "Known exploited vulnerabilities present",
      "Flaws attackers are actively using right now, weighted heavily", 0),
    F("critical_vulns", "int", "Other critical severity vulnerabilities",
      "Serious flaws not yet seen in active exploitation", 0),
    F("patch_age_days", "int", "Average age of missing patches in days",
      "Slow patching keeps known flaws open longer", 0),
    F("mfa_coverage", "num01", "Share of remote and admin accounts with multifactor login",
      "Multifactor login blocks most stolen password attacks", 0.0),
    F("backup_tested", "yesno", "Restore from backup tested in the last year",
      "Tested backups decide whether ransomware is an outage or a disaster", "No"),
    F("incidents_12m", "int", "Security incidents reported in the last 12 months",
      "Past incidents signal targeting and control weaknesses", 0),
    F("population_served", "int", "People who depend on the facility",
      "Scales the human consequence of disruption", 1000),
]

CYBER_ACTIONS = {"E": "Reduce internet exposed services",
                 "V": "Patch known exploited vulnerabilities",
                 "P": "Shorten the patch cycle",
                 "C": "Expand multifactor login",
                 "B": "Test backup restoration",
                 "H": "Review incident lessons learned"}
CYBER_W = {"E": 0.20, "V": 0.30, "P": 0.15, "C": 0.15, "B": 0.10, "H": 0.10}


def cyber_generate(n, seed):
    rng = np.random.default_rng(seed)
    towns = ["Riverton", "Lakeview", "Fairmont", "Cedar Falls", "Brookhaven", "Oak Ridge",
             "Pine Bluff", "Westfield", "Granite City", "Harbor Point"]
    kinds = {"Energy": "Power Co", "Water": "Water Authority", "Healthcare": "Regional Hospital",
             "Communications": "Telecom Hub", "Transportation": "Transit Authority"}
    rows = []
    for i in range(n):
        sector = rng.choice(SECTORS)
        weak = rng.random() < 0.35
        rows.append({
            "facility_id": f"CI{100 + i}",
            "facility_name": f"{rng.choice(towns)} {kinds[sector]}",
            "sector": sector,
            "exposed_services": int(rng.poisson(6 if weak else 2)),
            "kev_vulns": int(rng.poisson(2.0 if weak else 0.2)),
            "critical_vulns": int(rng.poisson(5 if weak else 1)),
            "patch_age_days": int(rng.gamma(4, 30 if weak else 10)),
            "mfa_coverage": round(float(rng.beta(3, 4) if weak else rng.beta(8, 2)), 2),
            "backup_tested": "No" if rng.random() < (0.6 if weak else 0.15) else "Yes",
            "incidents_12m": int(rng.poisson(2 if weak else 0.4)),
            "population_served": int(10 ** rng.uniform(3.5, 6.5)),
        })
    return pd.DataFrame(rows)


def cyber_score(df):
    out = df.copy()
    comp = pd.DataFrame(index=out.index)
    comp["E"] = clip01(out["exposed_services"] / 10.0)
    comp["V"] = 1.0 - np.exp(-(3.0 * out["kev_vulns"] + out["critical_vulns"]) / 10.0)
    comp["P"] = clip01(out["patch_age_days"] / 180.0)
    comp["C"] = 1.0 - clip01(out["mfa_coverage"])
    comp["B"] = np.where(is_yes(out["backup_tested"]), 0.0, 1.0)
    comp["H"] = clip01(out["incidents_12m"] / 5.0)
    weighted = pd.DataFrame({k: comp[k] * w for k, w in CYBER_W.items()})
    out["likelihood"] = weighted.sum(axis=1).round(3)
    pop_factor = clip01(np.log10(out["population_served"].clip(lower=1)) / 7.0)
    out["impact"] = (out["sector"].map(SECTOR_WEIGHT).fillna(0.8)
                     * (0.5 + 0.5 * pop_factor)).round(3)
    out["risk_score"] = (100.0 * out["likelihood"] * out["impact"]).round(1)
    out["risk_band"] = band(out["risk_score"], [60, 40, 20],
                            ["Critical", "High", "Medium", "Low"])
    out["top_action"] = weighted.idxmax(axis=1).map(CYBER_ACTIONS)
    return out


def cyber_charts(scored):
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_circle(size=80, opacity=0.8).encode(
            x=alt.X("likelihood:Q", title="Likelihood 0 to 1"),
            y=alt.Y("impact:Q", title="Impact 0 to 1"),
            color=band_color(MODULE_BY_KEY["cyber"]),
            tooltip=["facility_name", "sector", "risk_score", "top_action"],
        ).properties(height=300, title="Likelihood against impact"), use_container_width=True)
    with b:
        st.altair_chart(alt.Chart(scored).mark_bar(color="#1565C0").encode(
            x=alt.X("sector:N", title=None),
            y=alt.Y("mean(risk_score):Q", title="Average risk score"),
        ).properties(height=300, title="Average risk by sector"), use_container_width=True)


# ==========================================================================
# Module 2  Counter drone incident tracker
# ==========================================================================

SITE_TYPES = ["Airport", "Power plant", "Prison", "Water facility", "Stadium"]
SITE_WEIGHT = {"Airport": 1.2, "Power plant": 1.1, "Prison": 1.0,
               "Water facility": 1.0, "Stadium": 0.9}

DRONE_FIELDS = [
    F("sighting_id", "text", "Unique sighting identifier", "Tracks each report", "S0"),
    F("sighting_date", "date", "Date of the sighting", "Used for trends and hotspot windows",
      TODAY),
    F("site_name", "text", "Protected site nearest the sighting", "Groups sightings into hotspots",
      "Unknown site"),
    F("site_type", "cat", ", ".join(SITE_TYPES), "Sets the consequence weight of the site",
      "Power plant", SITE_TYPES),
    F("latitude", "num", "Latitude of the sighting", "Places the sighting on the map", 38.9),
    F("longitude", "num", "Longitude of the sighting", "Places the sighting on the map", -77.0),
    F("altitude_ft", "num", "Estimated altitude in feet",
      "Low flights near a site are more concerning", 400.0),
    F("duration_min", "num", "Minutes the drone was observed",
      "Long loitering suggests surveillance", 1.0),
    F("distance_to_site_m", "num", "Distance from the site boundary in meters",
      "Closer flights are more threatening", 1000.0),
    F("payload_observed", "yesno", "Was a payload or attachment seen",
      "Payloads can mean contraband delivery or worse", "No"),
    F("night_flight", "yesno", "Did the flight occur at night",
      "Night flights avoid observation and are less often recreational", "No"),
    F("remote_id_broadcast", "yesno", "Was a Remote ID signal detected",
      "No Remote ID means the operator is hiding or noncompliant", "No"),
]

DRONE_SITES = [
    ("Metro International Airport", "Airport", 39.18, -76.67),
    ("Northside Generating Station", "Power plant", 39.45, -76.40),
    ("State Correctional Center", "Prison", 39.05, -77.10),
    ("Eastbay Water Treatment", "Water facility", 38.85, -76.90),
    ("City Stadium", "Stadium", 39.28, -76.62),
    ("Riverbend Substation", "Power plant", 38.70, -77.20),
]
DRONE_W = {"proximity": 0.25, "low_altitude": 0.15, "loiter": 0.15, "payload": 0.20,
           "night": 0.10, "no_remote_id": 0.15}


def drone_generate(n, seed):
    rng = np.random.default_rng(seed)
    hot = rng.choice(len(DRONE_SITES), size=2, replace=False)
    rows = []
    for i in range(n):
        idx = rng.choice(hot) if rng.random() < 0.45 else rng.integers(0, len(DRONE_SITES))
        name, kind, lat, lon = DRONE_SITES[idx]
        suspicious = rng.random() < 0.3
        rows.append({
            "sighting_id": f"S{5000 + i}",
            "sighting_date": str(TODAY - datetime.timedelta(days=int(rng.integers(0, 120)))),
            "site_name": name, "site_type": kind,
            "latitude": round(lat + rng.normal(0, 0.01), 5),
            "longitude": round(lon + rng.normal(0, 0.01), 5),
            "altitude_ft": round(float(rng.uniform(50, 350) if suspicious
                                       else rng.uniform(150, 900)), 0),
            "duration_min": round(float(rng.gamma(3, 6) if suspicious else rng.gamma(2, 2)), 1),
            "distance_to_site_m": round(float(rng.uniform(0, 600) if suspicious
                                              else rng.uniform(200, 4000)), 0),
            "payload_observed": "Yes" if rng.random() < (0.35 if suspicious else 0.03) else "No",
            "night_flight": "Yes" if rng.random() < (0.55 if suspicious else 0.15) else "No",
            "remote_id_broadcast": "No" if rng.random() < (0.7 if suspicious else 0.2) else "Yes",
        })
    return pd.DataFrame(rows)


def drone_score(df):
    out = df.copy()
    comp = pd.DataFrame(index=out.index)
    comp["proximity"] = clip01(1.0 - out["distance_to_site_m"] / 3000.0)
    comp["low_altitude"] = clip01((1000.0 - out["altitude_ft"]) / 1000.0)
    comp["loiter"] = clip01(out["duration_min"] / 30.0)
    comp["payload"] = np.where(is_yes(out["payload_observed"]), 1.0, 0.0)
    comp["night"] = np.where(is_yes(out["night_flight"]), 1.0, 0.0)
    comp["no_remote_id"] = np.where(is_yes(out["remote_id_broadcast"]), 0.0, 1.0)
    base = sum(comp[k] * w for k, w in DRONE_W.items())
    out["threat_score"] = (100.0 * base * out["site_type"].map(SITE_WEIGHT).fillna(1.0)) \
        .clip(upper=100).round(1)
    out["threat_band"] = band(out["threat_score"], [70, 45], ["Severe", "Elevated", "Routine"])
    return out


def drone_hotspots(scored):
    data = scored.copy()
    data["sighting_date"] = pd.to_datetime(data["sighting_date"], errors="coerce")
    recent = data[data["sighting_date"] >= pd.Timestamp(TODAY - datetime.timedelta(days=30))]
    groups = data.groupby("site_name").agg(
        site_type=("site_type", "first"), sightings=("sighting_id", "count"),
        mean_threat=("threat_score", "mean"), max_threat=("threat_score", "max"))
    groups["sightings_30d"] = recent.groupby("site_name")["sighting_id"].count()
    groups["sightings_30d"] = groups["sightings_30d"].fillna(0).astype(int)
    groups["hotspot_index"] = (groups["mean_threat"]
                               * (1.0 + np.log1p(groups["sightings_30d"]))).round(1)
    return groups.sort_values("hotspot_index", ascending=False).reset_index()


def drone_charts(scored):
    hotspots = drone_hotspots(scored)
    st.markdown("**Hotspot ranking by site**")
    st.dataframe(hotspots.round(1), use_container_width=True, hide_index=True)
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_circle(opacity=0.7).encode(
            x=alt.X("longitude:Q", scale=alt.Scale(zero=False)),
            y=alt.Y("latitude:Q", scale=alt.Scale(zero=False)),
            size=alt.Size("threat_score:Q", legend=None),
            color=band_color(MODULE_BY_KEY["drone"]),
            tooltip=["site_name", "sighting_date", "threat_score", "threat_band"],
        ).properties(height=320, title="Sighting locations sized by threat"),
            use_container_width=True)
    with b:
        weekly = scored.copy()
        weekly["week"] = pd.to_datetime(weekly["sighting_date"], errors="coerce") \
            .dt.to_period("W").dt.start_time
        st.altair_chart(alt.Chart(weekly.dropna(subset=["week"])).mark_bar().encode(
            x=alt.X("week:T", title="Week"),
            y=alt.Y("count():Q", title="Sightings"),
            color=band_color(MODULE_BY_KEY["drone"]),
        ).properties(height=320, title="Sightings per week"), use_container_width=True)
    if st.checkbox("Show sightings on a street map (needs internet access)", value=False):
        st.map(scored.rename(columns={"latitude": "lat", "longitude": "lon"})[["lat", "lon"]])


# ==========================================================================
# Module 3  Disaster aid navigator
# ==========================================================================

DISASTERS = ["Flood", "Hurricane", "Wildfire", "Tornado", "Winter storm"]

PROGRAMS = [
    {"name": "Public Assistance", "needs_declaration": True, "min_damage_pc": 1.5,
     "window_days": 30, "docs": "Request for public assistance, damage inventory, cost records"},
    {"name": "Individual Assistance", "needs_declaration": True, "min_damage_pc": 0.0,
     "window_days": 60, "docs": "Household registrations, proof of occupancy, insurance letters"},
    {"name": "Hazard Mitigation Grant Program", "needs_declaration": True,
     "min_damage_pc": 0.0, "window_days": 365,
     "docs": "Mitigation plan, project scope, benefit cost analysis"},
    {"name": "SBA Disaster Loans", "needs_declaration": False, "min_damage_pc": 0.0,
     "window_days": 60, "docs": "Loan application, tax returns, loss estimates"},
    {"name": "CDBG Disaster Recovery", "needs_declaration": True, "min_damage_pc": 500.0,
     "window_days": 180, "docs": "Action plan, unmet needs assessment, public comment record"},
    {"name": "State Emergency Fund", "needs_declaration": False, "min_damage_pc": 50.0,
     "window_days": 45, "docs": "Local emergency declaration, preliminary damage estimate"},
]

AID_FIELDS = [
    F("community_id", "text", "Unique community identifier", "Links applications and checklists",
      "C0"),
    F("community_name", "text", "Community name", "Readable label", "Unknown"),
    F("disaster_type", "cat", ", ".join(DISASTERS), "Kind of event", "Flood", DISASTERS),
    F("declared_disaster", "yesno", "Is there a federal major disaster declaration",
      "Most federal recovery programs require a declaration", "No"),
    F("population", "int", "Residents in the community", "Used for damage per resident", 1000),
    F("damage_usd", "num", "Estimated total damage in dollars",
      "Drives eligibility thresholds and need", 0.0),
    F("insured_share", "num01", "Share of damage covered by insurance",
      "Uninsured losses create unmet need", 0.0),
    F("has_grant_staff", "yesno", "Does the community have dedicated grant staff",
      "Small communities without staff struggle to apply on time", "No"),
    F("days_since_event", "int", "Days since the disaster occurred",
      "Application windows close over time", 0),
    F("docs_complete", "num01", "Share of required documents already gathered",
      "Incomplete files are the main cause of rejection and delay", 0.0),
]


def aid_generate(n, seed):
    rng = np.random.default_rng(seed)
    names = ["Millbrook", "Stony Creek", "Bayport", "Elk Grove", "Sandy Hollow", "Red Mesa",
             "Clearwater", "Ashford", "Fox Run", "Willow Bend", "North Platte", "Silver Lake"]
    rows = []
    for i in range(n):
        pop = int(10 ** rng.uniform(2.8, 5.3))
        rows.append({
            "community_id": f"C{300 + i}",
            "community_name": f"{rng.choice(names)} {i + 1}",
            "disaster_type": rng.choice(DISASTERS),
            "declared_disaster": "Yes" if rng.random() < 0.7 else "No",
            "population": pop,
            "damage_usd": round(float(pop * rng.gamma(2, 600)), 0),
            "insured_share": round(float(rng.beta(2, 4)), 2),
            "has_grant_staff": "Yes" if pop > 30000 or rng.random() < 0.2 else "No",
            "days_since_event": int(rng.integers(1, 200)),
            "docs_complete": round(float(rng.beta(3, 3)), 2),
        })
    return pd.DataFrame(rows)


def aid_programs_for(row):
    """Return a checklist of programs with eligibility and days remaining."""
    damage_pc = row["damage_usd"] / max(1, row["population"])
    declared = str(row["declared_disaster"]) == "Yes"
    items = []
    for p in PROGRAMS:
        eligible = (declared or not p["needs_declaration"]) and damage_pc >= p["min_damage_pc"]
        remaining = p["window_days"] - int(row["days_since_event"])
        if not eligible:
            status = "Not eligible"
        elif remaining < 0:
            status = "Window closed"
        else:
            status = "Open"
        items.append({"program": p["name"], "eligible": "Yes" if eligible else "No",
                      "days_remaining": remaining if eligible else None, "status": status,
                      "documents_needed": p["docs"]})
    return pd.DataFrame(items)


def aid_score(df):
    out = df.copy()
    damage_pc = out["damage_usd"] / out["population"].clip(lower=1)
    dpc = clip01(damage_pc / 2000.0)
    staff = np.where(is_yes(out["has_grant_staff"]), 0.0, 1.0)
    out["need_score"] = (100.0 * (0.35 * dpc + 0.25 * (1.0 - clip01(out["insured_share"]))
                                  + 0.20 * staff + 0.20 * (1.0 - clip01(out["docs_complete"])))
                         ).round(1)
    out["damage_per_resident"] = damage_pc.round(0)
    open_names, next_deadline, closed = [], [], []
    for _, row in out.iterrows():
        checklist = aid_programs_for(row)
        open_rows = checklist[checklist["status"] == "Open"]
        open_names.append(", ".join(open_rows["program"]))
        next_deadline.append(int(open_rows["days_remaining"].min()) if len(open_rows) else None)
        closed.append(int((checklist["status"] == "Window closed").sum()))
    out["open_programs"] = open_names
    out["days_to_next_deadline"] = next_deadline
    out["windows_missed"] = closed
    out["rejection_risk"] = (1.0 - clip01(out["docs_complete"])).round(2)
    out["need_band"] = band(out["need_score"], [60, 35], ["High need", "Moderate need", "Low need"])
    return out


def aid_charts(scored):
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_circle(size=80, opacity=0.8).encode(
            x=alt.X("docs_complete:Q", title="Documents complete"),
            y=alt.Y("need_score:Q", title="Need score"),
            color=band_color(MODULE_BY_KEY["aid"]),
            tooltip=["community_name", "need_score", "open_programs", "days_to_next_deadline"],
        ).properties(height=300, title="Need against application readiness"),
            use_container_width=True)
    with b:
        urgent = scored.dropna(subset=["days_to_next_deadline"]) \
            .sort_values("days_to_next_deadline").head(12)
        st.altair_chart(alt.Chart(urgent).mark_bar(color="#C62828").encode(
            x=alt.X("days_to_next_deadline:Q", title="Days to next deadline"),
            y=alt.Y("community_name:N", sort="x", title=None),
        ).properties(height=300, title="Closest application deadlines"),
            use_container_width=True)
    st.markdown("**Program checklist for one community**")
    choice = st.selectbox("Community", scored["community_name"].tolist(), key="aid_pick")
    row = scored[scored["community_name"] == choice].iloc[0]
    st.dataframe(aid_programs_for(row), use_container_width=True, hide_index=True)
    st.caption("Program rules and windows here are simplified illustrations. Always confirm "
               "with current official program guidance.")


# ==========================================================================
# Module 4  Border security metrics quality dashboard
# ==========================================================================

BORDER_CATEGORIES = ["Between ports", "At ports", "Maritime", "Air"]
BORDER_MEASURES = ["Apprehensions", "Estimated unlawful entries", "Estimated got aways",
                   "Interdiction effectiveness rate", "Drug seizures by weight",
                   "Drug seizures by count", "Currency seizures", "Weapons seizures",
                   "Average response time", "Refusals of entry", "Turn back rate"]

BORDER_FIELDS = [
    F("metric_id", "text", "Metric number from 1 to 43", "Identifies the required metric", "M0"),
    F("metric_name", "text", "Name of the metric", "Readable label", "Unknown metric"),
    F("category", "cat", ", ".join(BORDER_CATEGORIES), "Border domain of the metric",
      "Between ports", BORDER_CATEGORIES),
    F("fiscal_year", "int", "Reporting fiscal year", "Groups the annual report", TODAY.year),
    F("value", "numblank", "Reported value for this year", "Blank means the metric is missing",
      None),
    F("prior_value", "numblank", "Value reported for the prior year",
      "Used to detect implausible jumps", None),
    F("reported", "yesno", "Was the metric included in the report",
      "Unreported metrics break the legal requirement", "No"),
    F("source_system", "text", "System the data came from", "Supports data lineage checks",
      "Unknown"),
    F("days_since_update", "int", "Days since the source data was refreshed",
      "Stale data reduces trust in the number", 999),
]


def border_generate(n, seed):
    rng = np.random.default_rng(seed)
    systems = ["Enforcement data system", "Port operations system", "Marine operations log",
               "Air operations log"]
    rows = []
    count = 0
    for cat_index, cat in enumerate(BORDER_CATEGORIES):
        for measure in BORDER_MEASURES:
            if count >= 43:
                break
            count += 1
            prior = float(rng.uniform(50, 50000))
            missing = rng.random() < 0.08
            jump = rng.random() < 0.10
            value = None if missing else round(prior * (rng.uniform(1.6, 2.5) if jump
                                                        else rng.uniform(0.8, 1.2)), 1)
            rows.append({
                "metric_id": f"M{count:02d}", "metric_name": f"{cat} {measure.lower()}",
                "category": cat, "fiscal_year": TODAY.year - 1, "value": value,
                "prior_value": round(prior, 1),
                "reported": "No" if missing else "Yes",
                "source_system": systems[cat_index],
                "days_since_update": int(rng.integers(5, 80) if rng.random() < 0.8
                                         else rng.integers(91, 300)),
            })
    frame = pd.DataFrame(rows)
    if n > 43:
        years = [frame]
        for k in range(1, int(math.ceil(n / 43))):
            prev = frame.copy()
            prev["fiscal_year"] = TODAY.year - 1 - k
            years.append(prev)
        frame = pd.concat(years, ignore_index=True).head(n)
    return frame


def border_score(df):
    out = df.copy()
    value = pd.to_numeric(out["value"], errors="coerce")
    prior = pd.to_numeric(out["prior_value"], errors="coerce")
    complete = (is_yes(out["reported"]) & value.notna()).astype(float)
    valid = ((value >= 0) & value.notna()).astype(float)
    timely = (out["days_since_update"] <= 90).astype(float)
    change = (value - prior).abs() / prior.abs().clip(lower=1.0)
    consistent = (prior.isna() | (change <= 0.5)).astype(float) * complete
    out["check_complete"] = np.where(complete == 1, "Pass", "Fail")
    out["check_timely"] = np.where(timely == 1, "Pass", "Fail")
    out["check_consistent"] = np.where(consistent == 1, "Pass", "Fail")
    out["check_valid"] = np.where(valid == 1, "Pass", "Fail")
    out["change_vs_prior"] = change.round(2)
    out["quality_score"] = (100.0 * (0.40 * complete + 0.20 * timely + 0.25 * consistent
                                     + 0.15 * valid)).round(1)
    out["quality_band"] = band(out["quality_score"], [85, 60],
                               ["Good", "Needs review", "Failing"])
    return out


def border_charts(scored):
    latest = scored[scored["fiscal_year"] == scored["fiscal_year"].max()]
    reported = int((latest["check_complete"] == "Pass").sum())
    a, b, c = st.columns(3)
    a.metric("Metrics required by law", 43)
    b.metric("Metrics complete in latest year", reported)
    c.metric("Report completeness", f"{reported / 43:.0%}")
    checks = latest.melt(id_vars=["category"], value_vars=[
        "check_complete", "check_timely", "check_consistent", "check_valid"],
        var_name="check", value_name="result")
    checks["pass"] = (checks["result"] == "Pass").astype(float)
    st.altair_chart(alt.Chart(checks).mark_rect().encode(
        x=alt.X("check:N", title=None), y=alt.Y("category:N", title=None),
        color=alt.Color("mean(pass):Q", title="Pass rate",
                        scale=alt.Scale(scheme="blues", domain=[0, 1])),
        tooltip=["category", "check", alt.Tooltip("mean(pass):Q", format=".0%")],
    ).properties(height=220, title="Pass rate by check and category"), use_container_width=True)


# ==========================================================================
# Module 5  Acquisition program health tracker
# ==========================================================================

COMPONENTS = ["CBP", "TSA", "USCG", "FEMA", "CISA", "ICE", "USCIS", "Science and Technology"]

ACQ_FIELDS = [
    F("program_id", "text", "Unique program identifier", "Links all program data", "P0"),
    F("program_name", "text", "Program name", "Readable label", "Unknown program"),
    F("component", "cat", ", ".join(COMPONENTS), "DHS component that owns the program",
      "CBP", COMPONENTS),
    F("baseline_cost_musd", "num", "Approved baseline cost in millions of dollars",
      "The commitment that overruns are measured against", 300.0),
    F("actual_spent_musd", "num", "Money spent to date in millions",
      "Compared with work completed to measure efficiency", 0.0),
    F("percent_complete", "num01", "Share of planned work completed",
      "Turns the baseline into earned value", 0.0),
    F("baseline_months", "int", "Approved schedule length in months",
      "Baseline for schedule slip", 60),
    F("forecast_months", "int", "Current forecast schedule length in months",
      "Shows how far delivery has slipped", 60),
    F("test_events_planned", "int", "Operational test events planned to date",
      "Evidence that the system works", 1),
    F("test_events_passed", "int", "Test events passed",
      "Failed tests often precede cost and schedule problems", 0),
    F("kpp_met", "num01", "Share of key performance parameters currently met",
      "Whether the system will deliver what was promised", 0.0),
]


def acq_generate(n, seed):
    rng = np.random.default_rng(seed)
    nouns = ["Border Surveillance Towers", "Checkpoint Screening", "Cutter Fleet",
             "Alert System Upgrade", "Cyber Diagnostics", "Case Management",
             "Biometric Identity", "Radar Modernization", "Financial Systems",
             "Aircraft Replacement", "Network Modernization", "Credential Authentication"]
    rows = []
    for i in range(n):
        trouble = rng.random() < 0.35
        base = float(rng.uniform(300, 9000))
        pct = float(rng.uniform(0.1, 0.9))
        cpi = rng.uniform(0.65, 0.92) if trouble else rng.uniform(0.95, 1.08)
        months = int(rng.integers(36, 120))
        planned = int(rng.integers(2, 12))
        rows.append({
            "program_id": f"P{700 + i}",
            "program_name": f"{rng.choice(nouns)} {chr(65 + i % 26)}",
            "component": rng.choice(COMPONENTS),
            "baseline_cost_musd": round(base, 1),
            "actual_spent_musd": round(base * pct / cpi, 1),
            "percent_complete": round(pct, 2),
            "baseline_months": months,
            "forecast_months": int(months * (rng.uniform(1.15, 1.6) if trouble
                                             else rng.uniform(0.95, 1.08))),
            "test_events_planned": planned,
            "test_events_passed": int(planned * (rng.uniform(0.4, 0.8) if trouble
                                                 else rng.uniform(0.85, 1.0))),
            "kpp_met": round(float(rng.beta(4, 3) if trouble else rng.beta(9, 1.5)), 2),
        })
    return pd.DataFrame(rows)


def acq_score(df):
    out = df.copy()
    ev = out["percent_complete"] * out["baseline_cost_musd"]
    cpi = (ev / out["actual_spent_musd"].replace(0, np.nan)).fillna(1.0)
    eac = out["baseline_cost_musd"] / cpi.replace(0, np.nan)
    growth = (eac / out["baseline_cost_musd"] - 1.0).fillna(0.0)
    slip = out["forecast_months"] / out["baseline_months"].clip(lower=1) - 1.0
    test = (out["test_events_passed"] / out["test_events_planned"].clip(lower=1)).clip(0, 1)
    out["earned_value_musd"] = ev.round(1)
    out["cpi"] = cpi.round(2)
    out["eac_musd"] = eac.round(1)
    out["cost_growth"] = growth.round(3)
    out["schedule_slip"] = slip.round(3)
    out["test_pass_rate"] = test.round(2)
    penalty = (40.0 * clip01(growth.clip(lower=0) / 0.5) + 30.0 * clip01(slip.clip(lower=0) / 0.5)
               + 15.0 * (1.0 - test) + 15.0 * (1.0 - clip01(out["kpp_met"])))
    out["health_score"] = (100.0 - penalty).round(1)
    out["health_band"] = band(out["health_score"], [75, 55], ["Green", "Yellow", "Red"])
    out["early_warning"] = np.where((growth > 0.15) | (slip > 0.20),
                                    "Possible baseline breach", "")
    return out


def acq_charts(scored):
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_circle(size=90, opacity=0.8).encode(
            x=alt.X("cost_growth:Q", title="Forecast cost growth", axis=alt.Axis(format="%")),
            y=alt.Y("schedule_slip:Q", title="Schedule slip", axis=alt.Axis(format="%")),
            color=band_color(MODULE_BY_KEY["acq"]),
            tooltip=["program_name", "component", "cpi", "eac_musd", "health_score"],
        ).properties(height=300, title="Cost growth against schedule slip"),
            use_container_width=True)
    with b:
        bars = scored.melt(id_vars=["program_name"], value_vars=["baseline_cost_musd",
                                                                 "eac_musd"],
                           var_name="measure", value_name="musd")
        st.altair_chart(alt.Chart(bars).mark_bar().encode(
            y=alt.Y("program_name:N", title=None),
            x=alt.X("musd:Q", title="Millions of dollars"),
            yOffset="measure:N",
            color=alt.Color("measure:N", title=None, scale=alt.Scale(
                range=["#90CAF9", "#0D47A1"])),
        ).properties(height=max(300, 26 * len(scored)),
                      title="Baseline against estimate at completion"),
            use_container_width=True)


# ==========================================================================
# Module 6  Open recommendations tracker
# ==========================================================================

REC_AREAS = ["IT and cybersecurity", "Border and immigration", "Disaster response",
             "Financial management", "Acquisition management"]
REC_STATUS = ["Open", "In progress", "Implemented", "Closed not implemented"]

REC_FIELDS = [
    F("rec_id", "text", "Unique recommendation identifier", "Tracks each recommendation", "R0"),
    F("report_number", "text", "Audit report the recommendation came from",
      "Links back to the source finding", "Unknown"),
    F("area", "cat", ", ".join(REC_AREAS), "Mission area", "IT and cybersecurity", REC_AREAS),
    F("priority", "yesno", "Designated as a priority recommendation",
      "Priority items have the largest benefit if implemented", "No"),
    F("owner", "text", "Office accountable for implementation", "Creates clear accountability",
      "Unassigned"),
    F("date_issued", "date", "Date the recommendation was issued",
      "Age shows how long a weakness has persisted", TODAY),
    F("due_date", "date", "Agreed target date for implementation",
      "Missed dates signal stalled work", TODAY),
    F("status", "cat", ", ".join(REC_STATUS), "Current status", "Open", REC_STATUS),
    F("evidence_progress", "num01", "Share of required closure evidence assembled",
      "Auditors close items only with evidence", 0.0),
]


def rec_generate(n, seed):
    rng = np.random.default_rng(seed)
    owners = ["Office of the CIO", "CBP", "FEMA", "CISA", "Office of the CFO", "TSA", "ICE",
              "Management Directorate"]
    rows = []
    for i in range(n):
        issued = TODAY - datetime.timedelta(days=int(rng.integers(30, 2600)))
        due = issued + datetime.timedelta(days=int(rng.integers(180, 900)))
        status = rng.choice(REC_STATUS, p=[0.40, 0.30, 0.25, 0.05])
        rows.append({
            "rec_id": f"R{1000 + i}",
            "report_number": f"Report {int(rng.integers(18, 26))} {int(rng.integers(100000, 109999))}",
            "area": rng.choice(REC_AREAS),
            "priority": "Yes" if rng.random() < 0.15 else "No",
            "owner": rng.choice(owners),
            "date_issued": str(issued), "due_date": str(due), "status": status,
            "evidence_progress": round(float(1.0 if status == "Implemented"
                                             else rng.beta(2, 3)), 2),
        })
    return pd.DataFrame(rows)


def rec_score(df):
    out = df.copy()
    issued = pd.to_datetime(out["date_issued"], errors="coerce")
    due = pd.to_datetime(out["due_date"], errors="coerce")
    now = pd.Timestamp(TODAY)
    active = out["status"].isin(["Open", "In progress"])
    out["age_days"] = (now - issued).dt.days.fillna(0).astype(int)
    out["overdue"] = np.where(active & (due < now), "Yes", "No")
    priority = np.where(is_yes(out["priority"]), 1.0, 0.0)
    overdue = np.where(out["overdue"] == "Yes", 1.0, 0.0)
    risk = 100.0 * (0.35 * priority + 0.25 * clip01(out["age_days"] / 1095.0)
                    + 0.25 * overdue + 0.15 * (1.0 - clip01(out["evidence_progress"])))
    out["risk_score"] = np.where(active, risk, 0.0).round(1)
    out["attention_band"] = np.where(active, band(out["risk_score"], [60, 35],
                                                  ["Urgent", "Watch", "On track"]), "Closed")
    return out


def rec_charts(scored):
    active = scored[scored["attention_band"] != "Closed"]
    total = len(scored)
    k = st.columns(4)
    k[0].metric("Open or in progress", len(active))
    k[1].metric("Priority open", int(is_yes(active["priority"]).sum()))
    k[2].metric("Overdue", int((active["overdue"] == "Yes").sum()))
    k[3].metric("Implementation rate",
                f"{(scored['status'] == 'Implemented').sum() / max(1, total):.0%}")
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(active).mark_bar().encode(
            x=alt.X("count():Q", title="Open recommendations"),
            y=alt.Y("area:N", title=None),
            color=alt.Color("priority:N", title="Priority", scale=alt.Scale(
                domain=["Yes", "No"], range=["#C62828", "#90CAF9"])),
        ).properties(height=260, title="Open recommendations by area"), use_container_width=True)
    with b:
        st.altair_chart(alt.Chart(active).mark_bar(color="#1565C0").encode(
            x=alt.X("age_days:Q", bin=alt.Bin(step=180), title="Age in days"),
            y=alt.Y("count():Q", title="Recommendations"),
        ).properties(height=260, title="Age of open recommendations"), use_container_width=True)


# ==========================================================================
# Module 7  Deepfake and impersonation verification
# ==========================================================================

DF_ROLES = ["Official", "Emergency manager", "Vendor", "Applicant"]
DF_REQUESTS = ["Routine", "Credential request", "Emergency directive", "Funds transfer"]
DF_C2PA = ["Valid", "Missing", "Invalid"]
DF_OOB = ["Confirmed", "Not attempted", "Failed"]
DF_PROV_RISK = {"Valid": 0.0, "Missing": 0.6, "Invalid": 1.0}
DF_OOB_RISK = {"Confirmed": 0.0, "Not attempted": 0.7, "Failed": 1.0}
DF_FACTOR = {"Routine": 1.00, "Credential request": 1.15, "Emergency directive": 1.20,
             "Funds transfer": 1.25}
DF_W = {"provenance": 0.20, "out_of_band": 0.30, "liveness": 0.20, "artifact": 0.15,
        "behavior": 0.10, "caller_id": 0.05}

DF_FIELDS = [
    F("case_id", "text", "Unique case identifier", "Links evidence to one call or file", "D0"),
    F("claimed_identity", "text", "Who the person claims to be", "The identity to prove",
      "Unknown"),
    F("claimed_role", "cat", ", ".join(DF_ROLES),
      "Role being claimed, impersonators target authority roles", "Official", DF_ROLES),
    F("request_type", "cat", ", ".join(DF_REQUESTS),
      "What is being requested, sets the impact multiplier", "Routine", DF_REQUESTS),
    F("urgency_level", "int", "Pressure applied, 1 to 5", "Manufactured urgency is a red flag", 1),
    F("c2pa_status", "cat", ", ".join(DF_C2PA),
      "Content credential result, signed provenance proves origin and invalid means tampering", "Missing", DF_C2PA),
    F("oob_status", "cat", ", ".join(DF_OOB),
      "Callback on a trusted directory number, the strongest single check", "Not attempted", DF_OOB),
    F("caller_id_match", "yesno", "Incoming number matches directory",
      "Weak signal because caller ID can be spoofed", "No"),
    F("liveness", "num01", "Detector confidence that a live human is present",
      "Synthetic voices and faces often fail liveness tests", 0.5),
    F("artifact_score", "num01", "Detector score for synthesis artifacts",
      "Higher means more traces of generation", 0.5),
    F("behavior_anomaly", "num01", "Analyst rating of red flags in the request",
      "Secrecy, bypassing process and new payment details", 0.5),
]


def df_generate(n, seed):
    rng = np.random.default_rng(seed)
    first = ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley", "Avery", "Quinn"]
    last = ["Carter", "Nguyen", "Patel", "Brooks", "Ramirez", "Kim", "Okafor", "Ellis"]
    rows = []
    for i in range(n):
        fake = rng.random() < 0.3
        rows.append({
            "case_id": f"D{4000 + i}",
            "claimed_identity": f"{rng.choice(first)} {rng.choice(last)}",
            "claimed_role": rng.choice(DF_ROLES),
            "request_type": rng.choice(DF_REQUESTS, p=[0.1, 0.3, 0.25, 0.35] if fake
                                       else [0.55, 0.2, 0.15, 0.1]),
            "urgency_level": int(rng.choice([3, 4, 5]) if fake else rng.choice([1, 2, 3])),
            "c2pa_status": rng.choice(DF_C2PA, p=[0.05, 0.75, 0.2] if fake
                                      else [0.45, 0.53, 0.02]),
            "oob_status": rng.choice(DF_OOB, p=[0.05, 0.5, 0.45] if fake
                                     else [0.55, 0.43, 0.02]),
            "caller_id_match": "Yes" if rng.random() < (0.35 if fake else 0.9) else "No",
            "liveness": round(float(rng.beta(2.5, 4) if fake else rng.beta(6, 1.8)), 2),
            "artifact_score": round(float(rng.beta(4, 2.5) if fake else rng.beta(1.5, 6)), 2),
            "behavior_anomaly": round(float(rng.beta(4, 2) if fake else rng.beta(1.5, 6)), 2),
        })
    return pd.DataFrame(rows)


def df_score(df):
    out = df.copy()
    comp = pd.DataFrame(index=out.index)
    comp["provenance"] = out["c2pa_status"].map(DF_PROV_RISK).fillna(0.6)
    comp["out_of_band"] = out["oob_status"].map(DF_OOB_RISK).fillna(0.7)
    comp["liveness"] = 1.0 - clip01(out["liveness"])
    comp["artifact"] = clip01(out["artifact_score"])
    comp["behavior"] = clip01(out["behavior_anomaly"])
    comp["caller_id"] = np.where(is_yes(out["caller_id_match"]), 0.0, 1.0)
    base = 100.0 * sum(comp[k] * w for k, w in DF_W.items())
    urgency = out["urgency_level"].clip(1, 5)
    mult = out["request_type"].map(DF_FACTOR).fillna(1.0) + 0.03 * (urgency - 1)
    score = (base * mult).clip(upper=100)
    score = np.where(out["c2pa_status"] == "Invalid", np.maximum(score, 70), score)
    score = np.where(out["oob_status"] == "Failed", np.maximum(score, 80), score)
    strong = (out["c2pa_status"] == "Valid") & (out["oob_status"] == "Confirmed")
    score = np.where(strong, np.minimum(score, 40), score)
    out["base_score"] = base.round(1)
    out["multiplier"] = mult.round(2)
    out["risk_score"] = np.round(score, 1)
    out["decision"] = band(out["risk_score"], [60, 30],
                           ["Block and escalate", "Hold and verify", "Proceed"])
    return out


def df_charts(scored):
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_bar().encode(
            x=alt.X("risk_score:Q", bin=alt.Bin(step=5), title="Risk score"),
            y=alt.Y("count():Q", title="Cases"),
            color=band_color(MODULE_BY_KEY["deepfake"]),
        ).properties(height=280, title="Risk score distribution"), use_container_width=True)
    with b:
        st.altair_chart(alt.Chart(scored).mark_bar(color="#1565C0").encode(
            x=alt.X("request_type:N", title=None),
            y=alt.Y("mean(risk_score):Q", title="Average risk score"),
        ).properties(height=280, title="Average risk by request type"), use_container_width=True)


# ==========================================================================
# Module 8  Facility insider threat and supply chain checklist
# ==========================================================================

FAC_FIELDS = [
    F("facility_id", "text", "Unique facility identifier", "Links all checks to one site", "B0"),
    F("facility_name", "text", "Facility name", "Readable label", "Unknown facility"),
    F("component", "cat", ", ".join(COMPONENTS), "Owning DHS component", "CBP", COMPONENTS),
    F("personnel_total", "int", "People with access to the facility",
      "Denominator for background check coverage", 1),
    F("background_checks_current", "int", "Personnel with a current background check",
      "Lapsed checks are a core insider risk control gap", 0),
    F("vendors_total", "int", "Vendors supplying or servicing the facility",
      "Denominator for vendor assessment coverage", 1),
    F("vendors_assessed", "int", "Vendors with a current supply chain risk assessment",
      "Unassessed vendors are unknown risk", 0),
    F("vendors_high_risk", "int", "Vendors rated high risk", "Concentrated supply chain exposure",
      0),
    F("components_due_inspection", "int", "Critical components due for inspection",
      "IT cabling, HVAC controls and similar items attackers can tamper with", 1),
    F("components_inspected", "int", "Components inspected on schedule", "Inspection coverage",
      0),
    F("badge_anomalies_30d", "int", "Unusual access badge events in 30 days",
      "Odd hours, denied entries and tailgating are insider warning signs", 0),
    F("days_since_audit", "int", "Days since the last security audit",
      "Old audits miss new risks", 365),
]


def fac_generate(n, seed):
    rng = np.random.default_rng(seed)
    places = ["Field Office", "Operations Center", "Data Center", "Port Facility",
              "Training Center", "Logistics Depot", "Command Center", "Laboratory"]
    cities = ["Atlanta", "Denver", "El Paso", "Seattle", "Miami", "Chicago", "Boston", "Phoenix"]
    rows = []
    for i in range(n):
        weak = rng.random() < 0.35
        people = int(rng.integers(40, 1500))
        vendors = int(rng.integers(5, 120))
        due = int(rng.integers(10, 300))
        rows.append({
            "facility_id": f"B{200 + i}",
            "facility_name": f"{rng.choice(cities)} {rng.choice(places)}",
            "component": rng.choice(COMPONENTS),
            "personnel_total": people,
            "background_checks_current": int(people * (rng.uniform(0.75, 0.94) if weak
                                                       else rng.uniform(0.96, 1.0))),
            "vendors_total": vendors,
            "vendors_assessed": int(vendors * (rng.uniform(0.3, 0.7) if weak
                                               else rng.uniform(0.8, 1.0))),
            "vendors_high_risk": int(vendors * (rng.uniform(0.08, 0.25) if weak
                                                else rng.uniform(0.0, 0.06))),
            "components_due_inspection": due,
            "components_inspected": int(due * (rng.uniform(0.4, 0.8) if weak
                                               else rng.uniform(0.85, 1.0))),
            "badge_anomalies_30d": int(rng.poisson(6 if weak else 1)),
            "days_since_audit": int(rng.integers(200, 900) if weak else rng.integers(20, 360)),
        })
    return pd.DataFrame(rows)


def fac_score(df):
    out = df.copy()
    bg = clip01(out["background_checks_current"] / out["personnel_total"].clip(lower=1))
    va = clip01(out["vendors_assessed"] / out["vendors_total"].clip(lower=1))
    hr = clip01(out["vendors_high_risk"] / out["vendors_total"].clip(lower=1))
    ins = clip01(out["components_inspected"] / out["components_due_inspection"].clip(lower=1))
    audit = clip01(1.0 - out["days_since_audit"] / 365.0)
    out["background_rate"] = bg.round(3)
    out["vendor_assessed_rate"] = va.round(3)
    out["inspection_rate"] = ins.round(3)
    out["compliance_score"] = (100.0 * (0.35 * bg + 0.25 * va + 0.25 * ins + 0.15 * audit)
                               ).round(1)
    out["exposure_score"] = ((100.0 - out["compliance_score"]) + 5.0 * out["badge_anomalies_30d"]
                             + 20.0 * hr).clip(upper=100).round(1)
    out["exposure_band"] = band(out["exposure_score"], [50, 25], ["High", "Moderate", "Low"])
    alerts = []
    for i in out.index:
        items = []
        if bg[i] < 0.95:
            items.append("Background checks below 95 percent")
        if va[i] < 0.80:
            items.append("Vendor assessments below 80 percent")
        if ins[i] < 0.90:
            items.append("Inspections overdue")
        if out.at[i, "days_since_audit"] > 365:
            items.append("Audit older than one year")
        if out.at[i, "badge_anomalies_30d"] >= 5:
            items.append("Badge anomalies need review")
        alerts.append("; ".join(items))
    out["alerts"] = alerts
    return out


def fac_charts(scored):
    a, b = st.columns(2)
    with a:
        st.altair_chart(alt.Chart(scored).mark_circle(size=80, opacity=0.8).encode(
            x=alt.X("compliance_score:Q", title="Compliance score"),
            y=alt.Y("badge_anomalies_30d:Q", title="Badge anomalies in 30 days"),
            color=band_color(MODULE_BY_KEY["facility"]),
            tooltip=["facility_name", "compliance_score", "exposure_score", "alerts"],
        ).properties(height=300, title="Compliance against insider warning signs"),
            use_container_width=True)
    with b:
        alerts = scored["alerts"].str.split("; ").explode()
        alerts = alerts[alerts.str.len() > 0].value_counts().reset_index()
        alerts.columns = ["alert", "facilities"]
        st.altair_chart(alt.Chart(alerts).mark_bar(color="#C62828").encode(
            x=alt.X("facilities:Q", title="Facilities"),
            y=alt.Y("alert:N", sort="-x", title=None),
        ).properties(height=300, title="Most common alerts"), use_container_width=True)


# ==========================================================================
# Module registry: explanations, diagrams and formulas
# ==========================================================================

MODULES = [
    {
        "key": "cyber", "tab": "1 Cyber risk", "title": "Critical infrastructure cyber risk monitor",
        "gap": "The 2026 Annual Threat Assessment says China, Russia, Iran, North Korea and "
               "ransomware groups will keep trying to compromise government, private sector and "
               "critical infrastructure networks, and that AI will likely accelerate cyber "
               "threats. Federal cyber support for utilities, water systems and hospitals is "
               "limited, so it must go where risk is highest.",
        "what": "Scores each facility on exposure, vulnerabilities, patching, multifactor "
                "login, tested backups and incident history, then scales by sector consequence "
                "and population served. It ranks facilities and names the single most valuable "
                "fix for each.",
        "benefits": ["Directs scarce assessment teams and grants to the riskiest sites",
                     "Gives owners a concrete first action instead of a long report",
                     "Shows sector wide patterns for policy and outreach"],
        "fields": CYBER_FIELDS, "generate": cyber_generate, "score": cyber_score,
        "charts": cyber_charts, "id_col": "facility_id", "default_n": 60,
        "score_col": "risk_score", "score_label": "Risk score", "band_col": "risk_band",
        "band_labels": ["Critical", "High", "Medium", "Low"],
        "band_colors": ["#B71C1C", "#EF6C00", "#F9A825", "#2E7D32"],
        "report_cols": ["facility_id", "facility_name", "sector", "likelihood", "impact",
                        "risk_score", "risk_band", "top_action"],
        "dot": flow("Asset inventory and scans", "Vulnerability and patch data",
                    "Control checks\\nMFA and backups", "Likelihood score",
                    "Impact from sector\\nand population", "Risk ranking\\nand top action",
                    highlight=[3, 4, 5]),
        "formulas": [
            (r"E = \min(1, \tfrac{\text{exposed}}{10}) \quad V = 1 - e^{-(3\,\text{KEV} + "
             r"\text{critical})/10} \quad P = \min(1, \tfrac{\text{patch age}}{180})",
             "Exposure, vulnerability and patch components, each from 0 to 1. Known exploited "
             "vulnerabilities count three times as much as other critical ones."),
            (r"C = 1 - \text{MFA coverage} \quad B = [\text{backup not tested}] \quad "
             r"H = \min(1, \tfrac{\text{incidents}}{5})",
             "Control gap, backup gap and incident history components."),
            (r"L = 0.20E + 0.30V + 0.15P + 0.15C + 0.10B + 0.10H",
             "Likelihood of a damaging compromise, from 0 to 1."),
            (r"I = w_{sector} \times \left(0.5 + 0.5 \min\left(1, "
             r"\tfrac{\log_{10} \text{population}}{7}\right)\right)",
             "Impact. Energy and water carry weight 1.0, healthcare 0.9, communications and "
             "transportation 0.8. Serving ten million people gives the full population factor."),
            (r"\text{Risk} = 100 \times L \times I",
             "Bands: Critical at 60 and above, High from 40, Medium from 20, otherwise Low. The "
             "top action is the component with the largest weighted contribution."),
        ],
    },
    {
        "key": "drone", "tab": "2 Counter drone", "title": "Counter drone incident tracker",
        "gap": "Analysts note that authorities to counter drones have not progressed as needed, "
               "leaving security gaps at airports and critical infrastructure, and that much "
               "critical infrastructure has limited protection against low altitude threats.",
        "what": "Logs drone sightings near protected sites, scores each sighting for threat, "
                "and ranks sites as hotspots using recent sighting volume. The output is "
                "evidence that agencies with legal authority can act on.",
        "benefits": ["Turns scattered reports into patterns and evidence",
                     "Supports resourcing and policy decisions with data",
                     "Highlights payload and night flights that need fast follow up"],
        "fields": DRONE_FIELDS, "generate": drone_generate, "score": drone_score,
        "charts": drone_charts, "id_col": "sighting_id", "default_n": 150,
        "score_col": "threat_score", "score_label": "Threat score", "band_col": "threat_band",
        "band_labels": ["Severe", "Elevated", "Routine"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["sighting_id", "sighting_date", "site_name", "site_type",
                        "distance_to_site_m", "altitude_ft", "threat_score", "threat_band"],
        "dot": flow("Sighting report", "Normalize location\\naltitude and duration",
                    "Threat score per sighting", "Group by site\\nlast 30 days", "Hotspot index",
                    "Referral to agency\\nwith authority", highlight=[2, 4]),
        "formulas": [
            (r"\text{proximity} = \max(0, 1 - \tfrac{d}{3000}) \quad \text{low alt} = "
             r"\min(1, \max(0, \tfrac{1000 - h}{1000})) \quad \text{loiter} = "
             r"\min(1, \tfrac{t}{30})",
             "d is distance to the site in meters, h is altitude in feet, t is minutes observed."),
            (r"\text{base} = 0.25\,\text{prox} + 0.15\,\text{low alt} + 0.15\,\text{loiter} + "
             r"0.20\,\text{payload} + 0.10\,\text{night} + 0.15\,\text{no Remote ID}",
             "Payload, night and Remote ID are yes or no values of 1 or 0."),
            (r"\text{Threat} = \min(100,\ 100 \times \text{base} \times w_{site})",
             "Site weights: airport 1.2, power plant 1.1, prison and water 1.0, stadium 0.9. "
             "Severe at 70 and above, Elevated from 45."),
            (r"\text{Hotspot} = \overline{\text{Threat}} \times (1 + \ln(1 + n_{30}))",
             "Average threat at a site, boosted by the number of sightings in the last 30 days. "
             "The logarithm stops sheer volume from dominating."),
        ],
    },
    {
        "key": "aid", "tab": "3 Disaster aid", "title": "Disaster aid navigator",
        "gap": "GAO reports that state and local officials struggle to navigate multiple "
               "federal recovery programs with differing requirements and time frames.",
        "what": "Matches each community to the recovery programs it appears eligible for, "
                "counts days left in each application window, lists the documents needed, and "
                "scores overall need so help reaches small communities first.",
        "benefits": ["Fewer missed deadlines and rejected applications",
                     "Faster aid to communities without grant staff",
                     "One checklist instead of many program rulebooks"],
        "fields": AID_FIELDS, "generate": aid_generate, "score": aid_score,
        "charts": aid_charts, "id_col": "community_id", "default_n": 40,
        "score_col": "need_score", "score_label": "Need score", "band_col": "need_band",
        "band_labels": ["High need", "Moderate need", "Low need"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["community_id", "community_name", "disaster_type", "need_score",
                        "need_band", "days_to_next_deadline", "windows_missed", "open_programs"],
        "dot": flow("Community profile", "Eligibility rules\\nper program",
                    "Days left in\\neach window", "Document checklist", "Need score",
                    "Prioritized outreach", highlight=[1, 4]),
        "formulas": [
            (r"\text{damage per resident} = \tfrac{\text{damage}}{\text{population}}",
             "Used for program thresholds and need."),
            (r"\text{eligible} = (\text{declared} \lor \lnot\,\text{needs declaration}) \land "
             r"(\text{damage per resident} \ge \text{program minimum})",
             "A program is open when eligible and window days minus days since event is zero or "
             "more."),
            (r"\text{Need} = 100\,(0.35\,D + 0.25\,(1 - \text{insured}) + 0.20\,[\text{no staff}] "
             r"+ 0.20\,(1 - \text{docs}))",
             "D is damage per resident divided by 2000, capped at 1. High need at 60 and above, "
             "Moderate from 35."),
            (r"\text{rejection risk} = 1 - \text{docs complete}",
             "Simple indicator of how likely an application is to be returned."),
        ],
    },
    {
        "key": "border", "tab": "4 Border metrics", "title": "Border security metrics quality dashboard",
        "gap": "By law DHS must report annually on 43 specific border security metrics. GAO "
               "found the 2023 report included data on 40 of them and called for better "
               "metric quality.",
        "what": "Runs four automated quality checks on every metric, completeness, timeliness, "
                "consistency with the prior year and validity, then scores each metric and the "
                "report as a whole.",
        "benefits": ["Complete and on time reports to Congress",
                     "Implausible jumps caught before publication",
                     "Clear data lineage for every number"],
        "fields": BORDER_FIELDS, "generate": border_generate, "score": border_score,
        "charts": border_charts, "id_col": "metric_id", "default_n": 43,
        "score_col": "quality_score", "score_label": "Quality score", "band_col": "quality_band",
        "band_labels": ["Failing", "Needs review", "Good"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["metric_id", "metric_name", "fiscal_year", "value", "check_complete",
                        "check_timely", "check_consistent", "quality_score", "quality_band"],
        "dot": flow("Source systems", "Collect 43 metrics", "Completeness check",
                    "Timeliness check", "Consistency and\\nvalidity checks", "Quality score\\nand report",
                    highlight=[5]),
        "formulas": [
            (r"\text{complete} = [\text{reported} \land \text{value present}] \quad "
             r"\text{timely} = [\text{days since update} \le 90]",
             "Each check is 1 for pass and 0 for fail."),
            (r"\text{change} = \tfrac{|v - v_{prior}|}{\max(1, |v_{prior}|)} \quad "
             r"\text{consistent} = [\text{change} \le 0.5]",
             "A change of more than 50 percent from last year is flagged for review, not "
             "rejected."),
            (r"Q = 100\,(0.40\,\text{complete} + 0.20\,\text{timely} + 0.25\,\text{consistent} "
             r"+ 0.15\,\text{valid})",
             "Good at 85 and above, Needs review from 60, otherwise Failing."),
            (r"\text{Report completeness} = \tfrac{\text{complete metrics}}{43}", ""),
        ],
    },
    {
        "key": "acq", "tab": "5 Acquisitions", "title": "Acquisition program health tracker",
        "gap": "DHS plans to spend at least 55 billion dollars on major acquisition programs. "
               "GAO reviewed 27 major programs in fiscal year 2025 and tracks cost growth and "
               "schedule delays across the portfolio.",
        "what": "Uses earned value to forecast each program's final cost, measures schedule "
                "slip, test results and key performance parameters, and rolls them into a "
                "health score with early breach warnings.",
        "benefits": ["Overruns spotted months earlier", "Consistent portfolio view for leadership",
                     "Test failures linked to cost and schedule risk"],
        "fields": ACQ_FIELDS, "generate": acq_generate, "score": acq_score,
        "charts": acq_charts, "id_col": "program_id", "default_n": 27,
        "score_col": "health_score", "score_label": "Health score", "band_col": "health_band",
        "band_labels": ["Red", "Yellow", "Green"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["program_id", "program_name", "component", "cpi", "eac_musd",
                        "cost_growth", "schedule_slip", "health_score", "health_band"],
        "dot": flow("Baseline cost\\nand schedule", "Spend and percent\\ncomplete",
                    "Earned value and CPI", "Estimate at completion", "Schedule and test\\nperformance",
                    "Health score and\\nbreach warning", highlight=[2, 3, 5]),
        "formulas": [
            (r"EV = \text{percent complete} \times \text{baseline} \quad CPI = "
             r"\tfrac{EV}{\text{actual spent}}",
             "Earned value is the budgeted cost of the work actually done. A CPI below 1 means "
             "each dollar is buying less than a dollar of planned work."),
            (r"EAC = \tfrac{\text{baseline}}{CPI} \quad \text{cost growth} = "
             r"\tfrac{EAC}{\text{baseline}} - 1 \quad \text{slip} = "
             r"\tfrac{\text{forecast months}}{\text{baseline months}} - 1", ""),
            (r"H = 100 - 40\min(1, \tfrac{g}{0.5}) - 30\min(1, \tfrac{s}{0.5}) - "
             r"15(1 - \text{test pass}) - 15(1 - \text{KPP met})",
             "g and s are cost growth and slip, counted only when positive. Green at 75 and "
             "above, Yellow from 55. An early warning appears when cost growth exceeds 15 "
             "percent or slip exceeds 20 percent; these warning levels are illustrative."),
        ],
    },
    {
        "key": "rec", "tab": "6 Recommendations", "title": "Open recommendations tracker",
        "gap": "As of March 2025 GAO had 459 open recommendations to DHS. Of 39 priority "
               "recommendations identified in May 2025, DHS had implemented five by July 2026.",
        "what": "Gives every recommendation an owner, due date and evidence status, then scores "
                "open items for attention based on priority, age, overdue status and missing "
                "evidence.",
        "benefits": ["Clear accountability for each weakness",
                     "Faster closure of long standing priority items",
                     "Audit ready evidence in one place"],
        "fields": REC_FIELDS, "generate": rec_generate, "score": rec_score,
        "charts": rec_charts, "id_col": "rec_id", "default_n": 120,
        "score_col": "risk_score", "score_label": "Attention score", "band_col": "attention_band",
        "band_labels": ["Urgent", "Watch", "On track", "Closed"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32", "#9E9E9E"],
        "report_cols": ["rec_id", "area", "priority", "owner", "age_days", "overdue",
                        "status", "risk_score", "attention_band"],
        "dot": flow("Audit report", "Recommendation\\nwith owner and due date",
                    "Evidence collected", "Attention score", "Leadership review",
                    "Closure by auditors", highlight=[3]),
        "formulas": [
            (r"\text{age} = \text{today} - \text{date issued} \quad \text{overdue} = "
             r"[\text{active} \land \text{due date} < \text{today}]", ""),
            (r"A = 100\,(0.35\,[\text{priority}] + 0.25\min(1, \tfrac{\text{age}}{1095}) + "
             r"0.25\,[\text{overdue}] + 0.15\,(1 - \text{evidence}))",
             "Applies only to Open and In progress items; closed items score 0. Urgent at 60 "
             "and above, Watch from 35. Three years of age gives the full age component."),
            (r"\text{Implementation rate} = \tfrac{\text{implemented}}{\text{all}}", ""),
        ],
    },
    {
        "key": "deepfake", "tab": "7 Deepfake", "title": "Deepfake and impersonation verification",
        "gap": "AI driven threats are listed among the most urgent homeland security challenges "
               "for 2026. Deepfake voices and video can impersonate officials to issue false "
               "emergency directives, redirect funds or get impostors hired.",
        "what": "Fuses content credentials, out of band callback, liveness, artifact detection, "
                "behavior red flags and caller ID into one risk score, raises it for high "
                "consequence requests and enforces hard rules.",
        "benefits": ["Stops fraud and false emergency directives",
                     "Consistent verification habit across staff",
                     "Explainable decision for every case"],
        "fields": DF_FIELDS, "generate": df_generate, "score": df_score,
        "charts": df_charts, "id_col": "case_id", "default_n": 80,
        "score_col": "risk_score", "score_label": "Risk score", "band_col": "decision",
        "band_labels": ["Block and escalate", "Hold and verify", "Proceed"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["case_id", "claimed_identity", "claimed_role", "request_type",
                        "c2pa_status", "oob_status", "risk_score", "decision"],
        "dot": flow("Call or media received", "Content credential\\ncheck",
                    "Callback on directory\\nnumber", "Liveness and\\nartifact scores",
                    "Fused risk score", "Proceed, hold\\nor block", highlight=[4, 5]),
        "formulas": [
            (r"\text{Base} = 100\,(0.20\,r_{prov} + 0.30\,r_{oob} + 0.20\,(1 - \text{live}) + "
             r"0.15\,\text{artifact} + 0.10\,\text{behavior} + 0.05\,r_{cid})",
             "Provenance risk is 0 valid, 0.6 missing, 1 invalid. Callback risk is 0 confirmed, "
             "0.7 not attempted, 1 failed."),
            (r"M = F_{request} + 0.03\,(\text{urgency} - 1) \quad \text{Score} = "
             r"\min(100, \text{Base} \times M)",
             "Request factors: routine 1.00, credential 1.15, emergency directive 1.20, funds "
             "1.25."),
            (r"\text{Rules: invalid credentials} \Rightarrow \ge 70,\ \text{failed callback} "
             r"\Rightarrow \ge 80,\ \text{valid and confirmed} \Rightarrow \le 40",
             "Block at 60 and above, Hold from 30, otherwise Proceed."),
        ],
    },
    {
        "key": "facility", "tab": "8 Facility security",
        "title": "Facility insider threat and supply chain checklist",
        "gap": "Security experts recommend layered controls for homeland security facilities, "
               "including background checks for all personnel, supply chain monitoring and "
               "inspection of critical components such as IT cabling and HVAC systems.",
        "what": "Tracks background check coverage, vendor assessments, high risk vendors, "
                "component inspections, audit age and badge anomalies for each facility, then "
                "scores compliance and exposure and raises specific alerts.",
        "benefits": ["Lower insider and supply chain exposure",
                     "Lapses caught before an incident",
                     "Compliance evidence ready for audits"],
        "fields": FAC_FIELDS, "generate": fac_generate, "score": fac_score,
        "charts": fac_charts, "id_col": "facility_id", "default_n": 50,
        "score_col": "exposure_score", "score_label": "Exposure score", "band_col": "exposure_band",
        "band_labels": ["High", "Moderate", "Low"],
        "band_colors": ["#B71C1C", "#F9A825", "#2E7D32"],
        "report_cols": ["facility_id", "facility_name", "component", "compliance_score",
                        "exposure_score", "exposure_band", "alerts"],
        "dot": flow("Personnel records", "Vendor assessments", "Component inspections",
                    "Audit and badge logs", "Compliance and\\nexposure scores", "Alerts and\\naction list",
                    highlight=[4, 5]),
        "formulas": [
            (r"\text{bg} = \tfrac{\text{checks current}}{\text{personnel}} \quad \text{va} = "
             r"\tfrac{\text{vendors assessed}}{\text{vendors}} \quad \text{ins} = "
             r"\tfrac{\text{inspected}}{\text{due}} \quad \text{audit} = "
             r"\max(0, 1 - \tfrac{\text{days}}{365})", ""),
            (r"C = 100\,(0.35\,\text{bg} + 0.25\,\text{va} + 0.25\,\text{ins} + "
             r"0.15\,\text{audit})", "Compliance score, higher is better."),
            (r"X = \min(100,\ (100 - C) + 5 \times \text{badge anomalies} + 20 \times "
             r"\tfrac{\text{high risk vendors}}{\text{vendors}})",
             "Exposure score, higher is worse. High at 50 and above, Moderate from 25."),
        ],
    },
]

MODULE_BY_KEY = {m["key"]: m for m in MODULES}


def band_color(module):
    return alt.Color(f"{module['band_col']}:N", title=module["score_label"].replace(
        " score", " band"), scale=alt.Scale(domain=module["band_labels"],
                                            range=module["band_colors"]))


# ==========================================================================
# User interface
# ==========================================================================

def render_header():
    st.markdown(
        f"""
        <div style="padding: 14px 20px; border-bottom: 3px solid #0D47A1;
                    margin-bottom: 18px; background-color: #F4F8FE; border-radius: 6px;">
            <div style="color: #0D47A1; font-size: 34px; font-weight: 800;
                        line-height: 1.2;">{APP_TITLE}</div>
            <div style="color: #1565C0; font-size: 24px; font-weight: 700;
                        line-height: 1.3; margin-top: 4px;">{APP_SUBTITLE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def data_key(module):
    return f"data_{module['key']}"


def ensure_data(module):
    key = data_key(module)
    if key not in st.session_state:
        st.session_state[key] = module["generate"](module["default_n"], 7)
        st.session_state[key + "_source"] = f"Synthetic (default, {module['default_n']} records)"


def render_explanation(module):
    st.subheader(module["title"])
    left, right = st.columns([3, 2])
    with left:
        st.markdown("**The gap**")
        st.write(module["gap"])
        st.markdown("**What this module does**")
        st.write(module["what"])
    with right:
        st.markdown("**Benefits**")
        for b in module["benefits"]:
            st.markdown(f"- {b}")
    st.graphviz_chart(module["dot"], use_container_width=True)


def render_data(module):
    key = data_key(module)
    source = st.radio("Data source", ["Generate synthetic data", "Upload real data (CSV)"],
                      horizontal=True, key=f"src_{module['key']}")
    if source == "Generate synthetic data":
        a, b = st.columns(2)
        n = a.number_input("Number of records", 5, 5000, module["default_n"],
                           key=f"n_{module['key']}")
        seed = b.number_input("Random seed", 0, 99999, 7, key=f"seed_{module['key']}",
                              help="Same seed gives the same data for repeatable demos")
        if st.button("Generate synthetic data", type="primary", key=f"gen_{module['key']}"):
            st.session_state[key] = module["generate"](int(n), int(seed))
            st.session_state[key + "_source"] = f"Synthetic ({int(n)} records, seed {int(seed)})"
            st.success("Synthetic data generated.")
    else:
        template = module["generate"](3, 1)
        st.download_button("Download CSV template", template.to_csv(index=False).encode(),
                           f"{module['key']}_template.csv", "text/csv",
                           key=f"tpl_{module['key']}")
        uploaded = st.file_uploader("Upload CSV", type=["csv"], key=f"up_{module['key']}")
        if uploaded is not None:
            try:
                cleaned, missing = clean_upload(pd.read_csv(uploaded), module["fields"])
                st.session_state[key] = cleaned
                st.session_state[key + "_source"] = f"Uploaded file {uploaded.name}"
                st.success(f"Loaded {len(cleaned)} records.")
                if missing:
                    st.warning("Columns filled with defaults: " + ", ".join(missing))
            except Exception as error:
                st.error(f"Could not read the file: {error}")
    st.caption(f"Current data: {st.session_state[key + '_source']}")
    st.dataframe(st.session_state[key], use_container_width=True, height=300)


def render_results(module):
    scored = module["score"](st.session_state[data_key(module)])
    st.session_state[f"scored_{module['key']}"] = scored
    counts = scored[module["band_col"]].value_counts()
    cols = st.columns(len(module["band_labels"]) + 1)
    cols[0].metric(f"Average {module['score_label'].lower()}",
                   f"{scored[module['score_col']].mean():.1f}")
    for col, label in zip(cols[1:], module["band_labels"]):
        col.metric(label, int(counts.get(label, 0)))
    module["charts"](scored)
    choice = st.multiselect("Show bands", module["band_labels"],
                            default=module["band_labels"], key=f"bands_{module['key']}")
    view = scored[scored[module["band_col"]].isin(choice)]
    ascending = module["key"] in ("border", "acq")
    st.dataframe(view.sort_values(module["score_col"], ascending=ascending),
                 use_container_width=True, height=340)


def render_fields_formulas(module):
    st.markdown("**Field dictionary**")
    st.dataframe(pd.DataFrame(
        [(f["name"], f["kind"], f["meaning"], f["relevance"]) for f in module["fields"]],
        columns=["Field", "Type", "Meaning", "Relevance to the module"]),
        use_container_width=True, hide_index=True)
    st.markdown("**Calculations and formulas**")
    for i, (latex, text) in enumerate(module["formulas"], start=1):
        st.markdown(f"Step {i}")
        st.latex(latex)
        if text:
            st.write(text)


def render_reports(module):
    scored = st.session_state.get(f"scored_{module['key']}")
    if scored is None:
        scored = module["score"](st.session_state[data_key(module)])
    k = module["key"]
    c = st.columns(4)
    c[0].download_button("Download CSV", scored.to_csv(index=False).encode(),
                         f"{k}_results.csv", "text/csv", key=f"csv_{k}")
    c[1].download_button("Download text", export_txt(module, scored), f"{k}_results.txt",
                         "text/plain", key=f"txt_{k}")
    if HAVE_DOCX:
        c[2].download_button("Download Word", export_docx(module, scored), f"{k}_results.docx",
                             "application/vnd.openxmlformats-officedocument."
                             "wordprocessingml.document", key=f"docx_{k}")
    if HAVE_FPDF:
        c[3].download_button("Download PDF", export_pdf(module, scored), f"{k}_results.pdf",
                             "application/pdf", key=f"pdf_{k}")
    st.markdown("**View an existing result file**")
    uploaded = st.file_uploader("Upload a PDF, Word, text or CSV file",
                                type=["pdf", "docx", "txt", "csv"], key=f"view_{k}")
    if uploaded is not None:
        kind, content = read_uploaded_document(uploaded)
        if kind == "table":
            st.dataframe(content, use_container_width=True)
        elif kind == "docx":
            text, tables = content
            st.text_area("Document text", text, height=220, key=f"dt_{k}")
            for table in tables:
                st.dataframe(table, use_container_width=True)
        else:
            st.text_area("File contents", content, height=360, key=f"ft_{k}")


def render_module(module):
    ensure_data(module)
    render_explanation(module)
    inner = st.tabs(["Results dashboard", "Data", "Fields and formulas", "Reports"])
    with inner[0]:
        render_results(module)
    with inner[1]:
        render_data(module)
    with inner[2]:
        render_fields_formulas(module)
    with inner[3]:
        render_reports(module)


OVERVIEW_DOT = """digraph G {
    graph [rankdir=LR, bgcolor=transparent, fontname=Helvetica, nodesep=0.25, ranksep=0.9];
    node  [shape=box, style="rounded,filled", fillcolor="#E3ECFA", color="#0D47A1",
           fontname=Helvetica, fontsize=11];
    edge  [color="#0D47A1"];
    D [label="Data\\nsynthetic or uploaded CSV", fillcolor="#FFFFFF"];
    H [label="Shared engine\\nclean, score, band", fillcolor="#BBDEFB"];
    R [label="Reports\\nCSV, text, Word, PDF", fillcolor="#FFFFFF"];
    M1 [label="1 Cyber risk"]; M2 [label="2 Counter drone"]; M3 [label="3 Disaster aid"];
    M4 [label="4 Border metrics"]; M5 [label="5 Acquisitions"]; M6 [label="6 Recommendations"];
    M7 [label="7 Deepfake"]; M8 [label="8 Facility security"];
    D -> H;
    H -> M1; H -> M2; H -> M3; H -> M4; H -> M5; H -> M6; H -> M7; H -> M8;
    M1 -> R; M2 -> R; M3 -> R; M4 -> R; M5 -> R; M6 -> R; M7 -> R; M8 -> R;
}"""


def render_overview():
    st.subheader("Suite overview")
    st.write(
        "Each tab addresses one documented homeland security gap. Every module follows the "
        "same pattern: load synthetic or real data, apply a transparent scoring model, place "
        "each record in a band, chart the results and export a report. Open a tab to see the "
        "gap it addresses, how it works, a flowchart, every field and every formula."
    )
    st.graphviz_chart(OVERVIEW_DOT, use_container_width=True)
    st.markdown("**Common workflow inside every module**")
    st.graphviz_chart(flow("Choose data source", "Validate and clean\\nfields",
                           "Compute components\\n0 to 1", "Weighted score\\n0 to 100",
                           "Assign band", "Charts, tables\\nand exports", highlight=[3, 4]),
                      use_container_width=True)
    rows = []
    for m in MODULES:
        ensure_data(m)
        scored = m["score"](st.session_state[data_key(m)])
        top = m["band_labels"][0]
        rows.append({"Module": m["title"], "Records": len(scored),
                     "In top band": int((scored[m["band_col"]] == top).sum()),
                     "Top band": top, "Gap addressed": m["gap"][:120] + "..."})
    st.markdown("**Current status across modules**")
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    st.markdown("**Sources for the gaps**")
    st.write("GAO Priority Open Recommendations for DHS, report 26 109077, July 2026. GAO DHS "
             "Annual Assessment of major acquisitions, report 26 108118, June 2026. GAO border "
             "security metrics reporting, report 26 108715, June 2026. GAO testimony on key "
             "areas for DHS action, report 25 108165, March 2025. ODNI 2026 Annual Threat "
             "Assessment. Homeland Security Today 2026 threat forecast. IDGA homeland security "
             "challenges for 2026.")


def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    render_header()
    with st.sidebar:
        st.markdown("### About")
        st.write("Eight decision support modules for homeland security mission gaps.")
        st.markdown("### Modules")
        for m in MODULES:
            st.write(m["tab"].split(" ", 1)[0] + ". " + m["title"])
        st.caption("Prototype. Weights, thresholds and program rules are illustrative and must "
                   "be validated against official policy before operational use.")
    tabs = st.tabs(["Overview"] + [m["tab"] for m in MODULES])
    with tabs[0]:
        render_overview()
    for tab, module in zip(tabs[1:], MODULES):
        with tab:
            render_module(module)


if __name__ == "__main__":
    main()