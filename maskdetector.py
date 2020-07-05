#v1.0

#LIBRARIES
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model

#LOADING MODEL 
model = load_model(r'C:\Users\malha\Desktop\ML\Mask Detector\model')

#INITIALIZATION
SIZE = 80
CATEGORIES = ['No Mask','Mask']
labels_dict = {0:'No Mask',1:'Mask'}
colour_dict = {0:(255,0,0),1:(0,225,0)}


#OPENCV SCRIPT
face_cascade = cv2.CascadeClassifier(r'C:\Users\malha\Desktop\ML\Mask Detector\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    without_mask = 0
    with_mask = 0
    
    for (x,y,w,h) in faces:
        #face_image = gray[y:y+h,x:x+w]
        #resized = cv2.resize(gray[y:y+h,x:x+w],(SIZE,SIZE))
        #reshaped = np.array(cv2.resize(gray[y:y+h,x:x+w],(SIZE,SIZE))).reshape(1,SIZE,SIZE,1)
        faceimg = (np.array(cv2.resize(gray[y:y+h,x:x+w],(SIZE,SIZE))).reshape(1,SIZE,SIZE,1))/255.0
        result = model.predict_classes(faceimg)[0][0]
        
        if result == 0:
            without_mask += 1
        else:
            with_mask += 1
            
        cv2.rectangle(img,(x,y),(x+w,y+h),colour_dict[result],2)
        cv2.rectangle(img,(x,y-40),(x+w,y),colour_dict[result],-1)

        cv2.putText(img,labels_dict[result],(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        
    cv2.putText(img,'Without Mask: ' + str(without_mask),(0,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),1)
    cv2.putText(img,'With Mask: ' + str(with_mask),(0,80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),1)


    cv2.imshow('MASK DETECTOR',img)

    key = cv2.waitKey(80) & 0xff
    if key == 27:
        break
      
        
cap.release()
cv2.destroyAllWindows()

input("Press ENTER to exit")

                
        
        
        