import tkinter as tk
from tkinter import messagebox
from auth.auth_system import register, login
from ui.app_ui import launch_main_app

def open_login():
    root = tk.Tk()
    root.title("Login System")

    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def handle_login():
        user = username_entry.get()
        pwd = password_entry.get()
        if login(user, pwd):
            messagebox.showinfo("Success", "Login Successful")
            root.destroy()
            launch_main_app()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def handle_register():
        user = username_entry.get()
        pwd = password_entry.get()
        register(user, pwd)
        messagebox.showinfo("Success", "Registered Successfully")

    tk.Button(root, text="Login", command=handle_login).pack()
    tk.Button(root, text="Register", command=handle_register).pack()

    root.mainloop()