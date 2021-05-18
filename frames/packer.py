import threading
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
        self.btnPack = ttk.Button(self, text='Pack', command=self.doPack)
        self.btnPack.grid(column=2, row=2, padx=5, pady=5, sticky='nwse')

        ttk.Separator(self, orient='horizontal').grid(column=0, row=3, columnspan=3, sticky='we')

        self.status = tk.StringVar()
        self.status.set('Status: Ready.')
        self.lbStatus = ttk.Label(self, textvariable=self.status)
        self.lbStatus.grid(column=0, row=4, columnspan=3, padx=5, pady=0, sticky='w')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def doPack(self):
        def realPack():
            os.makedirs(f'{self.gameDirectory.get()}/data/text/dat_en', exist_ok=True)
            import packer.packer, packer.scriptpacker
            self.status.set('Packing tbl files...')
            packer.packer.pack(self.gameDirectory.get(), self.projectName.get())
            self.status.set('Packing script files...')
            packer.scriptpacker.pack(self.gameDirectory.get(), self.projectName.get())
            self.status.set('Status: Ready.')
            messagebox.showinfo('Finished', 'All Done!')
            self.btnDirectory['state'] = 'normal'
            self.btnPack['state'] = 'normal'
            self.btnBack['state'] = 'normal'

        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
            return
        self.btnDirectory['state'] = 'disabled'
        self.btnPack['state'] = 'disabled'
        self.btnBack['state'] = 'disabled'
        threading.Thread(target=realPack).start()