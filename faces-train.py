import os
import numpy as np
from PIL import  Image
import cv2
import pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"images")
faceDetection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
y_labels = []
x_train = []
current_id = 0
label_ids = {}
for root,dirs,files in os.walk((image_dir)):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            print(label,path)
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)
            #y_labels.append(label)
            #x_train.append(path) #Mengubah gambar menjadi susunan array
            pil_image = Image.open(path).convert("L") #convert menjadi grayscale

            image_array = np.array(pil_image,"uint8")
            print (image_array)
            faces = faceDetection.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h,x:x+h]
                x_train.append(roi)
                y_labels.append(id_)
#print(y_labels)
#print(x_train)

with open("labels.pickle",'wb') as f :
    pickle.dump(label_ids,f)
#TRAIN
recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")
#Implement Recognizer
print('Finish Train Data')












