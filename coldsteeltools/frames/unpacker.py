import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from ..frames import mainFrame as Main

import os, shutil, threading

class Frame(ttk.Frame):
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

        self.frmScript = ttk.Labelframe(self, text='Script Unpacking')
        self.frmScript.grid(column=0, row=3, columnspan=3, padx=5, pady=5, sticky='nwse')

        self.unpackScript = tk.IntVar(value=1)
        self.cbtnUnpackScript = ttk.Checkbutton(self.frmScript, text='Unpack the game script', variable=self.unpackScript, command=self.displayScriptSelect)
        self.cbtnUnpackScript.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='w')

        self.frmScriptSelect = tk.Frame(self.frmScript)
        self.frmScriptSelect.grid(row=1, column=0, columnspan=3, sticky='nwse')

        ttk.Label(self.frmScriptSelect, text='Available').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frmScriptSelect, text='Selected').grid(row=0, column=2, padx=5, pady=5)
        self.availableList = ['ani', 'battle', 'book', 'minigame', 'scena', 'talk']
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

        self.btnUnpack = ttk.Button(self, text='Unpack', command=self.doUnpack)
        self.btnUnpack.grid(column=2, row=4, padx=5, pady=5, sticky='nwse')
        
        ttk.Separator(self, orient='horizontal').grid(column=0, row=5, columnspan=3, sticky='we')

        self.status = tk.StringVar()
        self.status.set('Status: Ready.')
        self.lbStatus = ttk.Label(self, textvariable=self.status)
        self.lbStatus.grid(column=0, row=6, columnspan=3, padx=5, pady=0, sticky='w')

    
    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def displayScriptSelect(self):
        if not self.unpackScript.get():
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

    def doUnpack(self):
        def realUnpack():
            os.mkdir('projects/' + self.projectName.get())
            from ..unpacker import unpacker, scriptunpacker
            self.status.set('Status: Unpacking tbl files...')
            try:
                unpacker.unpacker.unpack(self.gameDirectory.get(), self.projectName.get())
                if self.unpackScript.get() and len(self.selectedList):
                    self.status.set('Status: Unpacking script files...')
                    unpacker.scriptunpacker.unpack(self, self.gameDirectory.get(), self.projectName.get(), self.selectedList)
                self.status.set('Status: Ready.')
                messagebox.showinfo('Finished', 'All Done!')
            except Exception:
                import traceback
                messagebox.showerror('Error', traceback.format_exc())
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