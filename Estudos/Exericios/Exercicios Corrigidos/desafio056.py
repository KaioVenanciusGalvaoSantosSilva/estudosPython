#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.

nome =[]
idade = []
sexo = []

media = 0.0
mais_velho = 0
nome_mais_velho = ""
mulheres_menos_20 = 0

for i in range(4):
    nome.append(input("Digite o nome da pessoa {}: ".format(i+1)))
    idade.append(int(input("Digite a idade da pessoa {}: ".format(i+1))))
    sexo.append(input("Digite o sexo da pessoa {} (M/F): ".format(i+1)))

for j in range(4):
    media = media+idade[j]
    gen = sexo[j].upper()
    if gen == 'M' and idade[j] > mais_velho:
         mais_velho = idade[j]
         nome_mais_velho = nome[j]
    elif gen == 'F' and idade[j] < 20:
        mulheres_menos_20 = mulheres_menos_20 + 1

media = (media/4)

print("A média de idade do grupo é: {}".format(media))
print("O homem mais velho é: {}".format(nome_mais_velho))
print("Tem {} mulheres que tem menos de 20 anos.".format(mulheres_menos_20))
    