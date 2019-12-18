import tkinter as tk
from tkinter import ttk
import math


class Table(tk.Canvas):
    def __init__(self, parent, width, height, number):
        tk.Canvas.__init__(self, parent)
        self.width = width
        self.height = height
        self.number = number
        self.seatSize = self.width / 10
        self.gap = 10
        self.players = []
        self.activeSeats = 0
        self.configure(width=width, height=height)
        self.create_oval(self.seatSize + self.gap, self.seatSize + self.gap,
                         self.width - self.seatSize - self.gap, self.height - self.seatSize - self.gap, fill="green")

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.seatSize = self.width / 10
        self.gap = 20

        self.configure(width=self.width, height=self.height, bd=1, bg="black")
        self.create_oval(self.seatSize + self.gap, self.seatSize + self.gap,
                         self.width - self.seatSize - self.gap, self.height - self.seatSize - self.gap, fill="green")

        center = (self.width / 2, self.height / 2)
        lenght = center[0] - self.seatSize
        angle = math.acos(-1) / 5

        i = 0
        while i <= self.activeSeats:
            x = int(center[0] + lenght * math.cos(angle * i) - self.seatSize / 2)
            y = int(center[1] + lenght * math.sin(angle * i) - self.seatSize / 2)
            self.create_oval(x, y, x + self.seatSize, y + self.seatSize, fill="red")
            i += 1

        while i <= 10:
            x = int(center[0] + lenght * math.cos(angle * i) - self.seatSize / 2)
            y = int(center[1] + lenght * math.sin(angle * i) - self.seatSize / 2)
            self.create_oval(x, y, x + self.seatSize, y + self.seatSize, fill="green")
            i += 1

    def setPlayers(self, players):
        self.players = players
        self.activeSeats = len(self.players)