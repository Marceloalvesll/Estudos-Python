nome = input("Digite aqui seu nome: ")


email = input("Digite aqui seu email: ")


#descobrir o servidor do email
position_base = email.find("@")
servidor = email[position_base:]

print("O servidor do email " + email + " é: " + servidor)

# novo_server = "new.com"
# email_trocado = email.replace(servidor, novo_server)
# print("O novo email é: "+email_trocado)


#pegar o primeiro nome
position_nula = nome.find(" ")
primeiro_nome = nome[:position_nula]
print(primeiro_nome)


mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

primeira_letra = email[0]
mensagem2 = f"Enviamos um link de confirmação para o email {primeira_letra}*****{servidor}"
print(mensagem2)

