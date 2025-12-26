# app.py

import tkinter as tk
from database.db import initialize_database
from auth.login import LoginWindow
from auth.register import RegisterWindow
from dashboard_gui.dashboard import Dashboard

def open_login():
    root = tk.Tk()

    def open_dashboard():
        dashboard_root = tk.Tk()
        Dashboard(dashboard_root)
        dashboard_root.mainloop()

    LoginWindow(root, open_dashboard)
    root.mainloop()


def open_register():
    root = tk.Tk()
    RegisterWindow(root)
    root.mainloop()
    open_login()


if __name__ == "__main__":
    initialize_database()
    open_register()
