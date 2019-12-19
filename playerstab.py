import tkinter as tk
from tkinter import ttk
from tab import Tab
import random

class PlayersTab(Tab):
    players = list()
    with open("data\\names.txt") as f:
        for line in f:
            players.append(line.rstrip('\n'))

    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.playersAmount = len(self.players)
        self.playersLists = []
        self.isShuffled = False
        self.startButton = tk.Button(self, text="shuffle", command=self.shuffle)
        self.startButton.grid(row=7, column=4, ipady=10, ipadx=15, padx=20)


    def shuffle(self):
        random.shuffle(self.players)
        tables = 4
        tmp = divmod(len(self.players), tables)
        while tables > 0 and tmp[0] < 6:
            tables -= 1
            tmp = divmod(len(self.players), tables)

        if tables < 1:
            tables = 1

        if tmp[0] > 10:
            tables += 1

        tmp = divmod(len(self.players), tables)

        sizes = []
        for i in range(tables):
            sizes.insert(i, tmp[0])

        i = 0
        remainder = tmp[1]
        while remainder > 0:
            sizes[i] += 1
            remainder -= 1
            i = (i + 1) % tables


        i = 0
        j = 0
        t = 0
        tablesList = []
        for k in sizes:
            playersList = []
            for i in range(k):
                playersList.insert(i, self.players[j])
                j  += 1
            tablesList.insert(t, playersList)
            t += 1

        self.playersLists = tablesList
        self.isShuffled = True


