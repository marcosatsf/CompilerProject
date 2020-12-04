#from app import Application
from compilerIDE import Application
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Compilador - IDE LPD")
#root.resizable(width=False, height=False)
Application(root)
root.mainloop()
