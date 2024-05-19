#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.05
preco_desconto = preco - desconto

print("O novo preço do produto é: {}".format(preco_desconto))
