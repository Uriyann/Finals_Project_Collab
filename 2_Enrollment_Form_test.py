import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox

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

def image_id_section_debugger():
    student= Student_entry.get()
    course= Course_Section_enrty.get()
    lrn= lrn_entry.get()
    suname= surname_entry.get()
    firsname= firstname_entry.get()
    m_i= middle_entry.get()
    month= month_box.get()
    day= day_box.get()
    year= year_box.get()
    age= age_box.get()
    religion= religion_box.get()
    marital= marital_box.get()



    if (student and course and lrn and suname and firsname and m_i and month and day and year 
        and age and religion and marital and month != "MM" and day != "DD" and year != "YYYY" and religion != "Select Religion" 
        and marital != "Select Marital Status"):
        
    
        print("Enrollment Entry: \n" \
        "Student ID: " + student + "\n"
        "Course/Section: " + course + "\n" \
        "LRN: " + lrn + "\n"
            
        "Surname: " + suname + "\n\n" \
        "Firstname: " + firsname + "\n" \
        "M.I.: " + m_i + "\n"
        
        "Birthdate: " + month + "/n" + day + "/n" + year + "\n" \
        "Age: " + age + "\n" ) 
        

        messagebox.showinfo(title="Enrollment Entry", message="Enrollment Entry Successful!")
        return True
    else:
        messagebox.showerror(title="Enrollment Entry", message="Please fill in all fields.")
        return False
    





Student_ID= tk.Label(left_top, text="Student ID:").grid(row=0, column=0, sticky="w")
Student_entry = tk.Entry(left_top, width=30)
Student_entry.grid(row=0, column=1, pady=5)

Course_Section= tk.Label(left_top, text="Course/Section:").grid(row=1, column=0, sticky="w")
Course_Section_enrty= tk.Entry(left_top, width=30)
Course_Section_enrty.grid(row=1, column=1, pady=5)

lrn= tk.Label(left_top, text="LRN:").grid(row=2, column=0, sticky="w")
lrn_entry= tk.Entry(left_top, width=30)
lrn_entry.grid(row=2, column=1, pady=5)

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
tk.Label(personal, text="Age").grid(row=0, column=0, sticky="w", padx=5, pady=3)
age_values = list(range(1, 101))  # Assuming age between 1 and 100
age_box = ttk.Combobox(personal, values=age_values, width=8, state="readonly")
age_box.set("Select Age")
age_box.grid(row=0, column=1, sticky="w", padx=5, pady=3)

fields = [
    ("Birthdate (MM/DD/YYYY)", 1),
    ("Birthplace City", 2),
    ("Nationality", 4), ("Religion", 5),
    ("Marital Status", 6), ("Language Spoken", 7)
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

    else:
        personal_info = tk.Entry(personal, width=40)
        personal_info.grid(row=i+1, column=1, padx=5, pady=3)

tk.Label(personal, text="Gender").grid(row=9, column=0, sticky="w", padx=5, pady=3)

gender_frame = tk.Frame(personal, bg="#f4f4f4")
gender_frame.grid(row=9, column=1, sticky="w", padx=5)

male_var = tk.IntVar()
female_var = tk.IntVar()

tk.Checkbutton(gender_frame, text="Male", variable=male_var, bg="#f4f4f4").pack(side="left", padx=5)
tk.Checkbutton(gender_frame, text="Female", variable=female_var, bg="#f4f4f4").pack(side="left", padx=5)

# Address Section
address = tk.LabelFrame(frame, text="Address", padx=10, pady=10)
address.pack(padx=20, pady=10, fill="x")

address_fields = ["Street No.", "Barangay", "City/Municipality", "Province", "Zip Code", "Country"]
for i, field in enumerate(address_fields):
    tk.Label(address, text=field).grid(row=i, column=0, padx=5, pady=3)
    tk.Entry(address, width=30).grid(row=i, column=1, padx=5, pady=3)

# Contact Information
contact = tk.LabelFrame(frame, text="Contact Information", padx=10, pady=10)
contact.pack(padx=20, pady=10, fill="x")

tk.Label(contact, text="Email:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
tk.Entry(contact, width=40).grid(row=0, column=1, padx=5)
tk.Label(contact, text="Phone No:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
tk.Entry(contact, width=40).grid(row=1, column=1, padx=5)

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
tk.Entry(elementary_frame, width=30).grid(row=0, column=1, pady=5)

tk.Label(elementary_frame, text="Year Graduated:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(elementary_frame, width=20).grid(row=1, column=1, pady=5)

# Junior High Frame
junior_frame = tk.LabelFrame(education_section, text="Junior High School", padx=10, pady=10)
junior_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(junior_frame, text="School Name:").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(junior_frame, width=30).grid(row=0, column=1, pady=5)

tk.Label(junior_frame, text="Year Graduated:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(junior_frame, width=20).grid(row=1, column=1, pady=5)

# Senior High Frame
senior_frame = tk.LabelFrame(education_section, text="Senior High School", padx=10, pady=10)
senior_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

tk.Label(senior_frame, text="School Name:").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(senior_frame, width=30).grid(row=0, column=1, pady=5)

tk.Label(senior_frame, text="Strand:").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(senior_frame, width=20).grid(row=1, column=1, pady=5)

tk.Label(senior_frame, text="Year Graduated:").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(senior_frame, width=20).grid(row=2, column=1, pady=5)

# College
college_section = tk.LabelFrame(education_inner, text="College", padx=10, pady=10)
college_section.pack(padx=20, pady=10, fill="x")

# School Name
tk.Label(college_section, text="School Name:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
tk.Entry(college_section).grid(row=0, column=1, padx=5, pady=3)

# Year Graduated
tk.Label(college_section, text="Year Graduated:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
tk.Entry(college_section).grid(row=1, column=1, padx=5, pady=3)

# Checkboxes
transferee_var = tk.BooleanVar()
new_student_var = tk.BooleanVar()
old_student_var = tk.BooleanVar()
cross_enrollee_var = tk.BooleanVar()
returnee_var = tk.BooleanVar()  # added for Returnee

tk.Checkbutton(college_section, text="Transferee", variable=transferee_var, bg=college_section.cget("bg")).grid(row=2, column=0, sticky="w", padx=5, pady=3)
tk.Checkbutton(college_section, text="New Student", variable=new_student_var, bg=college_section.cget("bg")).grid(row=2, column=1, sticky="w", padx=5, pady=3)
tk.Checkbutton(college_section, text="Old Student", variable=old_student_var, bg=college_section.cget("bg")).grid(row=3, column=0, sticky="w", padx=5, pady=3)
tk.Checkbutton(college_section, text="Cross Enrollee", variable=cross_enrollee_var, bg=college_section.cget("bg")).grid(row=3, column=1, sticky="w", padx=5, pady=3)
tk.Checkbutton(college_section, text="Returnee", variable=returnee_var, bg=college_section.cget("bg")).grid(row=4, column=0, sticky="w", padx=5, pady=3)

# Make columns expand evenly
education_section.grid_columnconfigure(0, weight=1)
education_section.grid_columnconfigure(1, weight=1)
education_section.grid_columnconfigure(2, weight=1)

    # === Submit Button ===
submit_btn = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", padx=20, pady=10, command=image_id_section_debugger)
submit_btn.pack(pady=20)

# Show personal details first
show_frame(personal_frame)

root.mainloop()