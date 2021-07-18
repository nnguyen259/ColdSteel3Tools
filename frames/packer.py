import threading
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import frames.mainFrame as Main

import os

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

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
        self.entryName.bind('<<ComboboxSelected>>', self.updateProject)

        self.frmScript = ttk.Labelframe(self, text='Script Packing')
        self.frmScript.grid(column=0, row=3, columnspan=3, padx=5, pady=5, sticky='nwse')

        self.packScript = tk.IntVar(value=0)
        self.cbtnPackScript = ttk.Checkbutton(self.frmScript, text='Pack the game script', variable=self.packScript, command=self.displayScriptSelect)
        self.cbtnPackScript.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')

        self.frmScriptSelect = tk.Frame(self.frmScript)
        self.frmScriptSelect.grid(row=1, column=0, columnspan=3, sticky='nwse')

        ttk.Label(self.frmScriptSelect, text='Available').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frmScriptSelect, text='Selected').grid(row=0, column=2, padx=5, pady=5)
        self.availableList = []
        self.selectedList = []
        self.availableChoices = tk.StringVar(value=self.availableList)
        self.selectedChoices = tk.StringVar(value=self.selectedList)
        self.lstAvailable = tk.Listbox(self.frmScriptSelect, listvariable=self.availableChoices)
        self.lstAvailable.grid(row=1, column=0, rowspan=6, padx=5, pady=5, sticky='nwse')
        self.lstSelected = tk.Listbox(self.frmScriptSelect, listvariable=self.selectedChoices)
        self.lstSelected.grid(row=1, column=2, rowspan=6, padx=5, pady=5, sticky='nwse')

        self.btnMoveRightAll = ttk.Button(self.frmScriptSelect, text=' >>> ', command=self.moveRightAll)
        self.btnMoveRight = ttk.Button(self.frmScriptSelect, text=' > ', command=self.moveRight)
        self.btnMoveLeft = ttk.Button(self.frmScriptSelect, text=' < ', command=self.moveLeft)
        self.btnMoveLeftAll = ttk.Button(self.frmScriptSelect, text=' <<< ', command=self.moveLeftAll)

        self.btnMoveRightAll.grid(row=2, column=1, padx=5, pady=5)
        self.btnMoveRight.grid(row=3, column=1, padx=5, pady=5)
        self.btnMoveLeft.grid(row=4, column=1, padx=5, pady=5)
        self.btnMoveLeftAll.grid(row=5, column=1, padx=5, pady=5)

        self.btnPack = ttk.Button(self, text='Pack', command=self.doPack)
        self.btnPack.grid(column=2, row=2, padx=5, pady=5, sticky='nwse')

        ttk.Separator(self, orient='horizontal').grid(column=0, row=4, columnspan=3, sticky='we')

        self.status = tk.StringVar()
        self.status.set('Status: Ready.')
        self.lbStatus = ttk.Label(self, textvariable=self.status)
        self.lbStatus.grid(column=0, row=5, columnspan=3, padx=5, pady=0, sticky='w')

        self.update()
        self.displayScriptSelect()
    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def update(self):
        try:
            self.frmScript.grid()
            self.availableList = [f.name for f in os.scandir(f'projects/{self.projectName.get()}/scripts') if f.is_dir()]
            self.selectedList = []
            self.sortAndRefresh()
        except:
            self.frmScript.grid_remove()
            self.packScript.set(0)
        
        self.displayScriptSelect()

    def updateProject(self, event):
        self.update()

    def displayScriptSelect(self):
        if not self.packScript.get():
            self.frmScriptSelect.grid_remove()
        else:
            self.frmScriptSelect.grid()

    def sortAndRefresh(self):
        self.availableList.sort()
        self.selectedList.sort()
        self.availableChoices.set(self.availableList)
        self.selectedChoices.set(self.selectedList)

    def moveRight(self):
        selected = self.lstAvailable.curselection()
        selected = [self.availableList[i] for i in selected]
        if len(selected):
            self.selectedList.extend(selected)
            self.availableList = [item for item in self.availableList if item not in selected]
            self.sortAndRefresh()

    def moveLeft(self):
        selected = self.lstSelected.curselection()
        selected = [self.selectedList[i] for i in selected]
        if len(selected):
            self.availableList.extend(selected)
            self.selectedList = [item for item in self.selectedList if item not in selected]
            self.sortAndRefresh()

    def moveRightAll(self):
        if len(self.availableList):
            self.selectedList.extend(self.availableList)
            self.availableList = []
            self.sortAndRefresh()

    def moveLeftAll(self):
        if len(self.selectedList):
            self.availableList.extend(self.selectedList)
            self.selectedList = []
            self.sortAndRefresh()

    def doPack(self):
        def realPack():
            os.makedirs(f'{self.gameDirectory.get()}/data/text/dat_en', exist_ok=True)
            import packer.packer, packer.scriptpacker
            self.status.set('Packing tbl files...')
            packer.packer.pack(self.gameDirectory.get(), self.projectName.get())
            if self.packScript.get() and len(self.selectedList):
                self.status.set('Packing script files...')
                packer.scriptpacker.pack(self, self.gameDirectory.get(), self.projectName.get(), moduleList=self.selectedList)
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