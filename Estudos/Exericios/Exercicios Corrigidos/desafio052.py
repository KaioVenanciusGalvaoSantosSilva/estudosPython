#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Um número primo é um número natural maior que 1 que tem apenas dois divisores:
#1 e ele mesmo.

numero = int(input("Digite um número inteiro: "))

if numero > 1: # Verificamos se o número é maior que 1
    for i in range(2, numero): # Verificamos se o número tem divisores  
        if numero % i == 0: # Se o número for divisível por outro número 
            print("não é primo.")
            
        else: # Se o número não tiver divisores 
            print("é primo.")  
    if numero == 2 :
        print("é primo.")

else: # Se o número for menor ou igual a 1
    print("não é primo.")
    