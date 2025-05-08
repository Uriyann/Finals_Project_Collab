from customtkinter import *
import customtkinter as ctk
from datetime import datetime
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox
import subprocess
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import re
import random
    
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

# ==================== Functions ====================
# Creating a new sheet in the workbook and saving it
def create_new_sheet():
    if not FinalCheck():
        return
    
    try:

        sections = Course_Section_entry.get().strip()
        if sections not in ["1A", "1B", "1C"]:
            messagebox.showerror(title="Error", message="Please select a valid section.")
            return
        
        new_sheet_name = f"{sections} Enrollment Information "
        file_path_to_excel = "user_account_data.xlsx"

        try:
            wb = load_workbook(file_path_to_excel)
        except FileNotFoundError:
            wb = Workbook()
            wb.save(file_path_to_excel)

        if new_sheet_name in wb.sheetnames:
            new_sheet = wb[new_sheet_name]    

        else:
            new_sheet = wb.create_sheet(new_sheet_name)
            new_headers = [
                    "Student ID", "Course/Section", "LRN", 
                    "", 
                    "Surname", "Firstname", "Middle Initial", 
                    "", 
                    "Gender", "Age", "Birthdate", "Birthplace", "Nationality", "Religion", "Marital Status", "Language Spoken", 
                    "", 
                    "Street", "Barangay", "City", "Zip Code", "Province", "Country", 
                    "", 
                    "Email", "Contact Number",
                    "",
                    "Father's Name", "Father's Address", "Father's Occupation", "Father's Contact No",
                    "",
                    "Mother's Name", "Mother's Address","Mother's Occupation", "Mother's Contact No",
                    "",
                    "Guardian's Name", "Guardian's Relationship", "Guardian's Address", "Guardian's Occupation", "Guardian's Contact No",
                    "",
                    "Elementary School", "Elementary Address", "Elementary Year Graduated",
                    "",
                    "Junior High School", "Junior High Address", "Junior High Year Graduated",
                    "",
                    "Senior High School", "Senior High Address", "Senior High Strand", "Senior High Year Graduated",
                    "",
                    "College", "College Address", "College Year Graduated"
                        ]
            new_sheet.append(new_headers)

        student_info_data = [
                Student_entry.get().strip(), Course_Section_entry.get().strip(), lrn_entry.get().strip(), 
                ""
                ]
        student_name_data = [
            surname_entry.get().strip().strip(), firstname_entry.get().strip(), middle_entry.get().strip(), 
            ""
                ]
        
        student_personal_detail_data = [
                "Male" if gender_var.get() == 1 else "Female" if gender_var.get() == 2 else "Prefer not to answer", 
                age_box.get().strip(), f"{month_box.get().strip()} {day_box.get().strip()}, {year_box.get().strip()}",
                birthplace_entry.get().strip(), nationality_entry.get().strip(), religion_box.get().strip(), marital_status_box.get().strip(), 
                language_entry.get().strip(), 
                "", 
                street_entry.get().strip(), brgy_entry.get().strip(), city_entry.get().strip(),
                zip_code_entry.get().strip(), province_entry.get().strip(), country_entry.get().strip(), 
                "",
                email_entry.get().strip(), num_entry.get().strip(),
                ""
                ]
        student_family_detail_data = [
                name_father_entry.get().strip(), address_father_entry.get().strip(), occupation_father_entry.get().strip(), phon_father_entry.get().strip(),
                "",
                name_mother_entry.get().strip(), address_mother_entry.get().strip(), occupation_mother_entry.get().strip(), phon_mother_entry.get().strip(),
                "",
                name_guardian_entry.get().strip(), rel_guardian_entry.get().strip(), address_guardian_entry.get().strip(),
                occupation_guardian_entry.get().strip(), phon_guardian_entry.get().strip(),
                ""
                ]
        student_educational_detail_data = [
                schl_elem_entry.get().strip(), address_elem_entry.get().strip(), yr_elem_entry.get().strip(),
                "",
                schl_js_entry.get().strip(), address_js_entry.get().strip(), yr_js_entry.get().strip(),
                "",
                schl_shs_entry.get().strip(), address_shs_entry.get().strip(), strand_shs_entry.get().strip(), yr_shs_entry.get().strip(),
                "",
                schl_cg_entry.get().strip(), address_cg_entry.get().strip(), yr_cg_entry.get().strip()
                ]
        
        new_sheet.append(student_info_data + student_name_data + student_personal_detail_data + student_family_detail_data + student_educational_detail_data)
        

        wb.save(file_path_to_excel)
        messagebox.showinfo(title= "Success", message= "Data saved successfully!")
        format_excel()

        fields_to_readonly = [
                Student_entry, generate_student_id, Course_Section_entry, lrn_entry, generate_student_lrn,
                surname_entry, firstname_entry, middle_entry, male_checkbox, female_checkbox, none_binary_checkbox, 
                age_box, month_box, day_box, year_box, birthplace_entry, nationality_entry, religion_box, 
                marital_status_box, language_entry, street_entry, brgy_entry, city_entry, zip_code_entry, 
                province_entry, country_entry, email_entry, num_entry, name_father_entry, address_father_entry, 
                occupation_father_entry, phon_father_entry, name_mother_entry, address_mother_entry, occupation_mother_entry, 
                phon_mother_entry, name_guardian_entry, rel_guardian_entry, address_guardian_entry,
                occupation_guardian_entry, phon_guardian_entry, same_chk_box, schl_elem_entry, address_elem_entry,
                yr_elem_entry, schl_js_entry, address_js_entry, yr_js_entry, schl_shs_entry, address_shs_entry,
                strand_shs_entry, yr_shs_entry, schl_cg_entry, address_cg_entry, yr_cg_entry, if_transferee_chk_box
        ]
        for field in fields_to_readonly:
            try:
                field.configure(state="readonly")
            except AttributeError:
                pass

        gender_var.set(0)
        age_box.set("Select Age")
        month_box.set("MM")
        day_box.set("DD")
        year_box.set("YYYY")
        religion_box.set("Select Religion")
        marital_status_box.set("Select Marital Status")

    except Exception as e:
        messagebox.showerror(title= "Error", message= f"An error occurred: {e}")

# Validating the User per Email
def validating_user_email():
    try:

        email = email_entry.get().strip()
        if not email:
            messagebox.showerror(title="Error", message="Please enter an email address.")
            return

        wb = load_workbook("user_account_data.xlsx")
        account_data_sheet = wb["Userdata"]
        for row in account_data_sheet.iter_rows(min_row=2, values_only=True):
            if row[2] == email:
                surname_entry.delete(0, END)
                surname_entry.insert(0, row[1])

                firstname_entry.delete(0, END)
                firstname_entry.insert(0, row[0])

                email_entry.delete(0, END)
                email_entry.insert(0, row[2])
                return 
        
        messagebox.showerror(title="Error", message="User not found.")
            
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")

# Generating a Formatted User ID with Random Numbers
def generate_user_id(yr: int = 2025, existing_ids=None):
    try:

        section = Course_Section_entry.get().strip()

        if section not in ["1A", "1B", "1C"]:
            raise ValueError("Section must be '1A', '1B', or '1C'.")

        year_part = str(yr)[1:]

        if existing_ids is None:
            existing_ids = set()

        while True:
            number_part = f"{random.randint(0, 9999):04}"
            user_id = f"{year_part}{section}-{number_part}"

            if user_id not in existing_ids:
                Student_entry.delete(0, END)
                Student_entry.insert(0, user_id)
                Student_entry.configure(state="readonly")
                Course_Section_entry.configure(state="readonly")
                return user_id

    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")

# Generating a Formatted User LRN with Random Numbers
def generate_user_lrn(special_num: int = 20011213, existing_lrns=None):
    try:

        format_lrn = str(special_num)

        if existing_lrns is None:
            existing_lrns = set()

        while True:
            number_part = f"{random.randint(0, 9999):04}"
            user_lrn = f"{format_lrn}{number_part}"

            if user_lrn not in existing_lrns:
                lrn_entry.delete(0, END)
                lrn_entry.insert(0, user_lrn)
                lrn_entry.configure(state="readonly")
                return user_lrn

    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")

# Validating the User per Password
def ask_password():
    result = {"success": False}

    def check_password():
        try:
            file_path_to_excel = "user_account_data.xlsx"
            wb = load_workbook(file_path_to_excel)
            account_ask_password = wb["Userdata"]

            for row in account_ask_password.iter_rows(min_row=2, values_only=True):
                if row[4] == password_entry.get().strip():
                    result["success"] = True
                    ask_password_window.destroy()
                    return
                
            messagebox.showerror(title= "Access Denied", message= "Incorrect Password.")

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="The file 'user_account_data.xlsx' was not found.")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"An error occurred: {e}")

    ask_password_window = CTkToplevel(window)
    ask_password_window.title("Password Required")
    height = 160
    width = 300
    x = (ask_password_window.winfo_screenwidth()//2)-(width//2) 
    y = (ask_password_window.winfo_screenheight()//2)-(height//2) 
    ask_password_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    ask_password_window.resizable(False, False)
    ask_password_window.grab_set()

    pass_label = CTkLabel(ask_password_window, text="Enter Password:", font=("Arial", 16))
    pass_label.pack(pady=10)

    password_entry = CTkEntry(ask_password_window, show="*", width=200)
    password_entry.pack(pady=5)
    password_entry.focus()

    pass_submit_btn = ctk.CTkButton(ask_password_window, text="Submit", command=check_password)
    pass_submit_btn.pack(pady=15)

    ask_password_window.wait_window()
    return result["success"]

# Loading the user's data
def load_user_data():
    try:

        student_user_account = Student_entry.get().strip()
        student_sections = Course_Section_entry.get().strip()
        student_lrn = lrn_entry.get().strip()

        if not student_user_account:
            messagebox.showerror(title="Error", message="Please enter your Student ID.")
            return
        
        if student_sections not in ["1A", "1B", "1C"]:
            messagebox.showerror(title="Error", message="Please select a valid section.")
            return
        
        if not student_lrn:
            messagebox.showerror(title="Error", message="Please enter your LRN.")
            return

        new_sheet_name = f"{student_sections} Enrollment Information "
        file_path_to_excel = "user_account_data.xlsx"

        wb = load_workbook(file_path_to_excel)
        if new_sheet_name not in wb.sheetnames:
            messagebox.showerror(title="Error", message=f"Sheet '{new_sheet_name}' does not exist.")
            return
        
        student_details_sheet = wb[new_sheet_name]

        for row in student_details_sheet.iter_rows(min_row=2, values_only=True):
            if row[0] == student_user_account and row[1] == student_sections and row[2] == student_lrn:

                if not ask_password():
                    return

                surname_entry.delete(0, END)
                surname_entry.insert(0, row[4])
                firstname_entry.delete(0, END)
                firstname_entry.insert(0, row[5])
                middle_entry.delete(0, END)
                middle_entry.insert(0, row[6])

                gender = row[8]
                if gender == "Male":
                    gender_var.set(1)
                elif gender == "Female":
                    gender_var.set(2)
                elif gender == "Prefer not to answer":
                    gender_var.set(3)
                else:
                    gender_var.set(0)
                age_box.set(row[9])
                birthdate = row[10]
                if birthdate:
                    try:
                        month, day_year = birthdate.split(" ", 1)
                        day, year = day_year.replace(",", "").split(" ")
                        month_box.set(month)
                        day_box.set(day)
                        year_box.set(year)
                    except ValueError:
                        month_box.set("MM")
                        day_box.set("DD")
                        year_box.set("YYYY")
                else:
                    month_box.set("MM")
                    day_box.set("DD")
                    year_box.set("YYYY")
                birthplace_entry.delete(0, END)
                birthplace_entry.insert(0, row[11])
                nationality_entry.delete(0, END)
                nationality_entry.insert(0, row[12])
                religion_box.set(row[13])
                marital_status_box.set(row[14])
                language_entry.delete(0, END)
                language_entry.insert(0, row[15])

                street_entry.delete(0, END)
                street_entry.insert(0, row[17])
                brgy_entry.delete(0, END)
                brgy_entry.insert(0, row[18])
                city_entry.delete(0, END)
                city_entry.insert(0, row[19])
                zip_code_entry.delete(0, END)
                zip_code_entry.insert(0, row[20])
                province_entry.delete(0, END)
                province_entry.insert(0, row[21])
                country_entry.delete(0, END)
                country_entry.insert(0, row[22])

                email_entry.delete(0, END)
                email_entry.insert(0, row[24])
                num_entry.delete(0, END)
                num_entry.insert(0, row[25])

                name_father_entry.delete(0, END)
                name_father_entry.insert(0, row[27])
                address_father_entry.delete(0, END)
                if row[28] is not None and isinstance(row[28], str):
                    address_father_entry.insert(0, row[28])
                elif row[28] is not None:
                    address_father_entry.insert(0, str(row[28]))
                else:
                    address_father_entry.insert(0, "")
                occupation_father_entry.delete(0, END)
                occupation_father_entry.insert(0, row[29])                
                phon_father_entry.delete(0, END)
                phon_father_entry.insert(0, row[30])

                name_mother_entry.delete(0, END)
                name_mother_entry.insert(0, row[32])
                address_mother_entry.delete(0, END)
                address_mother_entry.insert(0, row[33])
                occupation_mother_entry.delete(0, END)
                occupation_mother_entry.insert(0, row[34])                
                phon_mother_entry.delete(0, END)
                phon_mother_entry.insert(0, row[35])

                name_guardian_entry.delete(0, END)
                if row[37] is not None and isinstance(row[37], str):
                    name_guardian_entry.insert(0, row[37])
                elif row[37] is not None:
                    name_guardian_entry.insert(0, str(row[37]))
                else:
                    name_guardian_entry.insert(0, "")
                rel_guardian_entry.delete(0, END)
                if row[38] is not None and isinstance(row[38], str):
                    rel_guardian_entry.insert(0, row[38])
                elif row[38] is not None:
                    rel_guardian_entry.insert(0, str(row[38]))
                else:
                    rel_guardian_entry.insert(0, "")
                address_guardian_entry.delete(0, END)
                if row[39] is not None and isinstance(row[39], str):
                    address_guardian_entry.insert(0, row[39])
                elif row[39] is not None:
                    address_guardian_entry.insert(0, str(row[39]))
                else:
                    address_guardian_entry.insert(0, "")
                occupation_guardian_entry.delete(0, END)
                if row[40] is not None and isinstance(row[40], str):
                    occupation_guardian_entry.insert(0, row[40])
                elif row[40] is not None:
                    occupation_guardian_entry.insert(0, str(row[40]))
                else:
                    occupation_guardian_entry.insert(0, "")                                           
                phon_guardian_entry.delete(0, END)
                if row[41] is not None and isinstance(row[41], str):
                    phon_guardian_entry.insert(0, row[41])
                elif row[41] is not None:
                    phon_guardian_entry.insert(0, str(row[41]))
                else:
                    phon_guardian_entry.insert(0, "")

                schl_elem_entry.delete(0, END)
                schl_elem_entry.insert(0, row[43])
                address_elem_entry.delete(0, END)
                address_elem_entry.insert(0, row[44])
                yr_elem_entry.delete(0, END)
                yr_elem_entry.insert(0, row[45])

                schl_js_entry.delete(0, END)
                schl_js_entry.insert(0, row[47])
                address_js_entry.delete(0, END)
                address_js_entry.insert(0, row[48])
                yr_js_entry.delete(0, END)
                yr_js_entry.insert(0, row[49])

                schl_shs_entry.delete(0, END)
                schl_shs_entry.insert(0, row[51])
                address_shs_entry.delete(0, END)
                address_shs_entry.insert(0, row[52])
                strand_shs_entry.delete(0, END)
                strand_shs_entry.insert(0, row[53])
                yr_shs_entry.delete(0, END)
                yr_shs_entry.insert(0, row[54])

                schl_cg_entry.delete(0, END)
                if row[56] is not None and isinstance(row[56], str):
                    schl_cg_entry.insert(0, row[56])
                elif row[56] is not None:
                    schl_cg_entry.insert(0, str(row[56]))
                else:
                    schl_cg_entry.insert(0, "")
                address_cg_entry.delete(0, END)
                if row[57] is not None and isinstance(row[57], str):
                    address_cg_entry.insert(0, row[57])
                elif row[57] is not None:
                    address_cg_entry.insert(0, str(row[57]))
                else:
                    address_cg_entry.insert(0, "")
                yr_cg_entry.delete(0, END)
                if row[58] is not None and isinstance(row[58], str):
                    yr_cg_entry.insert(0, row[58])
                elif row[58] is not None:
                    yr_cg_entry.insert(0, str(row[58]))
                else:
                    yr_cg_entry.insert(0, "")

                fields_to_disable = [
                        Student_entry, generate_student_id, Course_Section_entry, lrn_entry, generate_student_lrn,
                        surname_entry, firstname_entry, middle_entry, male_checkbox, female_checkbox, none_binary_checkbox, 
                        age_box, month_box, day_box, year_box, birthplace_entry, nationality_entry, religion_box, 
                        marital_status_box, language_entry, street_entry, brgy_entry, city_entry, zip_code_entry, 
                        province_entry, country_entry, email_entry, num_entry, name_father_entry, address_father_entry, 
                        occupation_father_entry, phon_father_entry, name_mother_entry, address_mother_entry, occupation_mother_entry, 
                        phon_mother_entry, name_guardian_entry, rel_guardian_entry, address_guardian_entry,
                        occupation_guardian_entry, phon_guardian_entry, same_chk_box, schl_elem_entry, address_elem_entry,
                        yr_elem_entry, schl_js_entry, address_js_entry, yr_js_entry, schl_shs_entry, address_shs_entry,
                        strand_shs_entry, yr_shs_entry, schl_cg_entry, address_cg_entry, yr_cg_entry, if_transferee_chk_box
                ]
                for field in fields_to_disable:
                    try:
                        field.configure(state="disable")
                    except AttributeError:
                        pass

                return

        messagebox.showerror(title="Error", message="User not found.")
            
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")

def edit_user_data():
    if not ask_password():
        return
        
    fields_to_enable = [
            Student_entry, generate_student_id, Course_Section_entry, lrn_entry, generate_student_lrn,
            surname_entry, firstname_entry, middle_entry, male_checkbox, female_checkbox, none_binary_checkbox, 
            age_box, month_box, day_box, year_box, birthplace_entry, nationality_entry, religion_box, 
            marital_status_box, language_entry, street_entry, brgy_entry, city_entry, zip_code_entry, 
            province_entry, country_entry, email_entry, num_entry, name_father_entry, address_father_entry, 
            occupation_father_entry, phon_father_entry, name_mother_entry, address_mother_entry, occupation_mother_entry, 
            phon_mother_entry, name_guardian_entry, rel_guardian_entry, address_guardian_entry,
            occupation_guardian_entry, phon_guardian_entry, same_chk_box, schl_elem_entry, address_elem_entry,
            yr_elem_entry, schl_js_entry, address_js_entry, yr_js_entry, schl_shs_entry, address_shs_entry,
            strand_shs_entry, yr_shs_entry, schl_cg_entry, address_cg_entry, yr_cg_entry, if_transferee_chk_box
    ]
    for field in fields_to_enable:
        try:
            field.configure(state="normal")
        except AttributeError:
            pass

def update_user_data():
    try:
        student_user_account = Student_entry.get().strip()
        student_sections = Course_Section_entry.get().strip()
        student_lrn = lrn_entry.get().strip()

        if not student_user_account:
            messagebox.showerror(title="Error", message="Please enter your Student ID.")
            return
        
        if student_sections not in ["1A", "1B", "1C"]:
            messagebox.showerror(title="Error", message="Please select a valid section.")
            return
        
        if not student_lrn:
            messagebox.showerror(title="Error", message="Please enter your LRN.")
            return

        new_sheet_name = f"{student_sections} Enrollment Information "
        file_path_to_excel = "user_account_data.xlsx"

        wb = load_workbook(file_path_to_excel)
        if new_sheet_name not in wb.sheetnames:
            messagebox.showerror(title="Error", message=f"Sheet '{new_sheet_name}' does not exist.")
            return

        ws = wb[new_sheet_name]

        for row in ws.iter_rows(min_row=2):
            if row[0].value == Student_entry.get().strip() and row[1].value == Course_Section_entry.get().strip() and row[2].value == lrn_entry.get().strip():

                if not ask_password():
                    return

                row[4].value = surname_entry.get().strip()
                row[5].value = firstname_entry.get().strip()
                row[6].value = middle_entry.get().strip()

                row[8].value = "Male" if gender_var.get() == 1 else "Female" if gender_var.get() == 2 else "Prefer not to answer"
                row[9].value = age_box.get().strip()
                row[10].value = f"{month_box.get().strip()} {day_box.get().strip()}, {year_box.get().strip()}"
                row[11].value = birthplace_entry.get().strip()
                row[12].value = nationality_entry.get().strip()
                row[13].value = religion_box.get().strip()
                row[14].value = marital_status_box.get().strip()
                row[15].value = language_entry.get().strip()

                row[17].value = street_entry.get().strip()
                row[18].value = brgy_entry.get().strip()
                row[19].value = city_entry.get().strip()
                row[20].value = zip_code_entry.get().strip()
                row[21].value = province_entry.get().strip()
                row[22].value = country_entry.get().strip()

                row[24].value = email_entry.get().strip()
                row[25].value = num_entry.get().strip()

                row[27].value =  name_father_entry.get().strip()
                row[28].value = address_father_entry.get().strip()
                row[29].value = occupation_father_entry.get().strip()
                row[30].value = phon_father_entry.get().strip()

                row[32].value = name_mother_entry.get().strip()
                row[33].value = address_mother_entry.get().strip()
                row[34].value = occupation_mother_entry.get().strip()
                row[35].value = phon_mother_entry.get().strip()

                row[37].value = name_guardian_entry.get().strip()
                row[38].value = rel_guardian_entry.get().strip()
                row[39].value = address_guardian_entry.get().strip()
                row[40].value = occupation_guardian_entry.get().strip()
                row[41].value = phon_guardian_entry.get().strip()

                row[43].value = schl_elem_entry.get().strip()
                row[44].value = address_elem_entry.get().strip()
                row[45].value = yr_elem_entry.get().strip()

                row[47].value = schl_js_entry.get().strip()
                row[48].value = address_js_entry.get().strip()
                row[49].value = yr_js_entry.get().strip()

                row[51].value = schl_shs_entry.get().strip()
                row[52].value = address_shs_entry.get().strip()
                row[53].value = strand_shs_entry.get().strip()
                row[54].value = yr_shs_entry.get().strip()

                row[56].value = schl_cg_entry.get().strip()
                row[57].value = address_cg_entry.get().strip()
                row[58].value = yr_cg_entry.get().strip()

                wb.save(file_path_to_excel)
                
                messagebox.showinfo(title="Success", message="User Data Updated Successfully.")
                return
            
            messagebox.showerror(title="Error", message="User not found.") 
    
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))

# Format Fixer Function
def format_excel():
    try:
        sections = Course_Section_entry.get().strip()
        if sections not in ["1A", "1B", "1C"]:
            messagebox.showerror(title="Error", message="Invalid section selected.")
            return

        new_sheet_name = f"{sections} Enrollment Information "
        file_path_to_excel = "user_account_data.xlsx"

        wb = load_workbook(file_path_to_excel)
        if new_sheet_name not in wb.sheetnames:
            messagebox.showerror(title="Error", message=f"Sheet '{new_sheet_name}' does not exist.")
            return
        
        ws = wb[new_sheet_name]

        for cells in ws[1]:
            if cells.value:
                cells.font = Font(bold=True)

        for cols in ws.columns:
            max_length = 0
            col_letter = get_column_letter(cols[0].column)
            for cell in cols:
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except Exception:
                    pass
            ws.column_dimensions[col_letter].width = max_length + 2

        wb.save(file_path_to_excel)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="The Excel file was not found.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")


# ==================== Validators ====================
# Final Check Function
def FinalCheck():
    # ==================== PERSONAL DETAILS PAGE ====================
    # Validate Student ID, Course/Section, and LRN fields
    ReqFields = [
        ("Student ID", Student_entry), 
        ("Course/Section", Course_Section_entry), 
        ("LRN", lrn_entry),
    ]
    for Fieldnames, field in ReqFields:
        try:
            if field.get().strip() == "":
                messagebox.showerror(title="Missing Requirement", message=f"Error: {Fieldnames} is required.")
                return False
        except AttributeError:
            messagebox.showerror(title="Internal Error", message=f"Field '{Fieldnames}' is not a valid input widget.")
            return False
        
    selected_section = Course_Section_entry.get().strip()
    if selected_section == "Select Section":
        messagebox.showerror(title="Missing Requirement", message="Error: Please select a course/section.")
        return False
    
    lrn_value = lrn_entry.get().strip()
    if not lrn_value.isdigit():
        messagebox.showerror(title="Invalid Input", message="Error: LRN must be a valid integer.")
        return False

    # Validate Full Name fields
    FullName = [
        ("Surname", surname_entry), 
        ("Firstname", firstname_entry), 
        ("Middle Initial", middle_entry),
    ]
    
    for Fieldnames, field in FullName:
        field_value = field.get().strip()
        
        
        if field_value == "" or (field_value == "Surname" and Fieldnames == "Surname") or \
           (field_value == "Firstname" and Fieldnames == "Firstname") or \
           (field_value == "M.I." and Fieldnames == "Middle Initial"):
            messagebox.showerror(title="Missing Requirement", message=f"Error: {Fieldnames} is required.")
            return False
        
        if not field_value.isalpha() and field_value != "":
            messagebox.showerror(title="Invalid Input", message=f"Error: {Fieldnames} should contain only letters.")
            return False

    # Check Gender Section
    if gender_var.get() == 0:
        messagebox.showerror(title="Missing Requirement", message="Error: Please select a gender.")
        return False

    # Validate Age field
    if age_box.get() == "Select Age":
        messagebox.showerror(title="Missing Requirement", message="Error: Please select your age.")
        return False

    # Validate Birthdate (Month, Day, Year)
    if month_box.get() in ["MM", "Select Month"]:
        messagebox.showerror(title="Missing Requirement", message="Error: Please select a month.")
        return False
    if day_box.get() in ["DD", "Select Day"]:
        messagebox.showerror(title="Missing Requirement", message="Error: Please select a day.")
        return False
    if year_box.get() in ["YYYY", "Select Year"]:
        messagebox.showerror(title="Missing Requirement", message="Error: Please select a year.")
        return False

    # Validate Birthplace
    birthplace_value = birthplace_entry.get().strip()
    if birthplace_value == "":
        messagebox.showerror(title="Missing Requirement", message="Error: Birthplace is required.")
        return False
    if not birthplace_value.isalpha():
        messagebox.showerror(title="Invalid Input", message="Error: Birthplace should contain only letters.")
        return False

    # Validate Nationality
    nationality_value = nationality_entry.get().strip()
    if nationality_value == "":
        messagebox.showerror(title="Missing Requirement", message="Error: Nationality is required.")
        return False
    if not nationality_value.isalpha():
        messagebox.showerror(title="Invalid Input", message="Error: Nationality should contain only letters.")
        return False

    # Validate Religion
    if religion_box.get() == "Select Religion":
        messagebox.showerror(title="Missing Requirement", message="Error: Religion is required.")
        return False

    # Validate Marital Status
    if marital_status_box.get() == "Select Marital Status":
        messagebox.showerror(title="Missing Requirement", message="Error: Marital Status is required.")
        return False

    # Validate Language Spoken
    language_value = language_entry.get().strip()
    if language_value == "":
        messagebox.showerror(title="Missing Requirement", message="Error: Language Spoken is required.")
        return False
    if not language_value.isalpha():
        messagebox.showerror(title="Invalid Input", message="Error: Language Spoken should contain only letters.")
        return False

    # Validate Address Section (Street, Barangay, City/Municipality, Province, Zip Code, Country)
    Address = [
        ("Street", street_entry),
        ("Barangay", brgy_entry),
        ("City/Municipality", city_entry),
        ("Zip Code", zip_code_entry),
        ("Province", province_entry),
        ("Country", country_entry),
    ]
    for Fieldnames, entry in Address:
        field_value = entry.get().strip()
        if not field_value:
            messagebox.showerror(title="Missing Requirement", message=f"Error: {Fieldnames} is required.")
            return False
        if Fieldnames == "Zip Code" and not field_value.isdigit():
                messagebox.showerror(title="Invalid Input", message=f"Error: {Fieldnames} must be a valid integer.")
                return False
        if Fieldnames in ["Street", "Barangay", "City/Municipality", "Province", "Country"]:
            if not field_value.isalpha():
                messagebox.showerror(title="Invalid Input", message=f"Error: {Fieldnames} should contain only letters.")
                return False
    
    # Validate Contact Information
    email_value = email_entry.get().strip()
    phone_value = num_entry.get().strip()

    if email_value == "":
        messagebox.showerror(title="Missing Requirement", message="Error: Email is required.")
        return False
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, email_value):
        messagebox.showerror(title="Invalid Input", message="Error: Please enter a valid email address.")
        return False

    if phone_value == "":
        messagebox.showerror(title="Missing Requirement", message="Error: Phone Number is required.")
        return False
    if not phone_value.isdigit() and not phone_value.startswith("+"):
        messagebox.showerror(title="Invalid Input", message="Error: Phone Number must be a valid integer or start with '+'.")
        return False

    # ==================== FAMILY BACKGROUND PAGE ====================
    # Validate Parents' Information
    father_name = name_father_entry.get().strip()
    father_occupation = occupation_father_entry.get().strip()
    father_contact = phon_father_entry.get().strip()

    if father_name == "" or father_occupation == "" or father_contact == "":
        messagebox.showerror("Missing Requirement", "Error: Father's information is incomplete.")
        return False
    if not father_name.isalpha() or not father_occupation.isalpha():
        messagebox.showerror("Invalid Input", "Error: Father's Name and Occupation should be strings.")
        return False
    if father_contact != "N/A" and not father_contact.isdigit():
        messagebox.showerror("Invalid Input", "Error: Father's Contact No should be an integer or 'N/A'.")
        return False

    mother_name = name_mother_entry.get().strip()  # Name entry
    mother_occupation = occupation_mother_entry.get().strip()  # Occupation entry
    mother_contact = phon_mother_entry.get().strip()  # Contact entry

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
    if same_chk_var.get() == 0:
        guardian_name = name_guardian_entry.get().strip()
        guardian_relationship = rel_guardian_entry.get().strip()
        guardian_address = address_guardian_entry.get().strip()
        guardian_occupation = occupation_guardian_entry.get().strip()
        guardian_contact = phon_guardian_entry.get().strip()

        
        if guardian_name == "" or guardian_relationship == "" or guardian_address == "" or guardian_occupation == "" or guardian_contact == "":
            messagebox.showerror("Missing Requirement", "Error: Guardian's information is incomplete.")
            return False
        if not guardian_name.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Error: Guardian's Name should contain only letters.")
            return False
        if not guardian_relationship.replace(" ", "").isalpha():
            messagebox.showerror("Invalid Input", "Error: Guardian's Relationship should contain only letters.")
            return False

        # Validate that Contact Number is a valid integer or "N/A"
        if guardian_contact != "N/A" and not guardian_contact.isdigit():
            messagebox.showerror("Invalid Input", "Error: Guardian's Contact Number should be a valid integer or 'N/A'.")
            return False

    # ==================== EDUCATIONAL BACKGROUND PAGE ====================
    # Validate Educational Information
    # Elementary
    elem_school_name = schl_elem_entry.get().strip()
    elem_address = address_elem_entry.get().strip()
    elem_year_grad = yr_elem_entry.get().strip()
    if elem_school_name == "" or elem_address == "" or elem_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Elementary school information is incomplete.")
        return False
    if not elem_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Elementary Year Graduated must be an integer.")
        return False

    # Junior High
    jun_school_name = schl_js_entry.get().strip()
    jun_address = address_js_entry.get().strip()
    jun_year_grad = yr_js_entry.get().strip()
    if jun_school_name == "" or jun_address == "" or jun_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Junior High school information is incomplete.")
        return False
    if not jun_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Junior High Year Graduated must be an integer.")
        return False

    # Senior High
    sen_school_name = schl_shs_entry.get().strip()
    sen_address = address_shs_entry.get().strip()
    sen_strand = strand_shs_entry.get().strip()
    sen_year_grad = yr_shs_entry.get().strip()
    if sen_school_name == "" or  sen_address == "" or sen_strand == "" or sen_year_grad == "":
        messagebox.showerror("Missing Requirement", "Error: Senior High school information is incomplete.")
        return False
    if not sen_year_grad.isdigit():
        messagebox.showerror("Invalid Input", "Error: Senior High Year Graduated must be an integer.")
        return False

    # College
    if if_transferee_var.get() == 0:
        col_school_name = schl_cg_entry.get().strip()
        col_address = address_cg_entry.get().strip()
        col_year_grad = yr_cg_entry.get().strip()

        if col_school_name == "" or col_address == "" or col_year_grad == "":
            messagebox.showerror("Missing Requirement", "Error: College information is incomplete.")
            return False
        if col_year_grad != "N/A" and not col_year_grad.isdigit():
            messagebox.showerror("Invalid Input", "Error: College Year Graduated must be an integer or 'N/A'.")
            return False
    
    return True

# Guardian Checkbox Toggler
def toggle_guardian_fields():
    state = "disabled" if same_chk_var.get() == 1 else "normal"
    if same_chk_var.get() == 1:
        name_guardian_entry.delete(0, END)
        address_guardian_entry.delete(0, END)
        phon_guardian_entry.delete(0, END)
        occupation_guardian_entry.delete(0, END)
        rel_guardian_entry.delete(0, END)

    else:
        name_guardian_entry.configure(state="normal")
        address_guardian_entry.configure(state="normal")
        phon_guardian_entry.configure(state="normal")
        occupation_guardian_entry.configure(state="normal")
        rel_guardian_entry.configure(state="normal")

        name_guardian_entry.insert(0, "Enter Name")
        address_guardian_entry.insert(0, "Enter Address")
        phon_guardian_entry.insert(0, "Enter Contact Number")
        occupation_guardian_entry.insert(0, "Enter Occupation")
        rel_guardian_entry.insert(0, "Relationship")

    name_guardian_entry.configure(state=state)
    address_guardian_entry.configure(state=state)
    phon_guardian_entry.configure(state=state)
    occupation_guardian_entry.configure(state=state)
    rel_guardian_entry.configure(state=state)

# Guardian Checkbox Toggler
def toggle_transferee_fields():
    state = "disabled" if if_transferee_var.get() == 1 else "normal"
    if if_transferee_var.get() == 1:
        schl_cg_entry.delete(0, END)
        address_cg_entry.delete(0, END)
        yr_cg_entry.delete(0, END)

    else:

        schl_cg_entry.configure(state="normal")
        address_cg_entry.configure(state="normal")
        yr_cg_entry.configure(state="normal")

    schl_cg_entry.configure(state=state)
    address_cg_entry.configure(state=state)
    yr_cg_entry.configure(state=state)

# Transferee Checkbox Toggler
def toggle_guardian_fields():
    state = "disabled" if same_chk_var.get() == 1 else "normal"
    if same_chk_var.get() == 1:
        name_guardian_entry.delete(0, END)
        address_guardian_entry.delete(0, END)
        phon_guardian_entry.delete(0, END)
        occupation_guardian_entry.delete(0, END)
        rel_guardian_entry.delete(0, END)

    else:
        name_guardian_entry.configure(state="normal")
        address_guardian_entry.configure(state="normal")
        phon_guardian_entry.configure(state="normal")
        occupation_guardian_entry.configure(state="normal")
        rel_guardian_entry.configure(state="normal")

    name_guardian_entry.configure(state=state)
    address_guardian_entry.configure(state=state)
    phon_guardian_entry.configure(state=state)
    occupation_guardian_entry.configure(state=state)
    rel_guardian_entry.configure(state=state)

# ==================== Events ====================
def change_light_dark_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

# ==================== Switch Window ====================
# Main Portal Window Switch Function
def GO_TO_PORTAL_WINDOW():
    window.destroy()
    subprocess.call(["python", "1_Portal_CTK.py"])

# Attendance Top Level Window Switch Function
def GO_TO_ATTENDANCE_WINDOW():
    subprocess.call(["python", "3_Attendance_Sheet_CTK.py"])

# //////////////////////////////////////////////////////////

# ==================== Navigation Buttons ====================
nav_frame = CTkFrame(window, fg_color="transparent")
nav_frame.pack(side="top", fill="x")

def show_frame(frame):
    frame.tkraise()

# Navigation Buttons
personal_btn = CTkButton(nav_frame, text="Personal Details", font=("Arial", 15, "bold"), command=lambda: show_frame(personal_frame))
personal_btn.pack(side="left", padx=5, pady=5)

family_btn = CTkButton(nav_frame, text="Family Background", font=("Arial", 15, "bold"), command=lambda: show_frame(family_frame))
family_btn.pack(side="left", padx=5, pady=5)

education_btn = CTkButton(nav_frame, text="Educational Background", font=("Arial", 15, "bold"), command=lambda: show_frame(education_frame))
education_btn.pack(side="left", padx=5, pady=5)

attendance_btn = CTkButton(nav_frame, text="Attendance", font=("Arial", 15, "bold"), command=GO_TO_ATTENDANCE_WINDOW)
attendance_btn.pack(side="left", padx=5, pady=5)

logout_btn = CTkButton(nav_frame, text="Logout", font=("Arial", 15, "bold"), command= GO_TO_PORTAL_WINDOW)
logout_btn.pack(side="right", padx=5, pady=5)

switch_light_button = CTkOptionMenu(nav_frame, values=["Dark", "Light"], command= change_light_dark_mode_event)
switch_light_button.pack(side="right", padx=5, pady=5)

# ==================== Main Container ====================
container = CTkFrame(window)
container.pack(fill="both", expand=True)

# ==================== Pages (Frames) ====================
personal_frame = CTkFrame(container)
family_frame = CTkFrame(container)
education_frame = CTkFrame(container)

for frame in (personal_frame, family_frame, education_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# ==================== Footer ====================
present = datetime.now().strftime("%B %d, %Y - %I:%M %p")

footer = CTkLabel(window, text=f"Enrollment Form | Logged in as: Student | © {present}", font=("Arial", 12))
footer.pack(side="bottom", fill="x", pady=5)

# ==================== Buttons ====================
sub_frame = CTkFrame(window, border_width=2)
sub_frame.pack(side="bottom", fill="x")

submit_btn = CTkButton(sub_frame, text="Submit", font=("Arial", 15, "bold"), command=create_new_sheet)
submit_btn.pack(side="right", padx=5, pady=5)

load_btn = CTkButton(sub_frame, text="Load User Data", font=("Arial", 15, "bold"), command=load_user_data)
load_btn.pack(side="left", padx=5, pady=5)

edit_btn = CTkButton(sub_frame, text="Edit User Data", font=("Arial", 15, "bold"), command=edit_user_data)
edit_btn.pack(side="left", padx=5, pady=5)

update_btn = CTkButton(sub_frame, text="Update User Data", font=("Arial", 15, "bold"), command=update_user_data)
update_btn.pack(side="left", padx=5, pady=5)

# ==================== PERSONAL DETAILS PAGE ====================
# Scrollable Frame
scrollable_personal_frame = CTkScrollableFrame(personal_frame)
scrollable_personal_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Headers
personal_header = CTkFrame(scrollable_personal_frame)
personal_header.pack(pady=20)
CTkLabel(personal_header, text="Lucena City", font=("Arial", 22)).pack()
CTkLabel(personal_header, text="STUDENT ENROLLMENT FORM", font=("Arial", 28, "bold")).pack()
CTkLabel(personal_header, text="Second Semester 2024-2025", font=("Arial", 22)).pack()

# Image and ID Section
top_section = CTkFrame(scrollable_personal_frame, fg_color= "transparent")
top_section.pack(padx=20, pady=10, fill="x")

left_top = CTkFrame(top_section, fg_color= "transparent")
left_top.pack(side="left", fill="both", expand=True)

Student_ID = CTkLabel(left_top, text="Student ID:", font=("Arial", 14))
Student_ID.grid(row=0, column=0, padx=40, pady=5, sticky="w")
Student_entry = CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter Student ID", height= 35, fg_color= "transparent", bg_color= "transparent")
Student_entry.grid(row=0, column=1, pady=5)

generate_student_id = CTkButton(left_top, text="Generate Student ID", font=("Arial", 14), command=generate_user_id)
generate_student_id.grid(row=0, column=2, padx=10, pady=5)

Course_Section = CTkLabel(left_top, text="Course/Section:", font=("Arial", 14))
Course_Section.grid(row=1, column=0, padx=40, pady=5, sticky="w")
sec_var = ["Select Section", "1A", "1B", "1C"]
Course_Section_entry= CTkComboBox(left_top, width=250, font=("Arial", 14), height= 35, bg_color= "transparent", values=sec_var, state="readonly")
Course_Section_entry.set("Select Section")
Course_Section_entry.grid(row=1, column=1, pady=5)

lrn = CTkLabel(left_top, text="LRN:", font=("Arial", 14))
lrn.grid(row=2, column=0, padx=40, pady=5, sticky="w")
lrn_entry= CTkEntry(left_top, width=250, font=("Arial", 14), placeholder_text="Enter LRN", height= 35, fg_color= "transparent", bg_color= "transparent")
lrn_entry.grid(row=2, column=1, pady=5)

generate_student_lrn = CTkButton(left_top, text="Generate LRN", font=("Arial", 14), command=generate_user_lrn)
generate_student_lrn.grid(row=2, column=2, padx=10, pady=5)

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

gender_var = IntVar(value=0)

male_checkbox = CTkRadioButton(gender_frame, text="Male", variable=gender_var, value=1)
male_checkbox.grid(row=0, column=0)
female_checkbox = CTkRadioButton(gender_frame, text="Female", variable=gender_var, value=2)
female_checkbox.grid(row=0, column=1)
none_binary_checkbox = CTkRadioButton(gender_frame, text="Prefer not to answer", variable=gender_var, value=3)
none_binary_checkbox.grid(row=0, column=2)

age_label = CTkLabel(second_row_personal_details_frame, text="Age:", font=("Arial", 14), bg_color="transparent")
age_label.grid(row=1, column=1, sticky="w", padx=20, pady=7)
age_values = ["Select Age"] + [str(i) for i in range(1, 101)]
age_box = CTkComboBox(second_row_personal_details_frame, values=age_values, width=150, height= 35, bg_color= "transparent", state="normal")
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
month_box = CTkComboBox(birthdate_frame, values=months, width=120, height= 35, bg_color= "transparent", state="normal")
month_box.set("MM")
month_box.grid(row=0, column=0, padx=3)

days = ["DD"] + [str(x) for x in range(1, 32)]
day_box = CTkComboBox(birthdate_frame, values=days, width=80, height= 35, bg_color= "transparent", state="normal")
day_box.set("DD")
day_box.grid(row=0, column=1, padx=3)

years = ["YYYY"] + [str(x) for x in range(1900, datetime.now().year + 11)]
year_box = CTkComboBox(birthdate_frame, values=years, width=150, height= 35, bg_color= "transparent", state="normal")
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
contact_title_info =CTkLabel(scrollable_personal_frame, text= "CONTACT INFORMATION", font= ("Id Inter", 25))
contact_title_info.pack(padx=20, pady=10, anchor=W)

# Contact Information Details Section
contact_info_details = CTkFrame(scrollable_personal_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
contact_info_details.pack(padx=20, pady=10, fill="x")

first_row_contact_info_details_frame = CTkFrame(contact_info_details, bg_color="transparent", fg_color= "transparent")
first_row_contact_info_details_frame.grid(row=0, column=0, columnspan=3, sticky="we", padx=35, pady=7)

email_label = CTkLabel(first_row_contact_info_details_frame, text="Email:", font=("Arial", 14), bg_color="transparent")
email_label.grid(row=0, column=0, padx=10, pady=7, sticky="w")
email_entry = CTkEntry(first_row_contact_info_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Email", height= 35, fg_color= "transparent", bg_color= "transparent")
email_entry.grid(row=0, column=1, padx=10, pady=7, sticky="wn")
email_entry.bind("<FocusOut>", lambda event: validating_user_email())

num_label = CTkLabel(first_row_contact_info_details_frame, text="Contact Number:", font=("Arial", 14), bg_color="transparent")
num_label.grid(row=0, column=2, padx=10, pady=7, sticky="w")
num_entry = CTkEntry(first_row_contact_info_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Contact Number", height= 35, fg_color= "transparent", bg_color= "transparent")
num_entry.grid(row=0, column=3, padx=10, pady=7, sticky="wn")

empty_frame = CTkFrame(contact_info_details, bg_color="transparent", fg_color= "transparent")
empty_frame.grid(row=1, column=0, columnspan=3, sticky="we", padx=20, pady=7)

empty_label = CTkLabel(empty_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)


# ==================== FAMILY BACKGROUND PAGE ====================
# Scrollable Frame
scrollable_family_background_frame = CTkScrollableFrame(family_frame)
scrollable_family_background_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Headers
family_background_header = CTkFrame(scrollable_family_background_frame)
family_background_header.pack(pady=20)
CTkLabel(family_background_header, text="FAMILY BACKGROUND", font=("Arial", 28, "bold")).pack()

# Parent's Information Title
family_background_title_info =CTkLabel(scrollable_family_background_frame, text= "PARENT'S INFORMATION", font= ("Id Inter", 25))
family_background_title_info.pack(padx=20, pady=10, anchor=W)

# Parent's Details Section
parents_details = CTkFrame(scrollable_family_background_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
parents_details.pack(padx=20, pady=10, fill="x")

row_column_parents_details_frame = CTkFrame(parents_details, bg_color="transparent", fg_color= "transparent")
row_column_parents_details_frame.pack(anchor = CENTER, pady=30)

empty_label = CTkLabel(row_column_parents_details_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)

father_label = CTkLabel(row_column_parents_details_frame, text="FATHER", font=("Arial", 14, "bold"), bg_color="transparent")
father_label.grid(row=0, column=1, padx=10, pady=7)

mother_label = CTkLabel(row_column_parents_details_frame, text="MOTHER", font=("Arial", 14, "bold"), bg_color="transparent")
mother_label.grid(row=0, column=2, padx=10, pady=7)

name_label = CTkLabel(row_column_parents_details_frame, text="Name:", font=("Arial", 14), bg_color="transparent")
name_label.grid(row=1, column=0, padx=10, pady=7, sticky="w")

name_father_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Name", height= 35, fg_color= "transparent", bg_color= "transparent")
name_father_entry.grid(row=1, column=1, padx=10, pady=7)

name_mother_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Name", height= 35, fg_color= "transparent", bg_color= "transparent")
name_mother_entry.grid(row=1, column=2, padx=10, pady=7)

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=2, column=0, padx=10, pady=7, sticky="w")

address_father_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_father_entry.grid(row=2, column=1, padx=10, pady=7)

address_mother_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_mother_entry.grid(row=2, column=2, padx=10, pady=7)

occupation_label = CTkLabel(row_column_parents_details_frame, text="Occupation:", font=("Arial", 14), bg_color="transparent")
occupation_label.grid(row=3, column=0, padx=10, pady=7, sticky="w")

occupation_father_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Occupation", height= 35, fg_color= "transparent", bg_color= "transparent")
occupation_father_entry.grid(row=3, column=1, padx=10, pady=7)

occupation_mother_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Occupation", height= 35, fg_color= "transparent", bg_color= "transparent")
occupation_mother_entry.grid(row=3, column=2, padx=10, pady=7)

phon_num_label = CTkLabel(row_column_parents_details_frame, text="Contact Number:", font=("Arial", 14), bg_color="transparent")
phon_num_label.grid(row=4, column=0, padx=10, pady=7, sticky="w")

phon_father_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Contact Number", height= 35, fg_color= "transparent", bg_color= "transparent")
phon_father_entry.grid(row=4, column=1, padx=10, pady=7)

phon_mother_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Contact Number", height= 35, fg_color= "transparent", bg_color= "transparent")
phon_mother_entry.grid(row=4, column=2, padx=10, pady=7)

guardian_label = CTkLabel(row_column_parents_details_frame, text="GUARDIAN", font=("Arial", 14, "bold"), bg_color="transparent")
guardian_label.grid(row=5, column=1, padx=10, pady=7)

same_chk_var = IntVar()
same_chk_box = CTkCheckBox(row_column_parents_details_frame, text="Same as Father and/or Mother", variable=same_chk_var)
same_chk_box.grid(row=5, column=2, padx=10, pady=7, sticky="w")
same_chk_box.configure(command=toggle_guardian_fields)

name_label = CTkLabel(row_column_parents_details_frame, text="Name:", font=("Arial", 14), bg_color="transparent")
name_label.grid(row=6, column=0, padx=10, pady=7, sticky="w")

name_guardian_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Name", height= 35, fg_color= "transparent", bg_color= "transparent")
name_guardian_entry.grid(row=6, column=1, padx=10, pady=7)

rel_label = CTkLabel(row_column_parents_details_frame, text="Relationship to Student:", font=("Arial", 14), bg_color="transparent")
rel_label.grid(row=6, column=2, padx=10, pady=7, sticky="s")

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=7, column=0, padx=10, pady=7, sticky="w")

address_guardian_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_guardian_entry.grid(row=7, column=1, padx=10, pady=7)

rel_guardian_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Relationship", height= 35, fg_color= "transparent", bg_color= "transparent")
rel_guardian_entry.grid(row=7, column=2, padx=10, pady=7)

occupation_label = CTkLabel(row_column_parents_details_frame, text="Occupation:", font=("Arial", 14), bg_color="transparent")
occupation_label.grid(row=8, column=0, padx=10, pady=7, sticky="w")

occupation_guardian_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Occupation", height= 35, fg_color= "transparent", bg_color= "transparent")
occupation_guardian_entry.grid(row=8, column=1, padx=10, pady=7)

phon_num_label = CTkLabel(row_column_parents_details_frame, text="Contact Number:", font=("Arial", 14), bg_color="transparent")
phon_num_label.grid(row=9, column=0, padx=10, pady=7, sticky="w")

phon_guardian_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Contact Number", height= 35, fg_color= "transparent", bg_color= "transparent")
phon_guardian_entry.grid(row=9, column=1, padx=10, pady=7)

toggle_guardian_fields()

# ==================== EDUCATIONAL BACKGROUND PAGE ====================
# Scrollable Frame
scrollable_educ_background_frame = CTkScrollableFrame(education_frame)
scrollable_educ_background_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Headers
educ_background_header = CTkFrame(scrollable_educ_background_frame)
educ_background_header.pack(pady=20)
CTkLabel(educ_background_header, text="EDUCATIONAL BACKGROUND", font=("Arial", 28, "bold")).pack()

# Educ's Information Title
family_background_title_info =CTkLabel(scrollable_educ_background_frame, text= "EDUCATIONAL INFORMATION", font= ("Id Inter", 25))
family_background_title_info.pack(padx=20, pady=10, anchor=W)

# Educ's Details Section
educ_details = CTkFrame(scrollable_educ_background_frame, bg_color="transparent", fg_color= "transparent", border_width=6, corner_radius=10)
educ_details.pack(padx=20, pady=10, fill="x")

row_column_parents_details_frame = CTkFrame(educ_details, bg_color="transparent", fg_color= "transparent")
row_column_parents_details_frame.pack(anchor = CENTER, pady=30)

empty_label = CTkLabel(row_column_parents_details_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=0)

elem_label = CTkLabel(row_column_parents_details_frame, text="ELEMENTARY", font=("Arial", 14, "bold"), bg_color="transparent")
elem_label.grid(row=0, column=1, padx=10, pady=7)

schl_label = CTkLabel(row_column_parents_details_frame, text="School Name:", font=("Arial", 14), bg_color="transparent")
schl_label.grid(row=1, column=0, padx=10, pady=7, sticky="w")
schl_elem_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter School", height= 35, fg_color= "transparent", bg_color= "transparent")
schl_elem_entry.grid(row=1, column=1, padx=10, pady=7)

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=2, column=0, padx=10, pady=7, sticky="w")
address_elem_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_elem_entry.grid(row=2, column=1, padx=10, pady=7)

yr_label = CTkLabel(row_column_parents_details_frame, text="Year Completed:", font=("Arial", 14), bg_color="transparent")
yr_label.grid(row=3, column=0, padx=10, pady=7, sticky="w")
yr_elem_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Year Completed", height= 35, fg_color= "transparent", bg_color= "transparent")
yr_elem_entry.grid(row=3, column=1, padx=10, pady=7)

empty_label = CTkLabel(row_column_parents_details_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=0, column=2)

js_label = CTkLabel(row_column_parents_details_frame, text="JUNIOR HIGH SCHOOL", font=("Arial", 14, "bold"), bg_color="transparent")
js_label.grid(row=0, column=3, padx=10, pady=7)

schl_label = CTkLabel(row_column_parents_details_frame, text="School Name:", font=("Arial", 14), bg_color="transparent")
schl_label.grid(row=1, column=2, padx=10, pady=7, sticky="w")
schl_js_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter School", height= 35, fg_color= "transparent", bg_color= "transparent")
schl_js_entry.grid(row=1, column=3, padx=10, pady=7)

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=2, column=2, padx=10, pady=7, sticky="w")
address_js_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_js_entry.grid(row=2, column=3, padx=10, pady=7)

yr_label = CTkLabel(row_column_parents_details_frame, text="Year Completed:", font=("Arial", 14), bg_color="transparent")
yr_label.grid(row=3, column=2, padx=10, pady=7, sticky="w")
yr_js_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Year Completed", height= 35, fg_color= "transparent", bg_color= "transparent")
yr_js_entry.grid(row=3, column=3, padx=10, pady=7)

empty_label = CTkLabel(row_column_parents_details_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=4, column=0)

shs_label = CTkLabel(row_column_parents_details_frame, text="SENIOR HIGH SCHOOL", font=("Arial", 14, "bold"), bg_color="transparent")
shs_label.grid(row=4, column=1, padx=10, pady=7)

schl_label = CTkLabel(row_column_parents_details_frame, text="School Name:", font=("Arial", 14), bg_color="transparent")
schl_label.grid(row=5, column=0, padx=10, pady=7, sticky="w")
schl_shs_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter School", height= 35, fg_color= "transparent", bg_color= "transparent")
schl_shs_entry.grid(row=5, column=1, padx=10, pady=7)

strand_label = CTkLabel(row_column_parents_details_frame, text="Strand:", font=("Arial", 14), bg_color="transparent")
strand_label.grid(row=6, column=0, padx=10, pady=7, sticky="w")
strand_shs_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Strand", height= 35, fg_color= "transparent", bg_color= "transparent")
strand_shs_entry.grid(row=6, column=1, padx=10, pady=7)

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=7, column=0, padx=10, pady=7, sticky="w")
address_shs_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_shs_entry.grid(row=7, column=1, padx=10, pady=7)

yr_label = CTkLabel(row_column_parents_details_frame, text="Year Completed:", font=("Arial", 14), bg_color="transparent")
yr_label.grid(row=8, column=0, padx=10, pady=7, sticky="wn")
yr_shs_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Year Completed", height= 35, fg_color= "transparent", bg_color= "transparent")
yr_shs_entry.grid(row=8, column=1, padx=10, pady=7, sticky="n")

empty_label = CTkLabel(row_column_parents_details_frame, text="", font=("Arial", 14), bg_color="transparent")
empty_label.grid(row=4, column=2)

cg_label = CTkLabel(row_column_parents_details_frame, text="COLLEGE", font=("Arial", 14, "bold"), bg_color="transparent")
cg_label.grid(row=4, column=3, padx=10, pady=7, sticky="w")

if_transferee_var = IntVar()
if_transferee_chk_box = CTkCheckBox(educ_details, text="Check if you are not a transferee", variable=if_transferee_var)
if_transferee_chk_box.place(x=834, y=230)
if_transferee_chk_box.configure(command=toggle_transferee_fields)

schl_label = CTkLabel(row_column_parents_details_frame, text="School Name:", font=("Arial", 14), bg_color="transparent")
schl_label.grid(row=5, column=2, padx=10, pady=7, sticky="w")
schl_cg_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter School", height= 35, fg_color= "transparent", bg_color= "transparent")
schl_cg_entry.grid(row=5, column=3, padx=10, pady=7)

address_label = CTkLabel(row_column_parents_details_frame, text="Address:", font=("Arial", 14), bg_color="transparent")
address_label.grid(row=6, column=2, padx=10, pady=7, sticky="w")
address_cg_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Address", height= 35, fg_color= "transparent", bg_color= "transparent")
address_cg_entry.grid(row=6, column=3, padx=10, pady=7)

yr_label = CTkLabel(row_column_parents_details_frame, text="Year Completed:", font=("Arial", 14), bg_color="transparent")
yr_label.grid(row=7, column=2, padx=10, pady=7, sticky="w")
yr_cg_entry = CTkEntry(row_column_parents_details_frame, width=250, font=("Arial", 14), placeholder_text="Enter Year Completed", height= 35, fg_color= "transparent", bg_color= "transparent")
yr_cg_entry.grid(row=7, column=3, padx=10, pady=7)

# ==================== Window Starter ====================
window.mainloop()