from lexico import AnalisadorLexico
from reader import Reader

class AnalisadorSintatico:
    def __init__(self, file_string):
        # Lê o texto
        self.texto = Reader(file_string)

    def run_analyzer(self):
        try:
            # Instancia o analisador com o programa já formatado
            self.lexico = AnalisadorLexico(self.texto.get_programa_formatted())    
            # Realiza a quebra em tokens
            self.lexico.pega_token()
            #self.lexico.beauty_print()
            self.token_idx = -1

            self.alg_sintatico()
            return "Compilado com sucesso!"
        except Exception as err:
            return err

    def raise_error_exp_got(self, exp, got, line):
        return f"Esperado {exp}, encontrado \'{got}\' na linha {line}!"

    def __get_next_token(self):
        self.token_idx += 1
        if self.token_idx == len(self.lexico.lista_tokens):
            raise AttributeError('Fim de arquivo, sem ponto final!')
        if self.lexico.lista_tokens[self.token_idx].get('simbolo') == 'serro':
            raise Exception(self.lexico.lista_tokens[self.token_idx].get('lexema'))
        print(self.lexico.lista_tokens[self.token_idx])
        return self.lexico.lista_tokens[self.token_idx]

        
    def alg_sintatico(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sprograma':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'sponto_vírgula':
                    self.alg_analisa_bloco()
                    if self.token_lido.get('simbolo') == 'sponto':
                        try:
                            self.token_lido = self.__get_next_token()
                        except AttributeError:
                            # SUCESSO
                            return 0
                        # ERRO 
                        raise AttributeError('Token após ponto final!')
                    else:
                        # ERRO
                        raise AttributeError(self.raise_error_exp_got('\'.\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('nome do programa',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('programa',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_bloco(self):
        self.token_lido = self.__get_next_token()
        self.alg_analisa_outro_planeta_var()
        self.alg_analisa_subrotina()
        self.alg_analisa_comandos()

    def alg_analisa_outro_planeta_var(self):
        if self.token_lido.get('simbolo') == 'svar':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                while self.token_lido.get('simbolo') == 'sidentificador':
                    self.alg_analisa_var()
                    if self.token_lido.get('simbolo') == 'sponto_vírgula':
                        self.token_lido = self.__get_next_token()
                    else:
                        # ERRO
                        raise AttributeError(self.raise_error_exp_got(';',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_var(self):
        while True:
            if self.token_lido.get('simbolo') == 'sidentificador':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') in ['sdoispontos','svírgula']:
                    if self.token_lido.get('simbolo') == 'svírgula': 
                        self.token_lido = self.__get_next_token()
                        if self.token_lido.get('simbolo') == 'sdoispontos': 
                            # ERRO
                            raise AttributeError(self.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got(', ou :',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))

            if self.token_lido.get('simbolo') == 'sdoispontos':
                break

        self.token_lido = self.__get_next_token()
        self.alg_analisa_tipo()

    def alg_analisa_tipo(self):
        if not self.token_lido.get('simbolo') in ['sinteiro','sbooleano']:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('inteiro ou booleano',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            self.token_lido = self.__get_next_token()

    def alg_analisa_comandos(self):
        if self.token_lido.get('simbolo') == 'sinicio':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_comando_simples()
            while self.token_lido.get('simbolo') != 'sfim':
                if self.token_lido.get('simbolo') == 'sponto_vírgula':
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') != 'sfim':
                        self.alg_analisa_comando_simples()
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            
            self.token_lido = self.__get_next_token()
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('inicio',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_comando_simples(self):
        if self.token_lido.get('simbolo') == 'sidentificador':
            self.alg_analisa_atrib_chproc()
        elif self.token_lido.get('simbolo') == 'sse':
            self.alg_analisa_se()
        elif self.token_lido.get('simbolo') == 'senquanto':
            self.alg_analisa_enquanto()
        elif self.token_lido.get('simbolo') == 'sleia':
            self.alg_analisa_leia()
        elif self.token_lido.get('simbolo') == 'sescreva':
            self.alg_analisa_escreva()
        else:
            self.alg_analisa_comandos()

    def alg_analisa_atrib_chproc(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'satribuição':
            self.alg_analisa_atribuicao()
        else:
            self.alg_analisa_ch_procedimento()
    
    def alg_analisa_leia(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                    self.token_lido = self.__get_next_token()
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('\'(\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_escreva(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                    self.token_lido = self.__get_next_token()
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('\'(\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_enquanto(self):
        self.token_lido = self.__get_next_token()
        self.alg_analisa_expressao()
        if self.token_lido.get('simbolo') == 'sfaca':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_comando_simples()
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('faca (início enquanto)',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_se(self):
        self.token_lido = self.__get_next_token()
        self.alg_analisa_expressao()
        if self.token_lido.get('simbolo') == 'sentao':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_comando_simples()
            if self.token_lido.get('simbolo') == 'ssenao':
                self.token_lido = self.__get_next_token()
                self.alg_analisa_comando_simples()
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('entao (início se)',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_subrotina(self):
        flag = 0
        if self.token_lido.get('simbolo') in ['sfuncao','sprocedimento']:
            #if funcao,proc - geração de código
            pass
        while self.token_lido.get('simbolo') in ['sfuncao','sprocedimento']:
            if self.token_lido.get('simbolo') == 'sprocedimento':
                self.alg_analisa_decl_proc()
            else:
                self.alg_analisa_decl_funcao()
            if self.token_lido.get('simbolo') == 'sponto_vírgula':
                self.token_lido = self.__get_next_token()
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        
        if flag:
            # semantico
            pass

    def alg_analisa_decl_proc(self):
        self.token_lido = self.__get_next_token() 
        if self.token_lido.get('simbolo') == 'sidentificador':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sponto_vírgula':
                self.alg_analisa_bloco()
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('nome do procedimento',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_decl_funcao(self):
        self.token_lido = self.__get_next_token() 
        if self.token_lido.get('simbolo') == 'sidentificador':
            self.token_lido = self.__get_next_token() 
            if self.token_lido.get('simbolo') == 'sdoispontos':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') in ['sinteiro','sbooleano']:
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') == 'sponto_vírgula':
                        self.alg_analisa_bloco()
                else:
                    # ERRO
                    raise AttributeError(self.raise_error_exp_got('inteiro ou booleano',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('\':\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('nome da função',self.token_lido.get('lexema'),self.token_lido.get('linha')))

    def alg_analisa_expressao(self):
        self.alg_analisa_expressao_simples()
        if self.token_lido.get('simbolo') in ['smaior','smaiorig','sig','smenor','smenorig','sdif']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_expressao_simples()

    def alg_analisa_expressao_simples(self):
        if self.token_lido.get('simbolo') in ['smais','smenos']:
            self.token_lido = self.__get_next_token()
        self.alg_analisa_termo()
        while self.token_lido.get('simbolo') in ['smais','smenos', 'sou']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_termo()

    def alg_analisa_termo(self):
        self.alg_analisa_fator()
        while self.token_lido.get('simbolo') in ['smult','sdiv','se']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_fator()

    def alg_analisa_fator(self):
        if self.token_lido.get('simbolo') == 'sidentificador':
            self.alg_analisa_ch_funcao()
        elif self.token_lido.get('simbolo') == 'snumero':
            ## POSSIVEL BUG HEHEHE
            self.token_lido = self.__get_next_token()
        elif self.token_lido.get('simbolo') == 'snao':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_fator()
        elif self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_expressao()
            if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                self.token_lido = self.__get_next_token()
            else:
               # ERRO
                raise AttributeError(self.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        elif self.token_lido.get('lexema') in ['verdadeiro','falso']:
            self.token_lido = self.__get_next_token()
        else:
            # ERRO
            raise AttributeError(self.raise_error_exp_got('um fator',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_ch_funcao(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()

            while self.token_lido.get('simbolo') == 'snumero':
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'svírgula':
                    self.token_lido = self.__get_next_token()
            
            if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                self.token_lido = self.__get_next_token()
            else:
                # ERRO
                raise AttributeError(self.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_ch_procedimento(self):
        pass

    def alg_analisa_atribuicao(self):
        self.token_lido = self.__get_next_token()
        self.alg_analisa_expressao()

