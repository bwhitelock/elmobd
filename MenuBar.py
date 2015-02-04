import Tkinter
import tkMessageBox
import sys, os
from DeviceSettings import DeviceSettings
import serial
from obdDevice import device

class MenuBar(Tkinter.Menu):
    def __init__(self, parent):
        Tkinter.Menu.__init__(self, parent)

        self.parent=parent

        self.fileMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=self.fileMenu)
        self.fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        self.deviceMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="Device",underline=0, menu=self.deviceMenu)
        self.deviceMenu.add_command(label="Settings", underline=1, command=self.onSettings)
        self.deviceMenu.add_separator()
        self.deviceMenu.add_command(label="Connect", underline=1, command=self.onConnect)
        self.deviceMenu.add_command(label="Clear", underline=1, command=self.onClear)
        self.deviceMenu.entryconfig("Clear", state="disabled")

    def onSettings(self):
        d = DeviceSettings(self.parent)
        device.portname=d.portname
        device.baudrate=d.baudrate
        #print d.result
        print "portname",device.portname
        print "baudrate",device.baudrate

    def onClear(self):
        if tkMessageBox.askyesno("Clear", "Clear DTC data?"):
            print "clear"
        else:
            print "cancel clear"

    def onConnect(self, portname=None):
        if portname:
            device.portname = portname
        if not device.portname:
            print "OpenPortFailed"

        try:
            device.port = serial.Serial(device.portname, device.baudrate,
                                  serial.EIGHTBITS,
                                  serial.PARITY_NONE,
                                  serial.STOPBITS_ONE,
                                  timeout = 1)
            #device.port = serial.Serial(device.portname, device.baudrate)
            print "self._port", device.port
            print "port is open",device.port.isOpen()
            self.parent.event_generate("<<test1>>") 
            self.parent.event_generate("<<test2>>") 
        except serial.SerialException:
            print "serial exception"

    def quit(self):
        sys.exit(0)
