# gui/student_add.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from PIL import Image, ImageTk

class AddStudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Student Profile")
        self.root.geometry("400x450")
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
            text="Add Student Profile",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        labels = [
            "Admission No", "Roll No", "Name",
            "Mother's Name", "Father's Name",
            "Gender (M/F)", "Class", "Section"
        ]

        self.entries = {}

        for i, label in enumerate(labels, start=1):
            tk.Label(frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(frame)
            entry.grid(row=i, column=1)
            self.entries[label] = entry

        tk.Button(
            frame,
            text="Save Student",
            width=18,
            command=self.save_student
        ).grid(row=len(labels) + 1, column=0, columnspan=2, pady=20)

    def save_student(self):
        try:
            data = {
                "adm_no": int(self.entries["Admission No"].get()),
                "roll_no": int(self.entries["Roll No"].get()),
                "name": self.entries["Name"].get(),
                "mother": self.entries["Mother's Name"].get(),
                "father": self.entries["Father's Name"].get(),
                "gender": self.entries["Gender (M/F)"].get().upper(),
                "class": self.entries["Class"].get(),
                "section": self.entries["Section"].get().upper()
            }

            if data["gender"] not in ("M", "F"):
                messagebox.showerror("Error", "Gender must be M or F")
                return

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO student_profile
                (adm_no, roll_no, name, mother_name, father_name, gender, class_name, section)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                data["adm_no"], data["roll_no"], data["name"],
                data["mother"], data["father"],
                data["gender"], data["class"], data["section"]
            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Student profile added successfully")
            self.root.destroy()

        except ValueError:
            messagebox.showerror("Error", "Admission No and Roll No must be numbers")
        except Exception:
            messagebox.showerror("Error", "Admission No or Roll No already exists")
