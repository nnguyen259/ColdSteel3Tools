import tkinter as tk
import tkinter.ttk as ttk
import frames.unpacker as Unpacker
import frames.editor as Editor
import frames.packer as Packer
import frames.randomizer as Randomizer

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        master.setTitle('CS3 Tools')

        ttk.Label(self, text='Select an option: ').grid(column=0, columnspan=2, row=0, padx=5, pady=5, sticky='w')

        self.btnUnpack = ttk.Button(self, text='Unpack Tool', command=lambda: master.replaceScreen(Unpacker.Frame))
        self.btnUnpack.grid(column=0, row=1, padx=5, pady=5, sticky='nwse')
        ttk.Label(self, text='Unpack the game files to a more readable format').grid(column=1, row=1, padx=5, pady=5, sticky='w')

        self.btnPack = ttk.Button(self, text='Pack Tool', command=lambda: master.replaceScreen(Packer.Frame))
        self.btnPack.grid(column=0, row=2, padx=5, pady=5, sticky='nwse')
        ttk.Label(self, text='Repack the files back to the format the game can understand').grid(column=1, row=2, padx=5, pady=5, sticky='w')

        self.btnEditor = ttk.Button(self, text='Editors', command=lambda: master.replaceScreen(Editor.Frame))
        self.btnEditor.state(['disabled'])
        self.btnEditor.grid(column=0, row=3, padx=5, pady=5, sticky='nwse')
        ttk.Label(self, text='Edit the game files').grid(column=1, row=3, padx=5, pady=5, sticky='w')

        self.btnEditor = ttk.Button(self, text='Randomizer', command=lambda: master.replaceScreen(Randomizer.Frame))
        self.btnEditor.grid(column=0, row=4, padx=5, pady=5, sticky='nwse')
        ttk.Label(self, text='Randomize the game').grid(column=1, row=4, padx=5, pady=5, sticky='w')