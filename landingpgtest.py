from tkinter import *
from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import customtkinter as ctk
import pywinstyles as pyw
import pygame
import os 
c=0
def addnum():
    global c
    c+=1
    print(c)

def showb(self):
    addnum()
    
    if c==1:
        pyw.set_opacity(b, 0.1, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==2:
        pyw.set_opacity(b, 0.2, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==3:
        pyw.set_opacity(b, 0.3, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==4:
        pyw.set_opacity(b, 0.4, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==5:
        pyw.set_opacity(b, 0.7, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==6:
        pyw.set_opacity(b, 0.9, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==7:
        pyw.set_opacity(b, 1, color="#000001")
        self.after(60, addnum)
    

def hideb(self):
    addnum()
    
    if c==1:
        pyw.set_opacity(b, 0.9, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==2:
        pyw.set_opacity(b, 0.7, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==3:
        pyw.set_opacity(b, 0.5, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==4:
        pyw.set_opacity(b, 0.3, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==5:
        pyw.set_opacity(b, 0.2, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==6:
        pyw.set_opacity(b, 0.1, color="#000001")
        self.after(60, lambda: [showb(self), addnum()])
    elif c==7:
        pyw.set_opacity(b, 0, color="#000001")
        self.after(60, addnum)
    

class slidepanel(ctk.CTkFrame):
    
    def __init__(self, parent, startpos, endpos):
        super().__init__(master=parent, fg_color='lightgray')
        
        #gen att
        self.startpos = startpos
        self.endpos = endpos
        self.width=abs(startpos-endpos)

        #animlogic
        self.pos= self.startpos
        self.instartpos=True
        
        #layout
        self.place(relx=self.startpos,rely=0,relwidth=self.width, relheight=1)
        self.tkraise()
    def animate(self):
        if self.instartpos:
            self.animateforward()
        else:
            self.animatebackwards()
    
    def animateforward(self):
        if self.pos>self.endpos:
            self.pos -= 0.008
            self.place(relx=self.pos,rely=0,relwidth=self.width, relheight=1)
            
            if self.pos>(self.endpos-(self.endpos*0.98)):
                self.after(30, self.animateforward)
                
            elif self.pos>(self.endpos-(self.endpos*0.8)):
                self.after(2, self.animateforward) 
            else:
                self.after(1, self.animateforward)
        else:
            self.instartpos=False
            

    def animatebackwards(self):
        if self.pos<self.startpos:
            self.pos += 0.008
            self.place(relx=self.pos,rely=0,relwidth=self.width, relheight=1)
            if self.pos>(self.endpos-(self.startpos*0.7)):
                self.after(2, self.animatebackwards)
            elif self.pos>(self.endpos-(self.startpos*0.9)):
                self.after(5, self.animatebackwards) 
            else:
                self.after(30, self.animatebackwards)
        else:
            self.instartpos=True
            
    
        

class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        
        try:
            #counts..
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
                print(i," frame/s loaded")

        except EOFError:
            pass

        os.system('cls')
        self.frames = cycle(frames)
        self.totalframes = i

        try:
            print("used gif speed")
            self.delay = im.info['duration']
            
        except:
            print("used default speed")
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
            
    isempty='no'

    def unload(self):
        if self.isempty=='no':
            self.config(image=None)
            self.frames = None
            print("cleared image")
            self.isempty='yup'
        elif self.isempty=='yup':
            print("shut up dude i already cleared it")
        
        
    counter=0
    def next_frame(self):
   
        if self.frames:

            self.counter+=1
            print(f"running frame {self.counter}")
            
            self.config(image=next(self.frames))
            
            if self.counter==self.totalframes:
                os.system('cls')
                print("RESULTS:")
                print(self.totalframes," total frame/s succesfully loaded")
                print(f"used delay: {self.delay} frames per second")
                print("gif stopped.")
                showb(b)
            elif self.counter<=self.totalframes:
                self.after(self.delay, self.next_frame)




window = tk.Tk()
window.geometry("640x480")
window.title("Unipass")
window.resizable(width=False, height=False)

#stuff
note=Label(window, text="about us section here", font="bahnschrift, 10")
note.place(relx=0.45,rely=0.45)

navpanel=slidepanel(window, 0, -1)

animpanel=slidepanel(window, 0, -1)
b1=CTkButton(navpanel, width=10, height=10, corner_radius=999, text='about us',hover_color="lightgray", text_color="black",font=("Bahnschrift", 24), bg_color="#000001", fg_color="lightgray", command=navpanel.animate)
lbl = ImageLabel(animpanel, width=900, height=600)
# button widget
b=CTkButton(master=animpanel, width=10, height=10, corner_radius=999, text='Next -->', bg_color="#000001", fg_color="gray18", command=lambda: [animpanel.animate(), hideb(b)]) 
lbl.pack()
lbl.load(r'python\Finals_Project_Collab-main\landpg.gif')
by=0.5

##hey man, here's the buttons for login in and sign up. if i have time ill clean my code
loginb=CTkButton(master=navpanel, width=10, height=10, corner_radius=999, text='login', bg_color="#000001", fg_color="gray18", command=print("login")) 
signupb=CTkButton(master=navpanel, width=10, height=10, corner_radius=999, text='signup', bg_color="#000001", fg_color="gray18", command=print("signup")) 
find me here


pyw.set_opacity(b, 0, color="#000001")
pyw.set_opacity(b1, 1, color="#000001")

#placement
#welcome.place(relx = 1, x =-1, y = 1, anchor = NE)
#desc.place(relx = 1, x =-150, y = 150, anchor = NE)
b.place(relx=1,rely=by, x =-157, y = 100, anchor = NE)
b1.place(relx=1,rely=by, x =-150, y = 100, anchor = NE)
loginb.place(relx=1,rely=by, x =-0, y = 0, anchor = NE)
signupb.place(relx=1,rely=by, x =0, y = 100, anchor = NE)


window.mainloop()