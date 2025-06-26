
faturamento = 1000
custo = 700
lucro = faturamento - custo

# print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

# print("Faturamento: " +
#        str(faturamento) + ", Custo: " + 
#        str(custo) + ", Lucro: " + 
#        str(lucro))

# email = "EMAIL_falso@gmail.com"

# print(email.lower())
# print(email.find("@"))

# # print(email[11])

# posicao = email.find("@")
# print(posicao)

# servidor = email[posicao:]
# nome_email = email[:posicao]

# print(servidor)
# print(nome_email)


#Tamanho de Texto

# tamanho = len(email)

# print(tamanho)

# #Trocar um pedaco do texto
# novo_email = "@hotmail.com"
# email_trocado = email.replace(servidor, novo_email)
# print(email_trocado)


# #tratar cases
# nome = "joao lira"
# print(nome.capitalize()) # Joao lira
# print(nome.title()) # Joao Lira

# # especiais formatacoes numericas
# margem = lucro / faturamento
# print(f"Faturamento: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}")
# print(f"Margem:  {margem:.1%}")

# exercicios

nome = "Fulano Silva"
email = "fulanosilva@gmail.com"

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

#construir uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o email primeira letra do email +******+@....
tamanho_email = len(email)
tamanho_email_sem_primeira_letra = tamanho_email - 1
print(tamanho_email_sem_primeira_letra)