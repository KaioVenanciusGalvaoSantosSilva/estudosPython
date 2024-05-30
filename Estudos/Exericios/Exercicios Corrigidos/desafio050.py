#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-0

soma = 0
print("Digite seis números inteiros")
for c in range(0,6):
    numero = (int(input("Digite o {}° número inteiro: ".format(c+1))))
    if numero % 2 == 0:
        soma = soma + numero
    
print("A soma apenas dos números que são pares: {}".format(soma))
