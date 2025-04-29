import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class LeftTabView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Left TabView")
        self.geometry("600x400")

        # Main layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Tab buttons (simulate tabs)
        self.tab_frame = ctk.CTkFrame(self)
        self.tab_frame.grid(row=0, column=0, sticky="ns")
        
        self.button1 = ctk.CTkButton(self.tab_frame, text="Tab 1", command=self.show_tab1)
        self.button1.pack(padx=10, pady=10)

        self.button2 = ctk.CTkButton(self.tab_frame, text="Tab 2", command=self.show_tab2)
        self.button2.pack(padx=10, pady=10)

        # Content area
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        self.tab1_content = ctk.CTkLabel(self.content_frame, text="Content of Tab 1")
        self.tab2_content = ctk.CTkLabel(self.content_frame, text="Content of Tab 2")

        self.show_tab1()  # Default tab

    def show_tab1(self):
        self.clear_content()
        self.tab1_content.pack(padx=20, pady=20)

    def show_tab2(self):
        self.clear_content()
        self.tab2_content.pack(padx=20, pady=20)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.pack_forget()

app = LeftTabView()
app.mainloop()
