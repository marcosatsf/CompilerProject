class Erro:
    def raise_error_exp_got(exp, got, line=None):
        """
        Erros que possuem um conjunto esperado/lido

        Args:
            exp (str): valor esperado
            got (str): valor lido
            line (int, optional): valor da linha. Padrão é None.

        Returns:
            str: string de erro
        """
        str_ret = f"Esperado {exp}, encontrado \'{got}\'"
        if line:
            str_ret += f" na linha {line}!"
        return str_ret

    def raise_error_texto(texto, line=None):
        """
        Mensagem de erro

        Args:
            texto (str): texto de erro
            line (int, optional): valor da linha. Padrão é None.

        Returns:
            str: string de erro
        """
        str_ret = texto
        if line:
            str_ret += f" na linha {line}!"
        return str_ret