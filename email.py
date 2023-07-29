import re

class email:
    def __init__(self, email):
        if self._valida_email(email):
            self._email = email
        else:
            raise ValueError("Email Inválido")

    @property
    def email(self):
        return self._email

    def _valida_email(self, email):
        padrao = "\w{5,50}@[a-z]{3,10}.com(.br)?"
        resposta = re.search(padrao, email)
        if resposta:
            return True
        else:
            return False
        

    
    def _formata_email(self):
        padrao = "\w{5,50}@[a-z]{3,10}.com(.br)?"
        resposta = re.search(padrao, self.email)
        email_formatado = resposta.group()
        return email_formatado

    def __str__(self):
        return self._formata_email()