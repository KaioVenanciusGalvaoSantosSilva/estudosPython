#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime #import para coletar o ano

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = datetime.now().year #usado para coletar o ano atual
idade = ano_atual- ano_nascimento

if idade < 18:
    print("Você ainda vai se alistar ao serviço militar. Faltam {} anos para seu alistamento.".format((18-idade)))
elif idade == 18:
    print("É hora de se alistar ao serviço militar. Você tem {} anos.".format(idade))
else:
    print("Você já passou do tempo de alistamento. Você tem {} anos e já passaram {} anos do prazo. Procure a junta militar.".format(idade, (idade-18)))
