from randomizer.mons import MonsRandomizer
import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Enemy '

        self.randomizeBase = tk.IntVar()
        self.cbtnRandomizeBase = ttk.Checkbutton(self, text='Randomize Base Stat', variable=self.randomizeBase)
        self.cbtnRandomizeBase.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.baseVariance = tk.IntVar(value=30)
        ttk.Label(self, text='Variance (10-100)').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.spinBaseVariance = ttk.Spinbox(self, from_=10, to=100, increment=5, textvariable=self.baseVariance, width=5, justify='center')
        self.spinBaseVariance.grid(row=1, column=1, padx=5, pady=5, sticky='e')

        self.randomizeGrowth = tk.IntVar()
        self.cbtnRandomizeGrowth = ttk.Checkbutton(self, text='Randomize Stat Growth', variable=self.randomizeGrowth)
        self.cbtnRandomizeGrowth.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.growthVariance = tk.IntVar(value=30)
        ttk.Label(self, text='Variance (10-100)').grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.spinGrowthVariance = ttk.Spinbox(self, from_=10, to=100, increment=5, textvariable=self.growthVariance, width=5, justify='center')
        self.spinGrowthVariance.grid(row=3, column=1, padx=5, pady=5, sticky='e')

        self.lowRollChance = tk.IntVar(value=30)
        ttk.Label(self, text='Chance for a low roll (0-100)').grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.spinlowRollChance = ttk.Spinbox(self, from_=0, to=100, increment=10, textvariable=self.lowRollChance, width=5, justify='center')
        self.spinlowRollChance.grid(row=0, column=3, padx=5, pady=5, sticky='e')

        self.randomizeElemental = tk.IntVar()
        self.cbtnRandomizeBaseEP = ttk.Checkbutton(self, text='Randomize Elemental Efficacy', variable=self.randomizeElemental)
        self.cbtnRandomizeBaseEP.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.randomizeStatus = tk.IntVar()
        self.cbtnRandomizeEPGrowth = ttk.Checkbutton(self, text='Randomize Status Efficacy', variable=self.randomizeStatus)
        self.cbtnRandomizeEPGrowth.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.keepDeathblow = tk.IntVar()
        self.cbtnKeepDeathblow = ttk.Checkbutton(self, text='Keep Deathblow/Petrify Efficacy', variable=self.keepDeathblow)
        self.cbtnKeepDeathblow.grid(row=3, column=2, columnspan=2, padx=20, pady=5, sticky='w')

        self.randomizeUnbalance = tk.IntVar()
        self.cbtnRandomizeUnbalance = ttk.Checkbutton(self, text='Randomize Status Efficacy', variable=self.randomizeUnbalance)
        self.cbtnRandomizeUnbalance.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky='w')

    def randomize(self, projectName, seed):
        randomizer = MonsRandomizer(projectName, seed)
        randomizer.randomize(enableBase=self.randomizeBase.get(), baseVariance=self.baseVariance.get(),
                             enableGrowth=self.randomizeGrowth.get(), growthVariance=self.growthVariance.get(),
                             lowRoll=self.lowRollChance.get(), randomizeElemental=self.randomizeElemental.get(),
                             randomizeStatus=self.randomizeStatus.get(), keepDeathblow=self.keepDeathblow.get(),
                             randomizeUnbalance=self.randomizeUnbalance.get())
