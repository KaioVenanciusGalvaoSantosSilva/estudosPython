#Faça um programa aque calcule a soma de todos os números impares que são multiplos de 3 e que esteja entre 1 e 500.

soma = 0
for c in range(0,500,3):
    if c % 3 == 0:
        soma = soma + c
print("A soma de todos os números multíplos de 3 que estão entre 1 e 500 é: {}".format(soma))
