import os
import time
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font

from reader import Reader
from sintatico import AnalisadorSintatico

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.minsize(700,700)
        self.master.geometry('900x700')
        self.tipo_arquivos = [("Todos arquivos","*.*"),("Documento texto","*.txt"),("Arquivo LPD","*.lpd")]

        self.font = StringVar(self.master)
        self.font.trace_add("write", self.muda_font)
        self.font.trace_add("read", self.muda_font)
        self.font.set("Courier")

        self.tema = StringVar(self.master)
        self.tema.trace_add("write", self.muda_tema)
        self.tema.set("#ffffff")

        self.container_editor = Frame(master)

        self.linearea = Text(self.container_editor, font=self.font.get(), background="#bfbfbf", width=5, foreground="#008f28", state=DISABLED)
        self.textarea = Text(self.container_editor, font=self.font.get(), background=self.tema.get(), wrap="none")
        self.terminal = Text(self.master, font=self.font.get(), height=1, background=self.tema.get(), state=DISABLED)

        self.menubar = Menu(self.master, activebackground="#009933",activeforeground="white",bg="green",fg="black", background=self.tema.get())
        self.menu_file=Menu(self.menubar, tearoff=0,activebackground="#009933",activeforeground="white", background=self.tema.get())
        self.menu_config=Menu(self.menubar, tearoff=0,activebackground="#009933",activeforeground="white", background=self.tema.get())
        self.menu_config_tema=Menu(self.menubar, tearoff=0,activebackground="#009933", activeforeground="white", background=self.tema.get())
        self.menu_config_font=Menu(self.menubar, tearoff=0,activebackground="#009933", activeforeground="white", background=self.tema.get())
        self.menu_help=Menu(self.menubar, tearoff=0,activebackground="#009933",activeforeground="white", background=self.tema.get())
        
        self.scrollbar = Scrollbar(self.textarea, orient=VERTICAL,bg=self.tema.get(), command=self.scrolling_y)
        self.scrollbar_hori = Scrollbar(self.master, orient=HORIZONTAL,bg=self.tema.get(), command=self.textarea.xview)
        self.scrollbar_terminal = Scrollbar(self.terminal,bg=self.tema.get(), command=self.terminal.yview)
        self.file = None
        
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=2)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=1)

        self.linearea.pack(side=LEFT, fill=Y)
        
        self.container_editor.grid(row=0, column=0, sticky=N+S+W+E)        
        self.scrollbar_hori.grid(row=1, column=0, sticky=N+E+W+S)
        self.terminal.grid(row=2,column=0,sticky= S+W+E+N)
        
        #Menu
        self.menu_file.add_command(label="Novo      Ctrl+N", command=self.newfile)
        self.menu_file.add_command(label="Abrir     Ctrl+O", command=self.openfile)
        self.menu_file.add_command(label="Salvar    Ctrl+S", command = self.savefile)
        self.menu_file.add_command(label="Salvar como", command=self.saveasfile)
        self.master.bind("<Control-n>",self.newfile)
        self.master.bind("<Control-o>",self.openfile)
        self.master.bind("<Control-s>",self.savefile)
        self.textarea.bind("<KeyRelease>", self.mostrar_linhas)
        self.textarea.bind("<MouseWheel>", self.ignora_scroll)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Sair",command=self.exitapp)
        self.menubar.add_cascade(label="Arquivo", menu=self.menu_file)

        self.menu_config_font.add_radiobutton(label="Courier", variable=self.font, value="Courier")
        self.menu_config_font.add_radiobutton(label="Helvetica", variable=self.font, value="Helvetica")
        self.menu_config_font.add_radiobutton(label="Verdana", variable=self.font, value="Verdana")
        self.menu_config.add_cascade(label="Fonte", menu=self.menu_config_font)
        self.menu_config_tema.add_radiobutton(label="Light", variable=self.tema, value="#ffffff")
        self.menu_config_tema.add_radiobutton(label="Dark", variable=self.tema, value="#331a00")
        self.menu_config.add_cascade(label="Tema", menu=self.menu_config_tema)
        self.menubar.add_cascade(label="Configurações", menu=self.menu_config)

        self.menubar.add_command(label="Compila[r]", command=self.compile)
        self.master.bind("<Control-r>", self.compile)

        self.menu_help.add_command(label="Sobre Compilador LPD",command=self.showhelp)
        self.menubar.add_cascade(label="Ajuda", menu=self.menu_help)

        self.master.config(menu=self.menubar)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.textarea.config(yscrollcommand=self.scrollbar.set, xscrollcommand=self.scrollbar_hori.set)
        self.textarea.pack(expand=True, side=RIGHT,fill=BOTH)
        self.linearea.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar_terminal.pack(side=RIGHT, fill=Y)
        self.terminal.config(yscrollcommand=self.scrollbar_terminal.set)

        self.textarea.tag_config("textarea", background="#ff0000", foreground="#ffffff")
        # self.last_time.pack()

    def exitapp(self):
        self.master.destroy()

    def showhelp(self):
        messagebox.showinfo("Compilador LPD em python 3.9", "Criado por Marcos Aurélio & Bruno Marini")

    def compile(self, *args):
        self.limpar_highlight()
        self.terminal["state"] = NORMAL
        analisador = AnalisadorSintatico(self.textarea.get(1.0, END), self.file)

        message = analisador.run_analyzer()

        c_time = datetime.datetime.now() 
        # print para amostragem da ultima vez processado!
        if not self.file:
            self.file = "Arquivo não salvo"
        self.terminal.insert(END, f"[{c_time.hour:02d}:{c_time.minute:02d}:{c_time.second:02d}]$> ({os.path.basename(self.file)}) {message}\n")
        self.terminal["state"] = DISABLED
        linha = None
        try:
            linha = int(str(message).split("linha")[1][1:-1])
        except IndexError:
            pass
        # Atualiza a scrollbar
        self.terminal.yview_moveto(self.scrollbar_terminal.get()[1])
        self.highlight_texto(linha)
        

    # method to highlight the selected text 
    def highlight_texto(self, line=None): 
          
        # if no text is selected then tk.TclError exception occurs 
        try:
            if line:
                self.textarea.tag_add("textarea", f"{line}.0", f"{line}.100")
        except TclError: 
            pass
  
    # method to clear all contents from text widget. 
    def limpar_highlight(self): 
        self.textarea.tag_remove("textarea",  "1.0", 'end')

    def openfile(self, *args):
        self.file=filedialog.askopenfilename(defaultextension=".txt", filetypes=self.tipo_arquivos)
        if self.file =="":
            self.file= None
            print("VAZIO")
        else:
            self.master.title(os.path.basename(self.file) + " -- IDE LPD")
            self.textarea.delete(1.0 , END)
            file=open(self.file, "r")
            self.textarea.insert(1.0, file.read())
            file.close()
        self.mostrar_linhas()

    def newfile(self, *args):
            self.master.title("Compilador - IDE LPD")
            self.file = None
            self.textarea.delete(1.0,END)

    def savefile(self, *args):
        if self.file == None:
            self.file=filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",filetypes=self.tipo_arquivos)
            if self.file == "":
                self.file =None
            else:
                file = open(self.file,"w")
                file.write(self.Textarea.get(1.0,END))
                file.close()
                self.master.title(os.path.basename(self.file)+"- IDE LPD")
        else:
            file=open(self.file, "w")
            file.write(self.textarea.get(1.0,END))
            file.close()

    def saveasfile(self):
        if self.file == None:
            self.file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                          filetypes=self.tipo_arquivos)
            if self.file=='':
                self.file=None
            else:
                file=open(self.file,"w")
                file.write(self.textarea.get(1.0,END))
                file.close()
                self.master.title(os.path.basename(self.file)+"- IDE LPD")
        else:
            self.file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                          filetypes=self.tipo_arquivos)
            file = open(self.file, "w")
            file.write(self.textarea.get(1.0, END))
            file.close()
            self.master.title(os.path.basename(self.file) + "- IDE LPD")

    def muda_tema(self, *args):
        self.textarea["background"] = self.tema.get()
        self.terminal["background"] = self.tema.get()
        if self.tema.get() == "#ffffff":
            self.textarea["foreground"] = "#000000"
            self.terminal["foreground"] = "#000000"
            self.linearea["foreground"] = "#008f28"
            self.linearea["background"] = "#bfbfbf"
        else:
            self.textarea["foreground"] = "#ff9c33"
            self.terminal["foreground"] = "#ff9c33"
            self.linearea["foreground"] = "#ffe6cc"
            self.linearea["background"] = "#663500"

    def muda_font(self, *args):
        self.linearea["font"] = Font(family=self.font.get(), size=12)
        self.textarea["font"] = Font(family=self.font.get(), size=12)
        self.terminal["font"] = Font(family=self.font.get(), size=12)

    def mostrar_linhas(self, *args):
        self.linearea["state"] = NORMAL
        self.linearea.delete(1.0, END)
        for n_lines in range(int(self.textarea.index('end-1c').split('.')[0])):
            self.linearea.insert(END,f"{n_lines+1}\n")
        self.linearea["state"] = DISABLED

    def scrolling_y(self, *args):
        self.linearea.yview(*args)
        self.textarea.yview(*args)

    def ignora_scroll(self, *args):
        return 'break'
