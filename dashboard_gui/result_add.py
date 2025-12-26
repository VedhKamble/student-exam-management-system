# gui/result_add.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from PIL import Image, ImageTk

class AddResultWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Exam Result")
        self.root.geometry("450x500")
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
            text="Exam Result Entry",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        labels = [
            "Admission No", "Exam Name",
            "Subject 1 (/100)", "Subject 2 (/100)", "Subject 3 (/100)",
            "Subject 4 (/100)", "Subject 5 (/100)",
            "Working Days", "Days Present"
        ]

        self.entries = {}

        for i, label in enumerate(labels, start=1):
            tk.Label(frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(frame)
            entry.grid(row=i, column=1)
            self.entries[label] = entry

        tk.Button(
            frame,
            text="Calculate & Save",
            width=18,
            command=self.save_result
        ).grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

    def save_result(self):
        try:
            adm_no = int(self.entries["Admission No"].get())
            exam = self.entries["Exam Name"].get()

            marks = [
                int(self.entries["Subject 1 (/100)"].get()),
                int(self.entries["Subject 2 (/100)"].get()),
                int(self.entries["Subject 3 (/100)"].get()),
                int(self.entries["Subject 4 (/100)"].get()),
                int(self.entries["Subject 5 (/100)"].get())
            ]

            work_days = int(self.entries["Working Days"].get())
            present_days = int(self.entries["Days Present"].get())

            total = sum(marks)
            percentage = total / 500 * 100
            attendance = (present_days / work_days) * 100

            if percentage >= 90:
                grade, remarks = "A", "Excellent Performance"
            elif percentage >= 75:
                grade, remarks = "B", "Very Good Performance"
            elif percentage >= 55:
                grade, remarks = "C", "Satisfactory Performance"
            elif percentage >= 35:
                grade, remarks = "D", "Average Performance"
            else:
                grade, remarks = "E", "Scope for Improvement"

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO results
                (adm_no, exam_name, sub1, sub2, sub3, sub4, sub5,
                 total, percentage, attendance, grade, remarks)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                adm_no, exam, *marks,
                total, percentage, attendance, grade, remarks
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Result saved successfully")
            self.root.destroy()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
        except Exception:
            messagebox.showerror("Error", "Result already exists or student not found")
