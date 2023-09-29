import cv2
from tkinter import *

#lANGKAH FACE RECOGNITION : rekam data wajah, trainning data, recognition
cam = cv2.VideoCapture(1)
cam.set(3,680)
cam.set(4,480)
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

root = Tk()
root.geometry("400x300")
root.configure(background = '#fcecdd')
neigh = IntVar()
scale = DoubleVar()
mylabel = Label (root,text="Memasukkan Parameter",font=("helectiva",14),fg='#ff6701',bg='#fcecdd')
mylabel.pack(pady=10)
mylabel = Label (root,text="Nilai minNeighboor",font=("helectiva",10),fg='#ff6701',bg='#fcecdd')
mylabel.pack(pady=10)
textbox1 = Entry(root,textvariable=neigh)
textbox1.pack(pady = 10)
mylabel = Label (root,text="Nilai scalefactor",font=("helectiva",10),fg='#ff6701',bg='#fcecdd')
mylabel.pack(pady=10)
textbox1 = Entry(root,textvariable=scale)
textbox1.pack(pady = 10)

def neighfunc():
 neighboor = neigh.get()
 return neighboor
def scalefunc():
 scalefac = scale.get()
 return scalefac

button = Button(root,text = "Input Nilai",command=root.destroy,fg='#fcecdd',bg='#ff6701')
button.pack(pady= 5)

emptylabel = Label(root)
emptylabel.pack(pady=50)
answer = Label(root, text=" ")
answer.pack(pady=20)
root.mainloop()

neighvar = neighfunc()
print(neighvar)
sfvar = scalefunc()
print(sfvar)

while True:
 retV, frame = cam.read()
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 faces = faceDetection.detectMultiScale(gray, scaleFactor=sfvar, minNeighbors=neighvar)
 for (x, y, w, h) in faces:
     color = (0, 0, 255)
     stroke = 2
     frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)
 cv2.imshow("webcam", frame)

 # cv2.imshow("webcam-gray",gray)

 key = cv2.waitKey(1) & 0xff
 if key == 27 or key == ord("q"):
     break

cam.release()
cv2.destroyAllWindows()


