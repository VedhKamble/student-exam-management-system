# gui/performance_graph.py

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from database.db import get_connection
from PIL import Image, ImageTk

class PerformanceGraphWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Performance Graph")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(Image.open('exam.jpg'))
        bg_label=tk.Label(root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Student Performance Graph",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        tk.Label(frame, text="Admission No").pack()
        self.adm_entry = tk.Entry(frame)
        self.adm_entry.pack(pady=5)

        tk.Button(
            frame,
            text="Show Graph",
            command=self.show_graph
        ).pack(pady=15)

    def show_graph(self):
        adm = self.adm_entry.get()
        if not adm:
            messagebox.showerror("Error", "Admission number required")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT section FROM student_profile WHERE adm_no=%s",
            (adm,)
        )
        sec = cursor.fetchone()

        cursor.execute(
            "SELECT sub1, sub2, sub3, sub4, sub5 FROM results WHERE adm_no=%s",
            (adm,)
        )
        marks = cursor.fetchone()

        conn.close()

        if not sec or not marks:
            messagebox.showerror("Error", "No data found")
            return

        subjects = self.get_subjects(sec[0])

        plt.figure()
        plt.bar(subjects, marks)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Marks Analysis")
        plt.show()

    def get_subjects(self, section):
        if section == "A":
            return ["English", "History", "Pol.Sc", "Eco", "Geo"]
        elif section == "B":
            return ["English", "Acc", "B.St", "Eco", "IP"]
        elif section == "C":
            return ["English", "Phy", "CS", "Chem", "Math"]
        elif section == "D":
            return ["English", "Phy", "Bio", "Chem", "Math"]
        else:
            return ["S1", "S2", "S3", "S4", "S5"]
