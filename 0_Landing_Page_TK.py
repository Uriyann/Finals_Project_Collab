from tkinter import *
from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import customtkinter as ctk
import pywinstyles as pyw
import pygame
import os 
import subprocess

window = tk.Tk()
height = 480
width = 640
x = (window.winfo_screenwidth()//2)-(width//2) 
y = (window.winfo_screenheight()//2)-(height//2) 
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.title("Unipass")
window.resizable(width=False, height=False)
c=0
def addnum():
    global c
    if c==7:
        c=0
    else:
        c+=1
        
def showb(self):
    
    if c==0:
        addnum()
    if c==1:
        pyw.set_opacity(self, 0, color="#000001")
        self.after(200, lambda: [showb(self), addnum()])
    elif c==2:
        pyw.set_opacity(self, 0.2, color="#000001")
        self.after(30, lambda: [showb(self), addnum()])
    elif c==3:
        pyw.set_opacity(self, 0.3, color="#000001")
        self.after(30, lambda: [showb(self), addnum()])
    elif c==4:
        pyw.set_opacity(self, 0.4, color="#000001")
        self.after(30, lambda: [showb(self), addnum()])
    elif c==5:
        pyw.set_opacity(self, 0.7, color="#000001")
        self.after(30, lambda: [showb(self), addnum()])
    elif c==6:
        pyw.set_opacity(self, 0.9, color="#000001")
        self.after(30, lambda: [showb(self), addnum()])
    elif c==7:
        pyw.set_opacity(self, 1, color="#000001")

        
    

def hideb(self):
    if c==0:
        addnum()

    if c==1:
        pyw.set_opacity(self, 1, color="#000001")
        self.after(1, lambda: [hideb(self), addnum()])
    elif c==2:
        pyw.set_opacity(self, 0.7, color="#000001")
        self.after(30, lambda: [hideb(self), addnum()])
    elif c==3:
        pyw.set_opacity(self, 0.5, color="#000001")
        self.after(30, lambda: [hideb(self), addnum()])
    elif c==4:
        pyw.set_opacity(self, 0.3, color="#000001")
        self.after(30, lambda: [hideb(self), addnum()])
    elif c==5:
        pyw.set_opacity(self, 0.2, color="#000001")
        self.after(30, lambda: [hideb(self), addnum()])
    elif c==6:
        pyw.set_opacity(self, 0.1, color="#000001")
        self.after(30, lambda: [hideb(self), addnum()])
    elif c==7:
        pyw.set_opacity(self, 0, color="#000001")
        
        
        

class slidepanel(ctk.CTkFrame):
    def __init__(self, parent, startpos, endpos):
        super().__init__(master=parent,  fg_color='#d9d9d9')
        
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
        if self.startpos==0 and self.endpos==-1:
            if self.pos>self.endpos:
                self.pos -= 0.008
                self.place(relx=self.pos,rely=0,relwidth=self.width, relheight=1)
                
                if self.pos>(self.endpos-(self.endpos*0.98)):
                    self.after(20, self.animateforward)
                    
                elif self.pos>(self.endpos-(self.endpos*0.8)):
                    self.after(3, self.animateforward) 
                else:
                    self.after(1, self.animateforward)
            else:
                self.instartpos=False
                
        elif self.startpos==1 and self.endpos==0.6:
            if self.pos>self.endpos:
                self.pos -= 0.008
                self.place(relx=self.pos,rely=0,relwidth=self.width, relheight=1)
                self.after(7, self.animateforward)

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
            bgroup.enb()
           
            
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            sizechange=(1200, 1200)
            im = Image.open(im)
            
        frames = []
        
        try:
            #counts..
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)

        except EOFError:
            pass

        os.system('cls')
        self.frames = cycle(frames)
        self.totalframes = i

        try:
            self.delay = im.info['duration']
            
        except:
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
            self.isempty='yup'
        elif self.isempty=='yup':
            pass
        
    counter=0

    def next_frame(self):
   
        if self.frames:

            self.counter+=1
            
            self.config(image=next(self.frames))
            
            if self.counter==self.totalframes:
                os.system('cls')
                showb(bgroup.b)
            elif self.counter<=self.totalframes:
                self.after(self.delay, self.next_frame)

def GO_TO_LOGIN():
    window.destroy()
    subprocess.call(["python", "1_Portal_CTK.py"])

#stuff
note=Label(window, text="about us section here", font="Inter, 10")
note.place(relx=0.45,rely=0.45)
#panels
aboutpanel=slidepanel(window, 0,-1)
navpanel=slidepanel(window, 0, -1)
navimg = ImageLabel(navpanel, width=900, height=600)
animpanel=slidepanel(window, 0, -1)
navpanel1=slidepanel(navpanel, 1.0, 0.6)

#gif
lbl = ImageLabel(animpanel, width=900, height=600)
lbl.pack()
lbl.load(r"C:\Users\M S I\Desktop\BSIT_Finals_Project_Collab\assets\landpg.gif")
navimg.pack()
#img
background_image = Image.open(r"C:\Users\M S I\Desktop\BSIT_Finals_Project_Collab\assets\cuh.png")
bg_img = CTkImage(light_image=background_image, dark_image=background_image, size=(80, 80))
navicon=CTkLabel(master=navpanel1, image = bg_img, text="")
#labels
navheader=CTkLabel(master=navpanel1, font=("Inter", 30, "bold"), fg_color="gray18", text="Dive into", text_color="lightyellow")
navsubheader=CTkLabel(master=navpanel1, font=("Inter", 17), fg_color="gray18", text="Unipass!")
navdesc=CTkLabel(master=navpanel1, font=("Inter", 11), fg_color="gray18", text="Join our community \nof roughly 1 member! (my dog included).\nmanage your school attendance like \nnever before.")
#buttons
class buttongroup:
    def __init__(self):
            
        self.b=CTkButton(master=animpanel, width=25, height=15, corner_radius=999, text='Next -->', bg_color="#000001", fg_color="black", 
                    command=lambda: [animpanel.animate(), navimg.load(r'C:\Users\M S I\Desktop\BSIT_Finals_Project_Collab\assets\log.gif'), navpanel1.animate(), showb(bgroup.loginb),showb(bgroup.b1)])

        self.b1=CTkButton(master=navpanel1, width=10, height=10, corner_radius=999, text='learn more about us!',hover_color="gray18", text_color="white",font=("Inter", 14), bg_color="#000001", fg_color="gray18", 
                    command=lambda: [bgroup.disb(),hideb(bgroup.b1),navpanel.animate(), navpanel1.animate(), hideb(bgroup.loginb)])

        self.aboutext=CTkButton(master=aboutpanel, width=10, height=10, corner_radius=999, text='return',hover_color="gray18", text_color="white",font=("Inter", 20, "bold"), bg_color="#000001", fg_color="gray18", 
                        command=lambda: [bgroup.disb(),showb(bgroup.loginb),showb(bgroup.b1),navpanel.animate(), navpanel1.animate()])

        self.loginb=CTkButton(master=navpanel1,height=35, width=10, corner_radius=5, text='Continue', bg_color="#000001", fg_color="#1C66CE",font=("Inter", 15), command=GO_TO_LOGIN) 

    def disb(self):
        self.b.configure(state=tk.DISABLED)
        self.b1.configure(state=tk.DISABLED)
        self.aboutext.configure(state=tk.DISABLED)
        self.loginb.configure(state=tk.DISABLED)
    def enb(self):
        self.b.configure(state=tk.NORMAL)
        self.b1.configure(state=tk.NORMAL)
        self.aboutext.configure(state=tk.NORMAL)
        self.loginb.configure(state=tk.NORMAL)

bgroup=buttongroup()

#config
navpanel1.configure( fg_color='gray18')
aboutpanel.configure( fg_color='gray18', border_width=25, border_color="lightgray")
#opac
pyw.set_opacity(bgroup.b, 0, color="#000001")
pyw.set_opacity(bgroup.b1, 0, color="#000001")
pyw.set_opacity(bgroup.loginb, 0, color="#000001")
#placement
bgroup.b.place(relx=1,rely=0.5, x =-160, y = 100, anchor = NE)
bgroup.b1.place(rely=0.9,relx=0.5, anchor = CENTER)
bgroup.aboutext.place(rely=0.15,relx=0.1, anchor = CENTER)
bgroup.loginb.place(rely=0.80,relx=0.5, anchor = CENTER)
navheader.place(rely=0.30,relx=0.5, anchor = CENTER)
navsubheader.place(rely=0.36,relx=0.5, anchor = CENTER)
navdesc.place(rely=0.47,relx=0.5, anchor = CENTER)
navicon.place(rely=0.15,relx=0.5, anchor = CENTER)

window.mainloop()