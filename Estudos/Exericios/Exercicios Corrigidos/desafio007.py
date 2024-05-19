#Desenvolva um programa que leia as duas notas de um aluno, Calcule e mostre a sua média

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

soma = float(nota1 + nota2)
media =  float (soma/2)

print("A média do aluno foi de: {}".format(media))