import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

# === Functions ===
def FinalCheck():
    # Validate Student ID, Course/Section, and LRN fields
    ReqFields = [
        ("Student ID", StudentID_Entry), 
        ("Course/Section", CourSec_Entry), 
        ("LRN", LRN_Entry),
    ]
    for Fieldnames, field in ReqFields:
        try:
            if field.get().strip() == "":
                messagebox.showerror("Missing Requirement", f"Error: {Fieldnames} is required.")
                return False
        except AttributeError:
            messagebox.showerror("Internal Error", f"Field '{Fieldnames}' is not a valid input widget.")
            return False

    # Validate LRN (must be an integer)
    lrn_value = LRN_Entry.get().strip()
    if not lrn_value.isdigit():
        messagebox.showerror("Invalid Input", "Error: LRN must be a valid integer.")
        return False

    # Validate Full Name fields (Surname, Firstname, Middle Initial)
    FullName = [
        ("Surname", surname_entry), 
        ("Firstname", firstname_entry), 
        ("Middle Initial", middle_entry),
    ]
    
    for Fieldnames, field in FullName:
        field_value = field.get().strip()
        
        # Check if the field is empty or still contains the placeholder text
        if field_value == "" or (field_value == "Surname" and Fieldnames == "Surname") or \
           (field_value == "Firstname" and Fieldnames == "Firstname") or \
           (field_value == "M.I." and Fieldnames == "Middle Initial"):
            messagebox.showerror("Missing Requirement", f"Error: {Fieldnames} is required.")
            return False
        # Ensure all are strings
        if not field_value.isalpha() and field_value != "":
            messagebox.showerror("Invalid Input", f"Error: {Fieldnames} should contain only letters.")
            return False

    # Validate Age field
    if age_box.get() == "Select Age":
        messagebox.showerror("Missing Requirement", "Error: Please select your age.")
        return False

    # Validate Birthdate (Month, Day, Year)
    if month_box.get() in ["MM", "Select Month"]:
        messagebox.showerror("Missing Requirement", "Error: Please select a month.")
        return False
    if day_box.get() in ["DD", "Select Day"]:
        messagebox.showerror("Missing Requirement", "Error: Please select a day.")
        return False
    if year_box.get() in ["YYYY", "Select Year"]:
        messagebox.showerror("Missing Requirement", "Error: Please select a year.")
        return False

    # Validate Birthplace (must be a string)
    birthplace_value = birthplace_entry.get().strip()
    if birthplace_value == "":
        messagebox.showerror("Missing Requirement", "Error: Birthplace is required.")
        return False
    if not birthplace_value.isalpha():
        messagebox.showerror("Invalid Input", "Error: Birthplace should contain only letters.")
        return False

    # Validate Nationality (must be a string)
    nationality_value = nationality_entry.get().strip()
    if nationality_value == "":
        messagebox.showerror("Missing Requirement", "Error: Nationality is required.")
        return False
    if not nationality_value.isalpha():
        messagebox.showerror("Invalid Input", "Error: Nationality should contain only letters.")
        return False

    # Validate Religion
    if religion_box.get() == "Select Religion":
        messagebox.showerror("Missing Requirement", "Error: Religion is required.")
        return False

    # Validate Marital Status
    if marital_box.get() == "Select Marital Status":
        messagebox.showerror("Missing Requirement", "Error: Marital Status is required.")
        return False

    # Validate Language Spoken (must be a string)
    language_value = language_spoken_entry.get().strip()
    if language_value == "":
        messagebox.showerror("Missing Requirement", "Error: Language Spoken is required.")
        return False
    if not language_value.isalpha():
        messagebox.showerror("Invalid Input", "Error: Language Spoken should contain only letters.")
        return False

    # Check Gender Section
    if male_var.get() == 0 and female_var.get() == 0:
        messagebox.showerror("Missing Requirement", "Error: Please select a gender.")
        return False
    elif male_var.get() == 1 and female_var.get() == 1:
        messagebox.showerror("Invalid Selection", "Error: Please only select one gender.")
        return False

    # Validate Address Section (Street, Barangay, City/Municipality, Province, Zip Code, Country)
    Address = [
        ("Street", address_entries[0]),
        ("Barangay", address_entries[1]),
        ("City/Municipality", address_entries[2]),
        ("Province", address_entries[3]),
        ("Zip Code", address_entries[4]),
        ("Country", address_entries[5]),
    ]
    for Fieldnames, entry in Address:
        field_value = entry.get().strip()
        if not field_value:
            messagebox.showerror("Missing Requirement", f"Error: {Fieldnames} is required.")
            return False
        # Ensure Street No., Zip code are integers
        if Fieldnames in ["Street", "Zip Code"]:
            if not field_value.isdigit():
                messagebox.showerror("Invalid Input", f"Error: {Fieldnames} must be a valid integer.")
                return False
        # Ensure Barangay, City, Province, and Country are strings
        if Fieldnames in ["Barangay", "City/Municipality", "Province", "Country"]:
            if not field_value.isalpha():
                messagebox.showerror("Invalid Input", f"Error: {Fieldnames} should contain only letters.")
                return False

    # Validate Contact Information (Email and Phone No)
    email_value = email_entry.get().strip()
    phone_value = phone_entry.get().strip()

    if email_value == "":
        messagebox.showerror("Missing Requirement", "Error: Email is required.")
        return False
    if "@" not in email_value:
        messagebox.showerror("Invalid Input", "Error: Email must contain '@'.")
        return False

    if phone_value == "":
        messagebox.showerror("Missing Requirement", "Error: Phone Number is required.")
        return False
    if not phone_value.isdigit():
        messagebox.showerror("Invalid Input", "Error: Phone Number must be a valid integer.")
        return False

    # Validate Parents' Information (Father's and Mother's Sections)
    father_name = father_frame.winfo_children()[1].get().strip()  # Name entry
    father_occupation = father_frame.winfo_children()[3].get().strip()  # Occupation entry
    father_contact = father_frame.winfo_children()[5].get().strip()  # Contact entry
    
    if father_name == "" or father_occupation == "" or father_contact == "":
        messagebox.showerror("Missing Requirement", "Error: Father's information is incomplete.")
        return False
    if not father_name.isalpha() or not father_occupation.isalpha():
        messagebox.showerror("Invalid Input", "Error: Father's Name and Occupation should be strings.")
        return False
    if father_contact != "N/A" and not father_contact.isdigit():
        messagebox.showerror("Invalid Input", "Error: Father's Contact No should be an integer or 'N/A'.")
        return False

    mother_name = mother_frame.winfo_children()[1].get().strip()  # Name entry
    mother_occupation = mother_frame.winfo_children()[3].get().strip()  # Occupation entry
    mother_contact = mother_frame.winfo_children()[5].get().strip()  # Contact entry

    if mother_name == "" or mother_occupation == "" or mother_contact == "":
        messagebox.showerror("Missing Requirement", "Error: Mother's information is incomplete.")
        return False
    if not mother_name.isalpha() or not mother_occupation.isalpha():
        messagebox.showerror("Invalid Input", "Error: Mother's Name and Occupation should be strings.")
        return False
    if mother_contact != "N/A" and not mother_contact.isdigit():
        messagebox.showerror("Invalid Input", "Error: Mother's Contact No should be an integer or 'N/A'.")
        return False

    # Validate Guardian's Information
    guardian_name = guardian_section.winfo_children()[1].get().strip()  # Guardian's Name entry
    guardian_relationship = guardian_section.winfo_children()[3].get().strip()  # Relationship entry
    guardian_contact = guardian_section.winfo_children()[5].get().strip()  # Contact entry

    if guardian_name == "" or guardian_relationship == "" or guardian_contact == "":
        messagebox.showerror("Missing Requirement", "Error: Guardian's information is incomplete.")
        return False    
    if not guardian_name.isalpha() or not guardian_relationship.isalpha():
        messagebox.showerror("Invalid Input", "Error: Guardian's Name and Relationship should be strings.")
        return False
    if guardian_contact != "N/A" and not guardian_contact.isdigit():
        messagebox.showerror("Invalid Input", "Error: Guardian's Contact No should be an integer or 'N/A'.")
        return False    

    # Validate Educational Information (Elementary, Junior High, Senior High, College)
    # Elementary
    elem_school_name = SchoolNameElem.get().strip()
    elem_year_grad = YearGradElem.get().strip()

    if elem_school_name == "" or elem_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Elementary school information is incomplete.")
        return False
    if not elem_school_name.isalpha():
        messagebox.showerror("Invalid Input", "Error: Elementary school name should be a string.")
        return False
    if not elem_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Elementary Year Graduated must be an integer.")
        return False

    # Junior High
    jun_school_name = SchoolNameJun.get().strip()
    jun_year_grad = YearGradJun.get().strip()

    if jun_school_name == "" or jun_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Junior High school information is incomplete.")
        return False
    if not jun_school_name.isalpha():
        messagebox.showerror("Invalid Input", "Error: Junior High school name should be a string.")
        return False
    if not jun_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Junior High Year Graduated must be an integer.")
        return False

    # Senior High
    sen_school_name = SchoolNameSen.get().strip()
    sen_strand = StrandSen.get().strip()
    sen_year_grad = YearGradSen.get().strip()

    if sen_school_name == "" or sen_strand == "" or sen_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Senior High school information is incomplete.")
        return False
    if not sen_school_name.isalpha() or not sen_strand.isalpha():
        messagebox.showerror("Invalid Input", "Error: Senior High school name and strand should be strings.")
        return False
    if not sen_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Senior High Year Graduated must be an integer.")
        return False

    # College
    col_school_name = SchoolNameCol.get().strip()
    col_year_grad = YearGradCol.get().strip()

    if col_school_name == "" or col_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: College information is incomplete.")
        return False
    if not col_school_name.isalpha():
        messagebox.showerror("Invalid Input", "Error: College school name should be a string.")
        return False
    if col_year_grad != "N/A" and not col_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: College Year Graduated must be an integer or 'N/A'.")
        return False

    # Check Student Status (Only one should be selected)
    selected_status_count = sum(var.get() == 1 for var in [
        transferee_var, new_student_var, 
        old_student_var, cross_enrollee_var, 
        returnee_var])
    
    if selected_status_count > 1:
        messagebox.showerror("Invalid Selection", "Error: Please only select one student status.")
        return False
    elif selected_status_count == 0:
        messagebox.showerror("Missing Requirement", "Error: Please select a student status.")
        return False

    # If all checks pass
    return True


# === Main Window ===
root = tk.Tk()
root.title("Student Enrollment Form")
root.geometry("900x700")



# === Navigation Buttons ===
nav_frame = tk.Frame(root, bg="#ddd")
nav_frame.pack(side="top", fill="x")

def show_frame(frame):
    frame.tkraise()

personal_btn = tk.Button(nav_frame, text="Personal Details", command=lambda: show_frame(personal_frame))
personal_btn.pack(side="left", padx=10, pady=5)

family_btn = tk.Button(nav_frame, text="Family Background", command=lambda: show_frame(family_frame))
family_btn.pack(side="left", padx=10, pady=5)

education_btn = tk.Button(nav_frame, text="Educational Background", command=lambda: show_frame(education_frame))
education_btn.pack(side="left", padx=10, pady=5)

# === Main Container ===
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# === Pages (Frames) ===
personal_frame = tk.Frame(container, bg="#f4f4f4")
family_frame = tk.Frame(container, bg="#f4f4f4")
education_frame = tk.Frame(container, bg="#f4f4f4")

for frame in (personal_frame, family_frame, education_frame):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# === PERSONAL DETAILS PAGE ===
# Canvas for Scroll
main_canvas = tk.Canvas(personal_frame, borderwidth=0, background="#f4f4f4")
frame = tk.Frame(main_canvas, background="#f4f4f4")
vsb = tk.Scrollbar(personal_frame, orient="vertical", command=main_canvas.yview)
main_canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
main_canvas.pack(side="left", fill="both", expand=True)
main_canvas.create_window((0, 0), window=frame, anchor="n", tags="form_frame")

def on_frame_configure(event):
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))

def center_canvas_content(event=None):
    canvas_width = event.width if event else main_canvas.winfo_width()
    main_canvas.itemconfig("form_frame", width=canvas_width - 40)

frame.bind("<Configure>", on_frame_configure)
main_canvas.bind("<Configure>", center_canvas_content)

# Header
header = tk.Frame(frame, bg="#f4f4f4")
header.pack(pady=10)
tk.Label(header, text="Lucena City", font=("Arial", 12)).pack()
tk.Label(header, text="STUDENT ENROLLMENT FORM", font=("Arial", 18, "bold")).pack()
tk.Label(header, text="Second Semester 2024-2025", font=("Arial", 12)).pack()


# Image and ID Section
top_section = tk.Frame(frame, bg="#f4f4f4")
top_section.pack(padx=20, pady=10, fill="x")

left_top = tk.Frame(top_section, bg="#f4f4f4")
left_top.pack(side="left", fill="both", expand=True)

tk.Label(left_top, text="Student ID:").grid(row=0, column=0, sticky="w")
StudentID_Entry = tk.Entry(left_top, width=30)
StudentID_Entry.grid(row=0, column=1, pady=5)

tk.Label(left_top, text="Course/Section:").grid(row=1, column=0, sticky="w")
CourSec_Entry = tk.Entry(left_top, width=30)
CourSec_Entry.grid(row=1, column=1, pady=5)

tk.Label(left_top, text="LRN:").grid(row=2, column=0, sticky="w")
LRN_Entry = tk.Entry(left_top, width=30)
LRN_Entry.grid(row=2, column=1, pady=5)

right_top = tk.Frame(top_section, bg="#f4f4f4")
right_top.pack(side="right", padx=10)

# --- Upload Picture 1x1 ---
def upload_picture():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Resize smoothly
        img_tk = ImageTk.PhotoImage(img)
        picture_label.configure(image=img_tk)
        picture_label.image = img_tk

picture_frame = tk.Frame(right_top, width=100, height=100, bg="black")  # Frame for border
picture_frame.pack(padx=5, pady=5)
picture_frame.pack_propagate(False)  # Prevent frame from resizing

picture_label = tk.Label(
    picture_frame, 
    text="Upload\n1x1 Picture", 
    bg="white", 
    relief="solid"
)
picture_label.pack(fill="both", expand=True)
picture_label.bind("<Button-1>", lambda e: upload_picture())

# Show personal details first
show_frame(personal_frame)

# Full Name Section
fullname_section = tk.LabelFrame(frame, text="Full Name", padx=10, pady=10)
fullname_section.pack(padx=20, pady=10, fill="x")

def setup_entry(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="gray")
    entry.bind("<FocusIn>", lambda e: (entry.delete(0, tk.END), entry.config(fg="black")) if entry.get() == placeholder else None)
    entry.bind("<FocusOut>", lambda e: (entry.insert(0, placeholder), entry.config(fg="gray")) if entry.get() == "" else None)

surname_entry = tk.Entry(fullname_section, width=25)
surname_entry.grid(row=0, column=0, padx=5)
setup_entry(surname_entry, "Surname")

firstname_entry = tk.Entry(fullname_section, width=25)
firstname_entry.grid(row=0, column=1, padx=5)
setup_entry(firstname_entry, "Firstname")

middle_entry = tk.Entry(fullname_section, width=10)
middle_entry.grid(row=0, column=2, padx=5)
setup_entry(middle_entry, "M.I.")


# Personal Details Section
personal = tk.LabelFrame(frame, text="Personal Information", padx=10, pady=10)
personal.pack(padx=20, pady=10, fill="x")

tk.Label(personal, text="Age").grid(row=0, column=0, sticky="w", padx=5, pady=3)
age_values = list(range(1, 101))  # Assuming age between 1 and 100
age_box = ttk.Combobox(personal, values=age_values, width=10, state="readonly")
age_box.set("Select Age")
age_box.grid(row=0, column=1, sticky="w", padx=5, pady=3)


fields = [
    ("Birthdate (MM/DD/YYYY)", 1),
    ("Birthplace City", 2),
    ("Nationality", 4),
    ("Religion", 5),
    ("Marital Status", 6),
    ("Language Spoken", 7)
]

for label, i in fields:
    tk.Label(personal, text=label).grid(row=i+1, column=0, sticky="w", padx=5, pady=3)

    if label == "Birthdate (MM/DD/YYYY)":
        months = ["MM", "January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        month_box = ttk.Combobox(personal, values=months, width=10, state="readonly")
        month_box.set("MM")
        month_box.grid(row=i+1, column=1, sticky="w", padx=(5, 0), pady=3)

        days = ["DD"] + list(range(1, 32))
        day_box = ttk.Combobox(personal, values=days, width=5, state="readonly")
        day_box.set("DD")
        day_box.grid(row=i+1, column=1, padx=(90, 0), pady=3, sticky="w")

        current_year = datetime.now().year
        years = ["YYYY"] + list(range(1900, current_year + 11))
        year_box = ttk.Combobox(personal, values=years, width=7, state="readonly")
        year_box.set("YYYY")
        year_box.grid(row=i+1, column=1, padx=(150, 0), pady=3, sticky="w")

    elif label == "Religion":
        religion_options = ["Roman Catholic", "Iglesia ni Cristo", "Born Again", "Protestant", "Muslim", "Other"]
        religion_box = ttk.Combobox(personal, values=religion_options, width=40, state="readonly")
        religion_box.set("Select Religion")
        religion_box.grid(row=i+1, column=1, padx=5, pady=3)

    elif label == "Marital Status":
        marital_options = ["Select Marital Status", "Single", "Married", "Widowed", "Separated"]
        marital_box = ttk.Combobox(personal, values=marital_options, width=40, state="readonly")
        marital_box.set("Select Marital Status")
        marital_box.grid(row=i+1, column=1, padx=5, pady=3)

    elif label == "Birthplace City":
        birthplace_entry = tk.Entry(personal, width=40)
        birthplace_entry.grid(row=i+1, column=1, padx=5, pady=3)

    elif label == "Nationality":
        nationality_entry = tk.Entry(personal, width=40)
        nationality_entry.grid(row=i+1, column=1, padx=5, pady=3)

    elif label == "Language Spoken":
        language_spoken_entry = tk.Entry(personal, width=40)
        language_spoken_entry.grid(row=i+1, column=1, padx=5, pady=3)

    else:
        entry = tk.Entry(personal, width=40)
        entry.grid(row=i+1, column=1, padx=5, pady=3)
tk.Label(personal, text="Gender").grid(row=9, column=0, sticky="w", padx=5, pady=3)

gender_frame = tk.Frame(personal, bg="#f4f4f4")
gender_frame.grid(row=9, column=1, sticky="w", padx=5)

male_var = tk.IntVar()
female_var = tk.IntVar()

tk.Checkbutton(gender_frame, text="Male", variable=male_var, bg="#f4f4f4").pack(side="left", padx=5)
tk.Checkbutton(gender_frame, text="Female", variable=female_var, bg="#f4f4f4").pack(side="left", padx=5)

# Address Section
address_entries = []

address = tk.LabelFrame(frame, text="Address", padx=10, pady=10)
address.pack(padx=20, pady=10, fill="x")

address_fields = ["Street No.", "Barangay", "City/Municipality", "Province", "Zip Code", "Country"]
for i, field in enumerate(address_fields):
    tk.Label(address, text=field).grid(row=i, column=0, padx=5, pady=3)
    entry = tk.Entry(address, width=30)
    entry.grid(row=i, column=1, padx=5, pady=3)
    address_entries.append(entry)

# Contact Information
contact = tk.LabelFrame(frame, text="Contact Information", padx=10, pady=10)
contact.pack(padx=20, pady=10, fill="x")
contact_entries = []

tk.Label(contact, text="Email:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
email_entry = tk.Entry(contact, width=40)
email_entry.grid(row=0, column=1, padx=5)
contact_entries.append(email_entry)

tk.Label(contact, text="Phone No:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
phone_entry = tk.Entry(contact, width=40)
phone_entry.grid(row=1, column=1, padx=5)
contact_entries.append(phone_entry)

# === FAMILY BACKGROUND PAGE ===
family_canvas = tk.Canvas(family_frame, borderwidth=0, background="#f4f4f4")
family_inner = tk.Frame(family_canvas, background="#f4f4f4")
family_vsb = tk.Scrollbar(family_frame, orient="vertical", command=family_canvas.yview)
family_canvas.configure(yscrollcommand=family_vsb.set)

family_vsb.pack(side="right", fill="y")
family_canvas.pack(side="left", fill="both", expand=True)
family_canvas.create_window((0, 0), window=family_inner, anchor="n", tags="family_frame")

def on_family_configure(event):
    family_canvas.configure(scrollregion=family_canvas.bbox("all"))

def center_family_content(event=None):
    canvas_width = event.width if event else family_canvas.winfo_width()
    family_canvas.itemconfig("family_frame", width=canvas_width - 40)

family_inner.bind("<Configure>", on_family_configure)
family_canvas.bind("<Configure>", center_family_content)

# Title
tk.Label(family_inner, text="Family Background", font=("Arial", 24, "bold"), bg="#f4f4f4").pack(pady=20)

# Parents Section
parents_section = tk.LabelFrame(family_inner, text="Parents' Information", padx=15, pady=15)
parents_section.pack(padx=20, pady=10, fill="both", expand=True)

# Father and Mother Frames side-by-side
father_frame = tk.LabelFrame(parents_section, text="Father", padx=10, pady=10)
father_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(father_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(father_frame, width=30).grid(row=0, column=1, pady=5)

tk.Label(father_frame, text="Occupation:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(father_frame, width=30).grid(row=1, column=1, pady=5)

tk.Label(father_frame, text="Contact No:").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(father_frame, width=30).grid(row=2, column=1, pady=5)

mother_frame = tk.LabelFrame(parents_section, text="Mother", padx=10, pady=10)
mother_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(mother_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(mother_frame, width=30).grid(row=0, column=1, pady=5)

tk.Label(mother_frame, text="Occupation:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(mother_frame, width=30).grid(row=1, column=1, pady=5)

tk.Label(mother_frame, text="Contact No:").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(mother_frame, width=30).grid(row=2, column=1, pady=5)

# Make them expand evenly
parents_section.grid_columnconfigure(0, weight=1)
parents_section.grid_columnconfigure(1, weight=1)

checkbox = tk.Checkbutton(family_inner, text="Same as Guardian", bg=parents_section.cget("bg"))
checkbox.pack(pady=10, side="left", padx=20)

# Guardian Section
guardian_section = tk.LabelFrame(family_inner, text="Guardian's Information", padx=15, pady=15)
guardian_section.pack(padx=20, pady=20, fill="x")

tk.Label(guardian_section, text="Guardian's Name:").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(guardian_section, width=40).grid(row=0, column=1, pady=5)

tk.Label(guardian_section, text="Relationship:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(guardian_section, width=40).grid(row=1, column=1, pady=5)

tk.Label(guardian_section, text="Contact No:").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(guardian_section, width=40).grid(row=2, column=1, pady=5)

# === EDUCATIONAL BACKGROUND PAGE ===
education_canvas = tk.Canvas(education_frame, borderwidth=0, background="#f4f4f4")
education_inner = tk.Frame(education_canvas, background="#f4f4f4")
education_vsb = tk.Scrollbar(education_frame, orient="vertical", command=education_canvas.yview)
education_canvas.configure(yscrollcommand=education_vsb.set)

education_vsb.pack(side="right", fill="y")
education_canvas.pack(side="left", fill="both", expand=True)
education_canvas.create_window((0, 0), window=education_inner, anchor="n", tags="education_frame")

def on_education_configure(event):
    education_canvas.configure(scrollregion=education_canvas.bbox("all"))

def center_education_content(event=None):
    canvas_width = event.width if event else education_canvas.winfo_width()
    education_canvas.itemconfig("education_frame", width=canvas_width - 40)

education_inner.bind("<Configure>", on_education_configure)
education_canvas.bind("<Configure>", center_education_content)

# Title
tk.Label(education_inner, text="Educational Background", font=("Arial", 24, "bold"), bg="#f4f4f4").pack(pady=20)

# Educational Sections
education_section = tk.LabelFrame(education_inner, text="School Information", padx=15, pady=15)
education_section.pack(padx=20, pady=10, fill="both", expand=True)

# Elementary Frame
elementary_frame = tk.LabelFrame(education_section, text="Elementary", padx=10, pady=10)
elementary_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(elementary_frame, text="School Name:").grid(row=0, column=0, sticky="w", pady=5)
SchoolNameElem = tk.Entry(elementary_frame, width=30)
SchoolNameElem.grid(row=0, column=1, pady=5)

tk.Label(elementary_frame, text="Year Graduated:").grid(row=1, column=0, sticky="w", pady=5)
YearGradElem = tk.Entry(elementary_frame, width=20)
YearGradElem.grid(row=1, column=1, pady=5)

# Junior High Frame
junior_frame = tk.LabelFrame(education_section, text="Junior High School", padx=10, pady=10)
junior_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(junior_frame, text="School Name:").grid(row=0, column=0, sticky="w", pady=5)
SchoolNameJun = tk.Entry(junior_frame, width=30)
SchoolNameJun.grid(row=0, column=1, pady=5)

tk.Label(junior_frame, text="Year Graduated:").grid(row=1, column=0, sticky="w", pady=5)
YearGradJun = tk.Entry(junior_frame, width=20)
YearGradJun.grid(row=1, column=1, pady=5)

# Senior High Frame
senior_frame = tk.LabelFrame(education_section, text="Senior High School", padx=10, pady=10)
senior_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

tk.Label(senior_frame, text="School Name:").grid(row=0, column=0, sticky="w", pady=5)
SchoolNameSen = tk.Entry(senior_frame, width=30)
SchoolNameSen.grid(row=0, column=1, pady=5)

tk.Label(senior_frame, text="Strand:").grid(row=1, column=0, sticky="w", pady=5)
StrandSen = tk.Entry(senior_frame, width=20)
StrandSen.grid(row=1, column=1, pady=5)

tk.Label(senior_frame, text="Year Graduated:").grid(row=2, column=0, sticky="w", pady=5)
YearGradSen = tk.Entry(senior_frame, width=20)
YearGradSen.grid(row=2, column=1, pady=5)

# College
college_section = tk.LabelFrame(education_inner, text="College", padx=10, pady=10)
college_section.pack(padx=20, pady=10, fill="x")

# School Name
tk.Label(college_section, text="School Name:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
SchoolNameCol = tk.Entry(college_section)
SchoolNameCol.grid(row=0, column=1, padx=5, pady=3)

# Year Graduated
tk.Label(college_section, text="Year Graduated:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
YearGradCol = tk.Entry(college_section)
YearGradCol.grid(row=1, column=1, padx=5, pady=3)


# Checkboxes
transferee_var = tk.BooleanVar()
new_student_var = tk.BooleanVar()
old_student_var = tk.BooleanVar()
cross_enrollee_var = tk.BooleanVar()
returnee_var = tk.BooleanVar()

Checkbuttons_Info = [
    ("Transferee", transferee_var),
    ("New Student", new_student_var),
    ("Old Student", old_student_var),
    ("Cross Enrollee", cross_enrollee_var),
    ("Returnee", returnee_var)
]

for index, (text, var) in enumerate(Checkbuttons_Info):
    row = 2 + (index // 2)
    column = index % 2
    
    tk.Checkbutton(college_section, 
                   text=text, 
                   variable=var, 
                   bg=college_section.cget("bg")).grid(
                       row=row, column=column, sticky="w", padx=5, pady=3)
    
# Make columns expand evenly
education_section.grid_columnconfigure(0, weight=1)
education_section.grid_columnconfigure(1, weight=1)
education_section.grid_columnconfigure(2, weight=1)

    # === Submit Button ===
submit_btn = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",command=FinalCheck, padx=20, pady=10)
submit_btn.pack(pady=20)

# Show personal details first
show_frame(personal_frame)

root.mainloop()