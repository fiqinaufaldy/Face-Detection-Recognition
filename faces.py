
import cv2
import numpy as np
import pickle
import os

#lANGKAH FACE RECOGNITION : rekam data wajah, trainning data, recognition
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels = {"persons_name": 1}
label_ids = {}
scores = {}
with open("labels.pickle",'rb') as f :
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cam = cv2.VideoCapture(0)
cam.set(3,680)
cam.set(4,480)

while True:
 retV, frame = cam.read()
 gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
 faces = faceDetection.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
 for (x,y,w,h) in faces:

     roi_color = frame[y:y+h,x:x+w]
     roi_gray = gray[y:y+h,x:x+w]

     id_,conf= recognizer.predict(roi_gray)
     if conf >=45 and conf <=85:
         print(id_)
         print(labels[id_])
         font = cv2.FONT_HERSHEY_SIMPLEX
         name = labels[id_]
         conftxt = "{0}%".format(round(100-conf))
         color = (255,255,255)
         stroke = 2
         cv2.putText(frame,name,(x+5,y-5),font,1,color,stroke,cv2.LINE_AA)
         #cv2.putText(frame,str(conftxt), (x + 5, y+h- 5), font, 1, color, stroke, cv2.LINE_AA)
     else:
         cv2.putText(frame, str('unknown'), (x + 5, y - 5),font, 1, color, stroke, cv2.LINE_AA)

     img_item = "my-image.png"
     cv2.imwrite(img_item,roi_gray)
     color = (0,0,255)
     stroke = 2
     frame = cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)
 cv2.imshow("webcam",frame)
 #cv2.imshow("webcam-gray",gray)

 key =  cv2.waitKey(1) & 0xff
 if key == 27 or key == ord("q") :
     break
cam.release()
cv2.destroyAllWindows()

