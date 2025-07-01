for i in range(10):
    print("Teste de repeticao")


lista_precos = [1500, 1000, 800, 2000]

for preco in lista_precos:
    imposto = preco * 0.1
    print(f"O Preço é : {preco} imposto: {imposto}")
 


 # regra do imposto
 # preco até 1000 -> imposto é de 10%
 # preco maior 1000 -> imposto é de 15%


for preco in lista_precos:
    if preco >1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"O Preço é : {preco} imposto: {imposto}")