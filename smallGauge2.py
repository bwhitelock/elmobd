#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter as tk
from math import cos,sin,pi,ceil
import sys, time
from random import randrange

class smallGauge2(Frame):
    def __init__(self,master,size,minValue,maxValue,stepValue):
        Frame.__init__(self,master,borderwidth=5,relief=GROOVE)
        self.size=size
        self.minValue=minValue
        self.maxValue=maxValue
        self.stepValue=stepValue

        self.pack()
        self.Canvas = tk.Canvas(self, width=size, height=size, bg="#456", relief= "sunken", border=10)
        self.Canvas.pack(expand=True)

        self.circleStart=15
        self.circleSize = size
        self.Canvas.create_oval(15,15,self.circleSize,self.circleSize, fill="blue", width=2)
        #adjust = size*.35
        adjust = size*(self.circleStart*3.0/size)
        self.Canvas.create_arc(self.circleStart+adjust,self.circleStart+adjust,self.circleSize-adjust,self.circleSize-adjust,start=-45,extent=270,style="arc",width=2)
        self.Canvas.create_line(0,0,0,0, fill="red", tags="dialHand")

        tickValue=int(ceil(stepValue/2.0))
        self.degreeDivisor=ceil(maxValue/2.0)
        valueList = range(minValue,(maxValue+stepValue),stepValue)
        for value in valueList:
            degrees = round((value/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
            self.makeValueLine(degrees,str(int(value)))
            if (value+tickValue) < maxValue:
                degrees = round(((value+tickValue)/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
                self.makeTickLine(degrees)
        self.update_dial(randrange(0,maxValue))

    def makeValueLine(self,degrees,value):
        angle = degrees*pi*2/360
        tempAdjust = ((self.size-10.0)/1000.0)
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*tempAdjust
        #ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.125
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*tempAdjust
        #oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.125
        x1 = ox + self.circleSize*sin(angle)*.085
        y1 = oy - self.circleSize*cos(angle)*.085
        x2 = ox + self.circleSize*sin(angle)*.19
        y2 = oy - self.circleSize*cos(angle)*.19
        self.Canvas.create_line(ox,oy,x1,y1, fill="black",width=2)
        self.Canvas.create_text(x2,y2,text=value)

    def makeTickLine(self,degrees):
        angle = degrees*pi*2/360
        #ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.115
        #oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.115
        tempAdjust = ((self.size-5.0)/1000.0)
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*tempAdjust
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*tempAdjust
        x1 = ox + self.circleSize*sin(angle)*.070
        y1 = oy - self.circleSize*cos(angle)*.070
        self.Canvas.create_line(ox,oy,x1,y1, fill="black")

    def update_dial(self,value):
        degrees = round((value/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
        angle = degrees*pi*2/360
        ox = (self.circleSize+self.circleStart)/2
        oy = (self.circleSize+self.circleStart)/2
        x = ox + self.circleSize*sin(angle)*0.35
        y = oy - self.circleSize*cos(angle)*0.35
        self.Canvas.coords("dialHand", (ox,oy,x,y))
        self.after(1000, self.update_dial, randrange(0,self.maxValue))
