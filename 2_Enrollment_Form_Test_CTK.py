from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from tkinter import *
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
nav_frame = CTkFrame(window, fg_color="transparent", bg_color="gray13")
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

# Image and ID Section
top_section = CTkFrame(scrollable_personal_frame, fg_color= "transparent")
top_section.pack(padx=20, pady=10, fill="x")

left_top = CTkFrame(top_section, fg_color= "transparent")
left_top.pack(side="left", fill="both", expand=True)

Student_ID = CTkLabel(left_top, text="Student ID:", font=("Arial", 14))
Student_ID.grid(row=0, column=0, padx=40, pady=5, sticky="w")
Student_entry = CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter Student ID", height= 35, fg_color= "transparent", bg_color= "transparent")
Student_entry.grid(row=0, column=1, pady=5)

Course_Section = CTkLabel(left_top, text="Course/Section:", font=("Arial", 14))
Course_Section.grid(row=1, column=0, padx=40, pady=5, sticky="w")
Course_Section_enrty= CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter Course/Section", height= 35, fg_color= "transparent", bg_color= "transparent")
Course_Section_enrty.grid(row=1, column=1, pady=5)

lrn = CTkLabel(left_top, text="LRN:", font=("Arial", 14))
lrn.grid(row=2, column=0, padx=40, pady=5, sticky="w")
lrn_entry= CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter LRN", height= 35, fg_color= "transparent", bg_color= "transparent")
lrn_entry.grid(row=2, column=1, pady=5)

right_top = CTkFrame(top_section, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
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

# Personal Information Title
personal_title_info =CTkLabel(scrollable_personal_frame, text= "PERSONAL INFORMATION", font= ("Id Inter", 25))
personal_title_info.pack(padx=20, pady=10, anchor=W)

# Personal Details Section
personal_details = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
personal_details.pack(padx=20, pady=10, fill="x")

# First Row
first_row_personal_details_frame = CTkFrame(personal_details, bg_color="transparent", fg_color= "transparent")
first_row_personal_details_frame.grid(row=0, column=0, columnspan=3, sticky="w", padx=20, pady=7)

surname_label = CTkLabel(first_row_personal_details_frame, text="Surname:", font=("Arial", 14), bg_color="transparent")
surname_label.grid(row=0, column=0, padx=20, pady=7, sticky="w")
surname_entry = CTkEntry(first_row_personal_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Surname", height= 35, fg_color= "transparent", bg_color= "transparent")
surname_entry.grid(row=1, column=0, padx=20, sticky="wn")

firstname_label = CTkLabel(first_row_personal_details_frame, text="Firstname:", font=("Arial", 14), bg_color="transparent")
firstname_label.grid(row=0, column=1, padx=20, pady=7, sticky="w")
firstname_entry = CTkEntry(first_row_personal_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Firstname", height= 35, fg_color= "transparent", bg_color= "transparent")
firstname_entry.grid(row=1, column=1, padx=20, sticky="wn")

middle_label = CTkLabel(first_row_personal_details_frame, text="Middle Initial:", font=("Arial", 14), bg_color="transparent")
middle_label.grid(row=0, column=2, padx=20, pady=7, sticky="w")
middle_entry = CTkEntry(first_row_personal_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Middle Initial", height= 35, fg_color= "transparent", bg_color= "transparent")
middle_entry.grid(row=1, column=2, padx=20, sticky="wn")

# Second Row
second_row_personal_details_frame = CTkFrame(personal_details, bg_color="transparent", fg_color= "transparent")
second_row_personal_details_frame.grid(row=1, column=0, columnspan=3, sticky="w", padx=20, pady=7)

gender_label = CTkLabel(second_row_personal_details_frame, text="Gender:", font=("Arial", 14), bg_color="transparent")
gender_label.grid(row=1, column=0, sticky="w", padx=40, pady=7)
gender_frame = CTkFrame(second_row_personal_details_frame, bg_color="transparent", fg_color= "transparent")
gender_frame.grid(row=2, column=0, sticky="w", padx=40)

male_var = IntVar()
female_var = IntVar()
none_binary_var = IntVar()

male_checkbox = CTkCheckBox(gender_frame, text="Male", variable=male_var)
male_checkbox.grid(row=0, column=0)
female_checkbox = CTkCheckBox(gender_frame, text="Female", variable=female_var)
female_checkbox.grid(row=0, column=1)
none_binary_checkbox = CTkCheckBox(gender_frame, text="Prefer not to answer", variable=none_binary_var)
none_binary_checkbox.grid(row=0, column=2)

age_label = CTkLabel(second_row_personal_details_frame, text="Age:", font=("Arial", 14), bg_color="transparent")
age_label.grid(row=1, column=1, sticky="w", padx=20, pady=7)
age_values = ["Select Age"] + [str(i) for i in range(1, 101)]
age_box = CTkComboBox(second_row_personal_details_frame, values=age_values, width=150, height= 35, bg_color= "transparent", state="readonly")
age_box.set("Select Age")
age_box.grid(row=2, column=1, sticky="wn", padx=20)

birthdate_label = CTkLabel(second_row_personal_details_frame, text="Birthdate (MM/DD/YYYY):", font=("Arial", 14), bg_color="transparent")
birthdate_label.grid(row=1, column=2, sticky="w", padx=20, pady=7)
birthdate_frame = CTkFrame(second_row_personal_details_frame, bg_color="transparent", fg_color= "transparent")
birthdate_frame.grid(row=2, column=2, sticky="w", padx=20)

months = [
          "MM", "January", "February", "March", "April", 
          "May", "June", "July", "August", "September", 
          "October", "November", "December"
          ]
month_box = CTkComboBox(birthdate_frame, values=months, width=90, height= 35, bg_color= "transparent", state="readonly")
month_box.set("MM")
month_box.grid(row=0, column=0, padx=3)

days = ["DD"] + [str(x) for x in range(1, 32)]
day_box = CTkComboBox(birthdate_frame, values=days, width=80, height= 35, bg_color= "transparent", state="readonly")
day_box.set("DD")
day_box.grid(row=0, column=1, padx=3)

years = ["YYYY"] + [str(x) for x in range(1900, datetime.now().year + 11)]
year_box = CTkComboBox(birthdate_frame, values=years, width=150, height= 35, bg_color= "transparent", state="readonly")
year_box.set("YYYY")
year_box.grid(row=0, column=2, padx=3)

# Third Row
third_row_personal_details_frame = CTkFrame(personal_details, bg_color="transparent", fg_color= "transparent")
third_row_personal_details_frame.grid(row=3, column=0, columnspan=3, sticky="we", padx=20, pady=7)

birthplace_label = CTkLabel(third_row_personal_details_frame, text="Birthplace City:", font=("Arial", 14), bg_color="transparent")
birthplace_label.grid(row=0, column=0, sticky="w", padx=20, pady=7)
birthplace_entry = CTkEntry(third_row_personal_details_frame, width=200, font=("Arial", 14), placeholder_text="Birthplace", height= 35, fg_color= "transparent", bg_color= "transparent")
birthplace_entry.grid(row=1, column=0, padx=20, sticky="wn")

nationality_label = CTkLabel(third_row_personal_details_frame, text="Nationality:", font=("Arial", 14), bg_color="transparent")
nationality_label.grid(row=0, column=1, sticky="w", padx=20, pady=7)
nationality_entry = CTkEntry(third_row_personal_details_frame, width=200, font=("Arial", 14), placeholder_text="Nationality", height= 35, fg_color= "transparent", bg_color= "transparent")
nationality_entry.grid(row=1, column=1, padx=20, sticky="wn")

religion_label = CTkLabel(third_row_personal_details_frame, text="Religion:", font=("Arial", 14), bg_color="transparent")
religion_label.grid(row=0, column=2, sticky="w", padx=20, pady=7)
religions = [
             "Select Religion", "Roman Catholic", 
             "Iglesia ni Cristo", "Born Again", 
             "Protestant", "Muslim", "Other"
             ]
religion_box = CTkComboBox(third_row_personal_details_frame, values=religions, width=150, height= 35, bg_color= "transparent", state="readonly")
religion_box.set("Select Religion")
religion_box.grid(row=1, column=2, padx=20)

marital_status_label = CTkLabel(third_row_personal_details_frame, text="Marital Status:", font=("Arial", 14), bg_color="transparent")
marital_status_label.grid(row=0, column=3, sticky="w", padx=20, pady=7)
statuses = [
             "Select Marital Status", "Single", 
             "Married", "Widowed", "Separated"
            ]
marital_status_box = CTkComboBox(third_row_personal_details_frame, values=statuses, width=180, height= 35, bg_color= "transparent", state="readonly")
marital_status_box.set("Select Marital Status")
marital_status_box.grid(row=1, column=3, padx=20)

language_label = CTkLabel(third_row_personal_details_frame, text="Language Spoken:", font=("Arial", 14), bg_color="transparent")
language_label.grid(row=0, column=4, sticky="w", padx=20, pady=7)
language_entry = CTkEntry(third_row_personal_details_frame, width=200, font=("Arial", 14), placeholder_text="Language", height= 35, fg_color= "transparent", bg_color= "transparent")
language_entry.grid(row=1, column=4, padx=20, sticky="wn")

empty_frame = CTkFrame(personal_details, bg_color="transparent", fg_color= "transparent")
empty_frame.grid(row=4, column=0, columnspan=3, sticky="we", padx=20, pady=7)

empty_label = CTkLabel(empty_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)

# Address Title
address_title_info =CTkLabel(scrollable_personal_frame, text= "ADDRESS", font= ("Id Inter", 25))
address_title_info.pack(padx=20, pady=10, anchor=W)

# Address Details Section
address_details = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
address_details.pack(padx=20, pady=10, fill="x")

first_row_address_details_frame = CTkFrame(address_details, bg_color="transparent", fg_color= "transparent")
first_row_address_details_frame.grid(row=0, column=0, columnspan=3, sticky="we", padx=20, pady=7)

street_label = CTkLabel(first_row_address_details_frame, text="Street:", font=("Arial", 14), bg_color="transparent")
street_label.grid(row=0, column=0, padx=20, pady=7, sticky="w")
street_entry = CTkEntry(first_row_address_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Street", height= 35, fg_color= "transparent", bg_color= "transparent")
street_entry.grid(row=1, column=0, padx=20, sticky="wn")

brgy_label = CTkLabel(first_row_address_details_frame, text="Barangay:", font=("Arial", 14), bg_color="transparent")
brgy_label.grid(row=0, column=1, padx=20, pady=7, sticky="w")
brgy_entry = CTkEntry(first_row_address_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Barangay", height= 35, fg_color= "transparent", bg_color= "transparent")
brgy_entry.grid(row=1, column=1, padx=20, sticky="wn")

city_label = CTkLabel(first_row_address_details_frame, text="City/Municipality:", font=("Arial", 14), bg_color="transparent")
city_label.grid(row=0, column=2, padx=20, pady=7, sticky="w")
city_entry = CTkEntry(first_row_address_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter City", height= 35, fg_color= "transparent", bg_color= "transparent")
city_entry.grid(row=1, column=2, padx=20, sticky="wn")

zip_code_label = CTkLabel(first_row_address_details_frame, text="Zip Code:", font=("Arial", 14), bg_color="transparent")
zip_code_label.grid(row=0, column=3, padx=20, pady=7, sticky="w")
zip_code_entry = CTkEntry(first_row_address_details_frame, width=170, font=("Arial", 14), placeholder_text="Enter Zip Code", height= 35, fg_color= "transparent", bg_color= "transparent")
zip_code_entry.grid(row=1, column=3, padx=20, sticky="wn")

province_label = CTkLabel(first_row_address_details_frame, text="Province:", font=("Arial", 14), bg_color="transparent")
province_label.grid(row=2, column=0, padx=20, pady=7, sticky="w")
province_entry = CTkEntry(first_row_address_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Province", height= 35, fg_color= "transparent", bg_color= "transparent")
province_entry.grid(row=3, column=0, padx=20, sticky="wn")

country_label = CTkLabel(first_row_address_details_frame, text="Country:", font=("Arial", 14), bg_color="transparent")
country_label.grid(row=2, column=1, padx=20, pady=7, sticky="w")
country_entry = CTkEntry(first_row_address_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Country", height= 35, fg_color= "transparent", bg_color= "transparent")
country_entry.grid(row=3, column=1, padx=20, sticky="wn")

empty_frame = CTkFrame(address_details, bg_color="transparent", fg_color= "transparent")
empty_frame.grid(row=1, column=0, columnspan=3, sticky="we", padx=20, pady=6)

empty_label = CTkLabel(empty_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)

# Contact Information Title
contact_title_info =CTkLabel(scrollable_personal_frame, text= "CONTACT INFORMATIN", font= ("Id Inter", 25))
contact_title_info.pack(padx=20, pady=10, anchor=W)

# Contact Information Details Section
contact_info_details = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
contact_info_details.pack(padx=20, pady=10, fill="x")

first_row_contact_info_details_frame = CTkFrame(contact_info_details, bg_color="transparent", fg_color= "transparent")
first_row_contact_info_details_frame.grid(row=0, column=0, columnspan=3, sticky="we", padx=20, pady=7)

email_label = CTkLabel(first_row_contact_info_details_frame, text="Email:", font=("Arial", 14), bg_color="transparent")
email_label.grid(row=0, column=0, padx=10, pady=7, sticky="w")
email_entry = CTkEntry(first_row_contact_info_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Email", height= 35, fg_color= "transparent", bg_color= "transparent")
email_entry.grid(row=0, column=1, padx=10, pady=7, sticky="wn")

num_label = CTkLabel(first_row_contact_info_details_frame, text="Contact Number:", font=("Arial", 14), bg_color="transparent")
num_label.grid(row=0, column=2, padx=10, pady=7, sticky="w")
num_entry = CTkEntry(first_row_contact_info_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Contact Number", height= 35, fg_color= "transparent", bg_color= "transparent")
num_entry.grid(row=0, column=3, padx=10, pady=7, sticky="wn")

empty_frame = CTkFrame(contact_info_details, bg_color="transparent", fg_color= "transparent")
empty_frame.grid(row=1, column=0, columnspan=3, sticky="we", padx=20, pady=6)

empty_label = CTkLabel(empty_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)


# ==================== FAMILY BACKGROUND PAGE ====================
# Scrollable Frame
scrollable_family_background_frame = CTkScrollableFrame(family_frame)
scrollable_family_background_frame.place(x=0, y=0, relwidth=1, relheight=1)


# ==================== Window Starter ====================
window.mainloop()