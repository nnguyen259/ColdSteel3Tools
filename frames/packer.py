import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import frames.mainFrame as Main

import os

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        master.setTitle('CS3 Packer')

        self.btnBack = ttk.Button(self, text='<<Back', command=lambda: master.replaceScreen(Main.Frame))
        self.btnBack.grid(column=0, row=0, padx=5, pady=5, sticky='nwse')

        self.lbDirectory = ttk.Label(self, text='Output Directory:')
        self.lbDirectory.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        self.gameDirectory = tk.StringVar()
        self.entryDirectory = ttk.Entry(self, textvariable=self.gameDirectory, width=50)
        self.entryDirectory.grid(column=1, row=1, padx=5, pady=5, sticky='nwse')
        self.btnDirectory = ttk.Button(self, text='Browse', command=self.selectDirectory)
        self.btnDirectory.grid(column=2, row=1, padx=5, pady=5, sticky='nwes')

        self.lbName = ttk.Label(self, text='Project Name:')
        self.lbName.grid(column=0, row=2, padx=5, pady=5, sticky='w')
        projects = [f.name for f in os.scandir('projects') if f.is_dir()]
        self.projectName = tk.StringVar()
        self.entryName = ttk.Combobox(self, textvariable=self.projectName, values=projects, state='readonly')
        self.entryName.current(0)
        self.entryName.grid(column=1, row=2, padx=5, pady=5, sticky='nwse')
        self.btnUnpack = ttk.Button(self, text='Pack', command=self.doPack)
        self.btnUnpack.grid(column=2, row=2, padx=5, pady=5, sticky='nwse')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def doPack(self):
        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
            return
        if not os.path.exists(self.gameDirectory.get() + "/data"):
            os.mkdir(self.gameDirectory.get() + '/data')
            os.mkdir(self.gameDirectory.get() + '/data/text')
            os.mkdir(self.gameDirectory.get() + '/data/text/dat_en')
        import packer.packer
        packer.packer.pack(self.gameDirectory.get(), self.projectName.get())
        messagebox.showinfo('Finished', 'All Done!')