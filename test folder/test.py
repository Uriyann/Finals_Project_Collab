from PIL import Image
from customtkinter import *

window = CTk()
window.title("Login Portal")
window.geometry('1300x825')
window.configure()


# Frame
frame = CTkFrame(master=window)
frame.grid(row=0, column=1, padx=45)

# Project Name
project_label = CTkLabel(master=frame, text= "PROJECT", font= ("Times New Roman bold", 30))
project_label.grid(row=0, column=0, sticky="n", pady= 10)

# Short Description
short_desc_label =  CTkLabel(master=frame, text= "/Short Description/", font= ("Helvetica bold", 15))
short_desc_label.grid(row=1, column=0, sticky="n")

# Login
login_label = CTkLabel(master=frame, text= "Log In to Project", font= ("Arial bold", 16))
login_label.grid(row=2, column=0, sticky="w", pady=30, padx= 15)

def on_click(event):
    if user_entry.get() == "Username":
        user_entry.delete(0, 'end')

def on_leave(event):
    name = user_entry.get()
    if name == "":
        user_entry.insert(0, "Username")

# User Entry
user_entry = CTkEntry(master=frame, font= ("Arial", 15))
user_entry.grid(row=3, column=0, sticky= "new", padx= 15, columnspan=1)
user_entry.insert(0, "Username")
user_entry.bind("<FocusIn>", on_click)
user_entry.bind("<FocusOut>", on_leave)

# Underline using Frame
underline = CTkFrame(master=frame, height=2, border_color="white")
underline.grid(row=4, column=0, sticky= "new", pady=15, padx= 15, columnspan=1)

#-----------------------------------------------------------
def on_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, 'end')

def on_leave(event):
    password = password_entry.get()
    if password == "":
        password_entry.insert(0, "Password")

# Password Entry
password_entry = CTkEntry(master=frame, font= ("Arial", 15))
password_entry.grid(row=5, column=0, sticky= "new", padx= 15, columnspan=1)
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", on_click)
password_entry.bind("<FocusOut>", on_leave)

# Underline using Frame
underline = CTkFrame(master=frame, height=2, border_color="white")
underline.grid(row=6, column=0, sticky= "new", pady=15, padx= 15, columnspan=1)

#-------------------------------------------------------------

# Button Sign in
login_button = CTkButton(master=frame, text= "Log In", width=38, font= ("Arial bold", 15))
login_button.grid(row=7, column=0, pady=15, padx= 15)

# Remember Me Checkbutton
var1 = IntVar()
rem_cb = CTkCheckBox(master=frame, text="Remember Me", variable=var1, font=("Arial", 12))
rem_cb.grid(row=8, column=0, sticky="w", pady=10, padx= 15)

# Forget Password Label
forgpass_label = CTkButton(master=frame, text="Forgot Password?", fg_color= "dodgerblue2", font=("Arial", 12))
forgpass_label.grid(row=8, column=0, sticky="e", padx= 15)

# Underline using Frame
underline = CTkFrame(master=frame, height=2, border_color="white")
underline.grid(row=9, column=0, sticky= "new", pady=15, padx= 15, columnspan=1)

create_label = CTkButton(master=frame, text="Need an Account? SIGN UP", font=("Arial", 12), border_width= 0)
create_label.grid(row=10, column=0, sticky="n", pady=15)


window.mainloop()