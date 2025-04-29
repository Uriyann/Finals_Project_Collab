import customtkinter as ctk
import tkinter.ttk as ttk

app = ctk.CTk()
app.geometry("500x400")

frame = ctk.CTkFrame(app)
frame.pack(pady=20)

# CTk Label
ctk.CTkLabel(frame, text="CTk + ttk Example", font=("Arial", 18)).pack(pady=10)

# ttk Treeview
tree = ttk.Treeview(frame._get_tk(), columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.insert("", "end", values=("Joshua", "21"))
tree.pack()

app.mainloop()
