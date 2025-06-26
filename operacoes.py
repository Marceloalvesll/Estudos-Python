faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)


restituicao = imposto * 0.1
print(restituicao)

# print("mod de 10 dividido por 3 é", 10 % 3)

tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")


numero = 123.97
print(round(numero))

faturamento = 139_018_182