#Estrutura condicional
#Geram possibilidades no código de acordo com uma condicional - Exemplo: jogos interativos que permitem o usuário escolher um caminho x ou y
#O uso de IF(condição) auxilia a tomar decisões com base em uma condição especifica     #Estrutura condicional simples
#o uso de IF(condição) ELSE gera um segundo comportamento caso não atenda as condições esperadas no IF  #Estrutura condicional composta


#Exemplo1:
print("Exemplo 1")

nome = "João"
idade =  25
if idade >= 18 : #Verifica se a idade é maior ou igual a 18
    print("Você é maior de idade") # se sim realiza esse trecho de código (bloco de código)
else :
    print("Você é menor de idade")  # senão  realiza esse trecho de código (bloco de código)

#Exemplo2:
print("Exemplo 2")

print("Exemplo 2")

tempo = int(input("Quantos anos tem seu carro? "))

if tempo <= 3 : #Condição caso o tempo for menor ou igual a 3
    print("Carro novo")  # se sim realiza esse trecho de código (bloco de código)

else:
    print("Carro velho")  # senão  realiza esse trecho de código (bloco de código)
print("FIM") #identação a esquerda - será executado sempre

#Condição simplificada
#Exemplo2 Condição simplificada:
print("Exemplo 2 Com condição simplificada")

tempo = int(input("Quantos anos tem seu carro? "))

print("Carro novo" if tempo <=3 else "Carro velho") #Condição simplificada, (retorno1 IF ELSE retorno2) #semelhante ao operador ternário de outras linguagens
print("FIM")

#Exemplo3
print("Exemplo 3")

nome = str(input("Qual é seu nome? "))
if nome == 'Gustavo':
    print("Você é o dono do sistema")
else:
    print("Você não é o dono do sistema")

#Exemplo4
print("Exemplo 4")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print("A sua média foi {:.2}".format(media))

#print("Você foi aprovado" if media >= 6.0 else "Você foi reprovado") #Condição simplificada: equivale ao que foi digitado abaixo porem simplificado

if media >= 6.0:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")
    