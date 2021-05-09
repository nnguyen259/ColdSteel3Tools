import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import frames.mainFrame as Main
import frames.randomizers.magic as Magic
import frames.randomizers.status as Status

import os

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        master.setTitle('CS3 Randomizer')

        self.btnBack = ttk.Button(self, text='<<Back', command=lambda: master.replaceScreen(Main.Frame))
        self.btnBack.grid(column=0, row=0, padx=5, pady=5, sticky='nwse')

        self.lbDirectory = ttk.Label(self, text='Output Directory:')
        self.lbDirectory.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        self.gameDirectory = tk.StringVar()
        self.entryDirectory = ttk.Entry(self, textvariable=self.gameDirectory, width=40)
        self.entryDirectory.grid(column=1, row=1, padx=5, pady=5, sticky='nwse')
        self.btnDirectory = ttk.Button(self, text='Browse', command=self.selectDirectory)
        self.btnDirectory.grid(column=2, row=1, padx=5, pady=5, sticky='nwes')

        self.lbName = ttk.Label(self, text='Base Project:')
        self.lbName.grid(column=0, row=2, padx=5, pady=5, sticky='w')
        projects = [f.name for f in os.scandir('projects') if f.is_dir()]
        self.projectName = tk.StringVar()
        self.entryName = ttk.Combobox(self, textvariable=self.projectName, values=projects, state='readonly')
        self.entryName.current(0)
        self.entryName.grid(column=1, row=2, padx=5, pady=5, sticky='nwse')

        self.lbSeed = ttk.Label(self, text='Seed:')
        self.lbSeed.grid(column=0, row=3, padx=5, pady=5, sticky='w')
        self.seed = tk.StringVar()
        self.entrySeed = ttk.Entry(self, textvariable=self.seed, width=40)
        self.entrySeed.grid(column=1, row=3, padx=5, pady=5, sticky='nwse')

        self.notebook = ttk.Notebook(self)
        self.frameLists = [Magic.Frame(self.notebook)]
        for frame in self.frameLists:
            self.notebook.add(frame, text=frame.name)
        self.notebook.grid(column=0, row=4, padx=5, pady=5, sticky='nwse', columnspan=3)

        self.btnRandomize = ttk.Button(self, text='Randomize', command=self.doRandomize)
        self.btnRandomize.grid(column=2, row=5, padx=5, pady=5, sticky='nwse')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def doRandomize(self):
        from distutils.dir_util import copy_tree, remove_tree
        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
            return
        with open('result.txt', 'w') as resultFile:
            resultFile.write(f'CS3 Randomzier Results:\nSeed: {self.seed.get()}\n')
        os.makedirs(f'{self.gameDirectory.get()}/data/text/dat_en', exist_ok=True)
        copy_tree(f'projects/{self.projectName.get()}', f'projects/{self.projectName.get()}/tmp')
        for frame in self.frameLists:
            frame.randomize(self.projectName.get(), self.seed.get())
        import packer.packer
        packer.packer.pack(self.gameDirectory.get(), self.projectName.get(), mode=1)
        remove_tree(f'projects/{self.projectName.get()}/tmp')
        messagebox.showinfo('Finished', 'All Done!')