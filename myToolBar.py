from Tkinter import *

class ToolBar(Frame):
    def __init__(self, parent, master):
        Frame.__init__(self, parent)

        self.parent = parent

        toolbar = Frame(master, relief=RIDGE)

        #engineImg = Image.open("images/engine2.png")
        #eimg = ImageTk.PhotoImage(engineImg)  
        generalFrame = Frame(toolbar, relief=RAISED)
        generalImg = PhotoImage(file="images/engine2.png")
        self.generalButton = Button(generalFrame, image=generalImg, command=self.onEngine, state=ACTIVE)
        self.generalButton.image = generalImg
        #engineButton.pack(side=LEFT, padx=2, pady=2)
        #engineButton.config(relief=SUNKEN)
        self.generalButton.pack(padx=2, pady=2)
        generalLabel = Label(generalFrame, text="Summary")
        generalLabel.pack(padx=2,pady=2)
        generalFrame.pack(side=LEFT, padx=2, pady=2)

        settingsFrame = Frame(toolbar, relief=GROOVE)
        #settingsImg = Image.open("images/settings.png")
        #simg = ImageTk.PhotoImage(settingsImg)  
        settingsImg = PhotoImage(file="images/settings.png")
        self.settingsButton = Button(settingsFrame, image=settingsImg, command=self.onSettings)
        self.settingsButton.image = settingsImg
        #settingsButton.pack(side=LEFT, padx=2, pady=2)
        self.settingsButton.pack(padx=2, pady=2)
        settingsLabel = Label(settingsFrame, text="Settings")
        settingsLabel.pack(padx=2,pady=2)
        settingsFrame.pack(side=LEFT, padx=2, pady=2)

        dashboardFrame = Frame(toolbar, relief=SUNKEN)
        #dashboardImg = Image.open("images/car_dashboard.png")
        #dimg = ImageTk.PhotoImage(dashboardImg)  
        #dashboardImg = PhotoImage(file="images/car_dashboard.png")
        dashboardImg = PhotoImage(file="images/gauge.png")
        self.dashboardButton = Button(dashboardFrame, image=dashboardImg, command=self.onDashboard)
        self.dashboardButton.image = dashboardImg
        #dashboardButton.pack(side=LEFT, padx=2, pady=2)
        self.dashboardButton.pack(padx=2, pady=2)
        dashboardLabel = Label(dashboardFrame, text="Dashboard")
        dashboardLabel.pack(padx=2,pady=2)
        dashboardFrame.pack(side=LEFT, padx=2, pady=2)

        carFrame = Frame(toolbar, relief=RIDGE)
        #carImg = Image.open("images/car_40.png")
        #cimg = ImageTk.PhotoImage(carImg)  
        carImg = PhotoImage(file="images/car_40.png")
        self.carButton = Button(carFrame, image=carImg, command=self.onCar)
        self.carButton.image = carImg
        self.carButton.config(state=DISABLED)
        #carButton.pack(side=LEFT, padx=2, pady=2)
        self.carButton.pack(padx=2, pady=2)
        carLabel = Label(carFrame, text="Troubleshoot")
        carLabel.pack(padx=2,pady=2)
        carFrame.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X, padx=2, pady=2)

    def onEngine(self):
        #self.parent.notebook.tab(self.parent.notebook.select(),state='hidden')
        if not (str(self.parent.notebook.select()) == str(self.parent.generalTab)):
            self.parent.notebook.hide(self.parent.notebook.select())
            self.parent.notebook.add(self.parent.generalTab)
            self.parent.notebook.select(self.parent.generalTab)
            #self.parent.notebook.tab(self.engineTab,state='normal')
        self.generalButton.config(state=ACTIVE)
        #self.settingsButton.config(state=NORMAL)
        #self.dashboardButton.config(state=NORMAL)
        #self.carButton.config(state=NORMAL)

    def onSettings(self):
        #self.parent.notebook.tab(self.parent.notebook.select(),state='hidden')
        if not (str(self.parent.notebook.select()) == str(self.parent.testTab2)):
            self.parent.notebook.hide(self.parent.notebook.select())
            self.parent.notebook.add(self.parent.testTab2)
            self.parent.notebook.select(self.parent.testTab2)
            #self.parent.notebook.tab(self.engineTab,state='normal')
        self.settingsButton.config(state=ACTIVE)
        #self.engineButton.config(state=NORMAL)
        #self.dashboardButton.config(state=NORMAL)
        #self.carButton.config(state=NORMAL)

    def onDashboard(self):
        #self.parent.notebook.tab(self.parent.notebook.select(),state='hidden')
        if not (str(self.parent.notebook.select()) == str(self.parent.dashboard)):
            self.parent.notebook.hide(self.parent.notebook.select())
            self.parent.notebook.add(self.parent.dashboard)
            self.parent.notebook.select(self.parent.dashboard)
            #self.parent.notebook.tab(self.engineTab,state='normal')
        self.dashboardButton.config(state=ACTIVE)
        #self.engineButton.config(state=NORMAL)
        #self.settingsButton.config(state=NORMAL)
        #self.carButton.config(state=NORMAL)

    def onCar(self):
        #self.parent.notebook.tab(self.parent.notebook.select(),state='hidden')
        if not (str(self.parent.notebook.select()) == str(self.parent.console)):
            self.parent.notebook.hide(self.parent.notebook.select())
            self.parent.notebook.add(self.parent.console)
            self.parent.notebook.select(self.parent.console)
            #self.parent.notebook.tab(self.engineTab,state='normal')
        self.carButton.config(state=ACTIVE)
        #self.engineButton.config(state=NORMAL)
        #self.settingsButton.config(state=NORMAL)
        #self.dashboardButton.config(state=NORMAL)
