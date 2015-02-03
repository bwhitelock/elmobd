import Tkinter
import tkMessageBox
import sys
from DeviceSettings import DeviceSettings
import serial

class OBDError(Exception):
    """Base class for exceptions in this module"""

class OBDPortError(OBDError):
    """Exception to indicate that there was an error with the port"""

class OBDDataError(OBDError):
    """Exception to indicate a data error"""

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
        self.portname=d.portname
        self.baudrate=d.baudrate
        #print d.result
        print "portname",self.portname
        print "baudrate",self.baudrate

    def onClear(self):
        if tkMessageBox.askyesno("Clear", "Clear DTC data?"):
            print "clear"
        else:
            print "cancel clear"

    def onConnect(self, portname=None):
        if portname:
            self.portname = portname
        if not self.portname:
            print "OpenPortFailed"

        try:
            self.port = serial.Serial(self.portname, self.baudrate,
                                  serial.EIGHTBITS,
                                  serial.PARITY_NONE,
                                  serial.STOPBITS_ONE,
                                  timeout = 1)
            print "self._port", self.port
            print "port is open",self.port.isOpen()
        except serial.SerialException:
            print "serial exception"

    def quit(self):
        sys.exit(0)
