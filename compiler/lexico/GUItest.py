from reader import Reader
from analisador import AnalisadorLexico
from tkinter import *
from tkinter import filedialog
import os
import time
import datetime

class Application:
    def __init__(self, master=None):
        self.master = master

        self.fontePadrao = ("Verdana", "10")
        self.primeiro_container = Frame(master)
        self.primeiro_container["pady"] = 10
        self.primeiro_container.pack()

        self.segundo_container = Frame(master)
        self.segundo_container["padx"] = 20
        self.segundo_container.pack()

        self.terceiro_container = Frame(master)
        self.terceiro_container["pady"] = 20
        self.terceiro_container.pack()

        self.quarto_container = Frame(master)
        self.quarto_container["pady"] = 20
        self.quarto_container["padx"] = 50
        self.quarto_container["borderwidth"] = 2
        self.quarto_container["relief"] = "groove"
        self.quarto_container.pack()

        self.quinto_container = Frame(master)
        self.quinto_container["pady"] = 20
        self.quinto_container.pack()

        self.titulo = Label(self.primeiro_container, text="Carregar Arquivo")
        self.titulo["font"] = ("Verdana", "10", "bold")
        self.titulo.pack()

        self.carregar = Button(self.terceiro_container)
        self.carregar["text"] = "Carregar"
        self.carregar["font"] = ("Verdana", "10")
        self.carregar["command"] = self.carregar_arquivo
        self.carregar.pack()

        self.nomeLabel = Label(
                            self.segundo_container, 
                            text="Selecione um arquivo abaixo", 
                            font=self.fontePadrao
                            )
        self.nomeLabel.pack(side=RIGHT)

        self.carregar = Button(self.quarto_container)
        self.carregar["text"] = "Processar tokenização!"
        self.carregar["font"] = ("Verdana", "10")
        self.carregar["command"] = self.tokenizing
        self.carregar.pack()

        self.tokenizado = Label(self.quarto_container, text="Pronto para processar...", font=self.fontePadrao)
        self.tokenizado.pack()

        self.last_time = Label(self.quinto_container, text="Última vez processado: -")
        self.last_time["font"] = ("Verdana", "10", "bold")
        self.last_time.pack()

    def carregar_arquivo(self):
        self.nomeLabel["text"] = filedialog.askopenfilename(
                                        initialdir = os.getcwd(),
                                        title = "Selecionar arquivo",
                                        filetypes = (("Text File", "*.txt"),("All Files","*.*"))
                                        )

    def tokenizing(self):
        # Lê o texto
        texto = Reader(self.nomeLabel["text"])
        # Instancia o analisador com o programa já formatado
        analisador = AnalisadorLexico(texto.get_programa_formatted())    
        # Realiza a quebra em tokens
        try:
            analisador.pega_token()
            write_output = analisador.get_tokenizer_str()
            message = "Output gerado com sucesso!"
        except AttributeError as e:
            write_output = analisador.get_tokenizer_str(str(e))
            message = f"Output gerado com {str(e)}"
        # Mostra os tokens
        #analisador.beauty_print()
        get_path = self.nomeLabel["text"].rsplit('/', 1)[0]
        with open(f'{get_path}/output.txt', 'w') as writer:
            writer.write(write_output)
        self.tokenizado["text"] = message
        c_time = datetime.datetime.now() 
        self.last_time["text"] = f"Última vez processado: {c_time.day}/{c_time.month}/{c_time.year} - {c_time.hour}h{c_time.minute}"
        self.master.update_idletasks()
        time.sleep(5)
        self.tokenizado["text"] = "Pronto para processar..."
