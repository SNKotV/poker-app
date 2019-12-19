import tkinter as tk
from tkinter import messagebox
from tab import Tab

class TimerTab(Tab):

    levels = list()
    with open("data\levels.txt") as f:
        for line in f:
            levels.append(line.rstrip('\n'))

    topFont = ("Times New Roman", 36)
    midFont = ("Times New Roman", 54)
    botFont = ("Times New Roman", 24)

    def __init__(self, parent, width, height):
        Tab.__init__(self, parent, width, height)

        self.width = width
        self.height = height

        self.currentLevel = 0
        self.maxLevel = len(self.levels)


        self.timerTitle = tk.Label(self, text="Timer", font=self.topFont)
        self.timerTitle.grid(row=1, column=2, columnspan=4, ipady=40)
        self.timer = tk.Label(self, text="0 : 0", font=self.topFont, borderwidth=2, relief="groove")
        self.timer.grid(row=3, column=2, columnspan=4, ipady=10, ipadx=10)
        self.level = tk.Label(self, text=self.levels[self.currentLevel], font=self.midFont, width=30)
        self.level.grid(row=5, column=0, rowspan=1, columnspan=9, pady=180)

        self.minLbl = tk.Label(self, text="Min: ", font=self.botFont, padx=20)
        self.minLbl.grid(row=7, column=0, ipady=40, ipadx = 10)
        self.minTbox = tk.Entry(self, font=self.botFont, width="5")
        self.minTbox.grid(row=7, column=1, ipady=10, ipadx = 5)
        self.secLbl = tk.Label(self, text="Sec: ", font=self.botFont, padx=20)
        self.secLbl.grid(row=7, column=2, ipady=40, ipadx = 10)
        self.secTbox = tk.Entry(self, font=self.botFont, width="5")
        self.secTbox.grid(row=7, column=3, ipady=10, ipadx = 5)

        self.startButton = tk.Button(self, text="Start", font=self.botFont, command=self.start)
        self.startButton.grid(row=7, column=4, ipady=10, ipadx = 15, padx = 20)
        self.stopButton = tk.Button(self, text="Stop", font=self.botFont, command=self.stop, state="disabled")
        self.stopButton.grid(row=7, column=5, ipady=10, ipadx = 15, padx = 20)
        self.resetButton = tk.Button(self, text="Reset", font=self.botFont, command=self.reset, state="disabled")
        self.resetButton.grid(row=7, column=6, ipady=10, ipadx = 15, padx = 20)


    def start(self):
        if not self.minTbox.get():
            messagebox.showerror("Error", "Minutes field is empty")
            return
        if not self.secTbox.get():
            messagebox.showerror("Error", "Seconds field is empty")
            return
        min = self.minTbox.get()
        if not str(min).isdigit():
            messagebox.showerror("Error", "Minutes field has invalid value")
            return
        sec = self.secTbox.get()
        if not str(sec).isdigit():
            messagebox.showerror("Error", "Seconds field has invalid value")
            return
        self.iniTime = int(min) * 60 + int(sec)
        self.time = self.iniTime
        self.startButton.configure(state="disabled")
        self.minTbox.configure(state="disabled")
        self.secTbox.configure(state="disabled")
        self.stopButton.configure(state="active")
        self.stopped = False
        self.runTimer(self.time)

    def stop(self):
        self.stopped = True
        self.stopButton.configure(state="disabled")
        self.resetButton.configure(state="active")

    def reset(self):
        self.currentLevel = 0
        self.level.configure(text=self.levels[self.currentLevel])
        self.timer.configure(text="0 : 0")
        self.startButton.configure(state="active")
        self.minTbox.configure(state="normal")
        self.secTbox.configure(state="normal")
        self.resetButton.configure(state="disabled")

    def runTimer(self, time=None):
        if self.stopped:
            return
        if time is not None:
            self.time = time
        if self.time <= 0:
            if self.currentLevel < self.maxLevel - 1:
                self.currentLevel = self.currentLevel + 1
                self.level.configure(text=self.levels[self.currentLevel])
                self.time = self.iniTime
                self.runTimer(self.time)
            else:
                self.timer.configure(text="0 : 0")
        else:
            self.timer.configure(text="%d : %d" % (self.time / 60, self.time % 60))
            self.time = self.time - 1
            self.after(1000, self.runTimer)