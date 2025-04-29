from customtkinter import *
from PIL import Image

# ========== Window Setup ==========
window = CTk()
window.title("Login Portal")
window.geometry('1300x825')
window.resizable(False, False)

# ========== Background ==========
background_image = Image.open("./wallhaven-85gxp2.png")
bg_img = CTkImage(light_image=background_image, dark_image=background_image, size=(1300, 825))
bg_label = CTkLabel(window, image=bg_img, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # <<<<< Place background first!

# ========== Main Frame ==========
main_frame = CTkFrame(window, border_width=3, corner_radius=15, fg_color="transparent")  
main_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# ========== Side Image ==========
side_image = Image.open("./wallhaven-73616y.png")
side_img = CTkImage(light_image=side_image, dark_image=side_image, size=(550, 550))
side_label = CTkLabel(main_frame, image=side_img, text="")
side_label.grid(row=0, column=0, padx=15, pady=15)

# ========== Login Frame ==========
log_in_frame = CTkFrame(main_frame, border_width=3, corner_radius=15)
log_in_frame.grid(row=0, column=1, padx=15, pady=15)

window.mainloop()
