from customtkinter import *

app = CTk()
app.geometry("400x300")
set_appearance_mode("dark")

def slider_event(value):
    print(value)

slider = CTkSlider(app, from_=0, to=100, command=slider_event)
slider.pack(padx=20, pady=20)

app.mainloop()
