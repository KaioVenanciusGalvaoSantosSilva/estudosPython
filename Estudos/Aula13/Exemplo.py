#print oi 6 vezes
print("\n#print oi 6 vezes")

for c in range(0,6): # o zero é considerado um número
    print("Oi")
#fim do for
print("Fim")

#contagem de 1 a 6
print("\n#contagem de 1 a 6")
for c in range(1,7):
    print(c)

#contagem invertida
print("\n#contagem invertida de 6 a 1")

for c in range(6,0,-1): #o -1 é a iteração (incremento ou decremento)
    print(c)

#contagem pulando de 2 em 2
print("\n#contagem pulando de 2 em 2")

for c in range(0,7,2): #o 2 é a iteração (incremento ou decremento) de 2 em 2
    print(c)

    
#contagem com base no valor inserido pelo usuário
print("\n#contagem com base no valor inserido pelo usuário")

n = int(input("Digite um número: "))

for c in range(0,n+1):
    print(c)
print("Fim")

#contagem com base nos valores inseridos pelo usuário
print("\n#contagem com base nos valores inseridos pelo usuário")

inicio = int(input("Digite um número de início: "))
fim= int(input("Digite um número de fim: "))    
passo= int(input("Digite um número que irá incrementar: "))    

for c in range(inicio,fim+1,passo):
    print(c)
print("Fim")

#Pede ao usuário para digitar n valores
print("\n#Pede ao usuário para digitar n valores")

for c in range(0,3):
    n = int(input("Digite um número: "))
print("Fim")


#Pede ao usuário para digitar n valores
print("\n#Pede ao usuário para digitar n valores")

s = 0
for c in range(0,3):
    n = int(input("Digite um número: "))
    s = s+n

print("O somatório de todos os valores foi {}".format(s))
print("Fim")
