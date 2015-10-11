#!/usr/bin/python

import time
import subprocess
import sys
from SimpleCV import *

BASEDIR="/Users/Keshav/Documents/Code/WhIP 2.0 - Source Code/"

haaarcascade = HaarCascade("face")

image = Image.open(BASEDIR + "snapshot.jpg")
faces = image.findHaarFeatures(haarcascade)
if faces:
    face = face[-1]
    face.draw(Color.RED, 1)


# check if eyes are detectable
# if not detectable for x seconds
# exit('closed')
    
image.show()

