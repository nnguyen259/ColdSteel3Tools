from randomizer.slot import SlotRandomizer
from randomizer.status import StatusRandomizer
import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Stat '

        self.excludeGuest = tk.IntVar()
        self.cbtnExcludeGuestBase = ttk.Checkbutton(self, text='Exclude Guest Characters', variable=self.excludeGuest)
        self.cbtnExcludeGuestBase.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.randomizeBase = tk.IntVar()
        self.cbtnRandomizeBase = ttk.Checkbutton(self, text='Randomize Base Stat', variable=self.randomizeBase)
        self.cbtnRandomizeBase.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.baseVariance = tk.IntVar(value=30)
        ttk.Label(self, text='Variance (10-100)').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.spinBaseVariance = ttk.Spinbox(self, from_=10, to=100, increment=5, textvariable=self.baseVariance, width=5, justify='center')
        self.spinBaseVariance.grid(row=2, column=1, padx=5, pady=5, sticky='e')

        self.randomizeGrowth = tk.IntVar()
        self.cbtnRandomizeGrowth = ttk.Checkbutton(self, text='Randomize Stat Growth', variable=self.randomizeGrowth)
        self.cbtnRandomizeGrowth.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.growthVariance = tk.IntVar(value=30)
        ttk.Label(self, text='Variance (10-100)').grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.spinGrowthVariance = ttk.Spinbox(self, from_=10, to=100, increment=5, textvariable=self.growthVariance, width=5, justify='center')
        self.spinGrowthVariance.grid(row=4, column=1, padx=5, pady=5, sticky='e')

        self.randomizeBaseEP = tk.IntVar()
        self.cbtnRandomizeBaseEP = ttk.Checkbutton(self, text='Randomize Base EP', variable=self.randomizeBaseEP)
        self.cbtnRandomizeBaseEP.grid(row=1, column=3, columnspan=2, padx=50, pady=5, sticky='w')

        self.randomizeEPGrowth = tk.IntVar()
        self.cbtnRandomizeEPGrowth = ttk.Checkbutton(self, text='Randomize Stat Growth', variable=self.randomizeEPGrowth)
        self.cbtnRandomizeEPGrowth.grid(row=3, column=3, columnspan=2, padx=50, pady=5, sticky='w')

    def randomize(self, projectName, seed):
        if self.randomizeBase.get() or self.randomizeGrowth.get():
            randomizer = StatusRandomizer(projectName, seed)
            randomizer.randomize(enableBase=self.randomizeBase.get(), baseVariance=self.baseVariance.get(),
                                 enableGrowth=self.randomizeGrowth.get(), growthVariance=self.growthVariance.get(),
                                 excludeGuest=self.excludeGuest.get())

        if self.randomizeBaseEP.get() or self.randomizeEPGrowth.get():
            randomizer = SlotRandomizer(projectName, seed)
            randomizer.randomize(randomizeBase=self.randomizeBaseEP.get(), randomizeGrowth=self.randomizeEPGrowth.get(), excludeGuest=self.excludeGuest.get())
