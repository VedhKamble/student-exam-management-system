# auth/register.py

import tkinter as tk
from tkinter import messagebox
from database.db import get_connection, initialize_database
from mysql.connector import IntegrityError, Error
from utils.security import hash_password
from PIL import Image, ImageTk


class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(Image.open('exam.jpg'))
        bg_label=tk.Label(self.root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.build_ui()

    def build_ui(self):
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True)

        tk.Label(
            main_frame,
            text="User Registration",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(main_frame, text="Username").grid(row=1, column=0, sticky="w", pady=5)
        tk.Label(main_frame, text="Password").grid(row=2, column=0, sticky="w", pady=5)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Entry(main_frame, textvariable=self.username_var).grid(row=1, column=1)
        tk.Entry(main_frame, textvariable=self.password_var, show="*").grid(row=2, column=1)

        tk.Button(
            main_frame,
            text="Register",
            width=15,
            command=self.register_user
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def register_user(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()

            hashed = hash_password(password)

            cursor.execute(
                """INSERT INTO users (username, password_hash) VALUES (%s, %s)""",
                (username, hashed)
            )

            conn.commit()
            conn.close()

            messagebox.showinfo("Success!", "Account created successfully")
            self.root.destroy()

        except IntegrityError:
            messagebox.showerror("Error!!!", "Username already exists")
        
        except Error as e:
        # Any other MySQL-related error
            messagebox.showerror("Database Error", str(e))

        except Exception as e:
            # Any Python error
            messagebox.showerror("Error", str(e))
