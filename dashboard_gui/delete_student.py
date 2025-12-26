# gui/student_delete.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from PIL import Image, ImageTk

class DeleteStudentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Student Profile")
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
            text="Delete Student Profile",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Admission No").grid(row=1, column=0, sticky="w")
        self.adm_entry = tk.Entry(frame)
        self.adm_entry.grid(row=1, column=1)

        tk.Button(
            frame,
            text="Delete",
            width=15,
            command=self.delete_student
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def delete_student(self):
        adm = self.adm_entry.get()

        if not adm:
            messagebox.showerror("Error", "Admission number required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM student_profile WHERE adm_no=%s",
                (adm,)
            )

            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Admission number not found")
            else:
                conn.commit()
                messagebox.showinfo("Success", "Student profile deleted")

            conn.close()

        except Exception:
            messagebox.showerror("Error", "Deletion failed")
