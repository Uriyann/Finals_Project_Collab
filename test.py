from customtkinter import *
from PIL import Image

window = CTk()
window.title("Login Portal")
window.geometry('1300x825')
window.configure()

# First Name Delete & Restore Function
def sign_up_on_first_name_click(event):
    if sign_up_first_name_entry.get() == "First name":
        sign_up_first_name_entry.delete(0, END)
def sign_up_on_first_name_leave(event):
    name = sign_up_first_name_entry.get()
    if name == "":
        sign_up_first_name_entry.insert(0, "First name")

# Last Name Delete & Restore Function
def sign_up_on_last_name_click(event):
    if sign_up_last_name_entry.get() == "Last name":
        sign_up_last_name_entry.delete(0, END)
def sign_up_on_last_name_leave(event):
    password = sign_up_last_name_entry.get()
    if password == "":
        sign_up_last_name_entry.insert(0, "Last name")

# Email Delete & Restore Function
def sign_up_on_email_click(event):
    if sign_up_email_entry.get() == "Email":
        sign_up_email_entry.delete(0, END)
def sign_up_on_email_leave(event):
    name = sign_up_email_entry.get()
    if name == "":
        sign_up_email_entry.insert(0, "Email")

# Username Delete & Restore Function
def sign_up_on_username_click(event):
    if sign_up_username_entry.get() == "Username":
        sign_up_username_entry.delete(0, END)
def sign_up_on_username_leave(event):
    password = sign_up_username_entry.get()
    if password == "":
        sign_up_username_entry.insert(0, "Username")

# Password Delete & Restore Function
def sign_up_on_password_click(event):
    if sign_up_password_entry.get() == "Password":
        sign_up_password_entry.delete(0, END)
def sign_up_on_password_leave(event):
    name = sign_up_password_entry.get()
    if name == "":
        sign_up_password_entry.insert(0, "Password")

# Confirm Password Delete & Restore Function
def sign_up_on_confirm_password_click(event):
    if sign_up_confirm_password_entry.get() == "Confirm Password":
        sign_up_confirm_password_entry.delete(0, END)
def sign_up_on_confirm_password_leave(event):
    password = sign_up_confirm_password_entry.get()
    if password == "":
        sign_up_confirm_password_entry.insert(0, "Confirm Password")

# Log In Enter Event
def sign_up_handle_enter(event):
    sign_up_button.invoke()


# //////////////////////////////////////////////////////////

# ==================== UI ====================
# Background & Banner Img
background_image = Image.open(".\wallhaven-85gxp2.png")
bg_img = CTkImage(light_image=background_image, dark_image=background_image, size=(1300, 825))
bg_label = CTkLabel(window, image=bg_img, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# //////////////////////////////////////////////////////////

# ==================== Frames ====================
sign_up_frame = CTkFrame(window, border_width= 3, corner_radius= 15)
sign_up_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
# //////////////////////////////////////////////////////////

# ==================== Labels & Inputs ====================

# Project Name
sign_up_project_label = CTkLabel(sign_up_frame, text= "PROJECT UniPass", font= ("Times New Roman bold", 40))
sign_up_project_label.grid(row=0, column=0, sticky="n", pady= 10, padx= 15)

# Short Description
short_desc_label =  CTkLabel(sign_up_frame, text= "/Short Description/", font= ("Helvetica bold", 18))
short_desc_label.grid(row=1, column=0, sticky="n")

# Login
sign_up_label = CTkLabel(sign_up_frame, text= "Sign Up to Project", font= ("Helvetica bold", 17))
sign_up_label.grid(row=2, column=0, sticky="w", pady=15, padx= 15)

# Firstname Entry
sign_up_first_name_entry = CTkEntry(master=sign_up_frame, font= ("Arial", 16), border_width=0, width=195, placeholder_text="First name", height= 55)
sign_up_first_name_entry.grid(row=3, column=0, sticky= "nw", pady=6, padx= 15)
sign_up_first_name_entry.bind("<FocusIn>", sign_up_on_first_name_click)
sign_up_first_name_entry.bind("<FocusOut>", sign_up_on_first_name_leave)
sign_up_first_name_entry.bind('<Return>', sign_up_handle_enter)

# Lastname Entry
sign_up_last_name_entry = CTkEntry(sign_up_frame, font= ("Arial", 16), border_width=0, width=195, placeholder_text="Last name", height= 55)
sign_up_last_name_entry.grid(row=3, column=0, sticky= "ne", pady=6, padx= 15)
sign_up_last_name_entry.bind("<FocusIn>", sign_up_on_last_name_click)
sign_up_last_name_entry.bind("<FocusOut>", sign_up_on_last_name_leave)
sign_up_last_name_entry.bind('<Return>', sign_up_handle_enter)

# Email Entry
sign_up_email_entry = CTkEntry(sign_up_frame, font= ("Arial", 16), border_width=0, width=400, placeholder_text="Email", height= 55)
sign_up_email_entry.grid(row=4, column=0, sticky= "n", pady=6, padx= 15)
sign_up_email_entry.bind("<FocusIn>", sign_up_on_email_click)
sign_up_email_entry.bind("<FocusOut>", sign_up_on_email_leave)
sign_up_email_entry.bind('<Return>', sign_up_handle_enter)

# Username Entry
sign_up_username_entry = CTkEntry(sign_up_frame, font= ("Arial", 16), border_width=0, width=400, placeholder_text="Username", height= 55)
sign_up_username_entry.grid(row=5, column=0, sticky= "n", pady=6, padx= 15)
sign_up_username_entry.bind("<FocusIn>", sign_up_on_username_click)
sign_up_username_entry.bind("<FocusOut>", sign_up_on_username_leave)
sign_up_username_entry.bind('<Return>', sign_up_handle_enter)

# Password Entry
sign_up_password_entry = CTkEntry(sign_up_frame, font= ("Arial", 16), border_width=0, width=195, placeholder_text="Password", show="*", height= 55)
sign_up_password_entry.grid(row=6, column=0, sticky= "nw", pady=6, padx= 15)
sign_up_password_entry.bind("<FocusIn>", sign_up_on_password_click)
sign_up_password_entry.bind("<FocusOut>", sign_up_on_password_leave)
sign_up_password_entry.bind('<Return>', sign_up_handle_enter)

# Confirm Password Entry
sign_up_confirm_password_entry = CTkEntry(sign_up_frame, font= ("Arial", 16), border_width=0, width=195, placeholder_text="Confirm Password", show="*", height= 55)
sign_up_confirm_password_entry.grid(row=6, column=0, sticky= "ne", pady=6, padx= 15)
sign_up_confirm_password_entry.bind("<FocusIn>", sign_up_on_confirm_password_click)
sign_up_confirm_password_entry.bind("<FocusOut>", sign_up_on_confirm_password_leave)
sign_up_confirm_password_entry.bind('<Return>', sign_up_handle_enter)


# //////////////////////////////////////////////////////////

# ==================== Buttons ====================

# Button Login
sign_up_button = CTkButton(sign_up_frame, text= "Sign Up", width=325, font= ("Arial bold", 15), height= 35)
sign_up_button.grid(row=7, column=0, pady=15, padx= 15)

# Signup Text + Button
log_frame = CTkFrame(sign_up_frame)
log_frame.grid(row=8, column=0, pady=20)

need_account_label = CTkLabel(log_frame, text="Already a User?", font=("Arial", 12))
need_account_label.grid(row=0, column=0, padx=10)

login_button = CTkButton(log_frame, text="LOGIN", font=("Arial", 12), fg_color="transparent", hover_color="lightblue", text_color="dodgerblue2", width=50)
login_button.grid(row=0, column=1, padx=5)

# //////////////////////////////////////////////////////////

window.mainloop()