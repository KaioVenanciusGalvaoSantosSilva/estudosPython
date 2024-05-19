#Operadores aritméticos

# Adição: +
# Subtração: -
# Multiplicação: *
# Divisão: /
# Módulo: %
# Exponenciação: **
# Divisão inteira: //

#ORDEM DE PRECEDENCIA
#1 () parenteses
#2 ** potencias
#3 * / % // divisão inteira
#4 + -

a = 10
b = 2

adição = a + b
subtração = a - b
multiplicação = a * b
divisão = a / b
módulo = a % b
exponenciação = a ** b
divisão_inteira = a // b

print(f"Adição: {adição}")
print("Adição: {}".format(adição))
print(f"Subtração: {subtração}")
print(f"Multiplicação: {multiplicação}")
print(f"Divisão: {divisão}")
print(f"Módulo: {módulo}")
print(f"Exponenciação: {exponenciação}")
print(f"Divisão inteira: {divisão_inteira}")

# EXEMPLOS

exemplo1 = 5 + 3 * 2 # De acordo com a ordem de precedência  * + = 3*2 => 6 + 5 => 11
print("O resultado do exemplo1 é {}".format(exemplo1))

exemplo2 = 3 * 5 + 4 ** 2 # De acordo com a ordem de precedência ** * + => 4**2 = 16 => 3 * 5 = 15 => 15 + 16 = 31
print("O resultado do exemplo2 é {}".format(exemplo2))

exemplo3 = 3 * (5 + 4) ** 2 # De acordo com a ordem de precedência () ** * => (5+4) = 9 **2 = 81 => 3 * 81 = 243
print("O resultado do exemplo3 é {}".format(exemplo3))
