import tkinter as tk
from tkinter import ttk
from tab import Tab

class TimerTab(Tab):
    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.label = ttk.Label(self, text="Timer").grid(row=0)
