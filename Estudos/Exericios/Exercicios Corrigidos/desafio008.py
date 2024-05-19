#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valor = float (input("Digite um valor em metros para conversão: "))

centimetro = valor * 100
milimetro = valor * 1000

print("O valor de {} metros convertido é:\n{} centimetros e {} milimetros".format(valor, centimetro, milimetro))
