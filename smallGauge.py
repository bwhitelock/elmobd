#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter as tk
from math import cos,sin,pi
import sys, time

class smallGauge(Frame):
    def __init__(self,master=None,size=200):
        Frame.__init__(self,master)
        self.size=size

        self.pack(fill=BOTH)
        #self.Canvas = tk.Canvas(self, width=size, height=size, bg="#456", relief= "sunken", border=10)
        self.Canvas = tk.Canvas(self, width=size, height=size, border=2)
        self.Canvas.pack()

        self.Canvas.create_oval(6,6,size,size, fill="blue", width=4)
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=270,extent=90,style="arc",width=4)
        self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=-45,extent=270,style="arc",width=4)
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=180,extent=90,style="arc",width=4)
        #self.Canvas.create_arc(6+6,6+6,size-6,size-6,start=90,extent=90,style="arc",width=4)
        self.Canvas.create_line(0,0,0,0, fill="#ffc", tags="hour")
        self.Canvas.create_line(0,0,0,0, fill="red", tags="minute")
        self.Canvas.create_line(0,0,0,0, fill="black", tags="second")

        #self.Canvas.create_text((size*0.6),17,text="45")
        #self.Canvas.create_text((size*0.6),(size),text="46")
        self.Canvas.create_text((size/2),17,text="45")
        self.Canvas.create_text((size/2),(size),text="46")
        #uzr1 = tk.Label(self, text="12", bg="#456" )
        #uzr1.place(x=(size/2), y=13)
        #uzr2 = tk.Label(self, text="6", bg="#456" )
        #uzr2.place(x=160, y=303)
        #uzr3 = tk.Label(self, text="3", bg="#456" )
        #uzr3.place(x=310, y=160)
        #uzr4 = tk.Label(self, text="9", bg="#456" )
        #uzr4.place(x=11, y=160)

        self.update_clock()

    def update_clock(self):

        s=time.localtime()[5]
        m=time.localtime()[4]
        h=time.localtime()[3]

        degrees = 6*s
        angle = degrees*pi*2/360
        #ox = self.size*0.55
        #ox = self.size/2
        ox = (self.size+6)/2
        #oy = self.size*0.55
        #oy = self.size/2
        oy = (self.size+6)/2
        #oy = self.size
        #x = ox + self.size*sin(angle)*0.45
        #y = oy - self.size*cos(angle)*0.45
        x = ox + self.size*sin(angle)*0.3
        y = oy - self.size*cos(angle)*0.3
        self.Canvas.coords("hour", (ox,oy,x,y))

        degrees1 = 6*m
        angle1 = degrees1*pi*2/360
        #ox1 = 165
        #oy1 = 165
        ox1 = (self.size+6)/2
        oy1 = (self.size+6)/2
        #x1 = ox1 + self.size*sin(angle1)*0.4
        #y1 = oy1 - self.size*cos(angle1)*0.4
        x1 = ox1 + self.size*sin(angle1)*0.3
        y1 = oy1 - self.size*cos(angle1)*0.3
        self.Canvas.coords("minute", (ox1,oy1,x1,y1))

        degrees2 = 30*h
        angle2 = degrees2*pi*2/360
        #ox2 = 165
        #oy2 = 165
        ox2 = (self.size+6)/2
        oy2 = (self.size+6)/2
        x2 = ox2 + self.size*sin(angle2)*0.2
        y2 = oy2 - self.size*cos(angle2)*0.2
        self.Canvas.coords("second",(ox2,oy2,x2,y2))

        self.after(1000, self.update_clock)

