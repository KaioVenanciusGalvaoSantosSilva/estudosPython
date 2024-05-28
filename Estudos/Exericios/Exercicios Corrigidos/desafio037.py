#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

#Exemplos do numero 100 em suas conversoes
#Binário: 1100100
#Octal: 144
#Hexadecimal: 64

numero = int(input("Digite um número inteiro para converter: "))
base = int(input("Escolha a base de conversão:\n1 - Binário \n2 - Octal\n3 - Hexadecimal\n"))

if base== 1:
    print("O número {} em binário é: {}".format(numero, bin(numero).removeprefix("0b")))
    
elif base==2:
    print("O número {} em octal é: {}".format(numero, oct(numero).removeprefix("0o")))

elif base==3:
    print("O número {} em hexadecimal é: {}".format(numero, hex(numero).removeprefix("0x")))

else:
    print("Opção inválida!")
