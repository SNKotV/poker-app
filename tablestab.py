import tkinter as tk
from tkinter import ttk
from tab import Tab
from table import Table

class TablesTab(Tab):
    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.width = width
        self.height = height
        self.padding = 10
        self.tableWidth = self.width / 3
        self.tableHeight = self.height / 2
        self.tables = [Table(self, self.tableWidth, self.tableHeight, 1),
                       Table(self, self.tableWidth, self.tableHeight, 2),
                       Table(self, self.tableWidth, self.tableHeight, 3),
                       Table(self, self.tableWidth,self.tableHeight, 4)]
        self.tables[0].grid(row=0, column=0)
        self.tables[1].grid(row=0, column=1)
        self.tables[2].grid(row=1, column=0)
        self.tables[3].grid(row=1, column=1)

    def contentResize(self):
        self.clearTab()
        self.tableWidth = self.width / 3
        self.tableHeight = self.height / 2 - self.padding
        self.tables[0].resize(self.tableWidth, self.tableHeight)
        self.tables[1].resize(self.tableWidth, self.tableHeight)
        self.tables[2].resize(self.tableWidth, self.tableHeight)
        self.tables[3].resize(self.tableWidth, self.tableHeight)

    def clearTab(self):
        for i in range(0, 4):
            self.tables[i].delete("all")