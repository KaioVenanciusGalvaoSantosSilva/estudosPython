#Faça um programa que leia um número e mostre na tela cada um dos digitos separados.
#EX:
#Digite um número: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1

#usando matemática 

numero = float(input("Digite um número: "))
unidade = int(numero % 10)
dezena = int((numero % 100) / 10)
centena = int((numero % 1000) / 100)
milhar = int(numero / 1000)

print("Esse número possui: \nUnidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade,dezena, centena, milhar))

#usando string

numero1 = (input("Digite um número: "))
unidade1 = numero1[-1]
dezena1 = numero1[-2]
centena1 = numero1[-3]
milhar1 = numero1[-4]

print("Esse número possui: \nUnidade: {} \nDezena: {}\nCentena: {}\nMilhar: {}".format(unidade1,dezena1, centena1, milhar1))
