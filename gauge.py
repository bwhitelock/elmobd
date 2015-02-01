#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter as tk
from math import cos,sin,pi
import sys, time

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
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=270,extent=90,style="arc",width=4)
        adjust = size*.25
        self.Canvas.create_arc(5+adjust,5+adjust,self.circleSize-adjust,self.circleSize-adjust,start=-45,extent=270,style="arc",width=4)
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=180,extent=90,style="arc",width=4)
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=90,extent=90,style="arc",width=4)
        self.Canvas.create_line(0,0,0,0, fill="#ffc", tags="hour")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="minute")
        self.Canvas.create_line(0,0,0,0, fill="black", tags="second")
        #self.makeLine(360,"80")
        #self.makeLine(225,"0")
        #self.makeLine(52,"180")

        listValues = [0,20,40,60,80,100,120,140,160,180,200,220,240,260]
        for speed in listValues:
            degrees = round((speed/130.0*135.0+225.0) - 360.0*(1 if speed > 130.0 else 0))
            print "speed %s degrees %s" % (speed,degrees)
            self.makeLine(degrees,str(speed))
        #print listValues
        #testValue=80.0
        #myValue = (testValue/130*135+225)
        #print "myValue:", str(myValue)
        #print "test",(1 if testValue > 130 else 0)
        #myValue = myValue - 360*(1 if testValue > 130 else 0)
        #print "less than 130:", str(myValue)
        #testValue=180.0
        #print "testValue/130:", str(testValue/130)
        #myValue = (testValue/130.0*135.0+225.0)
        #print "myValue:", str(myValue)
        #print "test",(1 if testValue > 130 else 0)
        #myValue = myValue - 360*(1 if testValue > 130 else 0)
        #print "more than 130:", round(myValue)

        #self.Canvas.create_text((size*0.6),17,text="45")
        #self.Canvas.create_text((size*0.6),(size),text="46")
        #self.Canvas.create_text((size/2),(size),text="46")
        #uzr1 = tk.Label(self, text="12", bg="#456" )
        #uzr1.place(x=(size/2), y=13)
        #uzr2 = tk.Label(self, text="6", bg="#456" )
        #uzr2.place(x=160, y=303)
        #uzr3 = tk.Label(self, text="3", bg="#456" )
        #uzr3.place(x=310, y=160)
        #uzr4 = tk.Label(self, text="9", bg="#456" )
        #uzr4.place(x=11, y=160)

        self.update_clock()

    def makeLine(self,degrees,value):
        angle = degrees*pi*2/360
        #ox = (self.size+6)/2 + self.size*sin(angle)*.3
        #oy = (self.size+6)/2 - self.size*cos(angle)*.3
        ox = (self.circleSize)/2 + self.circleSize*sin(angle)*.3
        oy = (self.circleSize)/2 - self.circleSize*cos(angle)*.3
        x1 = ox + self.circleSize*sin(angle)*.090
        y1 = oy - self.circleSize*cos(angle)*.090
        x2 = ox + self.circleSize*sin(angle)*.13
        y2 = oy - self.circleSize*cos(angle)*.13
        self.Canvas.create_line(ox,oy,x1,y1, fill="black")
        self.Canvas.create_text(x2,y2,text=value)

    def update_clock(self):

        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        degrees = 6*s
        angle = degrees*pi*2/360
        #ox = self.size*0.55
        #ox = self.size/2
        ox = (self.circleSize)/2
        #oy = self.size*0.55
        #oy = self.size/2
        oy = (self.circleSize)/2
        #oy = self.size
        #x = ox + self.size*sin(angle)*0.45
        #y = oy - self.size*cos(angle)*0.45
        x = ox + self.circleSize*sin(angle)*0.3
        y = oy - self.circleSize*cos(angle)*0.3
        self.Canvas.coords("hour", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        #ox1 = 165
        #oy1 = 165
        ox1 = (self.circleSize)/2
        oy1 = (self.circleSize)/2
        #x1 = ox1 + self.size*sin(angle1)*0.4
        #y1 = oy1 - self.size*cos(angle1)*0.4
        x1 = ox1 + self.circleSize*sin(angle1)*0.3
        y1 = oy1 - self.circleSize*cos(angle1)*0.3
        self.Canvas.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        #ox2 = 165
        #oy2 = 165
        ox2 = (self.circleSize)/2
        oy2 = (self.circleSize)/2
        x2 = ox2 + self.circleSize*sin(angle2)*0.2
        y2 = oy2 - self.circleSize*cos(angle2)*0.2
        self.Canvas.coords("second",(ox2,oy2,x2,y2))

        self.after(1000, self.update_clock)

