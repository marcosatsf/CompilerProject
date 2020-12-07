from tkinter import *
from tkinter import filedialog

from compilerIDE import Application

root = Tk()
root.title("Compilador - IDE LPD")
#root.resizable(width=False, height=False)
Application(root)
root.mainloop()
