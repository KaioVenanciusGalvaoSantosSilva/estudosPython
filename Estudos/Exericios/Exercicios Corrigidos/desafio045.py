#Crie um programa que faça o computador jogar Jokenpô com você

#pedra ganha de tesoura     # 1 ganha de 3
#papel ganha de pedra       # 2 ganha de 1
#tesoura ganha de papel     # 3 ganha de 2
#tipo empata com tipo       # numero empata com numero

from random import randint
mao_usuario = 0
mao_maquina = 0
mao_maquina = randint(1,3)

mao_usuario = int(input("Escolha pedra, papel ou tesoura:\n"
                    "1 - pedra\n"
                     "2 - papel\n"
                     "3 - tesoura\n:"))

if mao_maquina == 1:
    mao_maquina_nome = "pedra"
elif mao_maquina == 2:
    mao_maquina_nome = "papel"
elif mao_maquina == 3:
    mao_maquina_nome = "tesoura"

print("A mão da maquina foi {}.".format(mao_maquina_nome))

if mao_usuario == mao_maquina:
    print("Empate!")
elif mao_usuario == 1 and mao_maquina == 3 or mao_usuario == 2 and mao_maquina == 1 or mao_usuario == 3 and mao_maquina == 2:
    print("Você ganhou!")
else:
    print("Você perdeu!")
