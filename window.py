#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import sys
from subprocess import Popen

from Tkinter import *
from ttk import Frame, Button, Style
from PIL import Image

BASEDIR = "/Users/Keshav/Documents/Code/WhIP 2.0 - Source Code/"
bHeight = 95

global job 
job = 0

def startMonitor():
	command = ['./img_cap.sh', '-v', '&']
	pro = Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	global job 
	job = pro
	return pro
#	call([BASEDIR+"img_cap.sh", "-v &"])
#	os.spawnl(os.P_DETACH, BASEDIR+'img_cap.sh -v &')

def quitMonitor():
	if (job != 0):
		os.killpg(job.pid, signal.SIGTERM)
		
	sys.exit()


class WhIP_window(Frame):
	
    def __init__(self, parent):
	    
	    Frame.__init__(self, parent)
	    
	    self.parent = parent

	    self.centerWindow()
	    self.startButton()
	    self.quitButton()

    def centerWindow(self):
	    w = 290
	    h = 150
	    sw = self.parent.winfo_screenwidth()
	    sh = self.parent.winfo_screenheight()
	    x = (sw-w)/2
	    y = (sh-h)/2
	    self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
    def startButton(self):
	    self.style = Style()
	    self.style.theme_use("default")
	    
	    self.pack(fill=BOTH, expand=1)
	    
	    startButton = Button(self, text="Start", command=startMonitor)
	    startButton.place(x=25, y=bHeight)

    def quitButton(self):
	    
	    self.style = Style()
	    self.style.theme_use("default")
	    
	    self.pack(fill=BOTH, expand=2)
	    
	    quitButton = Button(self, text="Quit", command=quitMonitor)
	    quitButton.place(x=185, y=bHeight)


def main():
        
    root = Tk()
    root.title("Whoops, I Procrastinated (WhIP)")
    root.geometry("500x500")
    root.resizable(width=FALSE, height=FALSE)

    root.configure(background='grey')

    app = WhIP_window(root)

    label = Label(app, text = "WhIP - The Alertness Assistant", font=("Helvetica", 16), justify=CENTER)
    label.pack()

    root.mainloop()
#    os.killpg(pro.pid, signal.SIGTERM)  


# main method        
if __name__ == '__main__':
    main()
    
