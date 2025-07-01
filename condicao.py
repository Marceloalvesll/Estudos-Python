# faturamento = 1000
# custo = 1800

# lucro = faturamento - custo


# if lucro  >= 0 :
#     print("Lucro:", lucro)
# else:
#     print("Prejuizo!!!!")
#     print(lucro)


# produtos = ["iphone", "ipad", "airpod"]
# # print(produtos)
# novo_produto = input("Digite aqui o produto:")
# # transforma o que o usuario digitou em letra minuscula
# novo_produto = novo_produto.lower()

# if novo_produto in produtos:
#     print("Produto já cadastrado.")
# else:
#     print("Produto cadastrado com sucesso.")
#     produtos.append(novo_produto)

# print(produtos)



# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus

vendas = 900

if vendas >= 15000:
    bonus = 500
elif vendas >= 10000:
    bonus = 150
elif vendas >= 5000:
    bonus = 50
else:
    bonus = 0

# print("Bonus", bonus)


# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
#  vendas da empresa > 50000

vendas = 17000
vendas_empresa = 40000
meta_empresa = 50000

if vendas >= 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas >= 10000 and vendas_empresa > meta_empresa:
    bonus = 150
elif vendas >= 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0

# 


if not vendas_empresa > meta_empresa:
    bonus = 0
else:
    if vendas >= 15000 :
        bonus = 500
    elif vendas >= 10000:
        bonus = 150
    elif vendas >= 5000:
        bonus = 50
    else:
        bonus = 0

# print("Bonus", bonus)



# exercicio desafios
# sistema de consulta de preço

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

busca_produto = input("Digite o nome do produto: ")
busca_produto = busca_produto.lower()
if busca_produto in produtos:
    posicao_produto = produtos.index(busca_produto)
    custo_produto = precos[posicao_produto]
    print(f"O preço do produto: {busca_produto}, é {custo_produto}")
else:
    print("Produto não cadastrado")