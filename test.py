import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class StudentManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Fake data
        self.student_data = [
            {"roll": "23", "name": "Shashank", "email": "shashank@gmail.com", "gender": "Male", "contact": "4154615468", "dob": "27/10/2004", "address": "ABCD"},
            {"roll": "24", "name": "Joshua", "email": "joshua@gmail.com", "gender": "Male", "contact": "1234567890", "dob": "01/01/2005", "address": "XYZ Street"},
            {"roll": "25", "name": "Anna", "email": "anna@gmail.com", "gender": "Female", "contact": "9876543210", "dob": "15/03/2004", "address": "LMN Road"},
        ]

        self.create_widgets()
        self.populate_table(self.student_data)

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Student Management System", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # === Left Form (not the focus here) ===
        self.left_frame = ctk.CTkFrame(self.content_frame, width=300, corner_radius=10)
        self.left_frame.pack(side="left", fill="y", padx=(0, 10))

        ctk.CTkLabel(self.left_frame, text="Manage Students", font=("Arial", 18, "bold")).pack(pady=10)

        self.entries = {}
        fields = ["Roll No.", "Name", "Email", "Contact", "D.O.B"]
        for field in fields:
            ctk.CTkLabel(self.left_frame, text=field).pack(anchor="w", padx=20)
            entry = ctk.CTkEntry(self.left_frame, width=250)
            entry.pack(padx=20, pady=5)
            self.entries[field] = entry

        ctk.CTkLabel(self.left_frame, text="Gender").pack(anchor="w", padx=20)
        self.gender_menu = ctk.CTkOptionMenu(self.left_frame, values=["Male", "Female", "Other"])
        self.gender_menu.pack(padx=20, pady=5)

        ctk.CTkLabel(self.left_frame, text="Address").pack(anchor="w", padx=20)
        self.address_textbox = ctk.CTkTextbox(self.left_frame, height=60, width=250)
        self.address_textbox.pack(padx=20, pady=5)

        btn_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        for btn in ["Add", "Update", "Delete", "Clear"]:
            ctk.CTkButton(btn_frame, text=btn, width=60).pack(side="left", padx=5)

        # === Right Side ===
        self.right_frame = ctk.CTkFrame(self.content_frame, corner_radius=10)
        self.right_frame.pack(side="right", fill="both", expand=True)

        search_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=10, pady=10)

        self.search_by_menu = ctk.CTkOptionMenu(search_frame, values=["Roll No.", "Name", "Email"])
        self.search_by_menu.pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search by")
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)

        ctk.CTkButton(search_frame, text="Search", command=self.search_student).pack(side="left", padx=5)
        ctk.CTkButton(search_frame, text="Show All", command=self.show_all_students).pack(side="left", padx=5)

        table_frame = ctk.CTkFrame(self.right_frame)
        table_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        columns = ("roll", "name", "email", "gender", "contact", "dob", "address")
        self.student_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)
        self.student_table.pack(fill="both", expand=True)

    def populate_table(self, data):
        self.student_table.delete(*self.student_table.get_children())
        for student in data:
            self.student_table.insert("", "end", values=(
                student["roll"], student["name"], student["email"], student["gender"],
                student["contact"], student["dob"], student["address"]
            ))

    def search_student(self):
        keyword = self.search_entry.get().strip().lower()
        search_by = self.search_by_menu.get().lower()

        if not keyword:
            return

        key_map = {
            "roll no.": "roll",
            "name": "name",
            "email": "email"
        }
        key = key_map.get(search_by)

        results = [s for s in self.student_data if keyword in s[key].lower()]
        self.populate_table(results)

    def show_all_students(self):
        self.populate_table(self.student_data)

if __name__ == "__main__":
    app = StudentManagementApp()
    app.mainloop()
