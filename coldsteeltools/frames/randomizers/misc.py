from ...randomizer.model import ModelRandomizer
import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Misc. '

        self.enabled = tk.IntVar(value=0)
        self.cbtnEnabled = ttk.Checkbutton(self, text='Randomize Character Models', variable=self.enabled)
        self.cbtnEnabled.grid(column=0, row=0, padx=5, pady=5, sticky='w')

        self.excludeGuest = tk.IntVar(value=0)
        self.cbtnEnabled = ttk.Checkbutton(self, text='Exclude Guest Characters', variable=self.excludeGuest)
        self.cbtnEnabled.grid(column=0, row=1, padx=20, sticky='w')

    def randomize(self, projectName, seed):
        if self.enabled.get():
            randomizer = ModelRandomizer(projectName, seed)
            randomizer.randomize(self.excludeGuest.get())