#!/bin/usr/python

BASEDIR="/Users/Keshav/Documents/WhIP 2.0 - Source Code"

import time
from SimpleCV import *
display = Display()
haarcascade = HaarCascade("face")

img = Image(BASEDIR + "snapshot.jpg")
faces = i.findHaarFeatures("/path/to/haarcascade_frontalface_alt.xml")

#print locations
for f in faces:
  print "I found a face at " + str(f.coordinates())

green = (0, 255, 0)
#outline who was drinking last night (or at least has the greenest pallor)
faces.sortColorDistance(green)[0].draw(green)
i.save("greenest_face_detected.png") 

 
