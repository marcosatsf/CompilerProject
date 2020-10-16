from tabela_tokens import TabelaTokens

class AnalisadorLexico:
    def __init__(self, dados):
        self.indice = 0
        self.lista_tokens = []
        self.tabela_tokens = TabelaTokens().tabela_tokens
        self.palavra_tratada = dados[0]
        self.palavra_original = dados[1]
        self.caractere_atual = self.__get_next()
        self.linha = 1
        self.palavra_restante = self.palavra_original.split('\n')

    def __ret_token(self,lexema,simbolo,linha):
        var_palavra = self.palavra_restante
        self.palavra_restante = []
        flag = 0
        for line in var_palavra:
            if not flag:
                if lexema in line:
                    pos = line.index(lexema)
                    res = line[pos+len(lexema):]
                    self.palavra_restante.append(res)
                    flag = 1
                else:
                    self.linha += 1
            else:
                self.palavra_restante.append(line)
        return {'lexema':lexema,'simbolo':simbolo,'linha':self.linha}  

    def __get_next(self):
        self.indice
        self.indice+=1
        return self.palavra_tratada[self.indice-1]

    # def get_next_token(self):
    #     for token in self.lista_tokens:
    #         yield token

    def beauty_print(self):
        for each in self.lista_tokens:
            print(each)

    def get_tokenizer_str(self, error=None):
        string_return = ''
        for tok in self.lista_tokens:
            string_return += str(tok) + '\n'
        if error:
            string_return += error
        return string_return

    def trata_erro(self):
        linha = 0
        qtd_tokens = 0
        # for token in self.lista_tokens:
        self.palavra_original = self.palavra_original.replace('\t', ' ')
        while qtd_tokens < len(self.lista_tokens):
            indice_n = self.palavra_original.find('\n')
            indice_token = self.palavra_original.find(self.lista_tokens[qtd_tokens]["lexema"])
            if indice_n < indice_token:
                linha += 1
                self.palavra_original = self.palavra_original[indice_n+1:]
            else:
                self.palavra_original = self.palavra_original[indice_token+len(self.lista_tokens[qtd_tokens]["lexema"]):]
                qtd_tokens += 1
        indice = 0

        while True:
            bool_para = True
            while self.palavra_original[indice] == '\n' or self.palavra_original[indice] == ' ':
                if self.palavra_original[indice] == '\n':
                    linha += 1
                indice += 1
                bool_para = False
            if self.palavra_original[indice] == '{':
                while self.palavra_original[indice] != '}':
                    if self.palavra_original[indice] == '\n':
                        linha += 1
                    indice += 1
                bool_para = False
            if self.palavra_original[indice] == '/' and self.palavra_original[indice+1] == '*':
                while not (self.palavra_original[indice] == '*' and self.palavra_original[indice+1] == '/'):
                    if self.palavra_original[indice] == '\n':
                        linha += 1
                    indice += 1
                indice += 2
                bool_para = False
            if bool_para:
                break

        return linha


    def pega_token(self):
        while self.indice <= len(self.palavra_tratada):
            if self.caractere_atual.isdigit():
                self.__trata_digito()
            elif self.caractere_atual.isalpha():
                self.__trata_iden_reserva()
            elif self.caractere_atual == ':':
                self.__trata_atribuicao()
            elif self.caractere_atual in ['+','-','*']:
                self.__trata_op_arit()
            elif self.caractere_atual in ['<','>','=','!']:
                try:
                    self.__trata_op_relac()
                except AttributeError as err:
                    self.lista_tokens.append(self.__ret_token(err,self.tabela_tokens['ERRO'],0))
                    break
            elif self.caractere_atual in ['(',';',')','.',',']:
                self.__trata_pontuacao()
            else:
                try:
                    if self.caractere_atual == ' ':
                        self.caractere_atual = self.__get_next()
                    else:
                        if self.caractere_atual in ['{','/']:
                            verify_error_string = f"ERRO no comentário, linha: {self.trata_erro()+1}"
                        else:
                            verify_error_string = f"ERRO, linha: {self.trata_erro()+1}, caractere: {self.caractere_atual}"

                        self.lista_tokens.append(self.__ret_token(verify_error_string,self.tabela_tokens['ERRO'],0))
                        break
                        #raise AttributeError(verify_error_string)
                except IndexError:
                    break

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
            else:
                raise AttributeError(f"ERRO, linha: {self.trata_erro()}, caractere: {c}")
        elif self.caractere_atual == '=':
            self.lista_tokens.append(self.__ret_token(self.caractere_atual,self.tabela_tokens[self.caractere_atual],0))
            self.caractere_atual = self.__get_next()

    def __trata_pontuacao(self):
        self.lista_tokens.append(self.__ret_token(self.caractere_atual,self.tabela_tokens[self.caractere_atual],0))
        try: 
            self.caractere_atual = self.__get_next()
        except IndexError:
            pass