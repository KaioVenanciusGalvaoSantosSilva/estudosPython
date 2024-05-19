#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input("Digite a quantidade de km percorrido pelo carro alugado: "))
dias_locado = float(input("Digite a quantidade de dias que o carro foi locado: "))
diaria = 60
preco_km = 0.15
preco_total = (preco_km * km_percorrido) + (dias_locado * diaria)

print("O valor total a ser pago pela locação é de R${:.2f}.".format( preco_total))
