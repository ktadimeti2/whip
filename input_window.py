#!/usr/bin/python
import os
import sys
import subprocess
import random
from Tkinter import *
from subprocess import Popen
from random import randint

fields = 'Total time to monitor', 'Interval between taking pictures', 'After how many seconds to alert if asleep', 'After how many seconds to alert if away from computer'

args = []
arg_id = ["-t", "-i", "--sleeplimit", "nofacelimit"]

def fetch(entries):
   i = 0
   for i in range(0, len(entries)):
      entry = entries[i]
      field = entry[0]
      text  = entry[1].get()
      if(text.strip() != ""):
         args.append(arg_id[i])
         args.append(text)

   arg_string = ""
   for arg in args:
      arg_string += arg + " "
   p = Popen(["python", "commence_whip.py", arg_string])
   sys.exit()

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=40, text=field, anchor="w", justify=LEFT)
      ent = Entry(row, width=5)
      row.pack(side=TOP, fill=X, padx=5, pady=0)
      lab.pack(side=LEFT, expand=NO)
      ent.pack(side=LEFT, expand=NO, fill=X)
      entries.append((field, ent))
   return entries

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


# main method
if __name__ == '__main__':
   
   # create message box for input
   root = Tk()
   root.title("Whoops, I Procrastinated (WhIP)")

   # to center the window and bring it to the front
   w = 450
   h = 310
   sw = root.winfo_screenwidth()
   sh = root.winfo_screenheight()
   x = (sw-w)/2
   y = (sh-h)/2
   root.geometry('%dx%d+%d+%d' % (w, h, x, y))
   root.resizable(width=FALSE, height=FALSE)


   root.attributes("-topmost", True)
   
   # for the title image - chosen randomly
   title_photo = PhotoImage(file= chooseTitle())
   p = Label(root, image=title_photo)
   p.pack()
   
   # for a line
   line = Label(root, text="-----------------------------------------------------", fg="#98AFC7")
   line.pack()
   
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Enter',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

   
