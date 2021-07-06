from randomizer.orb import OrbRandomizer
import tkinter as tk
from tkinter.constants import VERTICAL
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = 'Orbment Line'

        self.enabled = tk.IntVar(value=1)
        self.cbtnEnabled = ttk.Checkbutton(self, text='Enable Orbment Line Randomizer', variable=self.enabled)
        self.cbtnEnabled.grid(column=0, row=0, padx=5, pady=5, sticky='w')

        self.excludeGuess = tk.IntVar(value=0)
        self.cbtnEnabled = ttk.Checkbutton(self, text='Exclude Guess Characters', variable=self.excludeGuess)
        self.cbtnEnabled.grid(column=0, row=1, padx=20, pady=5, sticky='w')

        self.maxLine = tk.IntVar(value=3)
        ttk.Label(self, text='Max number of lines (1-7)').grid(column=0, row=2, padx=5, pady=5, sticky='w')
        self.spinMaxLine = ttk.Spinbox(self, from_=1, to=7, increment=1, textvariable=self.maxLine, width=10)
        self.spinMaxLine.grid(column=1, row=2, padx=5, pady=5, sticky='e')

        self.minEle = tk.IntVar(value=2)
        ttk.Label(self, text='Min number of elemental slot (0-7)').grid(column=0, row=3, padx=5, pady=5, sticky='w')
        self.spinMinEle = ttk.Spinbox(self, from_=0, to=7, increment=1, textvariable=self.minEle, width=10)
        self.spinMinEle.grid(column=1, row=3, padx=5, pady=5, sticky='e')

        self.maxEle = tk.IntVar(value=4)
        ttk.Label(self, text='Max number of elemental slot (0-7)').grid(column=0, row=4, padx=5, pady=5, sticky='w')
        self.spinMaxEle = ttk.Spinbox(self, from_=0, to=7, increment=1, textvariable=self.maxEle, width=10)
        self.spinMaxEle.grid(column=1, row=4, padx=5, pady=5, sticky='e')

    def randomize(self, projectName, seed):
        if self.enabled.get():
            randomzier = OrbRandomizer(projectName, seed)
            randomzier.randomize(maxLine=self.maxLine.get(), minEleSlot=self.minEle.get(), maxEleSlot=self.maxEle.get(), excludeGuess=self.excludeGuess.get())