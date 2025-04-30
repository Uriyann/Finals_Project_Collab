from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from PIL import Image, ImageTk

# ==================== Window Setup ====================
window = CTk()
window.title("Student Enrollment Form")
window.geometry('1300x825')
window.resizable(False, False)
ctk.set_appearance_mode("dark")

# ==================== Navigation Buttons ====================
nav_frame = CTkFrame(window, bg_color="gray18")
nav_frame.pack(side="top", fill="x")

def show_frame(frame):
    frame.tkraise()

personal_btn = CTkButton(nav_frame, text="Personal Details", command=lambda: show_frame(personal_frame))
personal_btn.pack(side="left", padx=5, pady=5)

family_btn = CTkButton(nav_frame, text="Family Background", command=lambda: show_frame(family_frame))
family_btn.pack(side="left", padx=5, pady=5)

education_btn = CTkButton(nav_frame, text="Educational Background", command=lambda: show_frame(education_frame))
education_btn.pack(side="left", padx=5, pady=5)

# ==================== Main Container ====================
container = CTkFrame(window)
container.pack(fill="both", expand=True)

# ==================== Pages (Frames) ====================
personal_frame = CTkFrame(container)
family_frame = CTkFrame(container)
education_frame = CTkFrame(container)

for frame in (personal_frame, family_frame, education_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# ==================== PERSONAL DETAILS PAGE ====================
# Scrollable Frame
scrollable_personal_frame = CTkScrollableFrame(personal_frame)
scrollable_personal_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Headers
personal_header = CTkFrame(scrollable_personal_frame)
personal_header.pack(pady=10)
CTkLabel(personal_header, text="Lucena City", font=("Arial", 12)).pack()
CTkLabel(personal_header, text="STUDENT ENROLLMENT FORM", font=("Arial", 18, "bold")).pack()
CTkLabel(personal_header, text="Second Semester 2024-2025", font=("Arial", 12)).pack()


# personal_header = CTkLabel(scrollable_personal_frame, text= "PERSONAL INFORMATION", font= ("Id Inter", 25))
# personal_header.grid(row=0, column=0, padx=15, pady=10)






# ==================== Window Starter ====================
window.mainloop()