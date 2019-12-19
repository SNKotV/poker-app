import tkinter as tk
from tkinter import ttk
from tab import Tab
from tkinter import messagebox
import random


class PlayersTab(Tab):
    players = list()
    with open("data\\names.txt") as f:
        for line in f:
            players.append(line.rstrip('\n'))

    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.width = width
        self.height = height
        self.playersAmount = len(self.players)
        self.playersLists = []
        self.isShuffled = False

        self.listOfPlayers = tk.Listbox(self, font="Times 16", height=int(self.height / 24), width=int(self.width/20), activestyle="none")
        for i in range(len(self.players)):
            self.listOfPlayers.insert(i, self.players[i])
        self.listOfPlayers.grid(row=0, column=0)

        self.panel = ttk.Frame(self)

        self.adding = ttk.Frame(self.panel)
        self.addLabel = tk.Label(self.adding, text="Player name:", font="Times 16")
        self.addLabel.grid(row=0, column=0, padx=20)
        self.addField = tk.Entry(self.adding, font="Times 16")
        self.addField.grid(row=0, column=1)
        self.addButton = tk.Button(self.adding, text="Add",  font="Times 16", command=self.addPlayer)
        self.addButton.grid(row=1, column=0, ipadx=15)
        self.adding.grid(row=0, column=0, pady= 150)

        self.removing = ttk.Frame(self.panel)
        self.removeLabel = tk.Label(self.removing, text="Player name:", font="Times 16")
        self.removeLabel.grid(row=0, column=0, padx=20)
        self.removeField = tk.Entry(self.removing, font="Times 16")
        self.removeField.grid(row=0, column=1)
        self.removeButton = tk.Button(self.removing, text="Remove", font="Times 16", command=self.removePlayer)
        self.removeButton.grid(row=1, column=0)
        self.removing.grid(row=2, column=0, pady= 150)


        self.shuffleButton = tk.Button(self.panel, text="Shuffle", font="Times 16", command=self.shuffle)
        self.shuffleButton.grid(row=4, column=3, ipady=10, ipadx=25, padx=20)


        self.panel.grid(row=0, column=1, rowspan = 2, columnspan=3)

    def addPlayer(self):
        if not self.addField.get():
            return
        name = self.addField.get()
        self.players.append(name)
        self.listOfPlayers.insert(tk.END, name)
        with open('data\\names.txt', 'a') as f:
            f.write(name + "\n")

    def removePlayer(self):
        name = self.removeField.get()
        if not name in self.players:
            return
        self.players.remove(name)
        idx = self.listOfPlayers.get(0, tk.END).index(name)
        self.listOfPlayers.delete(idx)

    def shuffle(self):
        if len(self.players) > 40:
            messagebox.showerror("Error", "Too many players")
            return

        if len(self.players) < 6:
            messagebox.showerror("Error", "Not enough players")
            return

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
                j += 1
            tablesList.insert(t, playersList)
            t += 1

        self.playersLists = tablesList
        self.isShuffled = True
