import tkinter as tk
from tkinter import ttk

class Table(tk.Canvas):
    def __init__(self, parent, x, y, width, height, number):
        tk.Canvas.__init__(self, parent)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.configure(width=width, height=height)
        self.create_oval(x, y, width, height)


    def resize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.configure(width=width, height=height)
        self.create_oval(x, y, width, height)