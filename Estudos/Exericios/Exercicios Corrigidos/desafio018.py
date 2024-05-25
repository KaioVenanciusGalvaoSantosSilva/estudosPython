#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan , radians

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("\nO ângulo digitado é {}° \nO valor de seno é {:.3f} \nO valor de cosseno é {:.3f} \nA tangente é {:.3f}".format(angulo, seno, cosseno, tangente))
