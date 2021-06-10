import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Stat '

        self.enableStat = tk.IntVar()
        self.cbtnEnableStat = ttk.Checkbutton(self, text='Enable Stat Randomizer', variable=self.enableStat)
        self.cbtnEnableStat.grid(row=0, column=0, columnspan=3, sticky='w')