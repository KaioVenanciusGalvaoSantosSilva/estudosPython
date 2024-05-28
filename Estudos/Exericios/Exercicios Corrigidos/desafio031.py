#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200 Km e R$ 0.45 para viagens mais longas

preco_curto = 0.50
preco_logo = 0.45
distancia = float(input("Qual a distância da viagem em Km? "))

if distancia <= 200:
    preco_passagem = distancia * preco_curto
    print("Viagem curta")
else:
    preco_passagem = distancia * preco_logo
    print("Viagem longa")

print("O preço da passagem é de R$ {:.2f}".format(preco_passagem))

