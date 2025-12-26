# gui/report_card.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from PIL import Image, ImageTk

class ReportCardWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Report Card")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(Image.open('exam.jpg'))
        bg_label=tk.Label(root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(
            frame,
            text="Student Report Card",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        entry_frame = tk.Frame(frame)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Admission No").grid(row=0, column=0, padx=5)
        self.adm_entry = tk.Entry(entry_frame)
        self.adm_entry.grid(row=0, column=1, padx=5)

        tk.Button(
            entry_frame,
            text="Generate",
            command=self.generate_report
        ).grid(row=0, column=2, padx=10)

        self.report_frame = tk.Frame(frame)
        self.report_frame.pack(pady=20)

    def generate_report(self):
        for widget in self.report_frame.winfo_children():
            widget.destroy()

        adm = self.adm_entry.get()
        if not adm:
            messagebox.showerror("Error", "Admission number required")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT adm_no, roll_no, name, class_name, section FROM student_profile WHERE adm_no=%s",
            (adm,)
        )
        student = cursor.fetchone()

        cursor.execute(
            "SELECT exam_name, sub1, sub2, sub3, sub4, sub5, total, percentage, attendance, grade, remarks "
            "FROM results WHERE adm_no=%s",
            (adm,)
        )
        result = cursor.fetchone()

        conn.close()

        if not student or not result:
            messagebox.showerror("Error", "No record found for this admission number")
            return

        subjects = self.get_subjects(student[4])
        marks = result[1:6]

        header = f"""
Admission No : {student[0]}
Roll No      : {student[1]}
Name         : {student[2]}
Class        : {student[3]} - {student[4]}
Exam         : {result[0]}
"""
        tk.Label(self.report_frame, text=header, justify="left").pack(anchor="w")

        tk.Label(self.report_frame, text="Marks:", font=("Arial", 11, "bold")).pack(anchor="w", pady=5)

        for sub, mark in zip(subjects, marks):
            tk.Label(self.report_frame, text=f"{sub:<15} : {mark}").pack(anchor="w")

        footer = f"""
Total       : {result[6]}
Percentage  : {result[7]:.2f} %
Attendance  : {result[8]:.2f} %
Grade       : {result[9]}
Remarks     : {result[10]}
"""
        tk.Label(self.report_frame, text=footer, justify="left").pack(anchor="w", pady=10)

    def get_subjects(self, section):
        if section == "A":
            return ["English", "History", "Pol. Science", "Economics", "Geography"]
        elif section == "B":
            return ["English", "Accountancy", "B. Studies", "Economics", "IP"]
        elif section == "C":
            return ["English", "Physics", "Computer Sci.", "Chemistry", "Mathematics"]
        elif section == "D":
            return ["English", "Physics", "Biology", "Chemistry", "Mathematics"]
        else:
            return ["Subject1", "Subject2", "Subject3", "Subject4", "Subject5"]
