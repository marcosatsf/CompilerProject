from erros import Erro
from tabela_simbolos import TabelaSimbolos

class AnalisadorSemantico:
    def __init__(self):
        self.semantico_tabela = TabelaSimbolos()
        self.expressao = {
            "str" : "",
            "struct" : [],
            "str_pos" : [],
            "struct_pos" : []
        }
        self.precedencia = {
            0 : ['-u', '+u', 'nao'],
            1 : ['*', 'div'],
            2 : ['-', '+'],
            3 : ['>', '>=', '<', '<='],
            4 : ['=', '!='],
            5 : ['e'],
            6 : ['ou'],
            7 : ['(']
        }
        # operador : (aceita tipo, quantos op, retorno)
        self.op_tipo = {
            'nao' : ('booleano', 1, 'booleano'),
            '-u' : ('inteiro', 1, 'inteiro'),
            '+u' : ('inteiro', 1, 'inteiro'),
            '*' : ('inteiro', 2, 'inteiro'),
            'div' : ('inteiro', 2, 'inteiro'),
            '-' : ('inteiro', 2, 'inteiro'),
            '+' : ('inteiro', 2, 'inteiro'),
            '>' : ('inteiro', 2, 'booleano'),
            '>=' : ('inteiro', 2, 'booleano'),
            '<' : ('inteiro', 2, 'booleano'),
            '<=' : ('inteiro', 2, 'booleano'),
            '=' : ('independente', 2, 'booleano'),
            '!=' : ('independente', 2, 'booleano'),
            'e' : ('booleano', 2, 'booleano'),
            'ou' : ('booleano', 2, 'booleano')
        }
        self.escopo = 0
        self.lendo_exp = False
        self.analise_funcao = []


    def ramifica_escopo(self):
        """
        Sobe o escopo de análise
        """
        self.escopo += 1


    def enraiza_escopo(self):
        """
        Desce o escopo de análise
        """
        self.semantico_tabela.deleta_escopo(self.escopo)
        self.escopo -= 1


    def add_tipo(self, tipo):
        """
        Adiciona tipo às variáveis

        Args:
            tipo (str): tipo a ser adicionado
        """
        #if identificador == "var":
        self.semantico_tabela.add_tipo_tabela_var(tipo, self.escopo)
        # elif identificador == "func":
        #     self.semantico_tabela.add_tipo_tabela_func(tipo, self.escopo)


    def insere_tabela(self, lexema, tipo_iden, rotulo=None, pos_pilha=None):
        """
        Insere uma estrutura de identificador na tabela

        Args:
            lexema (str): lexema do identificador
            tipo_iden (str): tipo do identificador (var | proc | prog | ...)
            rotulo (str, optional): Rótulo ou endereço da instrução. Defaults to None.
        """
        # Onde:
        # – Rótulo: Para geração de código
        self.semantico_tabela.add_tabela(lexema, tipo_iden, self.escopo, rotulo=rotulo, pos_pilha=pos_pilha)
        # DONE?

    def pesquisa_progfuncproc(self):
        return self.semantico_tabela.ret_nao_var()
    
    def pesquisa_duplic_var_tabela(self, lexema):
        """
        Verifica se há duplicidade de var no mesmo escopo ou se já existe
        algum identificador, com mesmo nome, fora deste escopo

        Args:
            lexema (str): lexema do identificador

        Returns:
            bool : Se existe duplicidade ou não
        """
        simbolo = self.semantico_tabela.checa_tabela(lexema)
        #print(simbolo, self.escopo)
        try:
            if simbolo.get('tipo_iden') == "var" and \
                simbolo.get('escopo') == self.escopo:
                return True
            if simbolo.get('tipo_iden') != "var" and \
                simbolo.get('escopo') != self.escopo:
                return True
        except Exception:
            pass
        return False
        # DONE?
        

    def pesquisa_declvar_tabela(self, lexema):
        # Na utilização de uma variável pesquisa se a
        # mesma foi declarada, se é uma variável e se está
        # visível no escopo.
        simbolo = self.semantico_tabela.checa_tabela(lexema)
        try:
            if simbolo.get('tipo_iden') == "var":
                return simbolo["pos_pilha"]
        except Exception:
            pass
        return False
        # DONE?


    def pesquisa_declvarfunc_tabela(self, lexema):
        # Verifica se um identificador é uma função ou uma
        # variável e se está visível no escopo de utilização.
        simbolo = self.semantico_tabela.checa_tabela(lexema)
        try:
            if simbolo.get('tipo_iden') in ["func_i", "func_b", "var"]:
                return simbolo
        except Exception:
            pass
        return False
        # DONE?


    def pesquisa_declvarprocfunc_tabela(self, lexema):
        # Verifica se um identificador é uma função ou uma
        # variável e se está visível no escopo de utilização.
        simbolo = self.semantico_tabela.checa_tabela(lexema)
        try:
            if simbolo.get('tipo_iden') == "proc":
                return "proc", None, None
            if simbolo.get('tipo_iden') == "var":
                return "var", simbolo.get('tipo'), simbolo.get('pos_pilha')
            if simbolo.get('tipo_iden') in ['func_i', 'func_b']:
                return "func", self.__ret_funcao_tipo(simbolo.get('tipo_iden')), 0
        except Exception:
            pass
        return False, None
        # DONE?


    def pesquisa_declprocfun_tabela(self, lexema):
        # Verifica se há duplicidade na declaração de um
        # procedimento.
        # Verifica se há duplicidade na declaração de uma
        # função.
        simbolo = self.semantico_tabela.checa_tabela(lexema)
        try:
            if isinstance(simbolo, dict):
            #if simbolo.get('tipo_iden') == "proc":
                return True
        except Exception:
            pass
        return False
        # DONE?

    def checa_tabela_simbolos(self, lexema):
        """
        Retorna o elemento da tabela de símbolos

        Args:
            lexema (str): lexema a ser pesquisado

        Returns:
            dict: estrutura do lexema pesquisado
        """
        return self.semantico_tabela.checa_tabela(lexema)


    def print_table(self):
        """
        Usada para fins de debug (imprime na tela a tabela de símbolos atual)
        """
        print(self.semantico_tabela.tabela_pilha)

    
    def expressao_semantica(self, tipo_necessario):
        """
        Realiza a transformação para a expressão pósfixa, verificando se
        os tipos são condizentes com a operação

        Args:
            tipo_necessario (str): tipo necessário para condizer com 
            a expressão

        Raises:
            AttributeError: Expressão inválida

        Returns:
            str : tipo da expressão
        """
        linha = self.expressao['struct'][0]['linha']
        # Analisa expressão semanticamente
        struct = self.expressao['struct'].pop()
        self.expressao['str'] = self.expressao['str'].removesuffix(struct['lexema'])

        self.expressao['struct_pos'] = {elem['lexema']:self.semantico_tabela.checa_tabela(elem['lexema']) for elem in self.expressao['struct'] if self.semantico_tabela.checa_tabela(elem['lexema'])}
        #print(self.expressao,end='\n\n')

        # armazena os tipos (inteiro ou booleano)
        valid_exp = []
        # armazena os operadores para análise posfixa
        pilha_exp = []

        # Avalia precedência na pilha de operadores
        def ret_precedencia(lexema):
            # print(pilha_exp)
            for el in self.precedencia.keys():
                if lexema in self.precedencia[el]:
                    return el

        # Desempilha pilha de operadores
        def desempilha_operadores(precedencia=False):
            while len(pilha_exp)>0:
                if pilha_exp[-1] == "(":
                    if not precedencia:
                        pilha_exp.pop()
                    break
                op = pilha_exp.pop()
                self.expressao['str_pos'].append(op)
                # TODO inserir tipo do operador
                valid_exp.append(op)

        # Analisa expressão válida
        def analisa_exp_valida(elementos):
            pilha_resultado = []
            #print(elementos)
            for elemento in elementos:
                # é um elemento inteiro ou booleano?
                if elemento in ['inteiro', 'booleano']:
                    # insere elemento
                    pilha_resultado.append(elemento)
                # está presente nos operadores?
                elif elemento in self.op_tipo.keys():
                    # unário?
                    try: 
                        if self.op_tipo[elemento][1] == 1:
                            elem1 = pilha_resultado.pop()
                            # condiz com o tipo do elemento anterior?
                            if self.op_tipo[elemento][0] == elem1:
                                pilha_resultado.append(self.op_tipo[elemento][2])
                            else: 
                                # ERRO SEMANTICO
                                raise AttributeError(Erro.raise_error_texto("Expressão inválida",linha))
                        else:
                            elem1 = pilha_resultado.pop()
                            elem2 = pilha_resultado.pop()
                            # aceita tanto bool quanto int?
                            if self.op_tipo[elemento][0] == 'independente':
                                # elementos têm tipos iguais?
                                if elem1 == elem2:
                                    pilha_resultado.append(self.op_tipo[elemento][2])
                                else:
                                    # ERRO SEMANTICO
                                    raise AttributeError(Erro.raise_error_texto("Expressão inválida",linha))
                            # condiz com o tipo dos elementos anteriores?
                            elif self.op_tipo[elemento][0] == elem1 == elem2:
                                pilha_resultado.append(self.op_tipo[elemento][2])
                            else:
                                # ERRO SEMANTICO
                                raise AttributeError(Erro.raise_error_texto("Expressão inválida",linha))
                    # tentativa de pop em pilha vazia
                    except IndexError:
                        raise AttributeError(Erro.raise_error_texto("Expressão inválida",linha))
            #print(len(pilha_resultado), pilha_resultado[0])
            if len(pilha_resultado) != 1:
                raise AttributeError(Erro.raise_error_texto("Expressão inválida",linha))
            return pilha_resultado[0]


        # Realiza a organização da pós fixa
        for elem in self.expressao['struct']:
            #print(elem)
            if elem['simbolo'] in ['sidentificador', 'snumero', 'sverdadeiro', 'sfalso']:
                self.expressao['str_pos'].append(elem['lexema'])
                if elem['simbolo'] == 'sidentificador':
                    simbolo = self.semantico_tabela.checa_tabela_reversed(elem['lexema'])
                    if simbolo.get('tipo_iden') in ['func_i','func_b']:
                        valid_exp.append(self.__ret_funcao_tipo(simbolo.get('tipo_iden')))
                    else:
                        valid_exp.append(simbolo['tipo'])
                elif elem['simbolo'] == 'snumero':
                    valid_exp.append('inteiro')
                else:
                    valid_exp.append('booleano')
            else:
                # É fecha parenteses - fim expressão?
                if elem['lexema'] != ')':
                    # É abre parenteses ? e (É pilha não vazia e temos 2 termos
                    # seguidos de "não"?)
                    if elem['lexema'] != '(' and \
                        ((len(pilha_exp) > 0) and \
                        not (pilha_exp[-1] == elem['lexema'] == 'nao')):
                        # É pilha não vazia e temos precedência
                        # menor ou igual ao atual?
                        if (len(pilha_exp) > 0) and \
                            (not (ret_precedencia(pilha_exp[-1]) > ret_precedencia(elem['lexema']))):
                            desempilha_operadores(precedencia=True)
                    pilha_exp.append(elem['lexema'])
                else:
                    desempilha_operadores()
        while len(pilha_exp)>0:
            op = pilha_exp.pop()
            self.expressao['str_pos'].append(op)
            valid_exp.append(op)
            #print(op, valid_exp)

        print(self.expressao["str_pos"],end='\n\n')
        print(self.expressao["struct"],end='\n\n')
        print(self.expressao["struct_pos"],end='\n\n')

        self.expressao_atual = self.expressao
        tipo_final = analisa_exp_valida(valid_exp)
        if tipo_necessario != None:
            # print(tipo_necessario, tipo_final)
            if tipo_necessario != tipo_final:
                raise AttributeError(
                    Erro.raise_error_texto(f"Retorno inválido da expressão (gerou {tipo_final}, requeria {tipo_necessario})",linha)
                )
        self.expressao = {
            "str" : "",
            "struct" : [],
            "str_pos" : [],
            "struct_pos" : []
        }
        #return tipo_final
  

    def trig_leitura_exp(self):
        """
        Habilita/Desabilita gravação dos tokens para análise de expressão
        """
        self.lendo_exp = not self.lendo_exp


    def agg_token(self, token):
        """
        Concatena um token para análise de expressão

        Args:
            token (dict): Contém info do lexema, símbolo e linha atuais
        """
        if self.lendo_exp:
            self.expressao['struct'].append(token)
            self.expressao['str'] += token['lexema']


    def change_token(self):
        """
        Modifica lexema '+' ou '-' em operadores unários
        """
        self.expressao['struct'][-1]['lexema'] = f"{self.expressao['struct'][-1]['lexema']}u"


    def trig_funcao(self, trigger=False):
        """
        Habilita/Desabilita análise de função
        """
        if trigger:
            dict_func = self.semantico_tabela.ret_func()
            #print('\n\n')
            #self.print_table()
            #print(dict_func)
            self.analise_funcao.append({
                'lexema': dict_func.get('lexema'),
                'tipo':self.__ret_funcao_tipo(dict_func.get('tipo_iden')),
                'retorno_valido':False,
                'retorno_valido_if':False
            })
        else:
            return self.analise_funcao.pop()


    def __ret_funcao_tipo(self, str_tipo):
        """
        Retorna tipo da função

        Returns:
            str: tipo da função
        """
        if str_tipo == 'func_i':
            return 'inteiro'
        elif str_tipo == 'func_b':
            return 'booleano'
        else:
            return False


    def set_if(self):
        if len(self.analise_funcao) > 0 and \
            (not self.analise_funcao[-1]['retorno_valido']):
            self.analise_funcao[-1]['retorno_valido_if'] = True


    def verifica_if(self):
        if len(self.analise_funcao) > 0 and \
            self.analise_funcao[-1]['retorno_valido_if'] and \
            self.analise_funcao[-1]['retorno_valido']:
            self.analise_funcao[-1]['retorno_valido'] = False


    def set_funcao_retorno(self, set):
        if len(self.analise_funcao) > 0:
            self.analise_funcao[-1]['retorno_valido'] = set


    def verificar_retorno(self):
        if len(self.analise_funcao) > 0:
            return self.analise_funcao[-1]['retorno_valido']
