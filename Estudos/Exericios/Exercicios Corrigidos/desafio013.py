#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário do funcionário: "))
novo_salario = salario + (salario * 0.15)

print("O novo salário do funcionário é: R$", novo_salario)
