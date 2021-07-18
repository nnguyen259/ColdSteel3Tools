import tkinter as tk
import frames.mainFrame as Main

class CS3App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.replaceScreen(Main.Frame)

    def replaceScreen(self, frameClass):
        newFrame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = newFrame
        self._frame.pack()

    def setTitle(self, title):
        self.title(title)

if __name__ == "__main__":
    app = CS3App()
    app.resizable(False, False)
    app.iconbitmap('icon.ico')
    app.mainloop()