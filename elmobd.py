#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Tkinter import *
from ttk import *
#from PIL import Image, ImageTk
from console import console
from settings import settings
from general import general
from dashboard import dashboard
from MenuBar import MenuBar
from myToolBar import ToolBar

class elmodb(Tkinter.Tk):
    def __init__(self,device=None):
        Tkinter.Tk.__init__(self)
        self.initialize()

    def initialize(self):
        master = Frame(name='master')
        master.pack(fill=BOTH,expand=True)

        self.menubar = MenuBar(self)
        self.config(menu=self.menubar)

        self.toolbar = ToolBar(self, master)
        
        self.notebook = Notebook(master, name='nb')
        self.notebook.pack(fill=BOTH,expand=True)

        self.general = general(self.notebook, name='general')
        self.notebook.add(self.general, text="General")

        self.console = console(self.notebook, name='console')
        self.notebook.add(self.console, text="Console")
        self.notebook.tab(self.console,state='disabled')
        self.notebook.hide(self.console)

        self.settings = settings(self, name='settings')
        self.notebook.add(self.settings, text="Settings")
        self.notebook.hide(self.settings)

        self.dashboard = dashboard(self.notebook, name='dashboard')
        self.notebook.add(self.dashboard, text="Dashboard")
        self.notebook.hide(self.dashboard)

        self.resizable(True,True)
        self.after(500,self.doCommand)
        #self.update()


    def doCommand(self):
        self.after(500,self.doCommand)

if __name__ == '__main__':
    app = elmodb(None)
    app.title('ELM327 OBD Interface')
    app.geometry("300x300")
    app.mainloop()
