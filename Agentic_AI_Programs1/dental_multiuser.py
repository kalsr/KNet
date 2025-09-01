

# python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import json
import random

# ---------------- Database Setup ----------------
conn = sqlite3.connect("patients.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    receptionist TEXT NOT NULL,
    treatment TEXT NOT NULL,
    insurance TEXT NOT NULL,
    copayment REAL NOT NULL
)
""")
conn.commit()

# ---------------- Sample Data ----------------
receptionists = ["Mary", "Jane", "Amy", "Nicole"]
statuses = ["Waiting", "In Progress", "Completed", "Billed"]
treatments = {
    "Cleaning": 100,
    "Deep Cleaning": 200,
    "Root Canal": 800,
    "Dental Crown": 1200
}
insurances = ["Aetna", "Delta Dental", "Cigna", "Self-Pay"]

# ---------------- Functions ----------------
def fetch_patients():
    """Load patients from database into treeview."""
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM patients")
    for patient in cursor.fetchall():
        tree.insert("", "end", values=patient)

def add_patient():
    """Add a new patient to database."""
    name = name_entry.get().strip()
    receptionist = receptionist_var.get()
    treatment = treatment_var.get()
    insurance = insurance_var.get()
    copayment = copayment_entry.get().strip()

    if not name:
        messagebox.showwarning("Input Error", "Please enter patient name")
        return
    if not copayment.isdigit():
        messagebox.showwarning("Input Error", "Please enter a valid numeric co-payment")
        return

    cursor.execute(
        "INSERT INTO patients (name, status, receptionist, treatment, insurance, copayment) VALUES (?, ?, ?, ?, ?, ?)",
        (name, "Waiting", receptionist, treatment, insurance, float(copayment))
    )
    conn.commit()
    name_entry.delete(0, tk.END)
    copayment_entry.delete(0, tk.END)
    fetch_patients()

def save_to_json():
    """Save patient records to JSON file."""
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    data = []
    for p in patients:
        data.append({
            "id": p[0],
            "name": p[1],
            "status": p[2],
            "receptionist": p[3],
            "treatment": p[4],
            "insurance": p[5],
            "copayment": p[6]
        })

    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Success", f"Data saved to {file_path}")

def clear_data():
    """Clear all patient data."""
    cursor.execute("DELETE FROM patients")
    conn.commit()
    fetch_patients()
    messagebox.showinfo("Cleared", "All patient records cleared.")

def generate_sample_data():
    """Generate 50 random patient records with treatment + insurance info."""
    clear_data()
    for i in range(50):
        name = f"Patient_{i+1}"
        status = random.choice(statuses)
        receptionist = random.choice(receptionists)
        treatment = random.choice(list(treatments.keys()))
        insurance = random.choice(insurances)
        copayment = random.randint(20, 200)
        cursor.execute(
            "INSERT INTO patients (name, status, receptionist, treatment, insurance, copayment) VALUES (?, ?, ?, ?, ?, ?)",
            (name, status, receptionist, treatment, insurance, copayment)
        )
    conn.commit()
    fetch_patients()
    messagebox.showinfo("Success", "50 sample records generated.")

def show_treatment_costs():
    """Display treatment costs in a popup."""
    cost_text = "\n".join([f"{t}: ${c}" for t, c in treatments.items()])
    messagebox.showinfo("Treatment Costs", cost_text)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Multi-User Dental Office System")
root.geometry("1000x600")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Patient Name:").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Receptionist:").grid(row=0, column=2, padx=5)
receptionist_var = tk.StringVar(value=receptionists[0])
receptionist_menu = ttk.Combobox(input_frame, textvariable=receptionist_var, values=receptionists, state="readonly")
receptionist_menu.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Treatment:").grid(row=1, column=0, padx=5)
treatment_var = tk.StringVar(value="Cleaning")
treatment_menu = ttk.Combobox(input_frame, textvariable=treatment_var, values=list(treatments.keys()), state="readonly")
treatment_menu.grid(row=1, column=1, padx=5)

tk.Label(input_frame, text="Insurance:").grid(row=1, column=2, padx=5)
insurance_var = tk.StringVar(value=insurances[0])
insurance_menu = ttk.Combobox(input_frame, textvariable=insurance_var, values=insurances, state="readonly")
insurance_menu.grid(row=1, column=3, padx=5)

tk.Label(input_frame, text="Co-Payment:").grid(row=2, column=0, padx=5)
copayment_entry = tk.Entry(input_frame)
copayment_entry.grid(row=2, column=1, padx=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Patient", command=add_patient, bg="#5cb85c", fg="white", width=15)
add_btn.grid(row=0, column=0, padx=5)

save_btn = tk.Button(button_frame, text="Save to JSON", command=save_to_json, bg="#0275d8", fg="white", width=15)
save_btn.grid(row=0, column=1, padx=5)

sample_btn = tk.Button(button_frame, text="Generate Sample Data", command=generate_sample_data, bg="#f0ad4e", fg="white", width=20)
sample_btn.grid(row=0, column=2, padx=5)

clear_btn = tk.Button(button_frame, text="Clear Data", command=clear_data, bg="#d9534f", fg="white", width=15)
clear_btn.grid(row=0, column=3, padx=5)

cost_btn = tk.Button(button_frame, text="Treatment Costs", command=show_treatment_costs, bg="#5bc0de", fg="white", width=15)
cost_btn.grid(row=0, column=4, padx=5)

# Table
columns = ("ID", "Name", "Status", "Receptionist", "Treatment", "Insurance", "Co-Payment")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(fill="both", expand=True, pady=10)

fetch_patients()
root.mainloop()
