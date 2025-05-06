import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")  # can be changed

class StudentManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("1000x600")
        

        # ==== Title ====
        self.title_label = ctk.CTkLabel(self, text="Student Management System", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        # ==== Main Content Frame ====
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # ==== Left Frame: Manage Students ====
        self.left_frame = ctk.CTkFrame(self.content_frame, width=300, corner_radius=10)
        self.left_frame.pack(side="left", fill="y", padx=(0, 10))

        ctk.CTkLabel(self.left_frame, text="Manage Students", font=("Arial", 18, "bold")).pack(pady=10)

        # Entry Fields
        self.entries = {}
        fields = ["Roll No.", "Name", "Email", "Contact", "D.O.B"]
        for field in fields:
            ctk.CTkLabel(self.left_frame, text=field).pack(anchor="w", padx=20)
            entry = ctk.CTkEntry(self.left_frame, width=250)
            entry.pack(padx=20, pady=5)
            self.entries[field] = entry

        # Gender OptionMenu
        ctk.CTkLabel(self.left_frame, text="Gender").pack(anchor="w", padx=20)
        self.gender_menu = ctk.CTkOptionMenu(self.left_frame, values=["Male", "Female", "Other"])
        self.gender_menu.pack(padx=20, pady=5)

        # Address Textbox
        ctk.CTkLabel(self.left_frame, text="Address").pack(anchor="w", padx=20)
        self.address_textbox = ctk.CTkTextbox(self.left_frame, height=60, width=250)
        self.address_textbox.pack(padx=20, pady=5)

        # Action Buttons
        btn_frame = ctk.CTkFrame(self.left_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        for btn in ["Add", "Update", "Delete", "Clear"]:
            ctk.CTkButton(btn_frame, text=btn, width=60).pack(side="left", padx=5)

        # ==== Right Frame: Search + Table ====
        self.right_frame = ctk.CTkFrame(self.content_frame, corner_radius=10)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Search Controls
        search_frame = ctk.CTkFrame(self.right_frame, fg_color="transparent")
        search_frame.pack(fill="x", padx=10, pady=10)

        self.search_option = ctk.CTkOptionMenu(search_frame, values=["Roll No.", "Name", "Email"])
        self.search_option.pack(side="left", padx=5)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search by")
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)

        ctk.CTkButton(search_frame, text="Search").pack(side="left", padx=5)
        ctk.CTkButton(search_frame, text="Show All").pack(side="left", padx=5)

        # Treeview for Table
        table_frame = ctk.CTkFrame(self.right_frame)
        table_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        columns = ("roll", "name", "email", "gender", "contact", "dob", "address")
        self.student_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)
        self.student_table.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = StudentManagementApp()
    app.mainloop()
