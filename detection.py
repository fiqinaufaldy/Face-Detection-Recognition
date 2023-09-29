import cv2

#lANGKAH FACE RECOGNITION : rekam data wajah, trainning data, recognition
cam = cv2.VideoCapture(0)
cam.set(3,680)
cam.set(4,480)
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
 retV, frame = cam.read()
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 faces = faceDetection.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
 for (x,y,w,h) in faces:
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

