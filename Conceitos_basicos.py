#Variaveis
#-------------------------------------------------------
# Variavel global e variavel local

global nome 
nome = "Kaio"

#-------------------------------------------------------
def example1():
    teste = "Teste"
    print("Variavel global é : ", nome)
    print("Variavel local é: ",teste)

example1()
#-------------------------------------------------------

# Tipo de variaveis
idade = 10 # int
altura = 1.85 # float
salario = 2345.90 # float com ponto flutuante
is_voto = True # bool - True ou False
carro = 'Fusca' # str - string

#-------------------------------------------------------
#Formatação de numeros
floatNumber = 1.9876

print("%f" % floatNumber) #formatação  para mostrar os números como float
print("%.1f" % floatNumber) #formatação para mostrar os números com uma casa decimal
print("%.2f" % floatNumber) #formatação para mostrar os números com duas casas decimais
print("%d" % floatNumber)  #formatação para mostrar os números como int (inteiro)

#sep é utilizado para formatação do print
print('Dia', 'Mês', 'Ano', sep='/') # Dia/Mês/Ano

#-------------------------------------------------------
#Concatenação 
texto1 =  "O nome do Batman é" 
texto2 = " Bruce Wayne da Silva"
print("O nome do Batman é " + " Bruce Wayne da Silva") # utilize  + entre os textos ou variaveis
print( texto1 + texto2) # utilize  + entre os textos ou variaveis

#Fatiamento
frase = "Python é incrível!"
parte = frase[7:10] # pega somente parte da frase contida na variavel

#-------------------------------------------------------
# Conversao de tipos

num_str = "123" #str string
num_int = int(num_str) # string para int

num_str = "123.45" # str string
num_float = float(num_str) # string para float

num_int = 123 # int
num_str = str(num_int) # int para string str

value = 0 # int
bool_value = bool(value) #int para boolean

char = chr(65)    # 'A' converte um número inteiro em um caractere Unicode
num = ord('A')    # 65 converte  um caractere Unicode em um número inteiro

num = 16
hex_num = hex(num)   # '0x10'   Convertem para representação hexadecimal
oct_num = oct(num)   # '0o20'   Convertem para representação octal
bin_num = bin(num)   # '0b1000' Convertem para representação binária
#-------------------------------------------------------
# Entrada de dados
nome = input("Escreva seu nome: ") #Entrada do usuário atribuição a variavel nome
print(nome)
#-------------------------------------------------------
#Saida
print('Olá Mundo')
print("Olá Mundo " + nome)
print(nome)
print("Olá Mundo, Meu nome é: ",  nome)
#-------------------------------------------------------
#Utilizando print para gravar dados em arquivos
#with open('arquivo.txt', 'w') as arquivo:
#    print("Escreva isso dentro do arquivo,", file=arquivo)
#    print("Escreva outra linha dentro do arquivo.", file=arquivo)

#-------------------------------------------------------
#Formatação de texto

texto3 = "esse texto é um exemplo"
texto3 = texto3.upper() #converte texto em mainuscula
texto3 = texto3.lower() #converte texto em minuscula

print(texto3.upper()) #exibe texto em maiuscula
print(texto3.lower()) #exibe texto em minuscula

#strip() função para remoção de espaço ou algum caracter na variavel
texto4 = " esse texto sem espaços " # remove os espaços das laterais
print(texto4.strip(" "))

#string = string.strip().replace(" ", "")  remove todos os espaços
print(texto4.strip().replace(" ", ""))


#Formatação datetime
from datetime import datetime
print(datetime.now()) #2020-08-08 06:28:42.715243
print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now())) # Today's date is 2020-08-08 06:29

#-------------------------------------------------------
#Operadores Lógicos e Comparativos:

# and, or, not para operações lógicas.
# ==, !=, <, >, <=, >= para comparações.

idade = 20
if idade >= 18 and idade < 60:
    print("Você é um adulto.")

#-------------------------------------------------------
#Condicional IF ELIF ELSE
def condicional():
    # Solicita um número do usuário
    numero = int(input("Digite um número: "))

    # Verifica se o número é positivo, negativo ou zero
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

condicional()
#-------------------------------------------------------
#Criar uma função 
# def nomedafuncao():
#   conteudo da função
# obs: fim da função é encerrado pela identação do código

#-------------------------------------------------------


#Estruturas de Repetição
#-------------------------------------------------------
#for

lista = 1,2,3,4,5,6
for item in lista:
    print("item: " + str(item))
#-------------------------------------------------------
#while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
#-------------------------------------------------------



#Funções 
#-------------------------------------------------------
#ex função soma
def somar(a, b):
    return a + b

resultado = somar(3, 4)
#-------------------------------------------------------

#1° função sem passagem de parametro

def saudacao():
    nome = "Maria"
    """Esta função imprime uma saudação ."""
    print(f"Olá, {nome}! Bem-vindo!")
#-------------------------------------------------------
# Chamando a função com um argumento
saudacao()
#-------------------------------------------------------


#2° função com passagem de parametro

def saudacao_personalizada(nome):
    """Esta função imprime uma saudação personalizada."""
    print(f"Olá, {nome}! Bem-vindo!")
#-------------------------------------------------------
# Chamando a função com um argumento
saudacao_personalizada("João")
#-------------------------------------------------------

#Imports importação de biblioteca interna e externa
import math
raiz_quadrada = math.sqrt(25)

#Tratamento de exceção 
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")

#Comentários 
#use # texto ou
    '''
    Comentario  em várias linhas
    Para
    textos mais
    complexos
    '''
#git
    #baixe o git https://git-scm.com/downloads
    #instale
    #configure    
    #abra o cmd (Windows + R -> cmd -> Enter) como administrador
    #navegue até a pasta onde será adicionado seus projetos cd C:\Users\Usuario\Documents\Git
    #digite os comandos abaixo para criar um repositório
        #git init 
        #git add . -> adiciona todos os arquivos do diretório atual ao repositório
        #Lembre-se de acessar o github e criar o repositório 
        #git clone  URL_DO_REPOSITÓRIO -> copia um repositório existente
        #Entre na pasta cd NomeDoProjeto
        #Insira o código na pasta que deseja enviar para o github
        #no terminal digite
        #git add *
        #git commit -m "Primeira versão do meu projeto"
        #agora você pode enviar seu projeto para o github
        #git push
    
#Fim    