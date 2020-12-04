
from erros import Erro

from reader import Reader
from lexico import AnalisadorLexico
from semantico import AnalisadorSemantico
from geracao_codigo import GeracaoCodigo

class AnalisadorSintatico:
    def __init__(self, file_string, file_name):
        # Lê o texto
        self.texto = Reader(file_string)
        self.file_name = file_name
        # Identificadores
        # "prog",     #0
        # "var",      #1
        # "proc",     #2
        # "func_b",   #3
        # "func_i",   #4


    def run_analyzer(self):
        try:
            # Instancia o analisador com o programa já formatado
            #print(self.texto.get_programa_formatted())
            self.lexico = AnalisadorLexico(self.texto.get_programa_formatted())    
            # Realiza a quebra em tokens
            self.lexico.pega_token()
            #self.lexico.beauty_print()
            self.token_idx = -1

            self.semantico = AnalisadorSemantico()

            self.alg_sintatico()

            ##self.semantico.print_table()
            return "Compilado com sucesso!"
        except Exception as err:
            return err


    # def raise_error_exp_got(self, exp, got, line):
    #     return f"Esperado {exp}, encontrado \'{got}\' na linha {line}!"


    # def raise_error_texto(self, texto, line):
    #     return f"{texto} na linha {line}!"


    def __get_next_token(self):
        self.token_idx += 1
        if self.token_idx == len(self.lexico.lista_tokens):
            raise AttributeError('Fim de arquivo, sem ponto final!')
        if self.lexico.lista_tokens[self.token_idx].get('simbolo') == 'serro':
            raise Exception(self.lexico.lista_tokens[self.token_idx].get('lexema'))
        self.semantico.agg_token(self.lexico.lista_tokens[self.token_idx])
        # imprime no console
        print(self.lexico.lista_tokens[self.token_idx])
        return self.lexico.lista_tokens[self.token_idx]
     

    def alg_sintatico(self):
        # GERA CÓDIGO
        self.g_codigo = GeracaoCodigo()
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sprograma':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                # INSERE TABELA (lexema)
                info_guardado = (self.token_lido.get('lexema'), 'prog')
                self.semantico.insere_tabela(self.token_lido.get('lexema'), tipo_iden="prog")
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'sponto_vírgula':
                    # GERA CÓDIGO
                    self.g_codigo.traduz(instrucao="START")
                    self.g_codigo.inc_alocacao()
                    self.g_codigo.aloca_mem_inicio()

                    self.alg_analisa_bloco()
                    if self.token_lido.get('simbolo') == 'sponto':
                        try:
                            self.token_lido = self.__get_next_token()
                        except AttributeError:
                            # SUCESSO
                            self.g_codigo.acessa_mem(info_guardado)
                            self.g_codigo.desaloc_mem(info_guardado)
                            self.g_codigo.desaloc_mem_inicio()
                            self.g_codigo.traduz(instrucao="HLT")
                            self.g_codigo.codigo2txt(self.file_name)
                            return 0
                        # ERRO 
                        raise AttributeError('Token após ponto final!')
                    else:
                        # ERRO
                        raise AttributeError(Erro.raise_error_exp_got('\'.\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO
                    raise AttributeError(Erro.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('nome do programa',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('programa',self.token_lido.get('lexema'),self.token_lido.get('linha')))


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
                        raise AttributeError(Erro.raise_error_exp_got(';',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                self.g_codigo.aloca_mem(self.semantico.pesquisa_progfuncproc())
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_var(self):
        while True:
            if self.token_lido.get('simbolo') == 'sidentificador':
                # pesquisa duplicvar tabela (lexema)
                if not self.semantico.pesquisa_duplic_var_tabela(self.token_lido.get('lexema')):
                    self.semantico.insere_tabela(self.token_lido.get('lexema'), tipo_iden="var", pos_pilha=self.g_codigo.get_alocacao())
                    self.g_codigo.inc_alocacao()
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') in ['sdoispontos','svírgula']:
                        if self.token_lido.get('simbolo') == 'svírgula': 
                            self.token_lido = self.__get_next_token()
                            if self.token_lido.get('simbolo') == 'sdoispontos': 
                                # ERRO
                                raise AttributeError(Erro.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                    else:
                        # ERRO
                        raise AttributeError(Erro.raise_error_exp_got(', ou :',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO SEMANTICO
                    raise AttributeError(Erro.raise_error_texto(f"\"{self.token_lido.get('lexema')}\" já é utilizado por variável|função|procedimento|programa",self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))

            if self.token_lido.get('simbolo') == 'sdoispontos':
                break

        self.token_lido = self.__get_next_token()
        self.alg_analisa_tipo()


    def alg_analisa_tipo(self):
        if not self.token_lido.get('simbolo') in ['sinteiro','sbooleano']:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('inteiro ou booleano',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            self.semantico.add_tipo(self.token_lido.get('lexema'))
            print(self.semantico.semantico_tabela.tabela_pilha)
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
                    raise AttributeError(Erro.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            
            self.token_lido = self.__get_next_token()
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('inicio',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_comando_simples(self):
        if self.semantico.verificar_retorno():
            # ERRO SEMANTICO
            raise AttributeError(Erro.raise_error_texto(f"Código inalcançável",self.token_lido.get('linha')))
        elif self.token_lido.get('simbolo') == 'sidentificador':
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
        tipo_iden, tipo, store_posicao = self.semantico.pesquisa_declvarprocfunc_tabela(self.token_lido.get('lexema'))
        token_var = self.token_lido.get('lexema')
        if not tipo_iden:
            # ERRO SEMANTICO
            raise AttributeError(Erro.raise_error_texto(f"Não há declaração de procedimento ou variável de \"{self.token_lido.get('lexema')}\"",self.token_lido.get('linha'))) 
        if tipo_iden == "proc":
            self.alg_analisa_ch_procedimento()
            self.token_lido = self.__get_next_token()
        else:
            self.token_lido = self.__get_next_token()
            if tipo_iden in ["var", "func"] and self.token_lido.get('simbolo') == 'satribuição':
                self.alg_analisa_atribuicao(tipo)
                self.g_codigo.traduz(instrucao="STR", arg1=store_posicao)
                if tipo_iden == "func" and (self.semantico.analise_funcao[-1]['lexema'] == token_var):
                    self.semantico.set_funcao_retorno(True)
                    # GERAÇÃO CÓDIGO
                    #self.g_codigo.traduz(instrucao="JMP", arg1=self.g_codigo.access_jmp())
                    self.g_codigo.acessa_mem((token_var, tipo_iden))
                    self.g_codigo.traduz(instrucao="RETURN")
            else:
                ret_erro = "variável" if tipo_iden == "var" else "função"
                # ERRO SEMANTICO
                raise AttributeError(Erro.raise_error_texto(f"Impossível chamar a {ret_erro} \"{token_var}\", pois não local de retorno",self.token_lido.get('linha'))) 
    

    def alg_analisa_leia(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                # pesquisa declvar tabela
                if var_pilha := self.semantico.pesquisa_declvar_tabela(self.token_lido.get('lexema')):
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                        # GERAÇÃO CÓDIGO
                        self.g_codigo.traduz(instrucao="RD")
                        self.g_codigo.traduz(instrucao="STR", arg1=var_pilha)

                        self.token_lido = self.__get_next_token()
                    else:
                        # ERRO
                        raise AttributeError(Erro.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO SEMANTICO
                    raise AttributeError(Erro.raise_error_texto(f"Não há variável válida para ler",self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('\'(\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_escreva(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            if self.token_lido.get('simbolo') == 'sidentificador':
                # pesquisa declvarfunc tabela - escreva(x)
                if simbolo := self.semantico.pesquisa_declvarfunc_tabela(self.token_lido.get('lexema')):
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                        # GERAÇÃO CÓDIGO
                        if simbolo.get("tipo_iden") == 'var':
                            self.g_codigo.traduz(instrucao="LDV", arg1=simbolo.get("pos_pilha"))
                        else:
                            self.g_codigo.traduz(instrucao="LDV", arg1=0)
                        self.g_codigo.traduz(instrucao="PRN")

                        self.token_lido = self.__get_next_token()
                    else:
                        # ERRO
                        raise AttributeError(Erro.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO SEMANTICO
                    raise AttributeError(Erro.raise_error_texto(f"Não há variável válida para escrever",self.token_lido.get('linha')))
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('uma variável',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('\'(\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_enquanto(self):
        # GERA CÓDIGO
        auxrot1 = self.g_codigo.get_rotulo()
        self.g_codigo.traduz(rotulo=self.g_codigo.get_rotulo() , instrucao="NULL")
        self.g_codigo.inc_rotulo()
        # self.token_lido = self.__get_next_token()
        # self.alg_analisa_expressao()
        self.alg_analisa_expressao_completa(tipo_necessario='booleano')
        if self.token_lido.get('simbolo') == 'sfaca':
            # GERA CÓDIGO
            auxrot2 = self.g_codigo.get_rotulo()
            self.g_codigo.traduz(instrucao="JMPF", arg1=self.g_codigo.get_rotulo())
            self.g_codigo.inc_rotulo()

            self.token_lido = self.__get_next_token()
            self.alg_analisa_comando_simples()

            # GERA CÓDIGO
            self.g_codigo.traduz(instrucao="JMP", arg1=auxrot1)
            self.g_codigo.traduz(rotulo=auxrot2, instrucao="NULL")
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('faca (início enquanto)',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_se(self):
        # GERAÇÃO CÓDIGO
        auxrot1 = self.g_codigo.get_rotulo()
        self.g_codigo.inc_rotulo()
        auxrot2 = self.g_codigo.get_rotulo()
        self.g_codigo.inc_rotulo()

        self.alg_analisa_expressao_completa(tipo_necessario='booleano')
        if self.token_lido.get('simbolo') == 'sentao':
            self.g_codigo.traduz(instrucao="JMPF", arg1=auxrot1)
            self.token_lido = self.__get_next_token()
            self.alg_analisa_comando_simples()
            self.semantico.set_if()
            self.semantico.set_funcao_retorno(False)
            if self.token_lido.get('simbolo') == 'ssenao':
                self.g_codigo.traduz(instrucao="JMP", arg1=auxrot2)
                self.g_codigo.traduz(rotulo=auxrot1, instrucao="NULL")
                self.token_lido = self.__get_next_token()
                self.alg_analisa_comando_simples()
                self.semantico.verifica_if()
                self.g_codigo.traduz(rotulo=auxrot2, instrucao="NULL")
            else:
                self.g_codigo.traduz(rotulo=auxrot1, instrucao="NULL")
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('entao (início se)',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_subrotina(self):
        flag = False
        auxrot = None
        if self.token_lido.get('simbolo') in ['sfuncao','sprocedimento']:
            # GERA CÓDIGO
            auxrot = self.g_codigo.get_rotulo()
            self.g_codigo.traduz(instrucao="JMP", arg1=self.g_codigo.get_rotulo())
            self.g_codigo.inc_rotulo()
            flag = True
            #if funcao,proc - geração de código
        while self.token_lido.get('simbolo') in ['sfuncao','sprocedimento']:
            if self.token_lido.get('simbolo') == 'sprocedimento':
                self.alg_analisa_decl_proc()
            else:
                self.alg_analisa_decl_funcao()
            if self.token_lido.get('simbolo') == 'sponto_vírgula':
                self.token_lido = self.__get_next_token()
            else:
                # ERRO
                raise AttributeError(Erro.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        
        if flag:
            # GERA CÓDIGO
            self.g_codigo.traduz(rotulo=auxrot, instrucao="NULL")


    def alg_analisa_decl_proc(self):
        self.token_lido = self.__get_next_token()
        if self.token_lido.get('simbolo') == 'sidentificador':
            if not self.semantico.pesquisa_declprocfun_tabela(self.token_lido.get('lexema')):
                info_guardado = (self.token_lido.get('lexema'), 'proc')
                self.semantico.insere_tabela(self.token_lido.get('lexema'), tipo_iden="proc", rotulo=self.g_codigo.get_rotulo())
                # GERA CÓDIGO
                self.g_codigo.traduz(rotulo=self.g_codigo.get_rotulo(), instrucao="NULL")
                self.g_codigo.inc_rotulo()

                self.semantico.ramifica_escopo()
                self.token_lido = self.__get_next_token()
                if self.token_lido.get('simbolo') == 'sponto_vírgula':
                    self.alg_analisa_bloco()
                    # GERAÇÃO CÓDIGO
                    self.g_codigo.acessa_mem(info_guardado)
                    self.g_codigo.desaloc_mem(info_guardado)
                    self.g_codigo.traduz(instrucao="RETURN")
                else:
                    # ERRO
                    raise AttributeError(Erro.raise_error_exp_got('\';\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO SEMANTICO
                raise AttributeError(Erro.raise_error_texto(f"Nome do procedimento \"{self.token_lido.get('lexema')}\" já existente",self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('nome do procedimento',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        # Retorna nível, marca ou galho
        self.semantico.enraiza_escopo()


    def alg_analisa_decl_funcao(self):
        self.token_lido = self.__get_next_token()
        # Ramifica - apostila
        if self.token_lido.get('simbolo') == 'sidentificador':
            if not self.semantico.pesquisa_declprocfun_tabela(self.token_lido.get('lexema')):
                nome_func = self.token_lido.get('lexema')
                self.token_lido = self.__get_next_token() 
                if self.token_lido.get('simbolo') == 'sdoispontos':
                    self.token_lido = self.__get_next_token()
                    if self.token_lido.get('simbolo') in ['sinteiro','sbooleano']:
                        # verificar qual o tipo do retorno
                        if self.token_lido.get('simbolo') == 'sinteiro':
                            self.semantico.insere_tabela(nome_func, tipo_iden="func_i", rotulo=self.g_codigo.get_rotulo())
                            #self.semantico.add_tipo("func", "func_i")
                        else:
                            self.semantico.insere_tabela(nome_func, tipo_iden="func_b", rotulo=self.g_codigo.get_rotulo())
                            #self.semantico.add_tipo("func", "func_b")
                        info_guardado = (nome_func, 'func')
                        # GERA CÓDIGO
                        self.g_codigo.traduz(rotulo=self.g_codigo.get_rotulo(), instrucao="NULL")
                        self.g_codigo.inc_rotulo()
                        #self.g_codigo.push_jmp(self.g_codigo.get_rotulo(), info_guardado)
                        #self.g_codigo.inc_rotulo()

                        self.semantico.ramifica_escopo()

                        self.token_lido = self.__get_next_token()
                        if self.token_lido.get('simbolo') == 'sponto_vírgula':
                            self.semantico.trig_funcao(True) # inicia analise função
                            self.alg_analisa_bloco()
                            ret_func = self.semantico.trig_funcao() # finaliza analise função
                            if not ret_func.get('retorno_valido'):
                                # ERRO SEMANTICO
                                raise AttributeError(Erro.raise_error_texto(f"Pode não haver retorno da função \"{ret_func.get('lexema')}\", verifique todos os caminhos!"))
                            # GERAÇÃO CÓDIGO
                            #self.g_codigo.traduz(rotulo=self.g_codigo.pop_jmp(info_guardado) ,instrucao="NULL")                
                            self.g_codigo.desaloc_mem(info_guardado)
                            #self.g_codigo.traduz(instrucao="RETURN")
                    else:
                        # ERRO
                        raise AttributeError(Erro.raise_error_exp_got('inteiro ou booleano',self.token_lido.get('lexema'),self.token_lido.get('linha')))
                else:
                    # ERRO
                    raise AttributeError(Erro.raise_error_exp_got('\':\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
            else:
                # ERRO SEMANTICO
                raise AttributeError(Erro.raise_error_texto(f"Nome da função \"{self.token_lido.get('lexema')}\" já existente",self.token_lido.get('linha')))
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('nome da função',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        # Retorna nível, marca ou galho
        self.semantico.enraiza_escopo()


    def alg_analisa_expressao(self):
        self.alg_analisa_expressao_simples() # exp simples
        # trocado o 'if' por 'while'
        while self.token_lido.get('simbolo') in ['smaior','smaiorig','sig','smenor','smenorig','sdif']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_expressao_simples() # exp simples


    def alg_analisa_expressao_simples(self):
        if self.token_lido.get('simbolo') in ['smais','smenos']:
            self.semantico.change_token()
            self.token_lido = self.__get_next_token()
        self.alg_analisa_termo() # analisa termo
        while self.token_lido.get('simbolo') in ['smais','smenos', 'sou']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_termo() # analisa termo
 

    def alg_analisa_termo(self):
        self.alg_analisa_fator() # analisa fator
        while self.token_lido.get('simbolo') in ['smult','sdiv','se']:
            self.token_lido = self.__get_next_token()
            self.alg_analisa_fator() # analisa fator


    def alg_analisa_fator(self):
        if self.token_lido.get('simbolo') == 'sidentificador':
            if simbolo := self.semantico.pesquisa_declvarfunc_tabela(self.token_lido.get('lexema')):
                if simbolo.get("tipo_iden") in ["func_i", "func_b"]:
                    # TODO verifica se é função inteiro ou booleano
                    self.alg_analisa_ch_funcao()
                else:
                    self.token_lido = self.__get_next_token()
            else:
                # ERRO SEMANTICO
                raise AttributeError(Erro.raise_error_texto(f"Não há declaração de \"{self.token_lido.get('lexema')}\"",self.token_lido.get('linha')))
        elif self.token_lido.get('simbolo') == 'snumero':
            self.token_lido = self.__get_next_token()
        elif self.token_lido.get('simbolo') == 'snao':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_fator() # analisa fator
        elif self.token_lido.get('simbolo') == 'sabre_parênteses':
            self.token_lido = self.__get_next_token()
            self.alg_analisa_expressao() # analisa exp
            if self.token_lido.get('simbolo') == 'sfecha_parênteses':
                self.token_lido = self.__get_next_token()
            else:
               # ERRO
                raise AttributeError(Erro.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))
        elif self.token_lido.get('lexema') in ['verdadeiro','falso']:
            self.token_lido = self.__get_next_token()
        else:
            # ERRO
            raise AttributeError(Erro.raise_error_exp_got('um fator',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_ch_funcao(self):
        # TODO vc será raidado com a força do goku
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
                raise AttributeError(Erro.raise_error_exp_got('\')\'',self.token_lido.get('lexema'),self.token_lido.get('linha')))


    def alg_analisa_ch_procedimento(self):
        simbolo = self.semantico.checa_tabela_simbolos(self.token_lido.get('lexema'))
        self.g_codigo.traduz(instrucao="CALL", arg1=simbolo['rotulo'])


    def alg_analisa_atribuicao(self, tipo):
        # self.token_lido = self.__get_next_token()
        # self.alg_analisa_expressao()
        self.alg_analisa_expressao_completa(tipo)


    def alg_analisa_expressao_completa(self, tipo_necessario=None):
        self.semantico.trig_leitura_exp() # inicia "gravação" expressão
        self.token_lido = self.__get_next_token()
        self.alg_analisa_expressao()
        self.semantico.trig_leitura_exp() # finaliza "gravação" expressão
        self.semantico.expressao_semantica(tipo_necessario)
        self.g_codigo.traduz_exp(self.semantico.expressao_atual)



