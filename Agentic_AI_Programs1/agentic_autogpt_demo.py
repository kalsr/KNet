

# Agentic AutoGPT-Style Demo (Tkinter GUI)
# Full-window GUI with scrollable task board
# Big, colored buttons
# Sample data generator
# Load/Save from JSON
# Clear data
# python agentic_autogpt_demo.py

import json
import random
import string
import time
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

APP_TITLE = "Agentic AutoGPT-Style Demo (Local)"
VERSION = "1.0"

# -----------------------------
# Utility & Data Model
# -----------------------------

STATUSES = ["PENDING", "RUNNING", "DONE", "ERROR", "SKIPPED"]

def gen_id(n=6):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))

def default_plan_for_goal(goal: str):
    """
    Very simple "planner" that turns a goal into 4-8 subtasks.
    This is a stub to emulate AutoGPT-style decomposition.
    """
    verbs = ["Research", "Outline", "Draft", "Review", "Refine", "Summarize", "Create", "Validate"]
    nouns = [
        "requirements", "resources", "steps", "risks", "timeline",
        "budget", "stakeholders", "deliverables", "examples", "dataset"
    ]
    num = random.randint(4, 8)
    tasks = []
    for i in range(1, num + 1):
        verb = random.choice(verbs)
        noun = random.choice(nouns)
        title = f"{verb} {noun}"
        desc = f"{verb} the {noun} related to: {goal}."
        tasks.append({
            "id": gen_id(),
            "title": title,
            "description": desc,
            "status": "PENDING",
            "result": "",
            "notes": []
        })
    return tasks

def sample_goal_and_tasks():
    goal = "Launch a weekly newsletter about agentic AI tools."
    tasks = [
        {
            "id": gen_id(),
            "title": "Research top agentic frameworks",
            "description": "Identify 6â8 frameworks (e.g., LangChain, LangGraph, AutoGen, CrewAI, LlamaIndex, Semantic Kernel).",
            "status": "PENDING",
            "result": "",
            "notes": []
        },
        {
            "id": gen_id(),
            "title": "Define content pillars",
            "description": "Pick recurring sections (News, Tutorials, Tool of the Week, Prompt Recipes).",
            "status": "PENDING",
            "result": "",
            "notes": []
        },
        {
            "id": gen_id(),
            "title": "Draft first issue",
            "description": "Write ~800 words with links and summaries.",
            "status": "PENDING",
            "result": "",
            "notes": []
        },
        {
            "id": gen_id(),
            "title": "Create simple landing page copy",
            "description": "Value prop + email form instructions.",
            "status": "PENDING",
            "result": "",
            "notes": []
        },
        {
            "id": gen_id(),
            "title": "Review and refine",
            "description": "Check clarity, tone, and accuracy.",
            "status": "PENDING",
            "result": "",
            "notes": []
        },
    ]
    return goal, tasks

# -----------------------------
# Agent Runner (simulated)
# -----------------------------

class AgentRunner:
    def __init__(self, app):
        self.app = app
        self._thread = None
        self._stop_flag = threading.Event()

    def is_running(self):
        return self._thread is not None and self._thread.is_alive()

    def start(self):
        if self.is_running():
            return
        self._stop_flag.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        if self.is_running():
            self._stop_flag.set()

    def _run(self):
        tasks = self.app.data.get("tasks", [])
        total = len(tasks)
        if total == 0:
            self.app.log("No tasks to run.")
            return

        self.app.log(f"Starting execution of {total} tasks...")
        done = 0
        for t in tasks:
            if self._stop_flag.is_set():
                self.app.log("Execution stopped by user.")
                break

            # Mark RUNNING
            t["status"] = "RUNNING"
            self.app.update_task_row(t["id"], status="RUNNING")
            self.app.progress.set(int((done / total) * 100))

            # Simulate work with random delays and notes
            steps = random.randint(2, 5)
            for step in range(1, steps + 1):
                if self._stop_flag.is_set():
                    break
                note = f"Working on step {step}/{steps}â¦"
                t["notes"].append(note)
                self.app.append_task_note(t["id"], note)
                time.sleep(random.uniform(0.3, 0.8))

            if self._stop_flag.is_set():
                t["status"] = "SKIPPED"
                self.app.update_task_row(t["id"], status="SKIPPED")
                continue

            # Randomly simulate an error ~10% of time
            if random.random() < 0.1:
                t["status"] = "ERROR"
                t["result"] = "Encountered an execution error."
                self.app.update_task_row(t["id"], status="ERROR", result=t["result"])
                self.app.log(f"[{t['title']}] failed.")
            else:
                t["status"] = "DONE"
                t["result"] = f"Completed: {t['title']}"
                self.app.update_task_row(t["id"], status="DONE", result=t["result"])
                self.app.log(f"[{t['title']}] completed.")
                done += 1

            self.app.progress.set(int((done / total) * 100))

        self.app.progress.set(100 if done == total else int((done / total) * 100))
        self.app.log("Execution finished.")
        self.app.refresh_summary()

# -----------------------------
# Scrollable Frame
# -----------------------------

class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = ttk.Frame(self.canvas)

        self.inner.bind("<Configure>", self._on_frame_configure)
        self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Mouse wheel support
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)       # Windows/Mac
        self.canvas.bind_all("<Button-4>", self._on_mousewheel_linux)   # Linux
        self.canvas.bind_all("<Button-5>", self._on_mousewheel_linux)

    def _on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        # On Windows/Mac, event.delta is positive/negative in steps of 120
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _on_mousewheel_linux(self, event):
        # On Linux, use Button-4/5 events
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

# -----------------------------
# Main Application
# -----------------------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_TITLE} v{VERSION}")
        self.geometry("1200x800")
        self.minsize(1000, 700)

        # Fullscreen toggle (F11), escape exits fullscreen
        self._fullscreen = False
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

        # Theme / styles
        self.style = ttk.Style(self)
        try:
            self.style.theme_use("clam")
        except Exception:
            pass

        # Data container
        self.data = {
            "goal": "",
            "tasks": []
        }

        # Top header
        self._build_header()

        # Button bar (colored)
        self._build_toolbar()

        # Center: left task board (scrollable), right details/log
        self._build_body()

        # Bottom status/progress
        self._build_statusbar()

        # Agent runner
        self.runner = AgentRunner(self)

        # Populate with a default sample so UI isn't empty
        self.new_sample()

    # ---------- UI Builders

    def _build_header(self):
        header = tk.Frame(self, bg="#1E293B")  # slate-800
        header.pack(side="top", fill="x")

        title = tk.Label(
            header, text=APP_TITLE, fg="white", bg="#1E293B",
            font=("Helvetica", 18, "bold"), pady=10
        )
        title.pack(side="left", padx=15)

        self.goal_var = tk.StringVar()
        self.goal_entry = tk.Entry(header, textvariable=self.goal_var, font=("Helvetica", 12))
        self.goal_entry.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        self.goal_entry.insert(0, "Type a high-level goal and press 'Plan'â¦")

    def _build_toolbar(self):
        bar = tk.Frame(self, bg="#0F172A")  # slate-900
        bar.pack(side="top", fill="x")

        def mkbtn(text, cmd, bg, fg="white"):
            btn = tk.Button(bar, text=text, command=cmd, bg=bg, fg=fg, padx=12, pady=8, bd=0,
                            activebackground="#111827", activeforeground="white",
                            font=("Helvetica", 11, "bold"))
            btn.pack(side="left", padx=6, pady=8)
            return btn

        # Color palette
        mkbtn("Plan", self.plan_from_goal, "#2563EB")          # blue
        mkbtn("Run", self.run_plan, "#16A34A")                 # green
        mkbtn("Stop", self.stop_run, "#DC2626")                # red
        mkbtn("New Sample", self.new_sample, "#7C3AED")        # purple
        mkbtn("Load JSON", self.load_json, "#0891B2")          # cyan
        mkbtn("Save JSON", self.save_json, "#D97706")          # amber
        mkbtn("Clear Data", self.clear_data, "#6B7280")        # gray
        mkbtn("Export Report", self.export_report, "#059669")  # emerald
        mkbtn("Fullscreen", self.toggle_fullscreen, "#374151") # gray-700
        mkbtn("Exit", self.safe_exit, "#111827")               # slate-900

    def _build_body(self):
        body = tk.Frame(self, bg="#0B1220")
        body.pack(side="top", fill="both", expand=True)

        # Left: tasks board (scrollable)
        left = tk.Frame(body, bg="#0B1220")
        left.pack(side="left", fill="both", expand=True)

        left_title = tk.Label(left, text="Task Board", bg="#0B1220", fg="white",
                              font=("Helvetica", 14, "bold"))
        left_title.pack(anchor="w", padx=12, pady=(12, 6))

        self.task_frame = ScrollableFrame(left)
        self.task_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # Columns header
        header = tk.Frame(self.task_frame.inner)
        header.pack(fill="x", pady=(0, 4))
        cols = ["ID", "Title", "Status", "Result"]
        widths = [10, 40, 12, 40]
        for c, w in zip(cols, widths):
            lbl = tk.Label(header, text=c, font=("Helvetica", 10, "bold"))
            lbl.pack(side="left", padx=4)
            header.grid_columnconfigure(0, weight=1)

        # Right: details & log
        right = tk.Frame(body, width=420, bg="#0B1220")
        right.pack(side="right", fill="y")

        # Summary
        sum_frame = tk.LabelFrame(right, text="Summary", padx=8, pady=6, bg="#0B1220", fg="white")
        sum_frame.pack(fill="x", padx=12, pady=(12, 8))

        self.summary_var = tk.StringVar(value="Tasks: 0 | Done: 0 | Errors: 0")
        sum_label = tk.Label(sum_frame, textvariable=self.summary_var, anchor="w",
                             bg="#0B1220", fg="white")
        sum_label.pack(fill="x")

        # Task details
        details = tk.LabelFrame(right, text="Task Details", padx=8, pady=6, bg="#0B1220", fg="white")
        details.pack(fill="both", expand=True, padx=12, pady=(0, 8))

        self.details_text = tk.Text(details, height=12, wrap="word")
        self.details_text.pack(fill="both", expand=True)

        # Log
        log_frame = tk.LabelFrame(right, text="Execution Log", padx=8, pady=6, bg="#0B1220", fg="white")
        log_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self.log_text = tk.Text(log_frame, height=10, wrap="word")
        self.log_text.pack(fill="both", expand=True)

    def _build_statusbar(self):
        status = tk.Frame(self, bg="#111827")
        status.pack(side="bottom", fill="x")

        self.status_var = tk.StringVar(value="Ready.")
        status_label = tk.Label(status, textvariable=self.status_var, fg="white", bg="#111827")
        status_label.pack(side="left", padx=10, pady=6)

        self.progress = tk.IntVar(value=0)
        self.progressbar = ttk.Progressbar(status, orient="horizontal", mode="determinate",
                                           maximum=100, variable=self.progress, length=300)
        self.progressbar.pack(side="right", padx=10, pady=6)

    # ---------- Actions

    def plan_from_goal(self):
        goal = self.goal_var.get().strip()
        if not goal or goal.startswith("Type a high-level goal"):
            messagebox.showinfo("Plan", "Please enter a real goal in the top box.")
            return
        self.data["goal"] = goal
        self.data["tasks"] = default_plan_for_goal(goal)
        self.refresh_tasks()
        self.log(f"Planned {len(self.data['tasks'])} tasks for goal: {goal}")
        self.refresh_summary()

    def new_sample(self):
        goal, tasks = sample_goal_and_tasks()
        self.goal_var.set(goal)
        self.data["goal"] = goal
        self.data["tasks"] = tasks
        self.refresh_tasks()
        self.log("Loaded sample goal & tasks.")
        self.refresh_summary()

    def load_json(self):
        path = filedialog.askopenfilename(
            title="Open Plan JSON",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            # Basic validation
            self.goal_var.set(self.data.get("goal", ""))
            if not isinstance(self.data.get("tasks", []), list):
                raise ValueError("Invalid JSON: 'tasks' must be a list.")
            self.refresh_tasks()
            self.refresh_summary()
            self.log(f"Loaded plan from {path}")
        except Exception as e:
            messagebox.showerror("Load JSON", f"Failed to load JSON:\n{e}")

    def save_json(self):
        path = filedialog.asksaveasfilename(
            title="Save Plan JSON",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )
        if not path:
            return
        try:
            payload = {
                "goal": self.goal_var.get().strip(),
                "tasks": self.data.get("tasks", [])
            }
            with open(path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
            self.log(f"Saved plan to {path}")
        except Exception as e:
            messagebox.showerror("Save JSON", f"Failed to save JSON:\n{e}")

    def export_report(self):
        """Export a simple text report of results."""
        path = filedialog.asksaveasfilename(
            title="Export Report",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if not path:
            return
        try:
            lines = [f"GOAL: {self.goal_var.get().strip()}", "-"*60]
            for t in self.data.get("tasks", []):
                lines.append(f"[{t['status']}] {t['title']}")
                if t.get("result"):
                    lines.append(f"  Result: {t['result']}")
                if t.get("notes"):
                    for n in t["notes"]:
                        lines.append(f"  - {n}")
                lines.append("")
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            self.log(f"Exported report to {path}")
        except Exception as e:
            messagebox.showerror("Export Report", f"Failed to export report:\n{e}")

    def clear_data(self):
        self.data = {"goal": "", "tasks": []}
        self.goal_var.set("")
        self.refresh_tasks()
        self.refresh_summary()
        self.log("Cleared data.")

    def run_plan(self):
        if self.runner.is_running():
            messagebox.showinfo("Run", "Already running.")
            return
        if not self.data.get("tasks"):
            messagebox.showinfo("Run", "No tasks to run. Plan something first.")
            return
        self.status_var.set("Runningâ¦")
        self.runner.start()

    def stop_run(self):
        self.runner.stop()
        self.status_var.set("Stoppingâ¦")

    def toggle_fullscreen(self, event=None):
        self._fullscreen = not self._fullscreen
        self.attributes("-fullscreen", self._fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self._fullscreen = False
        self.attributes("-fullscreen", False)
        return "break"

    def safe_exit(self):
        if self.runner and self.runner.is_running():
            if not messagebox.askyesno("Exit", "Agent is running. Stop and exit?"):
                return
            self.runner.stop()
        self.destroy()

    # ---------- Task Board Rendering

    def refresh_tasks(self):
        # Clear current rows
        for w in list(self.task_frame.inner.children.values()):
            w.destroy()

        # Rebuild header row
        header = tk.Frame(self.task_frame.inner)
        header.pack(fill="x", pady=(0, 4))
        headers = [("ID", 10), ("Title", 40), ("Status", 12), ("Result", 40)]
        for text, _ in headers:
            lbl = tk.Label(header, text=text, font=("Helvetica", 10, "bold"))
            lbl.pack(side="left", padx=4)

        # Build rows
        self._row_widgets = {}
        for t in self.data.get("tasks", []):
            row = tk.Frame(self.task_frame.inner, bd=1, relief="solid")
            row.pack(fill="x", padx=2, pady=2)

            lbl_id = tk.Label(row, text=t["id"], width=10, anchor="w")
            lbl_id.pack(side="left", padx=4)

            lbl_title = tk.Label(row, text=t["title"], width=40, anchor="w")
            lbl_title.pack(side="left", padx=4)

            lbl_status = tk.Label(row, text=t["status"], width=12, anchor="w")
            lbl_status.pack(side="left", padx=4)

            lbl_result = tk.Label(row, text=t.get("result",""), width=60, anchor="w", justify="left", wraplength=600)
            lbl_result.pack(side="left", padx=4, fill="x", expand=True)

            # When clicking a row, load details
            def make_onclick(task=t):
                def _():
                    self.show_task_details(task)
                return _
            row.bind("<Button-1>", lambda e, f=make_onclick(): f())
            for child in row.winfo_children():
                child.bind("<Button-1>", lambda e, f=make_onclick(): f())

            self._row_widgets[t["id"]] = {
                "row": row,
                "status": lbl_status,
                "result": lbl_result
            }

    def update_task_row(self, task_id, status=None, result=None):
        # Update model
        task = next((x for x in self.data.get("tasks", []) if x["id"] == task_id), None)
        if not task:
            return
        if status:
            task["status"] = status
        if result is not None:
            task["result"] = result

        # Update UI
        w = self._row_widgets.get(task_id)
        if not w:
            return
        if status:
            w["status"].config(text=status, fg=self.color_for_status(status))
        if result is not None:
            w["result"].config(text=result)

    def color_for_status(self, status):
        return {
            "PENDING": "#9CA3AF",  # gray
            "RUNNING": "#2563EB",  # blue
            "DONE":    "#16A34A",  # green
            "ERROR":   "#DC2626",  # red
            "SKIPPED": "#D97706",  # amber
        }.get(status, "black")

    def append_task_note(self, task_id, note):
        # Update model
        task = next((x for x in self.data.get("tasks", []) if x["id"] == task_id), None)
        if not task:
            return
        task.setdefault("notes", []).append(note)

        # If this task is currently visible in details, append there too
        current = self.details_text.get("1.0", "end-1c")
        if task["title"] in current:
            self.details_text.insert("end", f"  - {note}\n")
            self.details_text.see("end")

    def show_task_details(self, task):
        self.details_text.delete("1.0", "end")
        self.details_text.insert("end", f"ID: {task['id']}\n")
        self.details_text.insert("end", f"Title: {task['title']}\n")
        self.details_text.insert("end", f"Status: {task['status']}\n")
        self.details_text.insert("end", f"Description: {task['description']}\n")
        if task.get("result"):
            self.details_text.insert("end", f"Result: {task['result']}\n")
        if task.get("notes"):
            self.details_text.insert("end", "Notes:\n")
            for n in task["notes"]:
                self.details_text.insert("end", f"  - {n}\n")

    def refresh_summary(self):
        tasks = self.data.get("tasks", [])
        total = len(tasks)
        done = sum(1 for t in tasks if t["status"] == "DONE")
        errors = sum(1 for t in tasks if t["status"] == "ERROR")
        self.summary_var.set(f"Tasks: {total} | Done: {done} | Errors: {errors}")

    def log(self, msg):
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {msg}\n")
        self.log_text.see("end")

# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":
    app = App()
    app.mainloop()
