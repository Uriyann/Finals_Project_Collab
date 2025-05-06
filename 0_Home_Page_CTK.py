from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox
import subprocess
from datetime import datetime

# ==================== Window Setup ====================
window = CTk()
window.title("Home Page")
window.geometry('900x700')
window.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==================== Window Switch Function ====================
def GO_PORTAL():
    window.destroy()
    subprocess.run(["python", "1_Portal_CTK.py"])


main_button = CTkButton(window, text="Open Portal", font=("Arial", 20, "bold"), command=GO_PORTAL)
main_button.place(relx=0.5, rely=0.4, anchor="center")


window.mainloop()