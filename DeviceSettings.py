from Tkinter import *
import ttk
import tkSimpleDialog

class DeviceSettings(tkSimpleDialog.Dialog):

    def body(self, master):

        Label(master, text="Port Name:").grid(row=0)
        Label(master, text="Baud Rate:").grid(row=1)

        self.e1Var = StringVar()
        self.e1 = Entry(master, textvariable=self.e1Var)
        self.e1Var.set(u"/dev/ttyS1")
        self.b1 = ttk.Combobox(master)
        self.b1['values'] = ('9600', '38400', '57600', '115200')
        self.b1.current(0)

        self.e1.grid(row=0, column=1)
        self.b1.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        self.portname = self.e1.get()
        self.baudrate = self.b1.get()
        #print first, second # or something
