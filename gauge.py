#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter as tk
from math import cos,sin,pi
import sys, time
from random import randrange

class gauge(Frame):
    def __init__(self,master=None,size=200):
        Frame.__init__(self,master)
        self.size=size

        self.pack(fill=BOTH)
        #self.Canvas = tk.Canvas(self, width=size, height=size, bg="#456", relief= "sunken", border=10)
        #self.Canvas = tk.Canvas(self, width=size, height=size, border=2)
        self.Canvas = tk.Canvas(self)
        self.Canvas.pack()

        #self.Canvas.create_oval(6,6,size,size, fill="blue", width=4)
        self.circleSize = size - 5
        self.Canvas.create_oval(5,5,self.circleSize,self.circleSize, fill="blue", width=4)
        adjust = size*.25
        self.Canvas.create_arc(5+adjust,5+adjust,self.circleSize-adjust,self.circleSize-adjust,start=-45,extent=270,style="arc",width=4)
        self.Canvas.create_line(0,0,0,0, fill="#ffc", tags="hour")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="minute")
        self.Canvas.create_line(0,0,0,0, fill="black", tags="second")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="dialHand")

        listValues = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]
        for value in listValues:
            degrees = round((value/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
            self.makeValueLine(degrees,str(value))

        listValues = [0,10,30,50,70,90,110,130,150,170,190,210,230,250]
        for value in listValues:
            degrees = round((value/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
            self.makeTickLine(degrees)

        self.update_dial(randrange(0,255))

    def makeValueLine(self,degrees,value):
        angle = degrees*pi*2/360
        ox = (self.circleSize)/2 + self.circleSize*sin(angle)*.290
        oy = (self.circleSize)/2 - self.circleSize*cos(angle)*.290
        x1 = ox + self.circleSize*sin(angle)*.080
        y1 = oy - self.circleSize*cos(angle)*.080
        x2 = ox + self.circleSize*sin(angle)*.13
        y2 = oy - self.circleSize*cos(angle)*.13
        self.Canvas.create_line(ox,oy,x1,y1, fill="black",width=2)
        self.Canvas.create_text(x2,y2,text=value)

    def makeTickLine(self,degrees):
        angle = degrees*pi*2/360
        ox = (self.circleSize)/2 + self.circleSize*sin(angle)*.295
        oy = (self.circleSize)/2 - self.circleSize*cos(angle)*.295
        x1 = ox + self.circleSize*sin(angle)*.070
        y1 = oy - self.circleSize*cos(angle)*.070
        self.Canvas.create_line(ox,oy,x1,y1, fill="black")

    def update_dial(self,value):
        degrees = round((value/130.0*135.0+225.0) - 360.0*(1 if value > 130.0 else 0))
        angle = degrees*pi*2/360
        ox = (self.circleSize)/2
        oy = (self.circleSize)/2
        x = ox + self.circleSize*sin(angle)*0.35
        y = oy - self.circleSize*cos(angle)*0.35
        self.Canvas.coords("dialHand", (ox,oy,x,y))
        self.after(1000, self.update_dial, randrange(0,255))

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

