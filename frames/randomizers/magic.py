import tkinter as tk
from tkinter.constants import VERTICAL
import tkinter.ttk as ttk

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.name = 'Magic'

        self.enableCraft = tk.IntVar()
        self.cbtnEnableCraft = ttk.Checkbutton(self, text='Enable Crafts Randomizer', variable=self.enableCraft)
        self.cbtnEnableCraft.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')

        self.excludeGuess = tk.IntVar()
        self.cbtnExcludeGuess = ttk.Checkbutton(self, text='Exclude Guess Characters', variable=self.excludeGuess)
        self.cbtnExcludeGuess.grid(row=1, column=0, columnspan=3, padx=20, pady=0, sticky='w')

        ttk.Separator(self, orient=VERTICAL).grid(column=3, row=0, rowspan=4, sticky='ns')

        self.enableOrder = tk.IntVar()
        self.cbtnEnableOrder = ttk.Checkbutton(self, text='Enable Brave Orders Randomizer', variable=self.enableOrder)
        self.cbtnEnableOrder.grid(row=0, column=4, columnspan=3, padx=5, pady=5, sticky='w')

        self.excludeGuessOrder = tk.IntVar()
        self.cbtnExcludeGuessOrder = ttk.Checkbutton(self, text='Exclude Guess Characters', variable=self.excludeGuessOrder)
        self.cbtnExcludeGuessOrder.grid(row=1, column=4, columnspan=3, padx=20, pady=0, sticky='w')

        self.enableSCraft = tk.IntVar()
        self.cbtnEnableSCraft = ttk.Checkbutton(self, text='Enable S-Crafts Randomizer', variable=self.enableSCraft)
        self.cbtnEnableSCraft.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='w')

        self.excludeGuessSCraft = tk.IntVar()
        self.cbtnExcludeGuessSCraft = ttk.Checkbutton(self, text='Exclude Guess Characters', variable=self.excludeGuessSCraft)
        self.cbtnExcludeGuessSCraft.grid(row=3, column=0, columnspan=3, padx=20, pady=0, sticky='w')

    def randomize(self, projectName, seed):
        from randomizer.magic import randomize
        randomize(projectName=projectName, seed=seed, enableCraft=self.enableCraft.get(), excludeGuessCraft=self.excludeGuess.get(),
                  enableOrder=self.enableOrder.get(), excludeGuessOrder=self.excludeGuessOrder.get(),
                  enableSCraft=self.enableSCraft.get(), excludeGuessSCraft=self.excludeGuessSCraft.get())
