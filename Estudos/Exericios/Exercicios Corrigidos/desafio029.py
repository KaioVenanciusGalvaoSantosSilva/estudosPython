#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite

velocidade = float(input("Qual é a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Condutor foi multado. A multa foi de {}".format(multa))
else:
    print("Velocidade dentro do limite permitido na via")
