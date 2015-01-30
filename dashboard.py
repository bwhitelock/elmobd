#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from testTab1 import testTab1
from testTab2 import testTab2
from general import general
import Queue

class dashboard(Frame):
    #def __init__(self,parent,device,queue):
    #def __init__(self,parent,device,queue):
    def __init__(self,master=None,name=None):
        #Tkinter.Tk.__init__(self,parent)
        Frame.__init__(self,master)
        #self.device=device
        ##self.parent = parent
        #self.returnQueue=queue
        #master = Frame(self.parent, name='master')
        self.pack(fill=BOTH)
        tabFrame = Frame(self)
        tabFrame.pack(fill=BOTH,expand=True)
        self.notebook = Notebook(tabFrame, name='nb')
        self.notebook.pack(fill=BOTH,expand=True)

        #self.engineTab = engineTab(self.notebook, self.device, name='engineTab')
        self.general = general(self.notebook, name='general')
        self.notebook.add(self.general, text="General")

        #self.testTab1 = testTab1(self.notebook, self.device, name='Tab 1')
        self.testTab1 = testTab1(self.notebook, name='Tab 1')
        self.notebook.add(self.testTab1, text="Tab 1")

        #self.testTab2 = testTab2(self.notebook, self.device, name='secondTab')
        self.testTab2 = testTab2(self.notebook, name='secondTab')
        self.notebook.add(self.testTab2, text="Tab 2")
