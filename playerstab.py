import tkinter as tk
from tkinter import ttk
from tab import Tab

class PlayersTab(Tab):
    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.label = ttk.Label(self, text="Players")
        self.label.pack()