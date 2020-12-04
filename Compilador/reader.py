import re

class Reader:
    def __init__(self, string):
        self.regex_separacao = re.compile(r'[ \t\n]+')
        self.regex_excluir = re.compile(r'({[^}]+})|(/\*([\s\S]+?)\*/)')
        # passando ponteiro file
        # with open(string, 'r') as reader:
        #     self.dados = reader.read()
        self.dados = string
        self.codigo = self.dados
        self.__trata_texto()

    def __trata_texto(self):
        # Transforma todo texto para lowercase
        # self.dados = self.dados.lower()
        # Substitui tabulações, espaços e quebra de linha por espaços
        self.dados = re.sub(self.regex_separacao,' ',self.dados)
        # Exclui comentários cobertos de chaves {}        
        self.dados = re.sub(self.regex_excluir, '', self.dados)

    def get_programa_formatted(self):
        return self.dados, self.codigo

    