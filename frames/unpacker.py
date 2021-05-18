import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import frames.mainFrame as Main

import os, shutil, threading

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        master.setTitle('CS3 Unpacker')

        self.btnBack = ttk.Button(self, text='<<Back', command=lambda: master.replaceScreen(Main.Frame))
        self.btnBack.grid(column=0, row=0, padx=5, pady=5, sticky='nwse')

        self.lbDirectory = ttk.Label(self, text='Game Directory:')
        self.lbDirectory.grid(column=0, row=1, padx=5, pady=5, sticky='w')
        self.gameDirectory = tk.StringVar()
        self.entryDirectory = ttk.Entry(self, textvariable=self.gameDirectory, width=50)
        self.entryDirectory.grid(column=1, row=1, padx=5, pady=5, sticky='nwse')
        self.btnDirectory = ttk.Button(self, text='Browse', command=self.selectDirectory)
        self.btnDirectory.grid(column=2, row=1, padx=5, pady=5, sticky='nwes')

        self.lbName = ttk.Label(self, text='Project Name:')
        self.lbName.grid(column=0, row=2, padx=5, pady=5, sticky='w')
        self.projectName = tk.StringVar()
        self.entryName = ttk.Entry(self, textvariable=self.projectName, width=50)
        self.entryName.grid(column=1, row=2, padx=5, pady=5, sticky='nwse')
        self.btnUnpack = ttk.Button(self, text='Unpack', command=self.doUnpack)
        self.btnUnpack.grid(column=2, row=2, padx=5, pady=5, sticky='nwse')

        ttk.Separator(self, orient='horizontal').grid(column=0, row=3, columnspan=3, sticky='we')

        self.status = tk.StringVar()
        self.status.set('Status: Ready.')
        self.lbStatus = ttk.Label(self, textvariable=self.status)
        self.lbStatus.grid(column=0, row=4, columnspan=3, padx=5, pady=0, sticky='w')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def doUnpack(self):
        def realUnpack():
            os.mkdir('projects/' + self.projectName.get())
            import unpacker.unpacker, unpacker.scriptunpacker
            self.status.set('Status: Unpacking tbl files...')
            unpacker.unpacker.unpack(self.gameDirectory.get(), self.projectName.get())
            self.status.set('Status: Unpacking script files...')
            unpacker.scriptunpacker.unpack(self.gameDirectory.get(), self.projectName.get())
            self.status.set('Status: Ready.')
            messagebox.showinfo('Finished', 'All Done!')
            self.btnDirectory['state'] = 'normal'
            self.btnUnpack['state'] = 'normal'
            self.btnBack['state'] = 'normal'

        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
            return
        if not os.path.exists(self.gameDirectory.get() + "/data"):
            messagebox.showerror('Invalid Directory', 'Invalid game directory')
            return
        if not self.projectName.get():
            messagebox.showerror('No Project Name', 'No project name specified')
            return
        if os.path.exists('projects/' + self.projectName.get()):
            decision = messagebox.askyesno('Project Already Existed', 'The project is already existed. Would you like to override it?')
            if not decision:
                return
            else:
                shutil.rmtree('projects/' + self.projectName.get())
        self.btnDirectory['state'] = 'disabled'
        self.btnUnpack['state'] = 'disabled'
        self.btnBack['state'] = 'disabled'
        threading.Thread(target=realUnpack).start()