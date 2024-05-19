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
b = 3

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

#Formatação para uma linha /n
#Formatação para fim de linha end = " "

print("A soma é {}, o produto é {} e a divisão é {:.2f}".format(adição, multiplicação, divisão))  # :.2f realiza a formatação de duas casas decimais
print("A divisão inteira é {0} e a potência é {1}".format(divisão_inteira, exponenciação), end = " ")  # O uso do ,end = " " serve para ligar a proxima linha do print a atual
print("- Esses são os resultados dos operadores aritméticos")
print("\nUtilize o contra barra n para quebra de linha") # utilize \n para quebra de linha

# EXEMPLOS

exemplo1 = 5 + 3 * 2 # De acordo com a ordem de precedência  * + = 3*2 => 6 + 5 => 11
print("O resultado do exemplo1 é {}".format(exemplo1))

exemplo2 = 3 * 5 + 4 ** 2 # De acordo com a ordem de precedência ** * + => 4**2 = 16 => 3 * 5 = 15 => 15 + 16 = 31
print("O resultado do exemplo2 é {}".format(exemplo2))

exemplo3 = 3 * (5 + 4) ** 2 # De acordo com a ordem de precedência () ** * => (5+4) = 9 **2 = 81 => 3 * 81 = 243
print("O resultado do exemplo3 é {}".format(exemplo3))
print("FIM")
