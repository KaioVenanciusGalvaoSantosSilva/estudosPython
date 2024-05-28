#Escreva um programa que leia dois números inteiros e compare-os mostrando na tela a mensagem:
#O primeiro valor é o maior
#O segundo valor é o maior
#Não existe valor maior, os dois são iguais

numero1 =int(input("Digite o primeiro número inteiro: "))
numero2 =int(input("Digite o segundo número inteiro: "))

if numero1 == numero2:
    print("Não existe valor maior, os dois são iguais")
elif numero1 > numero2:
    print("O primeiro valor é o maior")
else:
    print("O segundo valor é o maior")
