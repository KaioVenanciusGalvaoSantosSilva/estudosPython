#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

numero_maquina = randint(0,5) # Gera numero inteiro de forma randomica
numero_usuario = int(input("Tente descobrir qual número o computador pensou entre 0 e 5. Digite o valor aqui: "))

while numero_usuario > 5: #uso do while para gerar um loop até que o usuário digite o valor correto # não obrigatório na atividade porém atende aos requisitos de funcionalidade
    print("Você digitou um número maior que 5. Tente novamente!")
    numero_usuario = int(input("Tente descobrir qual número o computador pensou entre 0 e 5. Digite o valor aqui: "))

if numero_usuario == numero_maquina:
    print("Você venceu. O número escolhido pelo computador foi: {} ".format(numero_maquina))
else:
    print("Você perdeu. O número escolhido pelo computador foi: {}".format(numero_maquina))
