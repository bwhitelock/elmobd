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
        testFrame=Frame(self)
        testFrame.pack()
        frame1=Frame(testFrame)
        frame1.pack(fill=BOTH,expand=True,side=LEFT)
        #self.columnconfigure(0,weight=1)
        #self.rowconfigure(0,weight=1)
        self.entryVariable = Tkinter.StringVar()
        #self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry = Entry(frame1,textvariable=self.entryVariable)
        #self.entry = Entry(self)
        self.entry.bind("<Return>", self.onPressEnter)
        self.entryVariable.set(u"Enter text here.")
        #self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.pack(side=LEFT,expand=True)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        sendFrame=Frame(testFrame)
        sendFrame.pack(fill=X,expand=True,side=LEFT)
        sendButton = Button(sendFrame,text="Send",command=self.onButtonPress)
        sendButton.bind("<Return>", self.onPressEnter)
        sendButton.pack(side=LEFT,padx=10)
        frame2=Frame(self)
        frame2.pack(fill=BOTH,expand=True,side=BOTTOM)
        self.cText = Text(frame2)
        self.cText.pack()

    def disableMe(self):
        self.configure(state='disabled')

    def enableMe(self):
        self.configure(state='normal')

    def onPressEnter(self,event):
        self.sendCommand()

    def onButtonPress(self):
        self.sendCommand()

    def sendCommand(self):
        textVar = self.entryVariable.get()
        print "You pressed enter !", textVar
        source = ['entry',textVar]
        textVar = textVar + "\n"
        self.cText.insert(END, textVar)
        #self.device.putData(source)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
