# THIS CUSTOMER RELATION SHIP MANAGEMENT APP IS DEVELOPED BY RANDY SINGH FROM KNET CONSUTINGS

# python
import streamlit as st
import pandas as pd
import numpy as np
import json
import random
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="CRM Dashboard", layout="wide")

# ---- Session State ----
if "clients" not in st.session_state:
    st.session_state.clients = pd.DataFrame()
if "invoices" not in st.session_state:
    st.session_state.invoices = pd.DataFrame()
if "tickets" not in st.session_state:
    st.session_state.tickets = pd.DataFrame()
if "log" not in st.session_state:
    st.session_state.log = []


# ---- Helpers ----
def log(msg: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.log.append(f"[{timestamp}] {msg}")


def generate_dummy_data():
    domains = ["example.com", "contoso.com", "fabrikam.org", "acme.co", "globex.net"]
    issues = ["System Crash", "Login Failure", "Email Down", "Slow Network", "Payment Error", "Access Denied"]
    priorities = ["Low", "Medium", "High"]
    t_statuses = ["Open", "In-Progress", "Resolved", "Closed"]
    i_statuses = ["Unpaid", "Paid"]

    # Clients
    clients = []
    for i in range(1, 51):
        domain = random.choice(domains)
        email = f"client{i}@{domain}"
        phone = f"+1-555-{1000+i}"
        clients.append([i, f"Client {i}", email, phone])
    df_clients = pd.DataFrame(clients, columns=["ID", "Name", "Email", "Phone"])

    # Invoices
    invoices = []
    for i in range(1, 51):
        client = random.choice(df_clients["Name"])
        amount = random.randint(500, 7500)
        due = (datetime.now() + timedelta(days=random.randint(1, 45))).strftime("%Y-%m-%d")
        status = random.choice(i_statuses)
        invoices.append([i, client, amount, due, status])
    df_invoices = pd.DataFrame(invoices, columns=["InvoiceID", "Client", "Amount", "DueDate", "Status"])

    # Tickets
    tickets = []
    for i in range(1, 51):
        client = random.choice(df_clients["Name"])
        issue = random.choice(issues)
        pri = random.choice(priorities)
        stat = random.choice(t_statuses)
        date = (datetime.now() - timedelta(days=random.randint(0, 20))).strftime("%Y-%m-%d")
        tickets.append([i, client, issue, pri, stat, date])
    df_tickets = pd.DataFrame(tickets, columns=["TicketID", "Client", "Issue", "Priority", "Status", "Date"])

    st.session_state.clients = df_clients
    st.session_state.invoices = df_invoices
    st.session_state.tickets = df_tickets
    log("Generated 50 Clients, 50 Invoices, 50 Tickets")


def export_csv(df: pd.DataFrame, filename: str):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"⬇️ Download {filename}",
        data=csv,
        file_name=filename,
        mime="text/csv",
    )


def save_json():
    data = {
        "clients": st.session_state.clients.to_dict(orient="records"),
        "invoices": st.session_state.invoices.to_dict(orient="records"),
        "tickets": st.session_state.tickets.to_dict(orient="records"),
    }
    json_str = json.dumps(data, indent=2)
    st.download_button("💾 Save JSON", json_str, file_name="crm_data.json", mime="application/json")


def load_json(uploaded_file):
    if uploaded_file is not None:
        try:
            content = uploaded_file.read().decode("utf-8")
            obj = json.loads(content)
            st.session_state.clients = pd.DataFrame(obj.get("clients", []))
            st.session_state.invoices = pd.DataFrame(obj.get("invoices", []))
            st.session_state.tickets = pd.DataFrame(obj.get("tickets", []))
            log("Loaded data from uploaded JSON")
        except Exception as e:
            st.error(f"Error loading JSON: {e}")


# ---- UI ----
st.title("📊 CRM Dashboard")

toolbar = st.container()
with toolbar:
    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button("Generate Dummy Data ✅"):
        generate_dummy_data()
    if col2.button("Reset View 🔄"):
        log("Reset view")
    if col3.button("Clear Filters 🧹"):
        log("Cleared filters (UI refresh)")
    save_json()
    uploaded = col5.file_uploader("Load JSON", type=["json"], label_visibility="collapsed")
    if uploaded:
        load_json(uploaded)

# ---- Executive Summary ----
if not st.session_state.invoices.empty and not st.session_state.tickets.empty:
    st.subheader("📌 Executive Summary")
    total_invoices = len(st.session_state.invoices)
    unpaid_invoices = len(st.session_state.invoices[st.session_state.invoices["Status"] == "Unpaid"])
    total_revenue = st.session_state.invoices["Amount"].sum()
    paid_revenue = st.session_state.invoices[st.session_state.invoices["Status"] == "Paid"]["Amount"].sum()
    total_tickets = len(st.session_state.tickets)
    resolved_tickets = len(st.session_state.tickets[st.session_state.tickets["Status"].isin(["Resolved", "Closed"])])

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
    kpi1.metric("Total Invoices", total_invoices)
    kpi2.metric("Unpaid Invoices", unpaid_invoices)
    kpi3.metric("Total Revenue", f"${total_revenue:,.0f}")
    kpi4.metric("Paid Revenue", f"${paid_revenue:,.0f}")
    kpi5.metric("Ticket Resolution Rate", f"{(resolved_tickets/total_tickets*100):.1f}%" if total_tickets else "0%")

# Tabs for Clients, Invoices, Tickets, Charts
tabs = st.tabs(["👥 Clients", "🧾 Invoices", "🎫 Tickets", "📈 Charts"])

with tabs[0]:
    st.subheader("Clients")
    if not st.session_state.clients.empty:
        domain = st.selectbox("Filter by Email Domain", [""] + sorted({e.split("@")[-1] for e in st.session_state.clients["Email"]}))
        df = st.session_state.clients
        if domain:
            df = df[df["Email"].str.endswith("@" + domain)]
            log(f"Filtered clients by domain: {domain}")
        st.dataframe(df, use_container_width=True, height=400)
        export_csv(df, "clients.csv")

with tabs[1]:
    st.subheader("Invoices")
    if not st.session_state.invoices.empty:
        status = st.selectbox("Status", [""] + sorted(st.session_state.invoices["Status"].unique()))
        min_amt = st.number_input("Min Amount", value=0)
        max_amt = st.number_input("Max Amount", value=10000)
        df = st.session_state.invoices
        if status:
            df = df[df["Status"] == status]
        df = df[(df["Amount"] >= min_amt) & (df["Amount"] <= max_amt)]
        st.dataframe(df, use_container_width=True, height=400)
        export_csv(df, "invoices.csv")

with tabs[2]:
    st.subheader("Tickets")
    if not st.session_state.tickets.empty:
        pri = st.selectbox("Priority", [""] + sorted(st.session_state.tickets["Priority"].unique()))
        stat = st.selectbox("Status", [""] + sorted(st.session_state.tickets["Status"].unique()))
        df = st.session_state.tickets
        if pri:
            df = df[df["Priority"] == pri]
        if stat:
            df = df[df["Status"] == stat]
        st.dataframe(df, use_container_width=True, height=400)
        export_csv(df, "tickets.csv")

with tabs[3]:
    st.subheader("📊 Visual Insights")
    if not st.session_state.invoices.empty:
        st.markdown("**Invoices by Status**")
        fig1 = px.bar(st.session_state.invoices.groupby("Status")["Amount"].sum().reset_index(),
                      x="Status", y="Amount", color="Status", title="Total Invoice Amount by Status")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("**Top 10 Clients by Invoice Amount**")
        top_clients = st.session_state.invoices.groupby("Client")["Amount"].sum().nlargest(10).reset_index()
        fig2 = px.bar(top_clients, x="Amount", y="Client", orientation="h",
                      title="Top Clients by Invoice Amount", text="Amount")
        st.plotly_chart(fig2, use_container_width=True)

    if not st.session_state.tickets.empty:
        st.markdown("**Tickets by Priority**")
        fig3 = px.pie(st.session_state.tickets, names="Priority", title="Ticket Distribution by Priority")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("**Tickets by Status Over Time**")
        df_timeline = st.session_state.tickets.groupby(["Date", "Status"]).size().reset_index(name="Count")
        fig4 = px.line(df_timeline, x="Date", y="Count", color="Status", markers=True,
                       title="Tickets by Status Over Time")
        st.plotly_chart(fig4, use_container_width=True)

# ---- Activity Log ----
st.subheader("📝 Activity Log")
st.text_area("Log", "\n".join(st.session_state.log[-50:]), height=200)
