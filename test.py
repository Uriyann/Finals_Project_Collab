import customtkinter as ctk
from tkinter import messagebox

# Set up theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create main root (can be hidden if only top-level is needed)
root = ctk.CTk()
root.withdraw()  # Hide the main window

# Correct password (you can change this or fetch from file/db)
CORRECT_PASSWORD = "admin123"

def check_password():
    entered_password = password_entry.get()
    if entered_password == CORRECT_PASSWORD:
        messagebox.showinfo("Access Granted", "Welcome!")
        password_window.destroy()
    else:
        messagebox.showerror("Access Denied", "Incorrect Password.")

# Create top-level password window
password_window = ctk.CTkToplevel()
password_window.title("Password Required")
password_window.geometry("300x160")
password_window.resizable(False, False)

# Label
label = ctk.CTkLabel(password_window, text="Enter Password:", font=("Arial", 16))
label.pack(pady=10)

# Password entry field
password_entry = ctk.CTkEntry(password_window, show="*", width=200)
password_entry.pack(pady=5)
password_entry.focus()

# Submit button
submit_btn = ctk.CTkButton(password_window, text="Submit", command=check_password)
submit_btn.pack(pady=15)

# Run
root.mainloop()
