#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter as tk
from math import cos,sin,pi,ceil
import sys, time
from random import randrange
import tkFont

class gauge(Frame):
    def __init__(self,master,size,minValue,maxValue,stepValue,gaugeText,tickMarks=1):
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
        self.Canvas.create_oval(self.circleStart,self.circleStart,self.circleSize,self.circleSize, fill="black", outline="white", width=2)
        #adjust = size*.15
        adjust = size*(self.circleStart*3.0/size)
        self.Canvas.create_arc(self.circleStart+adjust,self.circleStart+adjust,self.circleSize-adjust,self.circleSize-adjust,start=-45,extent=270,style="arc",width=2,fill="white")
        tickValue=stepValue/(tickMarks+1.0)
        self.degreeDivisor=ceil(maxValue/2.0)
        valueList = range(minValue,(maxValue+stepValue),stepValue)
        for value in valueList:
            degrees = round((value/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
            self.makeValueLine(degrees,str(int(value)))
            newvalue = value
            for x in xrange(tickMarks):
                newvalue = newvalue + tickValue
                if newvalue < maxValue:
                    degrees = round((newvalue/self.degreeDivisor*135.0+225.0) - 360.0*(1 if newvalue > self.degreeDivisor else 0))
                    self.makeTickLine(degrees)

        redDotRadius=5
        redDot0=(self.circleSize+self.circleStart)/2-redDotRadius
        redDot1=(self.circleSize+self.circleStart)/2+redDotRadius
        self.Canvas.create_oval(redDot0,redDot0,redDot1,redDot1, fill="red", outline="red")
        thisFont = tkFont.Font()
        print "font",thisFont['size']
        #self.Canvas.create_text((self.circleSize+self.circleStart)/2,(self.circleSize*.90),text=gaugeText, fill="white",font=('Helvetica', 12, 'normal'))
        self.Canvas.create_text((self.circleSize+self.circleStart)/2,(self.circleSize*.90),text=gaugeText, fill="white",font=thisFont)
        self.Canvas.create_line(0,0,0,0, fill="red", tags="dialHand")
        self.update_dial(randrange(0,maxValue))

    def makeValueLine(self,degrees,value):
        angle = degrees*pi*2/360
        tempAdjust = ((self.size-10.0)/1000.0)
        #ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.3
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*tempAdjust
        #oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.3
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*tempAdjust
        x1 = ox + self.circleSize*sin(angle)*.085
        y1 = oy - self.circleSize*cos(angle)*.085
        #x2 = ox + self.circleSize*sin(angle)*.13
        #y2 = oy - self.circleSize*cos(angle)*.13
        x2 = ox + self.circleSize*sin(angle)*((2-(2*tempAdjust))/10)
        y2 = oy - self.circleSize*cos(angle)*((2-(2*tempAdjust))/10)
        self.Canvas.create_line(ox,oy,x1,y1, fill="white",width=2)
        self.Canvas.create_text(x2,y2,text=value,fill="white")

    def makeTickLine(self,degrees):
        angle = degrees*pi*2/360
        #ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.295
        tempAdjust = ((self.size-5.0)/1000.0)
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*tempAdjust
        #oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.295
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*tempAdjust
        x1 = ox + self.circleSize*sin(angle)*.070
        y1 = oy - self.circleSize*cos(angle)*.070
        self.Canvas.create_line(ox,oy,x1,y1, fill="white")

    def update_dial(self,value):
        degrees = round((value/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
        angle = degrees*pi*2/360
        ox = (self.circleSize+self.circleStart)/2
        oy = (self.circleSize+self.circleStart)/2
        x = ox + self.circleSize*sin(angle)*0.35
        y = oy - self.circleSize*cos(angle)*0.35
        self.Canvas.coords("dialHand", (ox,oy,x,y))
        self.after(1000, self.update_dial, randrange(0,self.maxValue))
