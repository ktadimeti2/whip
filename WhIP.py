# ----------------------------------------------------------#
#    WhIP:  "Whoops, I Procrastinated" Anti-Sleep Program   |
#   By: Srikanth Kalluri, Shahryar Moohraj, Keshav Tadimeti |
# ----------------------------------------------------------#

import os
import cv2
import sys
import time
from Tkinter import *
from tkMessageBox import *

fcascPath = "haarcascade_frontalface_default.xml"
ecascPath = "haarcascade_eye.xml"
faceCascade = cv2.CascadeClassifier(fcascPath)
eyeCascade = cv2.CascadeClassifier(ecascPath)

video_capture = cv2.VideoCapture(0)
pid = os.getpid()

# -- Activate the WhIP Program -- #
def WhIP_On(length):
    fcascPath = "haarcascade_frontalface_default.xml"
    ecascPath = "haarcascade_eye.xml"
    faceCascade = cv2.CascadeClassifier(fcascPath)
    eyeCascade = cv2.CascadeClassifier(ecascPath)
    initial = time.time()

    video_capture = cv2.VideoCapture(0)
    while True:
        nextCheck = initial+int(length)
        current = time.time()

        if(current > nextCheck):
            break

        #  Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        num_faces = len(faces)

        if(num_faces >0):
            eyes = eyeCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=12,
                minSize=(20, 20),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

        # Timer
        numeyes=len(eyes)
        if(numeyes>=2):
            nextCheck = current + length
            initial=time.time()
        
        
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (212, 111, 249), 2)
        
        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

# -- Counter -- #
def counter(length):
    initial = time.time()
    final = initial + int(length)
    while (time.time() < final):
        time.sleep(1)
    return True

# -- Create box if found asleep -- #
def drawBox():
    b = False
    while(b!=True):
        b = counter(5)
    os.system("sound.py")
    showerror("Awake?", "It looked like you fell asleep. Better luck next time.")
    return

# -- Kill command -- #
def quit_system(): 
    os.system('kill %d'%pid)

# -- Check for rerun -- #
def rerun():
    rerun = askyesno("Shall we?", "Do you want to use WhIP to keep yourself awake?")
    if (rerun==True):
        relay_loop()
    else:
        quit_system()

# -- Relay Loop -- #
def relay_loop():
    WhIP_On(150)
    drawBox()
    rerun()


current = time.time()
# Start the program
relay_loop()


