#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Condição de existência de um triângulo
    #Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: 
    #um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
    #   | b - c | < a < b + c
    #   | a - c | < b < a + c
    #   | a - b | < c < a + b

a = float(input("Digite o comprimento da reta 1: "))
b = float(input("Digite o comprimento da reta 2: "))
c = float(input("Digite o comprimento da reta 3: "))

#print("As retas {:.2}, {:.2}, {:.2} podem formar um triângulo")
#função abs() retorna o módulo de um número de acordo com principio matemático |numero|

mod1 = abs(b - c)
mod2 = abs(a - c)
mod3 = abs(a - b)

if mod1 < a < (b+c):
    print("As retas {:.2f}, {:.2f}, {:.2f} podem formar um triângulo.".format(a, b, c))
else:
    if mod2 < b < (a+c):
        print("As retas {:.2f}, {:.2f}, {:.2f} podem formar um triângulo.".format(a, b, c))
    else:
        if mod3 < c < (a+b):
            print("As retas {:.2f}, {:.2f}, {:.2f} podem formar um triângulo.".format(a, b, c))  
        else:
            print("As retas {:.2f}, {:.2f}, {:.2f} não podem formar um triângulo.".format(a, b, c))
