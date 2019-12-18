import tkinter as tk
from tkinter import ttk

class Tab(ttk.Frame):
    def __init__(self, parent, width, height):
        ttk.Frame.__init__(self, parent)
        self.width = width
        self.height = height
        self.bind('<Configure>', self.resize)

    def resize(self, event):
        self.width = event.width
        self.height = event.height
        self.contentResize()

    def contentResize(self):
        """"""