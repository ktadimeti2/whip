#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
from PIL import Image

BASEDIR = "/Users/Keshav/Documents/Code/WhIP 2.0 - Source Code/"

im = Image.open(BASEDIR + "asleep.jpg")
im.show()

audio_file = BASEDIR + "Derp_song.wav"
print audio_file
return_code = subprocess.call(["afplay", audio_file])

