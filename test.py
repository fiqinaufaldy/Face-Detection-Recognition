from tkinter import *

root = Tk()
root.geometry("400x400")

tinggi = IntVar()
panjang = IntVar()

mylabel = Label (root,text="Masukkan nilai Tinggi")
mylabel.pack(pady=10)
textbox1 = Entry(root,textvariable=tinggi)
textbox1.pack(pady = 10)

def ambil():
 area = tinggi.get()
 emptylabel.config (text = "the area is "+str(area))
 return area

button = Button(root,text = "Input Nilai",command=ambil)
button.pack(pady= 5)
emptylabel = Label(root)
emptylabel.pack(pady=50)
answer = Label(root,text=" ")
answer.pack(pady=20)
root.mainloop()