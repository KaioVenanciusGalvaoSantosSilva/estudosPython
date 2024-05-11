# o caracter '#' serve para comentar uma linha
    #
# Mensagens possuem delimitadores " " aspas simples ou aspas dupla
#Exemplo
"Olá Mundo"

#Todo comando é uma função() e toda função possui parenteses ( )
    #print()
    #input()
    #len()
    #type()
    #int()
    #float()

#Comando para fazer algo aparecer na tela  'print()'

print("Olá Mundo") #Textos devem ser representados em aspas
print(8000) # Números não precisam de aspas
print(1 + 1) #soma os valores e a mensagem exibe o resultado do calculo 7+4 = 11
print("1"+"1") #Não se usa aspas para números, caso use aspas ele será representado como texto em vez de número

#Concatenação (juntar 2 variaveis)
# Concatenação de texto com número é feito da seguinte forma ("Texto" virgula numero)
# Concatenação de texto com texto pode ser feito da forma acima ou da seguinte forma ("Texto" + variavel)
print("Olá", 5)

#Caso use o + para concatenar texto com número retornará erro
#Desmarque a linha 28 para testar (tire o #)
#print("Olá" + 5)

#escreva tudo em letra minuscula quando não estiver dentro dos delimitadores " " ' '

#Variavel
# Variaveis podem receber valores com o '='

#Estrutura
#nome_da_variavel #atribuição '=' # valor 
nome = "Kaio"
idade = 26
peso = 120.5

#Imprime as variaveis
print(nome, idade, peso)

#Input("") serve para ler o que o usuario digitar
# input("Digite algo")

#Nesse caso estamos atribuindo o que o usuario digitar a variavel 'nome' 'idade' 'peso'
nome = input("Qual o nome? ")
idade = input("Quantos anos você tem? ")
peso = input("Qual é o seu peso? ")

print(nome, idade, peso) 

#Prática
#Desafio 1 - #Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado

#Desafio 2 - #Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

#Desafio 3 - #Crie um script Python que leia dois numeros e tente mostrar a soma entre eles