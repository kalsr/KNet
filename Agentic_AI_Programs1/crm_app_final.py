
# light, professional theme (no dark).
# Scrollable tables (Treeviews with scrollbars) and a scrollable Activity Log.
# Colored buttons via `ttkbootstrap` (`success`, `primary`, `warning`, etc.).
# Dummy data generator (50 Clients, 50 Invoices, 50 Tickets) and auto-save to `crm_data.json`.
# Search, per-tab filters, and Reset/Clear Filters.
# Save/Load JSON** (with file dialogs) and Export CSV (per-tab + all).

# python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# 3rd-party modern theming (light theme, colored buttons)
# pip install ttkbootstrap
import ttkbootstrap as tb


class CRMApp:
    def __init__(self, root: tb.Window):
        self.root = root
        self.root.title("CRM Dashboard")
        self.root.geometry("1300x820")
        self.root.minsize(1100, 700)

        # Use a LIGHT theme (no dark): flatly/litera/cosmo/journal/sandstone
        tb.Style("flatly")

        # ---- Data containers ----
        self.clients = []   # tuples: (ID, Name, Email, Phone)
        self.invoices = []  # tuples: (InvoiceID, Client, Amount, DueDate, Status)
        self.tickets = []   # tuples: (TicketID, Client, Issue, Priority, Status, Date)

        # ---- Overall Layout ----
        # Top toolbar
        self._build_toolbar()

        # Center split: tabs (left) + activity log (right)
        self._build_center()

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        self._build_statusbar()

        # Initialize filter state
        self._reset_filters()

    # ========================= UI: Toolbar =========================
    def _build_toolbar(self):
        bar = ttk.Frame(self.root, padding=(10, 8))
        bar.pack(fill="x")

        # Left group
        tb.Button(bar, text="Generate Dummy Data", bootstyle="success",
                  command=self.generate_dummy_data).pack(side="left", padx=4)
        tb.Button(bar, text="Reset View", bootstyle="secondary",
                  command=self.reset_view).pack(side="left", padx=4)
        tb.Button(bar, text="Clear Filters", bootstyle="warning",
                  command=self.clear_filters).pack(side="left", padx=4)

        # Middle group
        ttk.Separator(bar, orient="vertical").pack(side="left", fill="y", padx=8)
        tb.Button(bar, text="Save JSON", bootstyle="info",
                  command=self.save_json_dialog).pack(side="left", padx=4)
        tb.Button(bar, text="Load JSON", bootstyle="primary",
                  command=self.load_json_dialog).pack(side="left", padx=4)
        ttk.Separator(bar, orient="vertical").pack(side="left", fill="y", padx=8)
        tb.Button(bar, text="Export ALL CSV", bootstyle="outline",
                  command=self.export_all_csv).pack(side="left", padx=4)

        # Right group: Search box (applies to current tab)
        ttk.Separator(bar, orient="vertical").pack(side="right", fill="y", padx=8)
        tb.Button(bar, text="Search", bootstyle="dark",
                  command=self.search_current_tab).pack(side="right", padx=(4, 10))
        self.search_var = tk.StringVar()
        ttk.Entry(bar, textvariable=self.search_var, width=28).pack(side="right")

    # ========================= UI: Center (Tabs + Log) =========================
    def _build_center(self):
        paned = ttk.Panedwindow(self.root, orient="horizontal")
        paned.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        left = ttk.Frame(paned)
        right = ttk.Frame(paned)
        paned.add(left, weight=4)
        paned.add(right, weight=1)

        # Tabs (Clients, Invoices, Tickets)
        self.tabs = ttk.Notebook(left)
        self.tabs.pack(fill="both", expand=True)
        self.tabs.bind("<<NotebookTabChanged>>", lambda e: self._on_tab_change())

        # Build each tab
        self._build_clients_tab()
        self._build_invoices_tab()
        self._build_tickets_tab()

        # Activity log (scrollable)
        ttk.Label(right, text="Activity Log", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(4, 6))
        self.log_text = tk.Text(right, height=10, wrap="word")
        self.log_text.pack(fill="both", expand=True)
        yscroll = ttk.Scrollbar(self.log_text, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=yscroll.set)
        # Place scrollbar on the side of the Text
        yscroll.pack(side="right", fill="y")

    # ========================= UI: Statusbar =========================
    def _build_statusbar(self):
        status = ttk.Frame(self.root)
        status.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Label(status, textvariable=self.status_var).pack(anchor="w")

    # ========================= Helpers: Logging/Status =========================
    def log(self, msg: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {msg}\n")
        self.log_text.see("end")

    def set_status(self, msg: str):
        self.status_var.set(msg)

    # ========================= Tab: Clients =========================
    def _build_clients_tab(self):
        tab = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(tab, text="Clients")

        # Filters row
        filters = ttk.Frame(tab)
        filters.pack(fill="x", pady=(0, 8))

        ttk.Label(filters, text="Email Domain:").pack(side="left", padx=(0, 6))
        self.client_domain_var = tk.StringVar()
        self.client_domain_cb = ttk.Combobox(filters, textvariable=self.client_domain_var, width=18, state="readonly")
        self.client_domain_cb.pack(side="left")

        tb.Button(filters, text="Apply Filters", bootstyle="secondary",
                  command=self.apply_client_filters).pack(side="left", padx=6)
        tb.Button(filters, text="Export CSV", bootstyle="outline",
                  command=self.export_clients_csv).pack(side="left", padx=6)

        # Treeview + scrollbar (scrollable)
        cols = ("ID", "Name", "Email", "Phone")
        self.client_tree = ttk.Treeview(tab, columns=cols, show="headings", height=18)
        for c, w in zip(cols, (100, 240, 280, 160)):
            self.client_tree.heading(c, text=c)
            self.client_tree.column(c, width=w, anchor="w")
        self.client_tree.pack(fill="both", expand=True)

        client_scroll = ttk.Scrollbar(self.client_tree, orient="vertical", command=self.client_tree.yview)
        self.client_tree.configure(yscrollcommand=client_scroll.set)
        client_scroll.pack(side="right", fill="y")

    def apply_client_filters(self):
        domain = self.client_domain_var.get().strip()
        data = self.clients
        self._populate_tree(self.client_tree, [
            row for row in data if (not domain or row[2].lower().endswith("@" + domain.lower()))
        ])
        self.log(f"Clients filtered by domain: {domain or 'All'}")
        self.set_status("Clients filter applied")

    # ========================= Tab: Invoices =========================
    def _build_invoices_tab(self):
        tab = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(tab, text="Invoices")

        # Filters row
        filters = ttk.Frame(tab)
        filters.pack(fill="x", pady=(0, 8))

        ttk.Label(filters, text="Status:").pack(side="left", padx=(0, 6))
        self.inv_status_var = tk.StringVar()
        self.inv_status_cb = ttk.Combobox(filters, textvariable=self.inv_status_var, width=14, state="readonly")
        self.inv_status_cb.pack(side="left")

        ttk.Label(filters, text="Min Amount:").pack(side="left", padx=(10, 6))
        self.inv_min_amt = tk.StringVar()
        ttk.Entry(filters, textvariable=self.inv_min_amt, width=10).pack(side="left")

        ttk.Label(filters, text="Max Amount:").pack(side="left", padx=(10, 6))
        self.inv_max_amt = tk.StringVar()
        ttk.Entry(filters, textvariable=self.inv_max_amt, width=10).pack(side="left")

        tb.Button(filters, text="Apply Filters", bootstyle="secondary",
                  command=self.apply_invoice_filters).pack(side="left", padx=6)
        tb.Button(filters, text="Export CSV", bootstyle="outline",
                  command=self.export_invoices_csv).pack(side="left", padx=6)

        # Treeview + scrollbar
        cols = ("Invoice ID", "Client", "Amount", "Due Date", "Status")
        self.inv_tree = ttk.Treeview(tab, columns=cols, show="headings", height=18)
        for c, w in zip(cols, (120, 260, 120, 140, 120)):
            self.inv_tree.heading(c, text=c)
            self.inv_tree.column(c, width=w, anchor="w")
        self.inv_tree.pack(fill="both", expand=True)

        inv_scroll = ttk.Scrollbar(self.inv_tree, orient="vertical", command=self.inv_tree.yview)
        self.inv_tree.configure(yscrollcommand=inv_scroll.set)
        inv_scroll.pack(side="right", fill="y")

    def apply_invoice_filters(self):
        status = self.inv_status_var.get().strip()
        min_amt = self._safe_float(self.inv_min_amt.get())
        max_amt = self._safe_float(self.inv_max_amt.get())

        def ok_amount(a):
            if min_amt is not None and a < min_amt:
                return False
            if max_amt is not None and a > max_amt:
                return False
            return True

        data = self.invoices
        filtered = []
        for row in data:
            amt = float(row[2])
            if (not status or row[4] == status) and ok_amount(amt):
                filtered.append(row)
        self._populate_tree(self.inv_tree, filtered)
        self.log(f"Invoices filtered: Status={status or 'All'}, "
                 f"Min={min_amt if min_amt is not None else '-'}, "
                 f"Max={max_amt if max_amt is not None else '-'}")
        self.set_status("Invoices filter applied")

    # ========================= Tab: Tickets =========================
    def _build_tickets_tab(self):
        tab = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(tab, text="Tickets")

        # Filters row
        filters = ttk.Frame(tab)
        filters.pack(fill="x", pady=(0, 8))

        ttk.Label(filters, text="Priority:").pack(side="left", padx=(0, 6))
        self.tkt_pri_var = tk.StringVar()
        self.tkt_pri_cb = ttk.Combobox(filters, textvariable=self.tkt_pri_var, width=12, state="readonly")
        self.tkt_pri_cb.pack(side="left")

        ttk.Label(filters, text="Status:").pack(side="left", padx=(10, 6))
        self.tkt_stat_var = tk.StringVar()
        self.tkt_stat_cb = ttk.Combobox(filters, textvariable=self.tkt_stat_var, width=14, state="readonly")
        self.tkt_stat_cb.pack(side="left")

        tb.Button(filters, text="Apply Filters", bootstyle="secondary",
                  command=self.apply_ticket_filters).pack(side="left", padx=6)
        tb.Button(filters, text="Export CSV", bootstyle="outline",
                  command=self.export_tickets_csv).pack(side="left", padx=6)

        # Treeview + scrollbar
        cols = ("Ticket ID", "Client", "Issue", "Priority", "Status", "Date")
        self.tkt_tree = ttk.Treeview(tab, columns=cols, show="headings", height=18)
        for c, w in zip(cols, (110, 220, 260, 110, 120, 140)):
            self.tkt_tree.heading(c, text=c)
            self.tkt_tree.column(c, width=w, anchor="w")
        self.tkt_tree.pack(fill="both", expand=True)

        tkt_scroll = ttk.Scrollbar(self.tkt_tree, orient="vertical", command=self.tkt_tree.yview)
        self.tkt_tree.configure(yscrollcommand=tkt_scroll.set)
        tkt_scroll.pack(side="right", fill="y")

    def apply_ticket_filters(self):
        pri = self.tkt_pri_var.get().strip()
        stat = self.tkt_stat_var.get().strip()
        data = self.tickets
        self._populate_tree(self.tkt_tree, [
            row for row in data if (not pri or row[3] == pri) and (not stat or row[4] == stat)
        ])
        self.log(f"Tickets filtered: Priority={pri or 'All'}, Status={stat or 'All'}")
        self.set_status("Tickets filter applied")

    # ========================= Actions: Search/Filter Reset =========================
    def search_current_tab(self):
        query = self.search_var.get().strip().lower()
        if not query:
            self.set_status("Enter text to search")
            return

        idx = self.tabs.index(self.tabs.select())
        if idx == 0:
            data, tree = self.clients, self.client_tree
        elif idx == 1:
            data, tree = self.invoices, self.inv_tree
        else:
            data, tree = self.tickets, self.tkt_tree

        filtered = [row for row in data if any(query in str(x).lower() for x in row)]
        self._populate_tree(tree, filtered)
        self.log(f"Searched current tab for: '{query}'")
        self.set_status("Search applied")

    def clear_filters(self):
        self.search_var.set("")
        self._reset_filters()
        self.reset_view()
        self.log("Cleared search and filters")
        self.set_status("Filters cleared")

    def reset_view(self):
        # Show full datasets in all tabs
        self._populate_tree(self.client_tree, self.clients)
        self._populate_tree(self.inv_tree, self.invoices)
        self._populate_tree(self.tkt_tree, self.tickets)
        self.set_status("View reset to full data")

    def _reset_filters(self):
        self.client_domain_var.set("")
        self.inv_status_var.set("")
        self.inv_min_amt.set("") if hasattr(self, "inv_min_amt") else setattr(self, "inv_min_amt", tk.StringVar())
        self.inv_max_amt.set("") if hasattr(self, "inv_max_amt") else setattr(self, "inv_max_amt", tk.StringVar())
        self.tkt_pri_var.set("")
        self.tkt_stat_var.set("")

    # ========================= Data: Generate/Save/Load =========================
    def generate_dummy_data(self):
        # Clear all first
        self.clients.clear()
        self.invoices.clear()
        self.tickets.clear()

        for tree in (self.client_tree, self.inv_tree, self.tkt_tree):
            tree.delete(*tree.get_children())

        # Sample sets
        issues = ["System Crash", "Login Failure", "Email Down", "Slow Network", "Payment Error", "Access Denied"]
        priorities = ["Low", "Medium", "High"]
        t_statuses = ["Open", "In-Progress", "Resolved", "Closed"]
        i_statuses = ["Unpaid", "Paid"]
        domains = ["example.com", "contoso.com", "fabrikam.org", "acme.co", "globex.net"]

        # Clients (50)
        for i in range(1, 51):
            domain = random.choice(domains)
            email = f"client{i}@{domain}"
            phone = f"+1-555-{1000 + i}"
            row = (i, f"Client {i}", email, phone)
            self.clients.append(row)
        # Invoices (50)
        for i in range(1, 51):
            client = random.choice(self.clients)[1]
            amount = random.randint(500, 7500)
            due = (datetime.now() + timedelta(days=random.randint(1, 45))).strftime("%Y-%m-%d")
            status = random.choice(i_statuses)
            self.invoices.append((i, client, amount, due, status))
        # Tickets (50)
        for i in range(1, 51):
            client = random.choice(self.clients)[1]
            issue = random.choice(issues)
            pri = random.choice(priorities)
            stat = random.choice(t_statuses)
            date = (datetime.now() - timedelta(days=random.randint(0, 20))).strftime("%Y-%m-%d")
            self.tickets.append((i, client, issue, pri, stat, date))

        # Fill trees
        self.reset_view()

        # Populate filter dropdown values
        self.client_domain_cb["values"] = [""] + sorted({c[2].split("@")[-1] for c in self.clients})
        self.inv_status_cb["values"] = [""] + sorted({i[4] for i in self.invoices})
        self.tkt_pri_cb["values"] = [""] + sorted({t[3] for t in self.tickets})
        self.tkt_stat_cb["values"] = [""] + sorted({t[4] for t in self.tickets})

        # Auto-save to JSON in working directory
        self._save_json(Path("crm_data.json"))
        self.log("Generated 50 Clients, 50 Invoices, 50 Tickets (auto-saved to crm_data.json)")
        self.set_status("Dummy data generated and saved")

    def save_json_dialog(self):
        path = filedialog.asksaveasfilename(
            title="Save CRM JSON",
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
            initialfile="crm_data.json",
        )
        if not path:
            return
        self._save_json(Path(path))
        self.log(f"Saved data to {path}")
        self.set_status("Data saved")

    def _save_json(self, path: Path):
        data = {
            "clients": [dict(zip(["ID", "Name", "Email", "Phone"], c)) for c in self.clients],
            "invoices": [dict(zip(["InvoiceID", "Client", "Amount", "DueDate", "Status"], i)) for i in self.invoices],
            "tickets": [dict(zip(["TicketID", "Client", "Issue", "Priority", "Status", "Date"], t)) for t in self.tickets],
        }
        path.write_text(json.dumps(data, indent=2))

    def load_json_dialog(self):
        path = filedialog.askopenfilename(
            title="Open CRM JSON",
            filetypes=[("JSON", "*.json")]
        )
        if not path:
            return
        self._load_json(Path(path))
        self.reset_view()
        # Refresh filter values from loaded data
        if self.clients:
            self.client_domain_cb["values"] = [""] + sorted({c[2].split("@")[-1] for c in self.clients})
        if self.invoices:
            self.inv_status_cb["values"] = [""] + sorted({i[4] for i in self.invoices})
        if self.tickets:
            self.tkt_pri_cb["values"] = [""] + sorted({t[3] for t in self.tickets})
            self.tkt_stat_cb["values"] = [""] + sorted({t[4] for t in self.tickets})
        self.log(f"Loaded data from {path}")
        self.set_status("Data loaded")

    def _load_json(self, path: Path):
        try:
            obj = json.loads(Path(path).read_text())
            self.clients = [(c["ID"], c["Name"], c["Email"], c["Phone"]) for c in obj.get("clients", [])]
            self.invoices = [(i["InvoiceID"], i["Client"], i["Amount"], i["DueDate"], i["Status"])
                             for i in obj.get("invoices", [])]
            self.tickets = [(t["TicketID"], t["Client"], t["Issue"], t["Priority"], t["Status"], t["Date"])
                            for t in obj.get("tickets", [])]
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not load JSON:\n{e}")

    # ========================= Export CSV =========================
    def export_clients_csv(self):
        path = filedialog.asksaveasfilename(
            title="Export Clients CSV",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="clients.csv",
        )
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Name", "Email", "Phone"])
            for r in self._rows_from_tree(self.client_tree):
                w.writerow(r)
        self.log(f"Exported Clients CSV -> {path}")
        self.set_status("Clients CSV exported")

    def export_invoices_csv(self):
        path = filedialog.asksaveasfilename(
            title="Export Invoices CSV",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="invoices.csv",
        )
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["InvoiceID", "Client", "Amount", "DueDate", "Status"])
            for r in self._rows_from_tree(self.inv_tree):
                w.writerow(r)
        self.log(f"Exported Invoices CSV -> {path}")
        self.set_status("Invoices CSV exported")

    def export_tickets_csv(self):
        path = filedialog.asksaveasfilename(
            title="Export Tickets CSV",
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")],
            initialfile="tickets.csv",
        )
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["TicketID", "Client", "Issue", "Priority", "Status", "Date"])
            for r in self._rows_from_tree(self.tkt_tree):
                w.writerow(r)
        self.log(f"Exported Tickets CSV -> {path}")
        self.set_status("Tickets CSV exported")

    def export_all_csv(self):
        folder = filedialog.askdirectory(title="Choose folder for CSV export")
        if not folder:
            return
        base = Path(folder)
        # Clients
        with open(base / "clients.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["ID", "Name", "Email", "Phone"])
            for r in self.clients: w.writerow(r)
        # Invoices
        with open(base / "invoices.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["InvoiceID", "Client", "Amount", "DueDate", "Status"])
            for r in self.invoices: w.writerow(r)
        # Tickets
        with open(base / "tickets.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["TicketID", "Client", "Issue", "Priority", "Status", "Date"])
            for r in self.tickets: w.writerow(r)
        self.log(f"Exported ALL CSVs to folder: {base}")
        self.set_status("All CSVs exported")

    # ========================= Utilities =========================
    def _populate_tree(self, tree: ttk.Treeview, rows):
        tree.delete(*tree.get_children())
        for r in rows:
            tree.insert("", "end", values=r)

    def _rows_from_tree(self, tree: ttk.Treeview):
        out = []
        for iid in tree.get_children():
            out.append(tree.item(iid, "values"))
        return out

    def _safe_float(self, s: str):
        try:
            return float(s)
        except Exception:
            return None

    def _on_tab_change(self):
        # When tab changes, clear search result status to avoid confusion
        self.set_status("Tab changed")

# -------------------- Run App --------------------
if __name__ == "__main__":
    root = tb.Window(themename="flatly")  # light theme
    CRMApp(root)
    root.mainloop()






