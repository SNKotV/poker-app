import tkinter as tk
from tkinter import ttk
from tab import Tab
from timertab import TimerTab
from playerstab import PlayersTab
from tablestab import TablesTab

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.name = "Poker Application"
        self.title(self.name)
        self.width = 1200
        self.height = 800
        self.minsize(width=self.width, height=self.height)
        self.resizable(False, False)

        self.tabControl = ttk.Notebook(self)

        self.tabs = [TimerTab(self.tabControl, self.width, self.height),
                     PlayersTab(self.tabControl, self.width, self.height),
                     TablesTab(self.tabControl, self.width, self.height)]

        # self.tabControl.add(self.tabs[0], text="Timer")
        # self.tabControl.add(self.tabs[1], text="Players")
        self.tabControl.add(self.tabs[2], text="Tables")

        self.tabControl.pack(expand=True, fill="both")

    def run(self):
        self.after(1000, self.update())
        self.mainloop()

    def update(self):
        for tab in self.tabs:
            tab.update()


if __name__  == "__main__":
    app = Application()
    app.run()
