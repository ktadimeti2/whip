#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
from PIL import Image

im = Image.open("asleep.jpg")
im.show()

audio_file = "Derp_song.wav"
return_code = subprocess.call(["afplay", audio_file])

