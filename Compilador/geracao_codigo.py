class GeracaoCodigo:
    def __init__(self) -> None:
        self.rotulo = 1
        self.base_alloc = 0
        self.alocacao = 0
        self.alloc = []
        self.ret_func = []
        self.operadores = {
            'nao' : 'NEG',
            '-u' : 'INV',
            '*' : 'MULT',
            'div' : 'DIVI',
            '-' : 'SUB',
            '+' : 'ADD',
            '>' : 'CMA',
            '>=' : 'CMAQ',
            '<' : 'CME',
            '<=' : 'CMEQ',
            '=' : 'CEQ',
            '!=' : 'CDIF',
            'e' : 'AND',
            'ou' : 'OR' 
        }
        self.txt_maquina = []


    def codigo2txt(self, file_name):
        """
        Transcreve em asm o assembly o gerado

        Args:
            file_name (str): nome do arquivo que estamos editando
        """
        if file_name == "Arquivo não salvo":
            file_name = "compilado_lpd"
        file_name = file_name.split('.')[0]
        with open(f'{file_name}.asm', 'w') as f:
            for elem in self.txt_maquina:
                f.write(f'{elem}\n')


    def traduz(self, rotulo=None, instrucao=None, arg1=None, arg2=None):
        """
        Gera a tradução para o assembly. Função mais foda que resume
        o compilador.

        Args:
            rotulo (str, optional): número precedido de L. Defaults to None.
            instrucao (str, optional): instrução assembly. Defaults to None.
            arg1 (str | int, optional): 1° arg da instrução. Defaults to None.
            arg2 (str | int, optional): 2° arg da instrução. Defaults to None.
        """
        linha_atual = ''
        if rotulo:
            linha_atual += f"{rotulo} "
        if instrucao:
            linha_atual += f"{instrucao} "
        if arg1 != None:
            linha_atual += f"{arg1}"
            if arg2 != None:
                linha_atual += f",{arg2} "
        self.txt_maquina.append(linha_atual)


    def traduz_exp(self, exp):
        """
        Traduz uma expressão (pós-fixa)

        Args:
            exp (dict): dicionário contendo informações da expressão
            pós-fixa previamente calculada
        """
        for elem in exp["str_pos"]:
            if elem in self.operadores.keys():
                self.traduz(instrucao=self.operadores[elem])
            elif elem == '+u':
                continue
            else:
                try:
                    int_value = int(elem)
                    self.traduz(instrucao="LDC", arg1=int_value)
                    continue
                except ValueError:
                    pass
                if elem in ['verdadeiro', 'falso']:
                    valor = 1 if elem == 'verdadeiro' else 0
                    self.traduz(instrucao="LDC", arg1=valor)
                elif exp["struct_pos"][elem]["tipo_iden"] == 'var':
                    self.traduz(instrucao="LDV", arg1=exp["struct_pos"][elem]["pos_pilha"])
                elif exp["struct_pos"][elem]["tipo_iden"] in ['func_i', 'func_b']:
                    self.traduz(instrucao="CALL", arg1=exp["struct_pos"][elem]["rotulo"])
                    self.traduz(instrucao="LDV", arg1=0)


    def inc_rotulo(self):
        """
        Aumenta o rótulo para ser usado em jumps
        """
        self.rotulo+=1


    def get_rotulo(self):
        """
        Retorna rótulo

        Returns:
            str: Retorna o rótulo iniciando com L
        """
        return f'L{self.rotulo}'


    def inc_alocacao(self):
        """
        Incrementa as variáveis a serem empilhadas
        """
        self.alocacao += 1


    def get_alocacao(self):
        """
        Pega o total de variáveis alocadas e que serão alocadas,
        utilizado fundamentalmente para adquirir a posição em que
        uma variável será armazenada

        Returns:
            int: localização da pilha
        """
        return self.alocacao + self.base_alloc


    def push_jmp(self, rotulo, info):
        """
        Insere na pilha de rótulos

        Args:
            rotulo (str): label para salto
            info (tuple): lexema e tipo
        """
        self.ret_func.append({
            'lexema': info[0],
            'tipo': info[1],
            'rotulo': rotulo
        })


    def access_jmp(self):
        """
        Acessa o último label armazenado

        Returns:
            str: label para salto
        """
        return self.ret_func[-1]['rotulo']


    def pop_jmp(self, info):
        """
        Retira o último label armazenado

        Args:
            info (tuple): arg1 e arg2 da instrução

        Returns:
            str: label para salto retirado da pilha
        """
        if len(self.ret_func) > 0:
            if self.ret_func[-1]['lexema'] == info[0] and self.ret_func[-1]['tipo'] == info[1]:
                return self.ret_func.pop()['rotulo']


    def aloca_mem(self, simbolo):
        """
        Realiza a contagem da instrução ALLOC
        """
        if simbolo.get('tipo_iden') in ['func_i', 'func_b']:
            self.alloc.append({
                'pos_pilha': self.base_alloc,
                'quantidade' : self.alocacao,
                'lexema': simbolo.get('lexema'),
                'tipo': 'func'
                })
        else:
            self.alloc.append({
                'pos_pilha': self.base_alloc,
                'quantidade' : self.alocacao,
                'lexema': simbolo.get('lexema'),
                'tipo': simbolo.get('tipo_iden')
                })
        self.traduz(instrucao="ALLOC", arg1=self.base_alloc, arg2=self.alocacao)
        self.base_alloc = self.alocacao + self.base_alloc
        self.alocacao=0


    def acessa_mem(self, info):
        """
        Acessa a última memória de variáveis

        Args:
            info (tuple): arg1 e arg2
        """
        if info[1] in ['func_i', 'func_b']:
            info[1] = 'func'
        if len(self.alloc) > 0:
            if self.alloc[-1]['lexema'] == info[0] and self.alloc[-1]['tipo'] == info[1]:
                self.traduz(instrucao="DALLOC", arg1=self.alloc[-1]['pos_pilha'], arg2=self.alloc[-1]['quantidade'])

    def desaloc_mem(self, info):
        """
        Desaloca memória

        Args:
            info (tuple): lexema e tipo do escopo
        """
        if len(self.alloc) > 0:
            if self.alloc[-1]['lexema'] == info[0] and self.alloc[-1]['tipo'] == info[1]:
                struct = self.alloc.pop()
                self.base_alloc -= struct['quantidade']


    def aloca_mem_inicio(self):
        """
        Aloca a memória para retorno da função
        """
        self.traduz(instrucao="ALLOC", arg1=self.base_alloc, arg2=self.alocacao)
        self.base_alloc = self.alocacao + self.base_alloc
        self.alocacao=0

    
    def desaloc_mem_inicio(self):
        """
        Realiza a contagem da instrução DALLOC
        """
        self.traduz(instrucao="DALLOC", arg1=0, arg2=1)


    
