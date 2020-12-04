
class TabelaSimbolos:
    def __init__(self):
        self.tabela_pilha = []

    def __novo_simbolo(self,lexema=None,tipo_iden=None, escopo=None, rotulo=None, pos_pilha=None):
        """
        Cria um símbolo novo

        Args:
            lexema (str, optional): Nome do identificador. Defaults to None.
            tipo_iden (str, optional): Tipo do identificador. Defaults to None.
            escopo (str, optional): Escopo do identificador. Defaults to None.

        Returns:
            dict.Simbolo: Um símbolo que define um identificador
        """
        simbolo = {
            'lexema':lexema,
            'tipo_iden':tipo_iden,
            'escopo':escopo
        }
        if rotulo:
            simbolo['rotulo'] = rotulo
        if pos_pilha:
            simbolo['pos_pilha'] = pos_pilha
        return simbolo


    def add_tabela(self, lexema, tipo_iden, escopo, rotulo=None, pos_pilha=None):
        """
        Insere um símbolo na pilha

        Args:
            lexema (str, optional): Nome do identificador. Defaults to None.
            tipo_iden (str, optional): Tipo do identificador. Defaults to None.
            escopo (str, optional): Escopo do identificador. Defaults to None.
        """
        self.tabela_pilha.append(self.__novo_simbolo(lexema, tipo_iden, escopo, rotulo, pos_pilha))


    def add_tipo_tabela_var(self, tipo_var, escopo):
        """ 
        Adicionar tipo de variável

        Args:
            tipo_var (str): inteiro ou booleano
            escopo (int): nível de escopo
        """
        tab_pilha = []
        for elemento in reversed(self.tabela_pilha):
            if elemento['tipo_iden'] == "var" and \
                elemento['escopo'] == escopo and \
                len(elemento) < 5:
                elemento['tipo']=tipo_var
            tab_pilha.append(elemento)
        #print(tab_pilha)
        tab_pilha.reverse()
        self.tabela_pilha = tab_pilha
        #print(self.tabela_pilha)

    def ret_nao_var(self):
        for elem in reversed(self.tabela_pilha):
            if elem.get('tipo_iden') in ['func_i','func_b','proc','prog']:
                return elem
        return None


    def checa_tabela(self, lexema):
        """
        Verifica se há o lexema na pilha

        Args:
            lexema (str): Nome do identificador

        Returns:
            dict.Simbolo: Um símbolo que define um identificador
        """
        for elem in self.tabela_pilha:
            #print(elem)
            if elem['lexema'] == lexema:
                return elem

    
    def checa_tabela_reversed(self, lexema):
        """
        Verifica se há o lexema na pilha contrária

        Args:
            lexema (str): Nome do identificador

        Returns:
            dict.Simbolo: Um símbolo que define um identificador
        """
        for elem in reversed(self.tabela_pilha):
            #print(elem)
            if elem['lexema'] == lexema:
                return elem


    def ret_func(self):
        """
        Retorna a última função declarada

        Returns:
            str: lexema da função
        """
        for elemento in reversed(self.tabela_pilha):
            if elemento.get('tipo_iden') in ['func_i','func_b']:
                return elemento
        return None


    def deleta_escopo(self, escopo):
        """ 
        Remove escopo

        Args:
            escopo (int): nível de escopo
        """
        self.tabela_pilha = [elem for elem in self.tabela_pilha if elem['escopo']!=escopo]

