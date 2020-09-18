import re

class Reader:
    def __init__(self, string):
        self.regex_separacao = re.compile(r'[ \t]+')
        self.regex_quebra_newline = re.compile(r'\n+')
        self.regex_excluir = re.compile(r'({[^}]+})|(/\*([\s\S]+?)\*/)')
        with open(string, 'r') as reader:
            self.dados = reader.read()
        self.codigo = self.dados
        self.__trata_texto()

    def __trata_texto(self):
        # Transforma todo texto para lowercase
        self.dados = self.dados.lower()
        # Substitui tabulações, espaços e quebra de linha por espaços
        self.dados = re.sub(self.regex_separacao,' ',self.dados)
        # Exclui comentários cobertos de chaves {}        
        self.dados = re.sub(self.regex_excluir, '', self.dados)

        self.dados = re.sub(self.regex_quebra_newline,'',self.dados)

    def get_programa_formatted(self):
        return self.dados, self.codigo

    