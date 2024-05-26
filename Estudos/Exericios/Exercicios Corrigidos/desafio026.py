#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezez aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input("Digite uma frase aqui: ")

print("A letra 'a' aparece {} vezes".format(frase.lower().count("a")))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.lower().index("a")+1))
print("A letra 'a' aparece pela última vez na posição {}".format(frase.lower().rindex("a")+1)) #rindex usado para contar a partir do indice a direita
