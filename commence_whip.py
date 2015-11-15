#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import sys
import random
from subprocess import Popen
from subprocess import check_output

from Tkinter import *
from ttk import Button, Style
from PIL import Image
from random import randint

w = 350
h = 250

global job 
job = 0

def quitWhIP():
	global job
	if (job != 0):
		try:
                        os.killpg(job.pid, signal.SIGTERM)
                except OSError as e:
                        sys.exit()

def startMonitor():
	arg = '-v &'
	if (len(sys.argv) >= 2 and sys.argv[1].strip() != ''):
		arg = sys.argv[1]
	command = ['./img_cap.sh %s' % arg]
	pro = Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	global job 
	job = pro
	return pro

def callInputWindow():
	quitWhIP()
	p = Popen(["python", "input_window.py"])
	sys.exit()


def quitMonitor():
	quitWhIP()
	sys.exit()

def chooseTitle():
   rand = randint(0, 4)
   title = ""
   if(rand == 1):
      title = "Blue"
   elif (rand == 2):
      title = "Color"
   else:
      title = "Bold"

   return "title_gifs/WhIP_%s_Title.gif" % title

class WhIP_window(Frame):
	
    def __init__(self, parent):
	    
	    Frame.__init__(self, parent, background="white")
	    
	    self.parent = parent
	    self.centerWindow()
	    self.startButton()
	    self.quitButton()
	    self.backButton()

    def centerWindow(self):
	    sw = self.parent.winfo_screenwidth()
	    sh = self.parent.winfo_screenheight()
	    x = (sw-w)/2
	    y = (sh-h)/2
	    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
    def startButton(self):
	    self.style = Style()
	    self.style.theme_use("default")
	    
	    self.pack(fill=BOTH, expand=1)
	    
	    startButton = Button(self, text="Start   -->", command=startMonitor)

	    # to calculate where to put button
	    x1 = w - w/3 + 10
	    y1 = h/5
	    startButton.place(x=x1, y=y1)

    def backButton(self):
	    self.style = Style()
	    self.style.theme_use("default")
	    
	    self.pack(fill=BOTH, expand=1)
	    
	    backButton = Button(self, text="<--   Back", command=callInputWindow)

	    # to calculate where to put button
	    x1 = w/16 - 10
	    y1 = h/5
	    backButton.place(x=x1, y=y1)


    def quitButton(self):
	    
	    self.style = Style()
	    self.style.theme_use("default")
	    
	    self.pack(fill=BOTH, expand=2)
	    
	    quitButton = Button(self, text="Quit", command=quitMonitor)
	    
	    # to calculate where to put button
	    x1 = w/3 + 10
	    y1 = h/5
	    quitButton.place(x=x1, y=y1)


def main():
   # Create Tkinter message box
    root = Tk()
    root.title("Whoops, I Procrastinated (WhIP)")
    root.geometry("500x500")
    root.resizable(width=FALSE, height=FALSE)
    root.attributes("-topmost", True)
    root.configure(background='white')

    # for the title image - chosen randomly
    title_photo = PhotoImage(file= chooseTitle())
    p = Label(root, image=title_photo)
    p.pack()

    
   # Create the WhIP Window with 'Start' and 'Quit' buttons
    app = WhIP_window(root)
    root.mainloop()

# main method        
if __name__ == '__main__':
	main()
    
