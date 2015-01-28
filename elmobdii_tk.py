#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
from ttk import *
from PIL import Image, ImageTk
from console import console
from testTab2 import testTab2
from engineTab import engineTab
from tabTest import tabTest
from MenuBar import MenuBar

class elmodb(Tkinter.Tk):
    def __init__(self,device=None):
        Tkinter.Tk.__init__(self)
        self.initialize()

    def initialize(self):
        master = Frame(name='master')
        master.pack(fill=BOTH,expand=True)

        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)

        toolbar = Frame(master, relief=RAISED)

        engineImg = Image.open("images/engine2.png")
        eimg = ImageTk.PhotoImage(engineImg)  
        engineButton = Button(toolbar, image=eimg, command=self.onEngine)
        engineButton.image = eimg
        engineButton.pack(side=LEFT, padx=2, pady=2)

        settingsImg = Image.open("images/settings.png")
        simg = ImageTk.PhotoImage(settingsImg)  
        settingsButton = Button(toolbar, image=simg, command=self.onSettings)
        settingsButton.image = simg
        settingsButton.pack(side=LEFT, padx=2, pady=2)

        dashboardImg = Image.open("images/car_dashboard.png")
        dimg = ImageTk.PhotoImage(dashboardImg)  
        dashboardButton = Button(toolbar, image=dimg, command=self.onDashboard)
        dashboardButton.image = dimg
        dashboardButton.pack(side=LEFT, padx=2, pady=2)

        carImg = Image.open("images/car_40.png")
        cimg = ImageTk.PhotoImage(carImg)  
        carButton = Button(toolbar, image=cimg, command=self.onCar)
        carButton.image = cimg
        carButton.pack(side=LEFT, padx=2, pady=2)
       
        toolbar.pack(side=TOP, fill=X)
        
        self.notebook = Notebook(master, name='nb')
        self.notebook.pack(fill=BOTH,expand=True)

        self.engineTab = engineTab(self.notebook, name='engineTab')
        self.notebook.add(self.engineTab, text="Summary")

        self.console = console(self.notebook, name='console')
        self.notebook.add(self.console, text="Console")
        self.notebook.tab(self.console,state='disabled')
        self.notebook.hide(self.console)

        self.testTab2 = testTab2(self, name='secondTab')
        self.notebook.add(self.testTab2, text="This Tab 2")
        self.notebook.hide(self.testTab2)

        testImg = Image.open("images/icon_notebook.gif")
        testimg = ImageTk.PhotoImage(testImg)  
        #testImage = PhotoImage(file="icon_notebook.gif")
        self.tabTest = tabTest(self.notebook, name='tabTest')
        self.notebook.add(self.tabTest, text="tabTest", image=testimg)
        self.notebook.hide(self.tabTest)

        self.resizable(True,True)
        self.after(500,self.doCommand)
        #self.update()

    def onEngine(self):
        #self.notebook.tab(self.notebook.select(),state='hidden')
        print "selected",self.notebook.select()
        print "self.engine",self.engineTab
        if not (str(self.notebook.select()) == str(self.engineTab)):
            print "not the same tab"
            self.notebook.hide(self.notebook.select())
            self.notebook.add(self.engineTab)
            self.notebook.select(self.engineTab)
            #self.notebook.tab(self.engineTab,state='normal')
        else:
            print "the same tab"

    def onSettings(self):
        #self.notebook.tab(self.notebook.select(),state='hidden')
        print "selected",self.notebook.select()
        print "self.engine",self.testTab2
        if not (str(self.notebook.select()) == str(self.testTab2)):
            print "not the same tab"
            self.notebook.hide(self.notebook.select())
            self.notebook.add(self.testTab2)
            self.notebook.select(self.testTab2)
            #self.notebook.tab(self.engineTab,state='normal')
        else:
            print "the same tab"

    def onDashboard(self):
        #self.notebook.tab(self.notebook.select(),state='hidden')
        print "selected",self.notebook.select()
        print "self.engine",self.tabTest
        if not (str(self.notebook.select()) == str(self.tabTest)):
            print "not the same tab"
            self.notebook.hide(self.notebook.select())
            self.notebook.add(self.tabTest)
            self.notebook.select(self.tabTest)
            #self.notebook.tab(self.engineTab,state='normal')
        else:
            print "the same tab"

    def onCar(self):
        #self.notebook.tab(self.notebook.select(),state='hidden')
        print "selected",self.notebook.select()
        print "self.engine",self.console
        if not (str(self.notebook.select()) == str(self.console)):
            print "not the same tab"
            self.notebook.hide(self.notebook.select())
            self.notebook.add(self.console)
            self.notebook.select(self.console)
            #self.notebook.tab(self.engineTab,state='normal')
        else:
            print "the same tab"


    def doCommand(self):
        self.after(500,self.doCommand)

if __name__ == '__main__':
    app = elmodb(None)
    app.title('ELM327 OBD Interface')
    app.geometry("300x300")
    app.mainloop()
