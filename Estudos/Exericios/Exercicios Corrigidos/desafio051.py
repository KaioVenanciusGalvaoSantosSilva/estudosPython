#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo

for c in range(primeiro_termo,10+termo):

    print(termo)
    termo = termo+razao
    