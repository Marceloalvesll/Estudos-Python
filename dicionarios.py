precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500, "camera": 1000,
               "fone de ouvido": 800, "monitor": 2000}

# pegar um item
preco_celular = dic_precos["celular"]
print("preço antigo ", preco_celular)

dic_precos["celular"] = 2000
print("preço novo ", dic_precos["celular"])

#se nao existir ele adiciona o item
dic_precos["iphone"] = 4500
print(dic_precos)

# apagar um item
dic_precos.pop("iphone")
print(dic_precos)

print(len(dic_precos))

# procura nas chaves
print("celular" in dic_precos)
print(1500 in dic_precos.keys())

# procura nos valores
print(1000 in dic_precos.values())


#exercicio com dicionario
dic_precos = {"celular": 1500, "camera": 1000,
               "fone de ouvido": 800, "monitor": 2000}

produto_pesquisa = input("Digite o nome do produto: ")
produto_pesquisa = produto_pesquisa.lower()

if produto_pesquisa in dic_precos:
    print(f"O produto {produto_pesquisa} tem o valor de: {dic_precos[produto_pesquisa]}")
else:
    print("Produto não cadastrado.")