#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from gauge import gauge

class dashboard(Frame):
    def __init__(self,master=None,name=None):
        Frame.__init__(self,master)
        self.pack(fill=BOTH)
        speedFrame = Frame(self)
        speedFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        speedGauge=gauge(speedFrame,125)
        speedGauge.pack()

        middleFrame = Frame(self)
        middleFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        heatGauge = gauge(middleFrame,50)
        heatGauge.pack(padx=2,pady=2)
        oilGauge = gauge(middleFrame,50)
        oilGauge.pack(padx=2,pady=2)

        rpmFrame = Frame(self)
        rpmFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        rpmGauge=gauge(rpmFrame,125)
        rpmGauge.pack()
