#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Digite o valor da casa que deseja realizar o financiamento: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você deseja pagar o financiamento? "))
meses = 12
juros = 0

validador = salario * 0.3
emprestimo = (casa/anos/meses)*(1+juros)

if emprestimo > validador:
    print("O empréstimo foi negado pois a prestação mensal excede o permitido.")

elif emprestimo <= validador:
    print("Emprestimo concedido. O valor da prestação é de R${:.2f} com juros de {:.2f}% a.m.".format(emprestimo,juros))
