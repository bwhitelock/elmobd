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

        #self.pack(fill=BOTH)
        self.pack()
        self.Canvas = tk.Canvas(self, width=size, height=size, bg="#456", relief= "sunken", border=10)
        #self.Canvas = tk.Canvas(self, width=size, height=size, border=2)
        #self.Canvas = tk.Canvas(self)
        #self.Canvas.pack(fill=BOTH,expand=True)
        self.Canvas.pack(expand=True)

        #self.Canvas.create_oval(6,6,size,size, fill="blue", width=4)
        self.circleStart=15
        self.circleSize = size
        self.Canvas.create_oval(15,15,self.circleSize,self.circleSize, fill="blue", width=2)
        adjust = size*.35
        self.Canvas.create_arc(self.circleStart+adjust,self.circleStart+adjust,self.circleSize-adjust,self.circleSize-adjust,start=-45,extent=270,style="arc",width=2)
        self.Canvas.create_line(0,0,0,0, fill="#ffc", tags="hour")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="minute")
        self.Canvas.create_line(0,0,0,0, fill="black", tags="second")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="dialHand")

        #stepValue=int(ceil(maxValue/13.0))
        tickValue=int(ceil(stepValue/2.0))
        self.degreeDivisor=ceil(maxValue/2.0)
        print "step value",stepValue
        print "tick value",tickValue
        print "degree Divisor value",self.degreeDivisor
        valueList = range(minValue,(maxValue+stepValue),stepValue)
        print "valueList",valueList
        #for value in range(minValue,maxValue,int(stepValue)):
        for value in valueList:
            degrees = round((value/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
            print "value %s degrees %s" %(value,degrees)
            self.makeValueLine(degrees,str(int(value)))
            if (value+tickValue) < maxValue:
                #degrees = round(((value+tickValue)/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
                degrees = round(((value+tickValue)/self.degreeDivisor*135.0+225.0) - 360.0*(1 if value > self.degreeDivisor else 0))
                self.makeTickLine(degrees)
            print "value %s degrees %s" %((value+tickValue),degrees)

        #listValues = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]
        #for value in listValues:
            #degrees = round((value/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
            #self.makeValueLine(degrees,str(value))

        #listValues = [0,10,30,50,70,90,110,130,150,170,190,210,230,250]
        #for value in listValues:
            #degrees = round((value/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
            #self.makeTickLine(degrees)

        #self.update_dial(randrange(0,255))
        self.update_dial(randrange(0,maxValue))

    def makeValueLine(self,degrees,value):
        angle = degrees*pi*2/360
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.110
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.110
        x1 = ox + self.circleSize*sin(angle)*.090
        y1 = oy - self.circleSize*cos(angle)*.090
        x2 = ox + self.circleSize*sin(angle)*.19
        y2 = oy - self.circleSize*cos(angle)*.19
        self.Canvas.create_line(ox,oy,x1,y1, fill="black",width=2)
        self.Canvas.create_text(x2,y2,text=value)

    def makeTickLine(self,degrees):
        angle = degrees*pi*2/360
        ox = (self.circleSize+self.circleStart)/2 + self.circleSize*sin(angle)*.115
        oy = (self.circleSize+self.circleStart)/2 - self.circleSize*cos(angle)*.115
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

    def update_clock(self):

        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        degrees = 6*s
        angle = degrees*pi*2/360
        ox = (self.circleSize)/2
        oy = (self.circleSize)/2
        x = ox + self.circleSize*sin(angle)*0.3
        y = oy - self.circleSize*cos(angle)*0.3
        self.Canvas.coords("hour", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        ox1 = (self.circleSize)/2
        oy1 = (self.circleSize)/2
        x1 = ox1 + self.circleSize*sin(angle1)*0.3
        y1 = oy1 - self.circleSize*cos(angle1)*0.3
        self.Canvas.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        ox2 = (self.circleSize)/2
        oy2 = (self.circleSize)/2
        x2 = ox2 + self.circleSize*sin(angle2)*0.2
        y2 = oy2 - self.circleSize*cos(angle2)*0.2
        self.Canvas.coords("second",(ox2,oy2,x2,y2))

        self.after(1000, self.update_clock)

