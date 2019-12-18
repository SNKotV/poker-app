import tkinter as tk
from tkinter import ttk
from tab import Tab

class TimerTab(Tab):
    def __init__(self, parent):
        Tab.__init__(self, parent)
        self.label = ttk.Label(self, text="Label")
        self.label.pack()