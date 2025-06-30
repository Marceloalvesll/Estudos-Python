# produtos = ["iphone", "ipad", "airpod"]

vendas = [100, 50, 130, 80, 120]

print(vendas[-1])


total_vendas = sum(vendas)

print(total_vendas)

quantidade = len(vendas)

print(quantidade)

valor_max = max(vendas)
valor_min = min(vendas)

print(valor_max)
print(valor_min)

posicao = vendas.index(130)
print(posicao)

print(vendas[2:])


# EDITA UM ITEM
produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]
precos[0] = precos[0] * 1.1
print(precos)


# ADICIONA UM ITEM
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

# REMOVER UM ITEM
produtos.remove("macbook")
precos.pop(-1)
print(produtos)
print(precos)

#INSERIR ONDE QUISER
produtos.insert(1, "airpod")
print(produtos)

#CONTAR VALORES
print(produtos.count("airpod"))




# produto_usuario = input("Digite um produto:")
# print(produto_usuario in produtos)