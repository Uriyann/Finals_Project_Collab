from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

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
personal_header.pack(pady=20)
CTkLabel(personal_header, text="Lucena City", font=("Arial", 12)).pack()
CTkLabel(personal_header, text="STUDENT ENROLLMENT FORM", font=("Arial", 18, "bold")).pack()
CTkLabel(personal_header, text="Second Semester 2024-2025", font=("Arial", 12)).pack()

personal_header = CTkLabel(personal_header, text= "PERSONAL INFORMATION", font= ("Id Inter", 25))
personal_header.pack(padx=20, pady=10, side=LEFT)

# Image and ID Section
top_section = CTkFrame(scrollable_personal_frame, fg_color= "transparent")
top_section.pack(padx=20, pady=10, fill="x")

left_top = CTkFrame(top_section, fg_color= "transparent", border_color= "black", border_width=6, corner_radius=10)
left_top.pack(side="left", fill="both", expand=True)

Student_ID = CTkLabel(left_top, text="Student ID:", font=("Arial", 14))
Student_ID.grid(row=0, column=0, padx=40, pady=15, sticky="w")
Student_entry = CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter Student ID", height= 35, fg_color= "transparent", bg_color= "transparent")
Student_entry.grid(row=0, column=1, pady=15)

Course_Section = CTkLabel(left_top, text="Course/Section:", font=("Arial", 14))
Course_Section.grid(row=1, column=0, padx=40, pady=15, sticky="w")
Course_Section_enrty= CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter Course/Section", height= 35, fg_color= "transparent", bg_color= "transparent")
Course_Section_enrty.grid(row=1, column=1, pady=15)

lrn = CTkLabel(left_top, text="LRN:", font=("Arial", 14))
lrn.grid(row=2, column=0, padx=40, pady=15, sticky="w")
lrn_entry= CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter LRN", height= 35, fg_color= "transparent", bg_color= "transparent")
lrn_entry.grid(row=2, column=1, pady=15)

right_top = CTkFrame(top_section, bg_color="transparent", fg_color= "transparent", border_color= "black", border_width=6, corner_radius=10)
right_top.pack(side="right", padx=10)

# Upload Picture 2x2
def upload_image():
    """Uploads an image from the user's computer to the window."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        with Image.open(file_path) as img:
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            img_ctk = CTkImage(light_image=img, dark_image=img, size=(200, 200))
            picture_label.configure(image=img_ctk, text="")
            picture_label.image = img_ctk

picture_frame = CTkFrame(right_top, width=200, height=200, border_color="black", border_width=6, corner_radius=10, fg_color="transparent")
picture_frame.pack()
picture_frame.pack_propagate(False)  # Prevent frame from resizing

# Clickable label to display/upload image
picture_label = CTkLabel(
    picture_frame,
    text="Upload\n2x2 Picture",
    justify="center",
    font=("Arial", 12),
    bg_color="white",
    text_color="black"
)
picture_label.pack(fill="both", expand=True)
picture_label.bind("<Button-1>", lambda e: upload_image())

# Show personal details first
show_frame(personal_frame)

# Full Name Section
fullname_section = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_color= "black", border_width=6, corner_radius=10)
fullname_section.pack(padx=20, pady=10, fill="x")

surname_label = CTkLabel(fullname_section, text="Surname", font=("Arial", 14))
surname_label.grid(row=0, column=0, padx=40, pady=15, sticky="w")
surname_entry = CTkEntry(fullname_section, width=250, font=("Arial", 14), placeholder_text="Enter Surname", height= 35, fg_color= "transparent", bg_color= "transparent")
surname_entry.grid(row=0, column=0, padx=40, pady=15, sticky="s", rowspan=2)

firstname_label = CTkLabel(fullname_section, text="Firstname", font=("Arial", 14))
firstname_label.grid(row=0, column=1, padx=40, pady=15, sticky="w")
firstname_entry = CTkEntry(fullname_section, width=250, font=("Arial", 14), placeholder_text="Enter Firstname", height= 35, fg_color= "transparent", bg_color= "transparent")
firstname_entry.grid(row=0, column=1, padx=40, pady=15, sticky="s", rowspan=2)

middle_label = CTkLabel(fullname_section, text="Middle Initial", font=("Arial", 14))
middle_label.grid(row=0, column=2, padx=40, pady=15, sticky="w")
middle_entry = CTkEntry(fullname_section, width=250, font=("Arial", 14), placeholder_text="Enter Middle Initial", height= 35, fg_color= "transparent", bg_color= "transparent")
middle_entry.grid(row=0, column=2, padx=40, pady=15, sticky="s", rowspan=2)

# Extra Space
extra_space = CTkLabel(fullname_section, text="", font=("Arial", 14))
extra_space.grid(row=1, column=0, padx=20, pady=10, sticky="w")

# Personal Details Section
personal_details = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_color= "black", border_width=6, corner_radius=10)
personal_details.pack(padx=20, pady=10, fill="x")

age_label = CTkLabel(personal_details, text="Age", font=("Arial", 14))
age_label.grid(row=0, column=0, sticky="w", padx=40, pady=15)
age_values = ["Select Age"] + [str(i) for i in range(1, 101)]
age_box = CTkComboBox(personal_details, values=age_values, width=150, state="normal")
age_box.set("Select Age")
age_box.configure(state="readonly")
age_box.grid(row=0, column=1, sticky="w", padx=40, pady=15)


# ==================== Window Starter ====================
window.mainloop()