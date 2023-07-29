from validate_docbr import CNPJ
validate_cnpj = CNPJ()

class cnpj :
    def __init__(self, documento):
        self.documento = str(documento)
        if self.__valida_cnpj(self.documento):
            self._cnpj = self.documento
        else:
            raise ValueError("cnpj Inválido")
        self.__formata_cnpj()
    
    @property
    def cnpj(self):
        return self._cnpj
    
    def __valida_cnpj(self,cnpj):
        
        return validate_cnpj.validate(cnpj)
        
        
        
    def __formata_cnpj(self):
        self._cnpj = validate_cnpj.mask(self.cnpj)
    
    def __str__(self):
        return self.cnpj


