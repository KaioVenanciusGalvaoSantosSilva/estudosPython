#Faça um programa que leia um ano qualquer e mostra se ele é bissexto ou não.

#Exemplo de entrada:  ano = 2020
#Exemplo de saída: O ano 2020 é bissexto.
#Exemplo de entrada: ano = 2019
#Exemplo de saída: O ano 2019 não é bissexto.
#Bissexto - Um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e não divisivel por 100.

ano = int(input("Digite um ano:"))
if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
