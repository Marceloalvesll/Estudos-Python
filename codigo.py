faturamento = 1200 # int
custo = 770


novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_de_imposto = 0.1 # com casa decial é float
mensagem = "faturamento foi de "
teve_lucro = False

imposto = faturamento * taxa_de_imposto
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)