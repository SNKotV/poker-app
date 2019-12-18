import tkinter as tk
from tkinter import ttk

class Tab(ttk.Frame):
    def __init__(self, parent, width, height):
        ttk.Frame.__init__(self, parent)
        self.width = width
        self.height = height

    def resize(self, width, height):
        if self.width == width and self.height == height:
            print("ok")
            return
        self.width = width
        self.height = height
        self.contentResize()

    def contentResize(self):
        """"""