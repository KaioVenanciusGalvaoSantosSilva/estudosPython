# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar . Considere US$1,00 = R$3.27

dinheiro = float(input("Digite o valor em reais que deseja converter para dólar: "))
dolar = 3.27
print("Você pode comprar {} dólares".format(dinheiro/dolar))
