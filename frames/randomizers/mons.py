from randomizer.mons import MonsRandomizer
import tkinter as tk
import tkinter.ttk as ttk

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.name = ' Enemy '

        ttk.Label(self, text='Stat').grid(row=0, column=0, padx=5, pady=5, sticky='w')

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

        ttk.Separator(self, orient='vertical').grid(row=0, column=2, rowspan=15, padx=5, pady=5, sticky='ns')

        ttk.Label(self, text='Elemental Efficacy').grid(row=0, column=3, padx=5, pady=5, sticky='w')

        self.randomizeElemental = tk.IntVar()
        self.cbtnElemental = ttk.Checkbutton(self, text='Randomize Elemental Efficacy', variable=self.randomizeElemental)
        self.cbtnElemental.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky='w')

        self.elementalLowRollChance = tk.IntVar(value=30)
        ttk.Label(self, text='Chance for a low roll (0-100)').grid(row=2, column=3, padx=5, pady=5, sticky='w')
        self.spinElementalLowRollChance = ttk.Spinbox(self, from_=0, to=100, increment=10, textvariable=self.elementalLowRollChance, width=5, justify='center')
        self.spinElementalLowRollChance.grid(row=2, column=4, padx=5, pady=5, sticky='e')

        self.elementalLowRollCap = tk.IntVar(value=30)
        ttk.Label(self, text='Low Efficacy Cap (10-200)').grid(row=3, column=3, padx=5, pady=5, sticky='w')
        self.spinElementalLowRollCap = ttk.Spinbox(self, from_=10, to=200, increment=5, textvariable=self.elementalLowRollCap, width=5, justify='center')
        self.spinElementalLowRollCap.grid(row=3, column=4, padx=5, pady=5, sticky='e')

        self.elementalCap = tk.IntVar(value=200)
        ttk.Label(self, text='Efficacy Cap (10-200)').grid(row=4, column=3, padx=5, pady=5, sticky='w')
        self.spinElementalCap = ttk.Spinbox(self, from_=10, to=200, increment=5, textvariable=self.elementalCap, width=5, justify='center')
        self.spinElementalCap.grid(row=4, column=4, padx=5, pady=5, sticky='e')

        ttk.Separator(self, orient='horizontal').grid(row=5, column=0, columnspan=5, padx=5, pady=5, sticky='we')

        ttk.Label(self, text='Status Efficacy').grid(row=6, column=0, padx=5, pady=5, sticky='w')

        self.randomizeStatus = tk.IntVar()
        self.cbtnRandomizeStatus = ttk.Checkbutton(self, text='Randomize Status Efficacy', variable=self.randomizeStatus)
        self.cbtnRandomizeStatus.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.keepDeathblow = tk.IntVar()
        self.cbtnKeepDeathblow = ttk.Checkbutton(self, text='Keep Deathblow/Petrify/Vanish Efficacy', variable=self.keepDeathblow)
        self.cbtnKeepDeathblow.grid(row=8, column=0, columnspan=2, padx=20, pady=5, sticky='w')

        self.statusLowRollChance = tk.IntVar(value=30)
        ttk.Label(self, text='Chance for a low roll (0-100)').grid(row=9, column=0, padx=5, pady=5, sticky='w')
        self.spinStatusLowRollChance = ttk.Spinbox(self, from_=0, to=100, increment=10, textvariable=self.statusLowRollChance, width=5, justify='center')
        self.spinStatusLowRollChance.grid(row=9, column=1, padx=5, pady=5, sticky='e')

        self.statusLowRollCap = tk.IntVar(value=30)
        ttk.Label(self, text='Low Efficacy Cap (10-200)').grid(row=10, column=0, padx=5, pady=5, sticky='w')
        self.spinStatusLowRollCap = ttk.Spinbox(self, from_=10, to=200, increment=5, textvariable=self.statusLowRollCap, width=5, justify='center')
        self.spinStatusLowRollCap.grid(row=10, column=1, padx=5, pady=5, sticky='e')

        self.statusCap = tk.IntVar(value=200)
        ttk.Label(self, text='Efficacy Cap (10-200)').grid(row=11, column=0, padx=5, pady=5, sticky='w')
        self.spinStatusCap = ttk.Spinbox(self, from_=10, to=200, increment=5, textvariable=self.statusCap, width=5, justify='center')
        self.spinStatusCap.grid(row=11, column=1, padx=5, pady=5, sticky='e')

        ttk.Label(self, text='Unbalance Efficacy').grid(row=6, column=3, padx=5, pady=5, sticky='w')

        self.randomizeUnbalance = tk.IntVar()
        self.cbtnRandomizeUnbalance = ttk.Checkbutton(self, text='Randomize Unbalance Efficacy', variable=self.randomizeUnbalance)
        self.cbtnRandomizeUnbalance.grid(row=7, column=3, columnspan=2, padx=5, pady=5, sticky='w')

        self.unbalanceLowRollChance = tk.IntVar(value=30)
        ttk.Label(self, text='Chance for a low roll (0-100)').grid(row=8, column=3, padx=5, pady=5, sticky='w')
        self.spinUnbalanceLowRollChance = ttk.Spinbox(self, from_=0, to=100, increment=10, textvariable=self.unbalanceLowRollChance, width=5, justify='center')
        self.spinUnbalanceLowRollChance.grid(row=8, column=4, padx=5, pady=5, sticky='e')

    def randomize(self, projectName, seed):
        randomizer = MonsRandomizer(projectName, seed)
        randomizer.randomize(enableBase=self.randomizeBase.get(), baseVariance=self.baseVariance.get(),
                             enableGrowth=self.randomizeGrowth.get(), growthVariance=self.growthVariance.get(),
                             lowRollElemental=self.elementalLowRollChance.get(), lowCapElemental=self.elementalLowRollCap.get(),
                             highCapElemental=self.elementalCap.get(), randomizeElemental=self.randomizeElemental.get(),
                             lowRollStatus=self.statusLowRollChance.get(), lowCapStatus=self.statusLowRollCap.get(),
                             highCapStatus=self.statusCap.get(), randomizeStatus=self.randomizeStatus.get(), keepDeathblow=self.keepDeathblow.get(),
                             lowRollUnbalance=self.unbalanceLowRollChance.get(), randomizeUnbalance=self.randomizeUnbalance.get())
