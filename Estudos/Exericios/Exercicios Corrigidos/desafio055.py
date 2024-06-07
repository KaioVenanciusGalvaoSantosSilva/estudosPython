#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []

for i in range(5):
    kg = float(input("Peso da {}ª pessoa: ".format(i+1)))
    peso.append(kg)
    print(peso[i])          

for j in range(5):
    if peso[j] == max(peso):
        print("O maior peso é {} kg.".format(max(peso)))
    elif peso[j] == min(peso):
        print("O menor peso é {} kg.".format(min(peso)))
        