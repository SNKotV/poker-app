import tkinter as tk
from tkinter import font
from tkinter import ttk
from tab import Tab
from table import Table


class TablesTab(Tab):
    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)
        self.width = width
        self.height = height
        self.padding = 10
        self.tableWidth = self.width / 3
        self.tableHeight = self.height / 2
        self.playersTab = None
        self.columnconfigure(3, minsize=self.tableWidth)
        self.tables = [Table(self, self.tableWidth, self.tableHeight, 1),
                       Table(self, self.tableWidth, self.tableHeight, 2),
                       Table(self, self.tableWidth, self.tableHeight, 3),
                       Table(self, self.tableWidth, self.tableHeight, 4)]
        self.tables[0].grid(row=0, column=0)
        self.tables[1].grid(row=0, column=1)
        self.tables[2].grid(row=1, column=0)
        self.tables[3].grid(row=1, column=1)

        self.tableView = ttk.Frame(self)
        self.textFont = font.Font(size=32)
        self.label = tk.Label(self.tableView, text="Table #:", font=self.textFont)
        self.label.grid(row=0, column=0)
        self.tableNumber = tk.Label(self.tableView)
        self.listHeight = int(self.height / 18)
        self.listWidth = int(self.width / 18)
        self.playerList = tk.Listbox(self.tableView, width=self.listWidth, height=self.listHeight, activestyle="none")
        self.playerList.grid(row=1, column=0)
        self.tableView.grid(row=0, column=2, rowspan=2, columnspan=2)

    def connectToPlayersTab(self, playersTab):
        self.playersTab = playersTab

    def shuffle(self):
        if self.playersTab == None:
            return

        if self.playersTab.isShuffled:
            self.setPlayers(self.playersTab.playersLists)
            self.playersTab.isShuffled = False

    def contentUpdate(self):
        self.clearTab()
        self.shuffle()
        self.viewTable()
        self.tables[0].update(self.tableWidth, self.tableHeight)
        self.tables[1].update(self.tableWidth, self.tableHeight)
        self.tables[2].update(self.tableWidth, self.tableHeight)
        self.tables[3].update(self.tableWidth, self.tableHeight)
        self.listHeight = int(self.height / 18)
        self.listWidth = int(self.width / 18)
        self.playerList.configure(width=self.listWidth, height=self.listHeight)

    def clearTab(self):
        for i in range(0, 4):
            self.tables[i].delete("all")

    def viewTable(self):
        index = -1
        for table in self.tables:
            if table.isClicked:
                i = 0
                self.playerList.delete(0, tk.END)
                self.label.configure(text="Table #: " + str(table.number))
                for player in table.players:
                    self.playerList.insert(i, str(i + 1) + ". " + player)
                    i += 1
                table.isClicked = False

    def setPlayers(self, playerLists):
        i = 0
        for players in playerLists:
            self.tables[i].setPlayers(players)
            i += 1
