#!/usr/bin/python
import os
import sys
import subprocess
import random
from Tkinter import *
from subprocess import Popen
from random import randint

time=1
minus_plus_width = 2
tkinter_entries = []

fields = 'Total number of minutes to monitor for', 'After how many seconds to alert if asleep', 'After how many seconds to alert if away from computer'

args = []
arg_id = ["-t", "--sleeplimit", "nofacelimit"]

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

def create_set_time(entryIndex, num):
   e = tkinter_entries[entryIndex]
   def set_time():
      time = int(e.get())
      
      if (num > 0 or time > 0):
         time += num
         e.delete(0,END)
         e.insert(0,time)

   return set_time

def makeform(root, fields):
   entries = []

   entryIndex=-1
   for field in fields:
      entryIndex += 1
      row = Frame(root)

      # create the text box
      ent = Entry(row, width=5)
      ent.insert(0,1)

      global tkinter_entries
      tkinter_entries.append(ent)

      set_time_minus = create_set_time(entryIndex,-1)
      set_time_plus = create_set_time(entryIndex,1)

      minus = Button(row, width=minus_plus_width, text="-", command=set_time_minus)
      plus = Button(row, width=minus_plus_width, text="+", command=set_time_plus)
      lab = Label(row, width=40, text=field, anchor="w", justify=LEFT)

      row.pack(side=TOP, fill=X, padx=5, pady=0)
      lab.pack(side=LEFT, expand=NO)
      minus.pack(side=LEFT, expand=NO)
      plus.pack(side=RIGHT, expand=NO)
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
   h = 290
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

   
