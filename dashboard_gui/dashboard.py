# gui/dashboard.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from dashboard_gui.student_add import AddStudentWindow
from dashboard_gui.edit_student import EditStudentWindow
from dashboard_gui.delete_student import DeleteStudentWindow
from dashboard_gui.result_add import AddResultWindow
from dashboard_gui.report_card import ReportCardWindow
from dashboard_gui.performance_graph import PerformanceGraphWindow

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(Image.open('exam.jpg'))
        bg_label=tk.Label(self.root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")

        tk.Label(
            frame,
            text="Examination Management System",
            font=("Arial", 14, "bold"),
            wraplength=280,
            justify="center"
        ).pack(pady=10)

        buttons = [
            ("Add Student Profile", self.open_add_student),
            ("Edit Student Profile", self.open_edit_student),
            ("Delete Student Profile", self.open_delete_student),
            ("Enter Exam Results", self.open_add_result),
            ("Generate Report Card", self.open_report),
            ("Performance Graph", self.open_graph),
            ("Logout", self.logout)
        ]

        for text, command in buttons:
            tk.Button(
                frame,
                text=text,
                width=25,
                pady=5,
                command=command
            ).pack(pady=5)

    # Placeholder methods for button actions
    def open_add_student(self):
        win=tk.Toplevel()
        AddStudentWindow(win)
        win.mainloop()

    def open_edit_student(self):
        win=tk.Toplevel()
        EditStudentWindow(win)
        win.mainloop()

    def open_delete_student(self):
        win=tk.Toplevel()
        DeleteStudentWindow(win)
        win.mainloop()
    def open_add_result(self):
        win=tk.Toplevel()
        AddResultWindow(win)
        win.mainloop()
    def open_report(self):
        win=tk.Toplevel()
        ReportCardWindow(win)
        win.mainloop()

    def open_graph(self):
       win=tk.Toplevel()
       PerformanceGraphWindow(win)
       win.mainloop()

    def logout(self):
        self.root.destroy()
        messagebox.showinfo("Logged Out", "You have been logged out.")