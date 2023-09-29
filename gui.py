
from tkinter import *
from PIL import Image,ImageTk
from tkinter import  filedialog
import os
import shutil
window= Tk()
window.geometry("500x500")
color = (0,0,255)
window.configure(background = '#fcecdd')
def openrec():
   os.system('python faces.py')
def opentrain():
   os.system('python faces-train.py')
def openfile():
    src = filedialog.askdirectory(initialdir = "C:\\Users\\DELL\\PycharmProjects\\pengolahansinyal2")
    dst = r"C:\\Users\\DELL\\PycharmProjects\\pengolahansinyal2\\images"

    shutil.move(src=src, dst=dst)

def opendec():
       os.system('python cobalagi.py')


mytext = Label(window,text = 'Face Detection and Recognition',font=("helectiva",20),fg='#ff6701',bg='#fcecdd')
mytext.place(x=50,y=40)
mytext2 = Label(window,text = 'Face Detection',font=("helectiva",20),fg='#fcecdd',bg='#fea82f')
mytext2.place(x=150,y=120)
mytext3 = Label(window,text = 'Face Recognition',font=("helectiva",20),fg='#fcecdd',bg='#fea82f')
mytext3.place(x=135,y=230)

button4 = Button (window,text="Face Detection",font=("helectiva",10),command = opendec,padx=50,pady=10,fg='#fcecdd',bg='#ff6701')
button4.place(x=146,y=165)
button3 = Button (window,text="Input Data",font=("helectiva",10),command = openfile,padx=50,pady=10,fg='#fcecdd',bg='#ff6701')
button3.place(x=155,y=275)
button2 = Button (window,text="Train Data",font=("helectiva",10),command = opentrain,padx=50,pady=10,fg='#fcecdd',bg='#ff6701')
button2.place(x=155,y=325)
button = Button(window,text="Face Recognition",font=("helectiva",10),command=openrec,padx=50,pady=10,fg='#fcecdd',bg='#ff6701')
button.place(x=140,y=375)



window.mainloop()

