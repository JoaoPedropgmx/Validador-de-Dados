import re

class telefone:
    def __init__(self,telefone):
        telefone = str(telefone)
        if self._valida_telefone(telefone):
            self._telefone = str(telefone)
        else:
            raise ValueError("Numero inválido")
            


    @property
    def telefone(self):
        return self._telefone
        
    def _valida_telefone(self, telefone):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,telefone)
        if resposta :
            return True
        else:
            return False
    
    def _format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao,self.telefone)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado
    
    def __str__(self):
        return self._format_numero()
        