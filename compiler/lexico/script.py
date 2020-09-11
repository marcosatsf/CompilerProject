from reader import Reader
from analisador import AnalisadorLexico

# Lê o texto
texto = Reader('test.txt')
# Instancia o analisador com o programa já formatado
analisador = AnalisadorLexico(texto.get_programa_formatted())    
# Realiza a quebra em tokens
analisador.pega_token()
# Mostra os tokens
analisador.beauty_print()
