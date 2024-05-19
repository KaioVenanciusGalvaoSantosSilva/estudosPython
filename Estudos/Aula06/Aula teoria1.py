#Tipos primitivos

# #Inteiros (int): Números inteiros, como 1, 2, 3, 4, 5, etc.
# Ponto flutuante (float): Números de ponto flutuante, como 1.0, 2.5, 3.14, etc.
# Strings (str): Sequências de caracteres, como "olá", "mundo", "Python", etc.
# Booleanos (bool): Valores booleanos, como True ou False.

n1  = int (input("Digite um número: "))
n2  = int (input("Digite outro número: "))

s   = n1 + n2

#exemplos de variaveis 
num1 = 5            #int
num2 = 3.0          #float
nome = "Ana"        #string
verdadeiro = True   #boolean   
falso = False       #boolean


print("A soma vale", s)
print("A soma vale {}".format(s))
print (type(s)) # informa o tipo

print("A soma entre {0} e {1} é {2}".format(n1, n2, s)) #python 3
