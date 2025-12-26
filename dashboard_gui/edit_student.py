# gui/student_edit.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from PIL import Image, ImageTk

class EditStudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Edit Student Profile")
        self.root.geometry("420x300")
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
            text="Edit Student Profile",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Admission No").grid(row=1, column=0, sticky="w")
        self.adm_entry = tk.Entry(frame)
        self.adm_entry.grid(row=1, column=1)

        tk.Label(frame, text="Select Field").grid(row=2, column=0, sticky="w", pady=10)

        self.field_var = tk.StringVar(value="name")

        fields = {
            "Roll No": "roll_no",
            "Name": "name",
            "Mother Name": "mother_name",
            "Father Name": "father_name",
            "Class": "class_name",
            "Section": "section"
        }

        self.field_map = fields

        tk.OptionMenu(frame, self.field_var, *fields.keys()).grid(row=2, column=1)

        tk.Label(frame, text="New Value").grid(row=3, column=0, sticky="w")
        self.new_value_entry = tk.Entry(frame)
        self.new_value_entry.grid(row=3, column=1)

        tk.Button(
            frame,
            text="Update",
            width=15,
            command=self.update_field
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def update_field(self):
        adm = self.adm_entry.get()
        field_label = self.field_var.get()
        new_value = self.new_value_entry.get()

        if not adm or not new_value:
            messagebox.showerror("Error", "All fields are required")
            return

        column = self.field_map[field_label]

        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = f"UPDATE student_profile SET {column}=%s WHERE adm_no=%s"
            cursor.execute(query, (new_value, adm))

            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Admission number not found")
            else:
                conn.commit()
                messagebox.showinfo("Success", "Student profile updated")

            conn.close()

        except Exception:
            messagebox.showerror("Error", "Update failed")
