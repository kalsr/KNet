



# AI for Auto Ancillary Units — Casting & Machining
# Single-file Streamlit application.

# Modules:
  # 1. Vision QC — Casting Defect Detection
  # 2. Predictive Maintenance — Machine Health
  # 3. Tool Wear Prediction
  # 4. Demand & Inventory Forecast
  # 5. Energy Optimization
  # 6. Traceability / Root Cause
  # 7. ROI Summary

#Each module has:
  # - Generate Synthetic Data button
  # - Charts / tables
  # - Export to CSV button
  # - Reset Data button


import io
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="AI for Auto Ancillary Units",
    page_icon="⚙️",
    layout="wide",
)

RNG_SEED = 42

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def df_download_button(df: pd.DataFrame, label: str, filename: str, key: str):
    """Render a CSV export button for a dataframe."""
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    st.download_button(
        label=label,
        data=buf.getvalue(),
        file_name=filename,
        mime="text/csv",
        key=key,
        use_container_width=True,
    )


def reset_button(state_key: str, label: str = "🔄 Reset Data", key: str = None):
    if st.button(label, key=key or f"reset_{state_key}"):
        if state_key in st.session_state:
            del st.session_state[state_key]
        st.rerun()


def section_title(emoji: str, title: str, subtitle: str):
    st.markdown(f"## {emoji} {title}")
    st.caption(subtitle)
    st.divider()


def kpi_row(items):
    cols = st.columns(len(items))
    for c, (label, value, delta) in zip(cols, items):
        c.metric(label, value, delta)


# ----------------------------------------------------------------------------
# Synthetic data generators
# ----------------------------------------------------------------------------
def gen_casting_defects(n_days=30, seed=RNG_SEED):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=datetime.today(), periods=n_days)
    defect_types = ["Blowhole", "Shrinkage", "Cold Shut", "Gas Porosity", "Surface Crack"]
    rows = []
    base_rate = 0.035
    for i, d in enumerate(dates):
        produced = rng.integers(800, 1400)
        # rejection rate trending down (simulating AI deployment improving over time)
        trend = base_rate * (1 - 0.5 * i / n_days)
        rejected = int(produced * max(0.01, rng.normal(trend, 0.006)))
        rows.append({
            "Date": d.date(),
            "Produced": produced,
            "Rejected": rejected,
            "Rejection_%": round(100 * rejected / produced, 2),
            "Top_Defect": rng.choice(defect_types, p=[0.30, 0.25, 0.15, 0.20, 0.10]),
            "Melt_Temp_C": round(rng.normal(720, 8), 1),
            "Pour_Temp_C": round(rng.normal(700, 6), 1),
            "Mold_Temp_C": round(rng.normal(180, 10), 1),
            "Humidity_%": round(rng.normal(55, 7), 1),
        })
    return pd.DataFrame(rows)


def gen_machine_health(n_hours=240, seed=RNG_SEED):
    rng = np.random.default_rng(seed + 1)
    machines = ["VMC-01", "VMC-02", "HMC-01", "Press-01", "Press-02"]
    rows = []
    start = datetime.today() - timedelta(hours=n_hours)
    for m in machines:
        degradation_start = rng.integers(int(n_hours * 0.6), n_hours)
        for h in range(n_hours):
            t = start + timedelta(hours=h)
            failing = h > degradation_start
            vib = rng.normal(2.5, 0.3) + (3.0 * (h - degradation_start) / n_hours if failing else 0)
            temp = rng.normal(55, 3) + (15 * (h - degradation_start) / n_hours if failing else 0)
            current = rng.normal(12, 1) + (4 * (h - degradation_start) / n_hours if failing else 0)
            risk = min(99, max(1, (vib / 6 + temp / 90 + current / 18) * 33))
            rows.append({
                "Timestamp": t,
                "Machine": m,
                "Vibration_mm_s": round(vib, 2),
                "Temperature_C": round(temp, 1),
                "Current_A": round(current, 2),
                "Failure_Risk_%": round(risk, 1),
                "Predicted_Days_to_Failure": round(max(0.5, 21 - risk / 5), 1),
            })
    return pd.DataFrame(rows)


def gen_tool_wear(n_records=200, seed=RNG_SEED):
    rng = np.random.default_rng(seed + 2)
    tools = ["Insert-CNMG", "Insert-WNMG", "Drill-12mm", "Boring-Bar", "End-Mill-10mm"]
    rows = []
    for i in range(n_records):
        tool = rng.choice(tools)
        cycles = rng.integers(10, 500)
        wear = min(100, round(cycles / rng.uniform(4, 7) + rng.normal(0, 4), 1))
        wear = max(0, wear)
        spindle_load = round(rng.normal(60, 10) + wear * 0.2, 1)
        vib = round(rng.normal(1.8, 0.4) + wear * 0.02, 2)
        recommended_change = "Change Now" if wear > 80 else ("Monitor" if wear > 55 else "OK")
        rows.append({
            "Tool_ID": f"{tool}-{i%30:02d}",
            "Tool_Type": tool,
            "Cycles_Run": cycles,
            "Wear_%": wear,
            "Spindle_Load_%": spindle_load,
            "Vibration_mm_s": vib,
            "Recommendation": recommended_change,
        })
    return pd.DataFrame(rows)


def gen_demand_forecast(n_weeks=26, seed=RNG_SEED):
    rng = np.random.default_rng(seed + 3)
    parts = ["Bracket-A1", "Housing-B2", "Gear-C3", "Hub-D4"]
    rows = []
    weeks = pd.date_range(end=datetime.today(), periods=n_weeks, freq="W")
    for p in parts:
        base = rng.integers(2000, 6000)
        season_amp = base * 0.15
        for i, w in enumerate(weeks):
            actual = None if i >= n_weeks - 4 else int(
                base + season_amp * np.sin(i / 4) + rng.normal(0, base * 0.05)
            )
            forecast = int(base + season_amp * np.sin(i / 4) + rng.normal(0, base * 0.02))
            rows.append({
                "Week": w.date(),
                "Part": p,
                "Actual_Demand": actual,
                "AI_Forecast": max(0, forecast),
                "Safety_Stock": int(forecast * 0.12),
                "Reorder_Point": int(forecast * 0.35),
            })
    return pd.DataFrame(rows)


def gen_energy(n_days=30, seed=RNG_SEED):
    rng = np.random.default_rng(seed + 4)
    dates = pd.date_range(end=datetime.today(), periods=n_days)
    rows = []
    for d in dates:
        baseline_kwh = rng.normal(4200, 200)
        optimized_kwh = baseline_kwh * rng.uniform(0.82, 0.92)
        rows.append({
            "Date": d.date(),
            "Baseline_kWh": round(baseline_kwh, 0),
            "AI_Optimized_kWh": round(optimized_kwh, 0),
            "Savings_%": round(100 * (1 - optimized_kwh / baseline_kwh), 1),
            "Peak_Load_Shifted_kWh": round(rng.uniform(150, 500), 0),
        })
    return pd.DataFrame(rows)


def gen_traceability(n_events=15, seed=RNG_SEED):
    rng = np.random.default_rng(seed + 5)
    machines = ["VMC-01", "VMC-02", "HMC-01"]
    operators = ["Op-A", "Op-B", "Op-C", "Op-D"]
    rows = []
    for i in range(n_events):
        rows.append({
            "Defect_ID": f"DEF-{1000+i}",
            "Date": (datetime.today() - timedelta(days=rng.integers(0, 30))).date(),
            "Melt_Lot": f"ML-{rng.integers(100,999)}",
            "Machine": rng.choice(machines),
            "Operator": rng.choice(operators),
            "Tool_Used": f"Insert-{rng.integers(1,9)}",
            "Root_Cause_AI": rng.choice([
                "Die temperature deviation",
                "Raw material batch variance",
                "Tool wear beyond threshold",
                "Coolant pressure drop",
                "Operator parameter override",
            ]),
            "Manual_RCA_Time_Hrs": round(rng.uniform(8, 48), 1),
            "AI_RCA_Time_Min": round(rng.uniform(0.3, 3), 1),
        })
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
st.sidebar.title("⚙️ AI Ops Console")
st.sidebar.markdown(
    "Demo dashboard for **casting + machining auto ancillary units** — "
    "scrap reduction, downtime prediction, tool cost, demand forecasting, "
    "energy savings, and root-cause tracing."
)
st.sidebar.divider()
module = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Overview",
        "🔍 Vision QC — Casting Defects",
        "🛠️ Predictive Maintenance",
        "🔧 Tool Wear Prediction",
        "📦 Demand & Inventory Forecast",
        "⚡ Energy Optimization",
        "🧩 Traceability & Root Cause",
        "💰 ROI Summary",
    ],
)
st.sidebar.divider()
st.sidebar.caption("All data on this dashboard is synthetic, generated for demo purposes only.")

# ----------------------------------------------------------------------------
# OVERVIEW
# ----------------------------------------------------------------------------
if module == "🏠 Overview":
    st.title("⚙️ AI for Auto Ancillary Units — Casting & Machining")
    st.markdown(
        """
This app demonstrates where AI creates measurable value on the shop floor of a
**casting + machining auto ancillary unit**: cutting scrap, predicting downtime,
optimizing tool cost, sharpening demand forecasts, trimming energy spend, and
collapsing root-cause analysis from days to minutes.

Use the sidebar to open each module. Every module lets you:
- **Generate synthetic data** to simulate a live shop-floor feed
- **Visualize** the key metrics AI would surface
- **Export to CSV** for further analysis
- **Reset** to clear the simulated data
        """
    )
    st.divider()
    kpi_row([
        ("Casting Rejection", "3.5% → 1.8%", "-48%"),
        ("Machining Tool Cost/Part", "↓ 12–18%", None),
        ("Unplanned Downtime", "↓ 25%", None),
        ("Inventory Reduction", "15–25%", None),
    ])
    st.divider()
    st.markdown("### Module Map")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**🔍 Vision QC**\nCatch blowholes, shrinkage, cold shuts, porosity, cracks.")
        st.markdown("**🛠️ Predictive Maintenance**\nFlag bearing/spindle/die failures 2–4 weeks early.")
    with c2:
        st.markdown("**🔧 Tool Wear**\nReplace inserts on condition, not fixed schedule.")
        st.markdown("**📦 Demand Forecast**\nForecast FG/RM better than Excel for JIT OEM supply.")
    with c3:
        st.markdown("**⚡ Energy Optimization**\nShift furnace/machining load to cut bills 8–20%.")
        st.markdown("**🧩 Root Cause**\nCorrelate batch, machine, tool, operator in seconds.")

# ----------------------------------------------------------------------------
# 1. VISION QC
# ----------------------------------------------------------------------------
elif module == "🔍 Vision QC — Casting Defects":
    section_title("🔍", "Vision QC — Casting Defect Detection",
                  "Computer-vision style defect tracking: blowholes, shrinkage, cold shuts, porosity, cracks.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_days = st.slider("Days of shop-floor data to simulate", 7, 90, 30)
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_casting", use_container_width=True):
            st.session_state["casting_df"] = gen_casting_defects(n_days)

    if "casting_df" not in st.session_state:
        st.session_state["casting_df"] = gen_casting_defects(n_days)

    df = st.session_state["casting_df"]

    kpi_row([
        ("Avg Rejection %", f"{df['Rejection_%'].mean():.2f}%", None),
        ("Total Produced", f"{df['Produced'].sum():,}", None),
        ("Total Rejected", f"{df['Rejected'].sum():,}", None),
        ("Most Common Defect", df["Top_Defect"].mode()[0], None),
    ])

    st.markdown("#### Rejection % Trend (AI flags drift before it becomes a batch problem)")
    st.line_chart(df.set_index("Date")[["Rejection_%"]])

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("#### Defect Type Distribution")
        st.bar_chart(df["Top_Defect"].value_counts())
    with cc2:
        st.markdown("#### Process Parameters vs Rejection")
        st.scatter_chart(df, x="Pour_Temp_C", y="Rejection_%")

    st.markdown("#### Raw Data")
    st.dataframe(df, use_container_width=True, height=280)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "casting_defects.csv", "dl_casting")
    with b2:
        reset_button("casting_df", key="reset_casting")

# ----------------------------------------------------------------------------
# 2. PREDICTIVE MAINTENANCE
# ----------------------------------------------------------------------------
elif module == "🛠️ Predictive Maintenance":
    section_title("🛠️", "Predictive Maintenance — Machine Health",
                  "Vibration, temperature, current sensors → failure-risk scoring for VMC/HMC/Press machines.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_hours = st.slider("Hours of sensor history to simulate", 48, 720, 240, step=24)
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_health", use_container_width=True):
            st.session_state["health_df"] = gen_machine_health(n_hours)

    if "health_df" not in st.session_state:
        st.session_state["health_df"] = gen_machine_health(n_hours)

    df = st.session_state["health_df"]
    machine_sel = st.selectbox("Select machine", sorted(df["Machine"].unique()))
    mdf = df[df["Machine"] == machine_sel].sort_values("Timestamp")

    latest = mdf.iloc[-1]
    kpi_row([
        ("Current Failure Risk", f"{latest['Failure_Risk_%']:.0f}%", None),
        ("Predicted Days to Failure", f"{latest['Predicted_Days_to_Failure']:.1f} d", None),
        ("Vibration", f"{latest['Vibration_mm_s']} mm/s", None),
        ("Temperature", f"{latest['Temperature_C']} °C", None),
    ])

    st.markdown(f"#### Failure Risk Trend — {machine_sel}")
    st.line_chart(mdf.set_index("Timestamp")[["Failure_Risk_%"]])

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("#### Vibration & Current")
        st.line_chart(mdf.set_index("Timestamp")[["Vibration_mm_s", "Current_A"]])
    with cc2:
        st.markdown("#### Temperature")
        st.line_chart(mdf.set_index("Timestamp")[["Temperature_C"]])

    if latest["Failure_Risk_%"] > 65:
        st.error(f"⚠️ {machine_sel} is showing elevated failure risk — schedule maintenance within "
                  f"{latest['Predicted_Days_to_Failure']:.1f} days.")
    elif latest["Failure_Risk_%"] > 40:
        st.warning(f"🟡 {machine_sel} risk trending up — monitor closely.")
    else:
        st.success(f"🟢 {machine_sel} operating within normal parameters.")

    st.markdown("#### Raw Data")
    st.dataframe(df, use_container_width=True, height=280)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "machine_health.csv", "dl_health")
    with b2:
        reset_button("health_df", key="reset_health")

# ----------------------------------------------------------------------------
# 3. TOOL WEAR
# ----------------------------------------------------------------------------
elif module == "🔧 Tool Wear Prediction":
    section_title("🔧", "Tool Wear Prediction",
                  "Spindle load, vibration, and cycle count → condition-based insert/tool replacement.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_records = st.slider("Number of tools to simulate", 50, 500, 200, step=50)
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_tool", use_container_width=True):
            st.session_state["tool_df"] = gen_tool_wear(n_records)

    if "tool_df" not in st.session_state:
        st.session_state["tool_df"] = gen_tool_wear(n_records)

    df = st.session_state["tool_df"]

    kpi_row([
        ("Avg Wear %", f"{df['Wear_%'].mean():.1f}%", None),
        ("Tools to Change Now", int((df["Recommendation"] == "Change Now").sum()), None),
        ("Tools to Monitor", int((df["Recommendation"] == "Monitor").sum()), None),
        ("Tools OK", int((df["Recommendation"] == "OK").sum()), None),
    ])

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown("#### Wear % by Tool Type")
        st.bar_chart(df.groupby("Tool_Type")["Wear_%"].mean())
    with cc2:
        st.markdown("#### Spindle Load vs Wear")
        st.scatter_chart(df, x="Wear_%", y="Spindle_Load_%")

    st.markdown("#### Tools Needing Attention")
    st.dataframe(
        df[df["Recommendation"] != "OK"].sort_values("Wear_%", ascending=False),
        use_container_width=True, height=240,
    )

    st.markdown("#### Full Tool Data")
    st.dataframe(df, use_container_width=True, height=280)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "tool_wear.csv", "dl_tool")
    with b2:
        reset_button("tool_df", key="reset_tool")

# ----------------------------------------------------------------------------
# 4. DEMAND & INVENTORY FORECAST
# ----------------------------------------------------------------------------
elif module == "📦 Demand & Inventory Forecast":
    section_title("📦", "Demand & Inventory Forecast",
                  "AI forecast vs actual demand by part, with safety stock and reorder points.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_weeks = st.slider("Weeks of history to simulate", 12, 52, 26)
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_demand", use_container_width=True):
            st.session_state["demand_df"] = gen_demand_forecast(n_weeks)

    if "demand_df" not in st.session_state:
        st.session_state["demand_df"] = gen_demand_forecast(n_weeks)

    df = st.session_state["demand_df"]
    part_sel = st.selectbox("Select part", sorted(df["Part"].unique()))
    pdf_ = df[df["Part"] == part_sel].sort_values("Week")

    valid = pdf_.dropna(subset=["Actual_Demand"])
    mape = (abs(valid["Actual_Demand"] - valid["AI_Forecast"]) / valid["Actual_Demand"]).mean() * 100

    kpi_row([
        ("Forecast Accuracy (MAPE)", f"{100 - mape:.1f}%", None),
        ("Latest Safety Stock", int(pdf_.iloc[-1]["Safety_Stock"]), None),
        ("Latest Reorder Point", int(pdf_.iloc[-1]["Reorder_Point"]), None),
        ("Avg Weekly Demand", f"{valid['Actual_Demand'].mean():.0f}", None),
    ])

    st.markdown(f"#### Actual vs AI Forecast — {part_sel}")
    st.line_chart(pdf_.set_index("Week")[["Actual_Demand", "AI_Forecast"]])

    st.markdown("#### Safety Stock & Reorder Point")
    st.line_chart(pdf_.set_index("Week")[["Safety_Stock", "Reorder_Point"]])

    st.markdown("#### Raw Data")
    st.dataframe(df, use_container_width=True, height=280)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "demand_forecast.csv", "dl_demand")
    with b2:
        reset_button("demand_df", key="reset_demand")

# ----------------------------------------------------------------------------
# 5. ENERGY OPTIMIZATION
# ----------------------------------------------------------------------------
elif module == "⚡ Energy Optimization":
    section_title("⚡", "Energy Optimization",
                  "Baseline vs AI-optimized furnace/machining load, with peak-shift savings.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_days = st.slider("Days of energy data to simulate", 7, 90, 30, key="energy_days")
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_energy", use_container_width=True):
            st.session_state["energy_df"] = gen_energy(n_days)

    if "energy_df" not in st.session_state:
        st.session_state["energy_df"] = gen_energy(n_days)

    df = st.session_state["energy_df"]

    total_baseline = df["Baseline_kWh"].sum()
    total_optimized = df["AI_Optimized_kWh"].sum()
    savings_pct = 100 * (1 - total_optimized / total_baseline)

    kpi_row([
        ("Total Baseline kWh", f"{total_baseline:,.0f}", None),
        ("Total AI-Optimized kWh", f"{total_optimized:,.0f}", None),
        ("Avg Savings %", f"{savings_pct:.1f}%", None),
        ("Peak Load Shifted (avg/day)", f"{df['Peak_Load_Shifted_kWh'].mean():.0f} kWh", None),
    ])

    st.markdown("#### Baseline vs AI-Optimized Consumption")
    st.line_chart(df.set_index("Date")[["Baseline_kWh", "AI_Optimized_kWh"]])

    st.markdown("#### Daily Savings %")
    st.bar_chart(df.set_index("Date")[["Savings_%"]])

    st.markdown("#### Raw Data")
    st.dataframe(df, use_container_width=True, height=280)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "energy_optimization.csv", "dl_energy")
    with b2:
        reset_button("energy_df", key="reset_energy")

# ----------------------------------------------------------------------------
# 6. TRACEABILITY / ROOT CAUSE
# ----------------------------------------------------------------------------
elif module == "🧩 Traceability & Root Cause":
    section_title("🧩", "Traceability & Root Cause Analysis",
                  "AI correlates melt lot, machine, tool, and operator to find root cause in seconds.")

    c1, c2 = st.columns([3, 1])
    with c1:
        n_events = st.slider("Number of defect events to simulate", 5, 50, 15)
    with c2:
        st.write("")
        if st.button("▶️ Generate Synthetic Data", key="gen_trace", use_container_width=True):
            st.session_state["trace_df"] = gen_traceability(n_events)

    if "trace_df" not in st.session_state:
        st.session_state["trace_df"] = gen_traceability(n_events)

    df = st.session_state["trace_df"]

    kpi_row([
        ("Avg Manual RCA Time", f"{df['Manual_RCA_Time_Hrs'].mean():.1f} hrs", None),
        ("Avg AI RCA Time", f"{df['AI_RCA_Time_Min'].mean():.1f} min", None),
        ("Speed-up Factor", f"{(df['Manual_RCA_Time_Hrs'].mean()*60/df['AI_RCA_Time_Min'].mean()):.0f}x", None),
        ("Top Root Cause", df["Root_Cause_AI"].mode()[0], None),
    ])

    st.markdown("#### Root Cause Frequency")
    st.bar_chart(df["Root_Cause_AI"].value_counts())

    st.markdown("#### Manual vs AI RCA Time (per event)")
    comp = df[["Defect_ID", "Manual_RCA_Time_Hrs"]].copy()
    comp["AI_RCA_Time_Hrs"] = df["AI_RCA_Time_Min"] / 60
    st.bar_chart(comp.set_index("Defect_ID")[["Manual_RCA_Time_Hrs", "AI_RCA_Time_Hrs"]])

    st.markdown("#### Event Log")
    st.dataframe(df, use_container_width=True, height=300)

    b1, b2 = st.columns(2)
    with b1:
        df_download_button(df, "⬇️ Export CSV", "traceability_rca.csv", "dl_trace")
    with b2:
        reset_button("trace_df", key="reset_trace")

# ----------------------------------------------------------------------------
# 7. ROI SUMMARY
# ----------------------------------------------------------------------------
elif module == "💰 ROI Summary":
    section_title("💰", "ROI Summary",
                  "Typical results reported by Indian auto ancillary units after AI deployment.")

    roi_df = pd.DataFrame([
        {"Area": "Casting Rejection Rate", "Before": "3.5%", "After": "1.8%", "Improvement": "-48%"},
        {"Area": "Machining Tool Cost / Part", "Before": "Baseline", "After": "↓ 12–18%", "Improvement": "12-18%"},
        {"Area": "Unplanned Downtime", "Before": "Baseline", "After": "↓ 25%", "Improvement": "25%"},
        {"Area": "Inventory / Working Capital", "Before": "Baseline", "After": "↓ 15–25%", "Improvement": "15-25%"},
        {"Area": "Energy Bill", "Before": "Baseline", "After": "↓ 8–20%", "Improvement": "8-20%"},
        {"Area": "Customer Complaints (Vision QC)", "Before": "Baseline", "After": "↓ 50–80%", "Improvement": "50-80%"},
        {"Area": "Root Cause Analysis Time", "Before": "~2 days", "After": "~30 sec", "Improvement": ">99%"},
    ])

    st.dataframe(roi_df, use_container_width=True, height=300)

    st.markdown("#### Suggested Rollout Sequence (Low Budget First)")
    st.markdown(
        """
1. **Vision QC pilot** — 2–3 cameras + off-the-shelf vision software on highest-rejection line. Fastest ROI, easiest operator buy-in.
2. **Sensor retrofit** — vibration + current sensors on top 3 bottleneck machines (~₹50k/machine).
3. **Use existing data** — CMM logs, rejection logs, tool-change sheets feed the first predictive models.
4. **Scale to scheduling, demand forecasting, and energy** once shop floor trusts the QC/maintenance pilots.
        """
    )

    df_download_button(roi_df, "⬇️ Export ROI Summary CSV", "roi_summary.csv", "dl_roi")

st.sidebar.divider()
st.sidebar.caption("Demo build · All figures synthetic / illustrative · Not a substitute for a site-specific audit.")