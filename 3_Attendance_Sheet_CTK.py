from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox
import subprocess
from datetime import datetime
from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox, Toplevel, OptionMenu, StringVar
from collections import defaultdict
# ==================== Window Setup ====================
window = CTk()
window.title("Student Enrollment Form")
height = 825
width = 1300
x = (window.winfo_screenwidth()//2)-(width//2) 
y = (window.winfo_screenheight()//2)-(height//2) 
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==================== Window Switch Function ====================
def SWITCH_WINDOW():
    window.destroy()

# ==================== Top Frame ====================
nav_top_frame = CTkFrame(window, fg_color="transparent")
nav_top_frame.pack(side="top", fill="x")

logout_btn = CTkButton(nav_top_frame, text="Logout", font=("Arial", 15, "bold"), command=SWITCH_WINDOW)
logout_btn.pack(side="right", padx=5, pady=5)

# ==================== Main Container ====================
main_container = CTkFrame(window)
main_container.pack(fill="both", expand=True)

# ==================== Main Top Container ====================
main_top_container = CTkFrame(main_container, fg_color="transparent", bg_color="transparent")
main_top_container.pack(side="top", fill="x", padx=20, pady=20)

main_top_label = CTkLabel(main_top_container, text="Student Attendance Sheet", font=("Arial", 30, "bold"))
main_top_label.pack(pady=10, side="top")

# ==================== Footer ====================
present = datetime.now().strftime("%B %d, %Y - %I:%M %p")

footer = CTkLabel(window, text=f"Enrollment Form | Logged in as: Student | © {present}", font=("Arial", 12))
footer.pack(side="bottom", fill="x", pady=5)

# ==================== Main User Data Container ====================
user_data_container = CTkFrame(main_container)
user_data_container.pack(fill="both", expand=True)

top_section = CTkFrame(user_data_container, fg_color= "transparent")
top_section.pack(padx=20, pady=10, fill="x")

right_top = CTkFrame(top_section)
right_top.pack(side="right", fill="both", expand=True)
right_first_row = CTkFrame(right_top, fg_color= "transparent")
right_first_row.grid(row=0, column=0, padx=10, pady=5, sticky="w")
right_second_row = CTkFrame(right_top, fg_color= "transparent")
right_second_row.grid(row=1, column=0, padx=10, pady=5, sticky="w")

student_id_label = CTkLabel(right_first_row, text="Student ID:", font=("Arial", 14))
student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
student_entry = CTkEntry(right_first_row, width=250, font=("Arial", 14), placeholder_text="Enter Student ID", height= 35, fg_color= "transparent", bg_color= "transparent")
student_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

student_first_name_label = CTkLabel(right_first_row, text="First Name:", font=("Arial", 14))
student_first_name_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
student_first_name_entry = CTkEntry(right_first_row, width=220, font=("Arial", 14), placeholder_text="Enter First Name", height= 35, fg_color= "transparent", bg_color= "transparent")
student_first_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

student_last_name_label = CTkLabel(right_first_row, text="Last Name:", font=("Arial", 14))
student_last_name_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
student_last_name_entry = CTkEntry(right_first_row, width=220, font=("Arial", 14), placeholder_text="Enter Last Name", height= 35, fg_color= "transparent", bg_color= "transparent")
student_last_name_entry.grid(row=1, column=2, padx=10, pady=5, sticky="w")


course_section_label = CTkLabel(right_second_row, text="Course/Section:", font=("Arial", 14))
course_section_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
sec_var = ["Select Section", "1A", "1B", "1C"]
course_section_entry = CTkComboBox(right_second_row, width=250, font=("Arial", 14), height= 35, bg_color= "transparent", values=sec_var, state="readonly")
course_section_entry.set("Select Section")
course_section_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

lrn_label = CTkLabel(right_second_row, text="LRN:", font=("Arial", 14))
lrn_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
lrn_entry = CTkEntry(right_second_row, width=250, font=("Arial", 14), placeholder_text="Enter LRN", height= 35, fg_color= "transparent", bg_color= "transparent")
lrn_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

student_gender_label = CTkLabel(right_second_row, text="Gender:", font=("Arial", 14))
student_gender_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
gen_var = ["Select Gender", "Male", "Female"]
student_gender_entry = CTkComboBox(right_second_row, width=170, font=("Arial", 14), height= 35, bg_color= "transparent", values=gen_var, state="readonly")
student_gender_entry.set("Select Gender")
student_gender_entry.grid(row=1, column=2, padx=10, pady=5, sticky="w")

student_age_label = CTkLabel(right_second_row, text="Age:", font=("Arial", 14))
student_age_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")
student_age_entry = CTkEntry(right_second_row, width=150, font=("Arial", 14), placeholder_text="Enter Age", height= 35, fg_color= "transparent", bg_color= "transparent")
student_age_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

left_top = CTkFrame(top_section, bg_color="transparent", fg_color= "transparent")
left_top.pack(side="right", padx=10)

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

picture_frame = CTkFrame(left_top, width=200, height=200, border_color="black", border_width=6, corner_radius=10, fg_color="transparent")
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

# ==================== Subject Title Container ====================
subject_title_section = CTkFrame(user_data_container)
subject_title_section.pack(padx=20, pady=10, fill="x")

subject_title_label = CTkLabel(subject_title_section, text= "SUBJECTS", font= ("Id Inter", 25))
subject_title_label.pack(padx=20, pady=10, anchor=W)

# ==================== Subject Container ====================
scrollable_subject_container = CTkScrollableFrame(user_data_container, fg_color="transparent", bg_color="transparent")
scrollable_subject_container.pack(padx=20, fill="both", expand=True)

subject_data = [
    ("ITCS103", "Computer Programming 2"),
    ("ITPS102", "Introduction to Human Computer Interaction"),
    ("ITPS103", "Discrete Mathematics"),
    ("ETS", "Ethics"),
    ("US", "Understanding the Self")
]

current_month_year = datetime.now().strftime("%B, %Y")

for index, (subject_code, title) in enumerate(subject_data):
    subject_frame = CTkFrame(scrollable_subject_container, width=600, height=200, border_width=6, corner_radius=10)
    row = index // 2
    col = index % 2
    subject_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    subject_frame.pack_propagate(False)

    subject_code_label = CTkLabel(subject_frame, text=subject_code, font=("Arial", 18, "bold"))
    subject_code_label.pack(anchor="center", pady=(10, 0))

    subject_title_label = CTkLabel(subject_frame, text=title, font=("Arial", 12))
    subject_title_label.pack(anchor="center", pady=(5, 0))

    date_label = CTkLabel(subject_frame, text=current_month_year, font=("Arial", 14, "italic"))
    date_label.pack(anchor="center", pady=(5, 10))

    attendance_frame = CTkLabel(subject_frame)
    attendance_frame.pack(anchor="center")

    absent_box = CTkFrame(attendance_frame, width=100, height=60, border_width=2, corner_radius=8)
    absent_box.grid(row=0, column=0, padx=10)
    absent_box.pack_propagate(False)
    absent_label = CTkLabel(absent_box, text="0", font=("Arial", 16, "bold"))
    absent_label.pack(pady=3)
    absent_text = CTkLabel(absent_box, text="Absent", font=("Arial", 12))
    absent_text.pack(pady=5)

    present_box = CTkFrame(attendance_frame, width=100, height=60, border_width=2, corner_radius=8)
    present_box.grid(row=0, column=1, padx=10)
    present_box.pack_propagate(False)
    present_label = CTkLabel(present_box, text="0", font=("Arial", 16, "bold"))
    present_label.pack(pady=3)
    present_text = CTkLabel(present_box, text="Present", font=("Arial", 12))
    present_text.pack(pady=5)


# ==================== Function to Update Attendance Counts ====================
def update_attendance_counts():
    # Initialize counters for subjects
    subject_attendance_counts = defaultdict(lambda: {"Present": 0, "Absent": 0})

    try:
        # Read the Attendance Information sheet
        df = pd.read_excel('user_account_data.xlsx', sheet_name='Attendance Information')

        # Count Present and Absent for each subject code
        for _, row in df.iterrows():
            subject_code = row['Subject Code']
            attendance_status = row['Attendance Status']

            if attendance_status in subject_attendance_counts[subject_code]:
                subject_attendance_counts[subject_code][attendance_status] += 1

        # Update GUI with attendance counts
        for index, (subject_code, title) in enumerate(subject_data):
            present_count = subject_attendance_counts[subject_code]['Present']
            absent_count = subject_attendance_counts[subject_code]['Absent']

            present_label = present_box.grid_slaves(row=0, column=1)[0]
            absent_label = absent_box.grid_slaves(row=0, column=0)[0]

            present_label.configure(text=str(present_count))
            absent_label.configure(text=str(absent_count))

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while updating attendance counts: {e}")

# # Call the update_attendance_counts function when the application starts or at any other event based on requirement
# update_attendance_counts()

# ==================== Function Container For Saving and Gui  ====================
def save_entry_data(entries):
    # Collect data from entry fields
    student_id = student_entry.get()
    first_name = student_first_name_entry.get()
    last_name = student_last_name_entry.get()
    course_section = course_section_entry.get()
    lrn = lrn_entry.get()
    gender = student_gender_entry.get()
    age = student_age_entry.get()

    # Create a DataFrame from the collected data
    df = pd.DataFrame([entries], columns=[
        "Student ID",
        "First Name",
        "Last Name",
        "Course/Section",
        "LRN",
        "Gender",
        "Age",
        "Subject Code",
        "Attendance Status",
        "Date and Time"
    ])

    try:
        # Load existing workbook or create a new one
        with pd.ExcelWriter('user_account_data.xlsx', engine='openpyxl', mode='a') as writer:
            # Check if the sheet already exists and set header accordingly
            if 'Attendance Information' in writer.sheets:
                df.to_excel(writer, sheet_name='Attendance Information', index=False, header=False)
            else:
                df.to_excel(writer, sheet_name='Attendance Information', index=False)

        messagebox.showinfo("Success", "Data saved successfully to Attendance Information.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving data: {e}")
        # At the end of the save_entry_data function
    save_entry_data(entries)
def open_attendance_subjects():
    attendance_window = Toplevel(window)  # Create a new window
    attendance_window.title("Attendance")
    attendance_window.geometry("400x300")
    
    # Change the background color of the attendance window
    attendance_window.configure(bg="#f0f0f0")  # Light gray
    
    # Label for subject selection with increased font size
    subject_label = CTkLabel(attendance_window, text="Select Subject:", font=("Arial", 16, "bold"), text_color="black")
    subject_label.pack(pady=10)

    # Subject options
    subj_menu = ["ITCS103", "ITPS102", "ITPS103", "ETS", "US"]
    selected_subject = StringVar()
    subj_options = OptionMenu(attendance_window, selected_subject, *subj_menu)
    subj_options.config(font=("Arial", 14))  # Change font size for OptionMenu
    subj_options.pack(pady=10)

    # Status selection label and buttons with increased font size
    status_label = CTkLabel(attendance_window, text="Status:", font=("Arial", 16, "bold"), text_color="black")
    status_label.pack(pady=10)

    def mark_attendance(status):
        subject_code = selected_subject.get()
        if subject_code:
            # Capture the current date and time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entries = [
                student_entry.get(),
                student_first_name_entry.get(),
                student_last_name_entry.get(),
                course_section_entry.get(),
                lrn_entry.get(),
                student_gender_entry.get(),
                student_age_entry.get(),
                subject_code,
                status,
                current_time
            ]
            # Save the entry data
            save_entry_data(entries)
        else:
            messagebox.showwarning("Warning", "Please select a subject")

    # Present Button
    present_btn = CTkButton(attendance_window, text="Present", command=lambda: mark_attendance("Present"), font=("Arial", 14, "bold"))
    present_btn.pack(side="left", padx=20, pady=20)

    # Absent Button
    absent_btn = CTkButton(attendance_window, text="Absent", command=lambda: mark_attendance("Absent"), font=("Arial", 14, "bold"))
    absent_btn.pack(side="right", padx=20, pady=20)

# The button that opens the attendance window
submit_attendance_btn = CTkButton(right_first_row, text="Submit Attendance", font=("Arial", 15, "bold"), command=open_attendance_subjects)
submit_attendance_btn.grid(row=1, column=3, padx=10, pady=5, sticky="w")

# ==================== Function to Update Attendance Counts ====================
def update_attendance_counts():
    # Initialize counters for subjects
    subject_attendance_counts = defaultdict(lambda: {"Present": 0, "Absent": 0})

    try:
        # Read the Attendance Information sheet
        df = pd.read_excel('user_account_data.xlsx', sheet_name='Attendance Information')

        # Count Present and Absent for each subject code
        for _, row in df.iterrows():
            subject_code = row['Subject Code']
            attendance_status = row['Attendance Status']

            if attendance_status in subject_attendance_counts[subject_code]:
                subject_attendance_counts[subject_code][attendance_status] += 1

        # Update GUI with attendance counts
        for index, (subject_code, title) in enumerate(subject_data):
            # Retrieve counts
            present_count = subject_attendance_counts[subject_code]['Present']
            absent_count = subject_attendance_counts[subject_code]['Absent']

            # Find the subject frame
            subject_frame = scrollable_subject_container.grid_slaves(row=index // 2, column=index % 2)

            # Check if the subject frame exists before accessing
            if subject_frame:
                subject_frame = subject_frame[0]  # Get the first subject frame in the list

                # Update present label
                present_box = subject_frame.grid_slaves(row=1, column=1)  # Adjust as needed
                absent_box = subject_frame.grid_slaves(row=1, column=0)  # Adjust as needed

                # Only update if present and absent boxes exist
                if present_box:
                    present_label = present_box[0]
                    present_label.configure(text=str(present_count))

                if absent_box:
                    absent_label = absent_box[0]
                    absent_label.configure(text=str(absent_count))

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while updating attendance counts: {e}")

# ==================== Window Starter ====================

# update_attendance_counts()  # Refresh attendance counts after saving
window.mainloop()            # Start the main loop
