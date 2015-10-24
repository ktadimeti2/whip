import sys
import numpy as np
import cv2

def show_pic(cv2, img):
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

img = cv2.imread('snapshot.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Keep track of the number of faces
num_faces = len(faces)

# Initialize variable to keep track of number of eyes found
num_eyes = 0

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    num_eyes = len(eyes)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# Check if number of faces and eyes detected prove awakeness

if(num_faces > 0):
    if(num_eyes >= 2):
        exit('open')
    
    else:
        exit('closed')

else:
    exit('noFace')
