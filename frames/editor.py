import tkinter as tk
import tkinter.ttk as ttk
import frames.mainFrame as Main
import frames.editors.magic as Magic

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        master.setTitle('CS3 Editors')

        self.btnMagic = ttk.Button(self, text='Magic', command=lambda: master.replaceScreen(Magic.Frame))
        self.btnMagic.pack()

        self.btnBack = ttk.Button(self, text='Back', command=lambda: master.replaceScreen(Main.Frame))
        self.btnBack.pack()