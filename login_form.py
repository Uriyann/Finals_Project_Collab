import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("300x400")
window.title("ITCS103 TKINTER!")

frame1= tk.Frame()
frame2= tk.Frame()

frame1.pack()
frame2.pack()

label= tk.Label(frame1, text="Login Form", font=("Arial", 20, "bold"), fg="black",)
label.pack(pady=50)


entry1= tk.Entry(frame1, width=30, font=("Arial", 12))
entry2= tk.Entry(frame1, width=30, font=("Arial", 12))
entry1.insert(1, "Enter Username")
entry1.pack(pady=10)
entry2.insert(1, "Enter Password")
entry2.pack(pady=10)

button= tk.Button(frame1, text="Log in", font=("Arial", 12), width=30, bg="blue", fg="white")
button.pack(pady=20)

#label1= tk.Label(entry1, text="Username", font=("Arial", 12),width=40)
#label2= tk.Label(entry2, text="Password", font=("Arial", 12), width=40)

#label1.pack(side = LEFT)
#label2.pack(side = LEFT)

# label3= tk.Label(frame1, text="Log in", font=("Arial", 20, "bold"), fg="black",bg="blue",width=20)
# label3.pack(pady=50)

var1 = IntVar()
rem_cb = tk.Checkbutton(frame1, text="Remember Me", variable=var1, font=("Arial", 12))
rem_cb.pack(side="left")

forgot_pass= tk.Label(frame1, text="Forgot Password?", fg= "dodgerblue2", font=("Arial", 12))
forgot_pass.pack(side="right")


create_pass= tk.Label(frame2, text="Create an Account", fg= "dodgerblue2"
, font=("Arial", 12))
create_pass.pack(pady=45)


window.mainloop()
