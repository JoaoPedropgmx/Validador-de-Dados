from email import email
from documento import documento
from telefone import telefone

usuario_cnpj =  documento.cria_documento("cnpj do usuario")
usuario_cpf = documento.cria_documento("cpf do usuario")
usuario_telefone = telefone("telefone do usuario")
usuario_email = email("email do usuario")

print(usuario_telefone)
print(usuario_cpf)
print(usuario_cnpj)
print(usuario_email)