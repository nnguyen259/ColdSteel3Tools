from randomizer.magic import MagicRandomizer
import tkinter as tk
from tkinter.constants import VERTICAL
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Craft '

        self.enableCraft = tk.IntVar()
        self.cbtnEnableCraft = ttk.Checkbutton(self, text='Enable Crafts Randomizer', variable=self.enableCraft)
        self.cbtnEnableCraft.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.excludeGuest = tk.IntVar()
        self.cbtnExcludeGuest = ttk.Checkbutton(self, text='Exclude Guest Characters', variable=self.excludeGuest)
        self.cbtnExcludeGuest.grid(row=0, column=1, padx=5, pady=0, sticky='w')

        self.enableSCraft = tk.IntVar()
        self.cbtnEnableSCraft = ttk.Checkbutton(self, text='Enable S-Crafts Randomizer', variable=self.enableSCraft)
        self.cbtnEnableSCraft.grid(row=2, column=0, padx=5, pady=25, sticky='w')

        self.excludeGuestSCraft = tk.IntVar()
        self.cbtnExcludeGuestSCraft = ttk.Checkbutton(self, text='Exclude Guest Characters', variable=self.excludeGuestSCraft)
        self.cbtnExcludeGuestSCraft.grid(row=2, column=1, padx=5, pady=25, sticky='w')

        self.enableOrder = tk.IntVar()
        self.cbtnEnableOrder = ttk.Checkbutton(self, text='Enable Brave Orders Randomizer', variable=self.enableOrder)
        self.cbtnEnableOrder.grid(row=4, column=0, padx=5, pady=5, sticky='w')

        self.excludeGuestOrder = tk.IntVar()
        self.cbtnExcludeGuestOrder = ttk.Checkbutton(self, text='Exclude Guest Characters', variable=self.excludeGuestOrder)
        self.cbtnExcludeGuestOrder.grid(row=4, column=1, padx=5, pady=0, sticky='w')

    def randomize(self, projectName, seed):
        randomizer = MagicRandomizer(projectName, seed)
        randomizer.randomize(enableCraft=self.enableCraft.get(), excludeGuestCraft=self.excludeGuest.get(),
                  enableOrder=self.enableOrder.get(), excludeGuestOrder=self.excludeGuestOrder.get(),
                  enableSCraft=self.enableSCraft.get(), excludeGuestSCraft=self.excludeGuestSCraft.get())
