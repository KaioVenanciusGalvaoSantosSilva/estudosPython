#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = 0.00
salario = float(input("Digite seu salário: "))

if salario > 1250:
    salario = salario * 1.10
    print("Seu salario com aumento de 10% é de R${:.2f}".format(salario))
else:
    salario = salario * 1.15
    print("Seu salario com aumento de 15% é de R${:.2f}".format(salario))
