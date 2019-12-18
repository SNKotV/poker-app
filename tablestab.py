import tkinter as tk
from tkinter import ttk
from tab import Tab
from table import Table

class TablesTab(Tab):
    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.width = width
        self.height = height
        self.bind('<Configure>', self.resize)
        self.tables = [Table(self, 0, 0, self.width / 4, self.height / 4, 1),
                       Table(self, self.width / 4, 0, self.width / 2, self.height / 4, 2),
                       Table(self, 0, self.height / 4, self.width / 4, self.height / 2, 3),
                       Table(self, self.width / 4, self.height / 4, self.width / 2, self.height / 2, 4)]
        self.tables[0].grid(row=0, column=0)
        self.tables[1].grid(row=0, column=1)
        self.tables[2].grid(row=1, column=0)
        self.tables[3].grid(row=1, column=1)

    def resize(self, event):
        self.width = event.width
        self.height = event.height
        self.contentResize()

    def contentResize(self):
        self.clearTab()
        self.tables[0].resize(0, 0, self.width / 4, self.height / 4)
        self.tables[1].resize(self.width / 4, 0, self.width / 2, self.height / 4)
        self.tables[2].resize(0, self.height / 4, self.width / 4, self.height / 2)
        self.tables[3].resize(self.width / 4, self.height / 4, self.width / 2, self.height / 2)

    def clearTab(self):
        for i in range(0, 4):
            self.tables[i].delete("all")