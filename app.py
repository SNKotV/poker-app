import tkinter as tk
from tkinter import ttk
from tab import Tab
from timertab import TimerTab

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.name = "Poker Application"
        self.title(self.name)
        self.width = 800
        self.height = 600
        self.geometry(str(self.width) + 'x' + str(self.height))

        self.tabControl = ttk.Notebook(self)

        self.timerTab = TimerTab(self.tabControl)
        self.playersTab = Tab(self.tabControl)
        self.tablesTab = Tab(self.tabControl)

        self.tabControl.add(self.timerTab, text="Timer")
        self.tabControl.add(self.playersTab, text="Players")
        self.tabControl.add(self.tablesTab, text="Tables")

        self.tabControl.pack(expand=1, fill="both")


    def run(self):
       self.mainloop()


if __name__  == "__main__":
    app = Application()
    app.run()
