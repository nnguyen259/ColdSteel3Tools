import tkinter as tk
import tkinter.ttk as ttk
import frames.editor as Editor

class Frame(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        master.setTitle('CS3 Magic Editor')

        self.btnBack = ttk.Button(self, text='Unpack Tool', command=lambda: master.replaceScreen(Editor.Frame))
        self.btnBack.pack()