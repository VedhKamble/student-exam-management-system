# auth/login.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection
from utils.security import verify_password
from PIL import Image, ImageTk

class LoginWindow:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success

        self.root.title("Login")
        self.root.geometry("400x300")
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
            text="User Login",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(frame, text="Username").grid(row=1, column=0, sticky="w", pady=5)
        tk.Label(frame, text="Password").grid(row=2, column=0, sticky="w", pady=5)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Entry(frame, textvariable=self.username_var).grid(row=1, column=1)
        tk.Entry(frame, textvariable=self.password_var, show="*").grid(row=2, column=1)

        tk.Button(
            frame,
            text="Login",
            width=15,
            command=self.login_user
        ).grid(row=3, column=0, columnspan=2, pady=15)

    def login_user(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """SELECT password_hash FROM users WHERE username=%s""",
            (username,)
        )

        result = cursor.fetchone()
        conn.close()

        if result and verify_password(password, result[0]):
            messagebox.showinfo("Success", "Login successful")
            self.root.destroy()
            self.on_success()
        else:
            messagebox.showerror("Error", "Invalid username or password")
