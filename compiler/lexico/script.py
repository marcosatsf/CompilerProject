from GUItest import Application
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Analisador Léxico LPD")
root.geometry("500x300")
root.resizable(width=False, height=False)
Application(root)
root.mainloop()
