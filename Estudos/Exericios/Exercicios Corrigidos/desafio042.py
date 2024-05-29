#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:
#Equilatero: todos os lados são iguais
#Isóceles: dois lados são iguais
#Escaleno: todos os lados diferentes

#------------------------------------------------------------------------------------------------------------------------------------------------------#
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Condição de existência de um triângulo
    #Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: 
    #um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
    #   | b - c | < a < b + c
    #   | a - c | < b < a + c
    #   | a - b | < c < a + b

#------------------------------------------------------------------------------------------------------------------------------------------------------#
#Equilatero: todos os lados são iguais 
#Isóceles: dois lados são iguais
#Escaleno: todos os lados diferentes

# a = b = c
# a = b != c
# a != b = c
# a != b != c


a = float(input("Digite o comprimento da reta 1: "))
b = float(input("Digite o comprimento da reta 2: "))
c = float(input("Digite o comprimento da reta 3: "))

#print("As retas {:.2}, {:.2}, {:.2} podem formar um triângulo")
#função abs() retorna o módulo de um número de acordo com principio matemático |numero|

mod1 = abs(b - c)
mod2 = abs(a - c)
mod3 = abs(a - b)

equilatero = "equilatero"
isoceles = "isóceles"
escaleno = "escaleno"


if mod1 < a < (b+c) or mod2 < b < (a+c) or mod3 < c < (a+b):
    temp = ""
    if a == b and b == c:
        temp = equilatero
    elif a == b or b == c or a == c:
        temp = isoceles
    else:
        temp = escaleno
    
    print("As retas cujo os valores são {:.2f}, {:.2f}, {:.2f} podem formar um triângulo do tipo {}.".format(a, b, c,temp))

else:
    print("As retas cujo os valores são {:.2f}, {:.2f}, {:.2f} não podem formar um triângulo.".format(a, b, c))
