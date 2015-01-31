#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from largeGauge import largeGauge
from smallGauge import smallGauge

class dashboard(Frame):
    def __init__(self,master=None,name=None):
        Frame.__init__(self,master)
        self.pack(fill=BOTH)
        speedFrame = Frame(self)
        speedFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        speedGauge=largeGauge(speedFrame,250)
        speedGauge.pack()

        middleFrame = Frame(self)
        middleFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        heatGauge = smallGauge(middleFrame,125)
        heatGauge.pack(padx=2,pady=2)
        oilGauge = smallGauge(middleFrame,125)
        oilGauge.pack(padx=2,pady=2)

        rpmFrame = Frame(self)
        rpmFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        rpmGauge=largeGauge(rpmFrame,250)
        rpmGauge.pack()
