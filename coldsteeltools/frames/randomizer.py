import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from ..frames import mainFrame as Main
from ..frames.randomizers import magic as Magic
from ..frames.randomizers import orb as Orb
from ..frames.randomizers import status as Status
from ..frames.randomizers import misc as Misc
from ..frames.randomizers import mons as Mons

import os

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

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
        self.frameLists = [Mons.Frame(self.notebook), Status.Frame(self.notebook), Magic.Frame(self.notebook), Orb.Frame(self.notebook), Misc.Frame(self.notebook)]
        for frame in self.frameLists:
            self.notebook.add(frame, text=frame.name)
        self.notebook.grid(column=0, row=4, padx=5, pady=5, sticky='nwse', columnspan=3)

        self.status = tk.StringVar()
        self.status.set('Status: Ready.')
        self.lbStatus = ttk.Label(self, textvariable=self.status)
        self.lbStatus.grid(column=0, row=5, columnspan=2, padx=5, pady=0, sticky='w')

        self.btnRandomize = ttk.Button(self, text='Randomize', command=self.doRandomize)
        self.btnRandomize.grid(column=2, row=5, padx=5, pady=5, sticky='nwse')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def doRandomize(self):
        from distutils.dir_util import copy_tree, remove_tree

        def realRandomize():
            seed = self.seed.get()
            if not seed:
                import random, string
                seed = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
                print(seed)
            with open('result.txt', 'w') as resultFile:
                resultFile.write(f'CS3 Randomzier Results:\nSeed: {seed}\n')
            self.status.set('Preparing files...')
            os.makedirs(f'{self.gameDirectory.get()}/data/text/dat_en', exist_ok=True)
            copy_tree(f'projects/{self.projectName.get()}', f'projects/{self.projectName.get()}/tmp')
            try:
                for frame in self.frameLists:
                    self.status.set(f'Randomizing {frame.name}...')
                    frame.randomize(self.projectName.get(), seed)
                from ..packer import packer, scriptpacker
                self.status.set('Packing tbl files...')
                packer.packer.pack(self.gameDirectory.get(), self.projectName.get(), randomizer=True)
                self.status.set('Packing script files...')
                packer.scriptpacker.pack(self.gameDirectory.get(), self.projectName.get(), randomizer=True)
                remove_tree(f'projects/{self.projectName.get()}/tmp')
                self.status.set('Status: Ready.')
                messagebox.showinfo('Finished', 'All Done!')
            except Exception:
                import traceback
                messagebox.showerror('Error', traceback.format_exception())
            self.btnDirectory['state'] = 'normal'
            self.btnRandomize['state'] = 'normal'
            self.btnBack['state'] = 'normal'

        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
            return
        self.btnDirectory['state'] = 'disabled'
        self.btnRandomize['state'] = 'disabled'
        self.btnBack['state'] = 'disabled'
        threading.Thread(target=realRandomize).start()