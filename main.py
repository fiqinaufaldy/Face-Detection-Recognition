//code untuk interface 

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

window = Tk()
window.geometry("660x500")
color = (0, 0, 255)
window.configure(background='#000000')


def openrec():
    os.system('python gui.py')


image1 = (Image.open("orbit logo.png"))
resized = image1.resize((254, 75), Image.ANTIALIAS)
image = ImageTk.PhotoImage(resized)
label = Label(image=image)
label.place(x=210, y=140)


mytext = Label(window, text='Face Detection and Recognition',
               font=("helectiva bold", 30), fg='#ff6701', bg='#000000')
mytext.place(x=50, y=20)
mytext = Label(window, text='TUGAS AKHIR KELOMPOK 10',
               font=("Monaco", 20), fg='#ff6701', bg='#000000')
mytext.place(x=160, y=70)
mytext = Label(window, text='Sistem Pengenalan Wajah Karyawan Kantor', font=(
    "helectiva bold", 14), fg='#ff6701', bg='#000000')
mytext.place(x=150, y=250)

button = Button(window, text="Start", font=("helectiva", 10),
                command=openrec, padx=50, pady=10, fg='#fcecdd', bg='#ff6701')
button.place(x=270, y=380)


mytext = Label(window, text='credit', font=(
    "helectiva bold", 8), fg='#ff6701', bg='#000000')
button = Button(window, command=openrec, padx=100,
                pady=2, fg='#fcecdd', bg='#ff6701')
button.place(x=0, y=480)
button = Button(window, command=openrec, padx=120,
                pady=2, fg='#fcecdd', bg='#ff6701')
button.place(x=450, y=480)
window.mainloop()
