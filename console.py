#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *

class console(Frame):
    #def __init__(self, master=None, device=None, name=None):
    def __init__(self, master=None, name=None):
        Frame.__init__(self, master)
        #self.device=device
        self.name=name
        #self.grid(sticky=N+S+E+W)
        self.pack(fill=BOTH,expand=True)
        frame1=Frame(self)
        frame1.pack(fill=BOTH)
        #self.columnconfigure(0,weight=1)
        #self.rowconfigure(0,weight=1)
        self.entryVariable = Tkinter.StringVar()
        #self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry = Entry(frame1,textvariable=self.entryVariable)
        #self.entry = Entry(self)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")
        #self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.pack(fill=X,expand=True)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        frame2=Frame(self)
        frame2.pack(fill=BOTH,expand=True)
        self.cText = Text(frame2)
        self.cText.pack()

    def disableMe(self):
        self.configure(state='disabled')

    def enableMe(self):
        self.configure(state='normal')

    def OnPressEnter(self,event):
        #self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)" )
        textVar = self.entryVariable.get()
        print "You pressed enter !", textVar
        source = ['entry',textVar]
        textVar = textVar + "\n"
        self.cText.insert(END, textVar)
        #self.device.putData(source)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
