#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#Formula de conversão: F = C * 1.8 + 32

temperatura_celsius = float(input("Digite a temperatura em Celsius para converter em Fahrenheit: "))
temperatura_fahrenheit = temperatura_celsius * 1.8 + 32

print("A temperatura de {} graus Celsius é {} Fahrenheit".format(temperatura_celsius, temperatura_fahrenheit))
print("A temperatura de {} C° é {} F°".format(temperatura_celsius, temperatura_fahrenheit))
