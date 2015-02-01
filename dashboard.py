#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from gauge import gauge
from largeGauge import largeGauge
from smallGauge import smallGauge
from smallGauge2 import smallGauge2

class dashboard(Frame):
    def __init__(self,master=None,name=None):
        Frame.__init__(self,master,borderwidth=5,relief=GROOVE)
        self.pack(fill=BOTH)
        speedFrame = Frame(self)
        #speedFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
        #speedGauge=largeGauge(speedFrame,250)
        speedGauge=gauge(speedFrame,300,0,260,20)
        speedGauge.pack()
        speedFrame.pack(fill=BOTH,expand=True,side=LEFT)

        middleFrame = Frame(self)
        #heatGauge = smallGauge(middleFrame,125)
        heatGauge = smallGauge2(middleFrame,125,0,140,20)
        #heatGauge.pack(padx=2,pady=2)
        heatGauge.pack()
        #oilGauge = smallGauge(middleFrame,125)
        oilGauge = smallGauge2(middleFrame,125,0,100,10)
        #oilGauge.pack(padx=2,pady=2)
        oilGauge.pack()
        middleFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)

        rpmFrame = Frame(self)
        #rpmGauge=largeGauge(rpmFrame,250)
        rpmGauge=gauge(rpmFrame,300,0,170,10)
        rpmGauge.pack()
        rpmFrame.pack(fill=BOTH,expand=True,side=LEFT,padx=4,pady=4)
