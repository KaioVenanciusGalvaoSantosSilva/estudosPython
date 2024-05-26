#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Digite o nome de uma cidade: ")

print(cidade[0:5].upper().count("SANTO"))
