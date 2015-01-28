import Tkinter
import tkMessageBox
import sys
from DeviceSettings import DeviceSettings

class MenuBar(Tkinter.Menu):
    def __init__(self, parent):
        Tkinter.Menu.__init__(self, parent)

        self.parent=parent

        self.fileMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=self.fileMenu)
        self.fileMenu.add_command(label="Exit", underline=1, command=self.quit)

        self.deviceMenu = Tkinter.Menu(self, tearoff=False)
        self.add_cascade(label="Device",underline=0, menu=self.deviceMenu)
        self.deviceMenu.add_command(label="Test", underline=1, command=self.onTest)
        self.deviceMenu.add_separator()
        self.deviceMenu.add_command(label="Clear", underline=1, command=self.onClear)
        self.deviceMenu.entryconfig("Clear", state="disabled")

    def onTest(self):
        d = DeviceSettings(self.parent)
        print d.result

    def onClear(self):
        if tkMessageBox.askyesno("Clear", "Clear DTC data?"):
            print "clear"
        else:
            print "cancel clear"

    def quit(self):
        sys.exit(0)
