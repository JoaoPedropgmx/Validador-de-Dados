from validate_docbr  import CPF
validate_cpf = CPF()

class cpf :
    
    def __init__(self, documento):
        self.documento = str(documento)
        if self.__valida_cpf(self.documento):
            self._cpf = self.documento
        else:
            raise ValueError("Cpf Inválido")
        self.__formata_cpf()
    
    @property
    def cpf(self):
        return self._cpf
    
    def __valida_cpf(self,cpf):
        
        return validate_cpf.validate(cpf)
        
        
        
    def __formata_cpf(self):
        self._cpf = validate_cpf.mask(self.cpf)
    
    def __str__(self):
        return self.cpf
    
    