#Crie um programa que leia o número inteiro e mostre na tela se ele é PAR ou IMPAR
numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 2 == 0:
    print("O número {} é par.".format(numero_inteiro))
else:
    print("O número {} é ímpar.".format(numero_inteiro))
    