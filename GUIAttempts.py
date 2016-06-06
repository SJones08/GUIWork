# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:48:17 2016

@author: sherman
"""

#Making a GUI for various project parts
print "Give it a think, then give it a go!" 
from Tkinter import *
top = Tkinter.Tk()
#Code to add widgets will go here

C = Tkinter.Canvas(top, bg="green", height=300, width=300)

coord = 120, 60, 300, 300
arc = C.create_arc(coord, start=60, extent=60, fill="blue")

C.pack()
top.mainloop()