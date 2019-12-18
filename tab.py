import tkinter as tk
from tkinter import ttk

class Tab(ttk.Frame):
    def __init__(self, parent, width, height):
        ttk.Frame.__init__(self, parent)
        self.width = width
        self.height = height

    def update(self):
        self.contentUpdate()

    def contentUpdate(self):
        """"""