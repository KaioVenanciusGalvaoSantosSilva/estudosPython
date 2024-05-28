#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and  n1 > n3:
    print("{} é maior que os demais".format(n1))
else:
    if n2 > n1 and n2 > n3:
        print("{} é maior que os demais".format(n2))
    else:
        print("{} é maior que os demais".format(n3))

if n1 < n2 and  n1 < n3:
    print("{} é menor que os demais".format(n1))
else:
    if n2 < n1 and n2 < n3:
        print("{} é menor que os demais".format(n2))
    else:
        print("{} é menor que os demais".format(n3))
        