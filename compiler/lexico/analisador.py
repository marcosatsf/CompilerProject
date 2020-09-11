from tabela_tokens import TabelaTokens

class AnalisadorLexico:
    def __init__(self, dados):
        self.indice = 0
        self.lista_tokens = []
        self.tabela_tokens = TabelaTokens().tabela_tokens
        self.palavra = dados
        self.caractere_atual = self.__get_next()

    def __ret_token(self,lexema,simbolo,linha):
        return {'lexema':lexema,'simbolo':simbolo,'linha':linha}        

    def __get_next(self):
        self.indice
        self.indice+=1
        return self.palavra[self.indice-1]

    def beauty_print(self):
        for each in self.lista_tokens:
            print(each)

    def pega_token(self):
        while self.indice <= len(self.palavra):
            if self.caractere_atual.isdigit():
                self.__trata_digito()
            elif self.caractere_atual.isalpha():
                self.__trata_iden_reserva()
            elif self.caractere_atual == ':':
                self.__trata_atribuicao()
            elif self.caractere_atual in ['+','-','*']:
                self.__trata_op_arit()
            elif self.caractere_atual in ['<','>','=','!']:
                self.__trata_op_relac()
            elif self.caractere_atual in ['(',';',')','.',',']:
                self.__trata_pontuacao()
            else:
                try:
                    if self.caractere_atual == ' ':
                        self.caractere_atual = self.__get_next()
                    else:
                        print(f'Caractere atual : {self.caractere_atual}')
                        break
                except IndexError:
                    break
                #raise AttributeError("ERRO, análise léxica encontrou um erro na linha X")
        
    def __trata_digito(self):
        num = self.caractere_atual
        self.caractere_atual = self.__get_next()
        while self.caractere_atual.isdigit():
            num = num + self.caractere_atual
            self.caractere_atual = self.__get_next()
        self.lista_tokens.append(self.__ret_token(num,self.tabela_tokens['numero'],0))

    def __trata_iden_reserva(self):
        c = self.caractere_atual
        self.caractere_atual = self.__get_next()
        while self.caractere_atual.isalpha() or self.caractere_atual.isdigit() or self.caractere_atual == '_':
            c = c + self.caractere_atual
            self.caractere_atual = self.__get_next()
        try:
            self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens[c],0))
        except KeyError:
            self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens['identificador'],0))

    def __trata_atribuicao(self):
        c = self.caractere_atual
        self.caractere_atual = self.__get_next()
        if self.caractere_atual == '=':
            c = c + self.caractere_atual
            self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens[c],0))
            self.caractere_atual = self.__get_next()
        else:
            self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens[c],0))

    def __trata_op_arit(self):
        self.lista_tokens.append(self.__ret_token(self.caractere_atual,self.tabela_tokens[self.caractere_atual],0))
        self.caractere_atual = self.__get_next()

    def __trata_op_relac(self):
        if self.caractere_atual == '>':
            c = self.caractere_atual
            self.caractere_atual = self.__get_next()
            if self.caractere_atual == '=':
                self.lista_tokens.append(self.__ret_token(c+self.caractere_atual,self.tabela_tokens[c+self.caractere_atual],0))
                self.caractere_atual = self.__get_next()
            else:
                self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens[c],0))
        elif self.caractere_atual == '<':
            c = self.caractere_atual
            self.caractere_atual = self.__get_next()
            if self.caractere_atual == '=':
                self.lista_tokens.append(self.__ret_token(c+self.caractere_atual,self.tabela_tokens[c+self.caractere_atual],0))
                self.caractere_atual = self.__get_next()
            else:
                self.lista_tokens.append(self.__ret_token(c,self.tabela_tokens[c],0))
        elif self.caractere_atual == '!':
            c = self.caractere_atual
            self.caractere_atual = self.__get_next()
            if self.caractere_atual == '=':
                self.lista_tokens.append(self.__ret_token(c+self.caractere_atual,self.tabela_tokens[c+self.caractere_atual],0))
                self.caractere_atual = self.__get_next()
        elif self.caractere_atual == '=':
            self.lista_tokens.append(self.__ret_token(self.caractere_atual,self.tabela_tokens[self.caractere_atual],0))
            self.caractere_atual = self.__get_next()

    def __trata_pontuacao(self):
        self.lista_tokens.append(self.__ret_token(self.caractere_atual,self.tabela_tokens[self.caractere_atual],0))
        try: 
            self.caractere_atual = self.__get_next()
        except IndexError:
            pass