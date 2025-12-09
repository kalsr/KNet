# fraud_detector.py

import tkinter as tk

from tkinter import filedialog, messagebox, ttk

import random

import os



# -----------------------------

# SIMPLE FRAUD DETECTION LOGIC

# -----------------------------

def detect_fraud(lines):

    """A simple rule-based heuristic fraud detector.

    You can expand this with ML if needed."""

    suspicious_keywords = ["failed login", "invalid", "denied", "unauthorized",

                           "error 403", "multiple attempts", "blocked", "blacklisted"]



    score = 0

    flagged_lines = []



    for line in lines:

        for word in suspicious_keywords:

            if word.lower() in line.lower():

                score += 10

                flagged_lines.append(line.strip())

    return score, flagged_lines





# -----------------------------

# MAIN GUI APPLICATION

# -----------------------------

class FraudDetectorGUI:

    def __init__(self, root):

        self.root = root

        root.title("Fraud / Scam Detector – KNet Consulting")

        root.geometry("900x600")

        root.configure(bg="#f2f2f2")



        self.sample_data = []

        self.file_data = []



        # ---------- HEADER ----------

        header = tk.Label(

            root,

            text="Fraud or Scam Detector\nDesigned & Developed by Randy Singh from KNet Consulting",

            font=("Arial", 18, "bold"),

            bg="#004aad",

            fg="white",

            padx=20,

            pady=20

        )

        header.pack(fill="x")



        # ---------- SLIDER FRAME ----------

        slider_frame = tk.Frame(root, bg="#f2f2f2")

        slider_frame.pack(pady=20)



        self.slider = tk.Scale(

            slider_frame, from_=0, to=100, orient="horizontal",

            label="Generate Random Sample Log Data (0–100 entries)",

            length=400,

            bg="#f2f2f2"

        )

        self.slider.pack()



        generate_btn = tk.Button(

            slider_frame,

            text="Generate Sample Data",

            command=self.generate_sample_data,

            bg="#4CAF50",

            fg="white",

            font=("Arial", 12),

            width=20,

            height=2,

            relief="raised",

            bd=3

        )

        generate_btn.pack(pady=10)



        reset_btn = tk.Button(

            slider_frame,

            text="Reset Sample Data",

            command=self.reset_sample_data,

            bg="#e60000",

            fg="white",

            font=("Arial", 12),

            width=20,

            height=2,

            relief="raised",

            bd=3

        )

        reset_btn.pack(pady=5)



        upload_btn = tk.Button(

            slider_frame,

            text="Upload Your Own Log File",

            command=self.upload_file,

            bg="#ff9800",

            fg="white",

            font=("Arial", 12),

            width=22,

            height=2,

            relief="raised",

            bd=3

        )

        upload_btn.pack(pady=10)



        analyze_btn = tk.Button(

            slider_frame,

            text="Run Fraud Detection",

            command=self.run_analysis,

            bg="#007acc",

            fg="white",

            font=("Arial", 12),

            width=22,

            height=2,

            relief="raised",

            bd=3

        )

        analyze_btn.pack(pady=20)



        # ---------- OUTPUT BOX ----------

        self.output = tk.Text(root, width=110, height=15, font=("Courier", 10))

        self.output.pack(pady=10)



    # -----------------------------

    # BUTTON LOGIC

    # -----------------------------

    def generate_sample_data(self):

        n = self.slider.get()

        self.sample_data = []



        for i in range(n):

            entry_type = random.choice(["OK", "FAILED LOGIN", "ACCESS DENIED",

                                        "USER VALID", "UNAUTHORIZED ATTEMPT"])

            line = f"Event {i+1}: {entry_type}"

            self.sample_data.append(line)



        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, "Generated Sample Data:\n" + "\n".join(self.sample_data))



    def reset_sample_data(self):

        self.sample_data = []

        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, "Sample data reset.\n")



    def upload_file(self):

        path = filedialog.askopenfilename(

            title="Select log file",

            filetypes=[("Text Files", "*.txt"), ("Log Files", "*.log"), ("All Files", "*.*")]

        )

        if path:

            with open(path, "r") as f:

                self.file_data = f.readlines()



            self.output.delete("1.0", tk.END)

            self.output.insert(tk.END, f"Loaded file: {os.path.basename(path)}\n\n")

            self.output.insert(tk.END, "".join(self.file_data))



    def run_analysis(self):

        logs = self.sample_data or self.file_data



        if not logs:

            messagebox.showwarning("No Data", "No log data available to analyze.")

            return



        score, flagged = detect_fraud(logs)

        risk = "LOW"

        if score > 40:

            risk = "HIGH"

        elif score > 15:

            risk = "MEDIUM"



        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, "===== FRAUD ANALYSIS REPORT =====\n")

        self.output.insert(tk.END, f"Fraud Risk Score: {score}\n")

        self.output.insert(tk.END, f"Risk Level: {risk}\n\n")

        self.output.insert(tk.END, "Suspicious Entries:\n")

        self.output.insert(tk.END, "-------------------------------------\n")



        if flagged:

            self.output.insert(tk.END, "\n".join(flagged))

        else:

            self.output.insert(tk.END, "No suspicious log entries detected.\n")





# -----------------------------

# RUN APPLICATION

# -----------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = FraudDetectorGUI(root)

    root.mainloop()
