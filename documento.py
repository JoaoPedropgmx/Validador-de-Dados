from cnpj import cnpj
from cpf import cpf

class documento :
    @staticmethod
    def cria_documento(documento):
        tamanho_documento = len(str(documento))
        if tamanho_documento == 11:
            return cpf(documento)
        elif tamanho_documento ==  14:
            return cnpj(documento)
        else:
            raise ValueError("Documento inválido")