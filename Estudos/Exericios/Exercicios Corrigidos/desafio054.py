#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
pessoas = []
for i in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento da pessoa {}: ".format(i + 1)))
    pessoas.append(ano_nascimento)

ano_atual = datetime.datetime.now().year

maiores = 0
menores = 0

for j in range(7):
    if ano_atual - pessoas[j] >= 21:
        maiores += 1
    else:
        menores += 1

print("{} pessoas ainda não atingiram a maioridade e {} já são maiores.".format(menores,maiores))
