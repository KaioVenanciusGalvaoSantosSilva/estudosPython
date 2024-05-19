#Faça um programa que leia algo pelo teclado e mostre na tela do seu tipo primitivo e todas as informações possíveis sobre ele

valor = input("Digite algo")
print("O tipo primitivo desse valor é", type(valor))
print("Somente espaço", valor.isspace)
print("É um número?", valor.isnumeric())
print("É um número decimal?", valor.isdecimal())
print("É um valor imprimivel?", valor.isprintable())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Está capitalizada?", valor.istitle())

