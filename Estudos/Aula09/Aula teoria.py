#Leia o código, execute e leia o resultado
#Manipulção de Texto
#Manipulando Cadeias de texto 
#Cadeia de caracteres = STRING

# Todo objeto possui seus metodos e no caso de uma String não é diferente
# Existe várias metodos que podem ser utilizadas para manipular uma String

# Aqui estão algumas delas:
# upper() - Converte a string para maiúscula
# lower() - Converte a string para minúscula
# capitalize() - Converte a string para minúscula e deixa somente a primeira letra em maiuscula
# title() - Analisa quantas palavras existem e converte todas as strings para minúscula e deixa somente as primeiras letras em maiusculas
# strip() - Remove os espaços em branco do início e do fim da string
# lstrip() - Remove os espaços em branco do início da string
# rstrip() - Remove os espaços em branco do fim da string
# replace() - Substitui uma substring por outra
# find() - Retorna a posição da primeira ocorrência de uma substring
# split() - Divide a string em uma lista de substrings
# join() - Une uma lista de strings em uma única string
# len() - Retorna o tamanho da string
# count() - Retorna o número de ocorrências de uma substring

frase = " Frase aleatória "
print("\n")

print("#Exibe o elemento na posição 1")
print(frase[1]) #Exibe o elemento na posição x
print("\n")
print("# Exibe somente os elementos nas posições 3 até 9-1")
print(frase[3:9]) # Exibe somente os elementos nas posições x:y-1
print("\n")
print("# Exibe os elementos da posição 0 até a posição 9")
print(frase[:9]) # Exibe os elementos da posição 0 até a posição x
print("\n")
print("# Exibe os elementos da posição 9 até o final da string")
print(frase[9:]) # Exibe os elementos da posição x até o final da string
print("\n")
print("# Exibe somente os elementos nas posições 3 até 9-1 pulando de 2 em 2")
print(frase[3:9:2]) # Exibe somente os elementos nas posições x:y-1 pulando de 2 em 2
print("\n")
print("# Exibe os elementos da posição 9 até o final, pula de 3 elementos #semelhante ao exemplo acima porém o final não foi definido logo irá percorrer tudo")
print(frase[9::3]) # Exibe os elementos da posição x até o final, pula de y elementos #semelhante ao exemplo acima porém o final não foi definido logo irá percorrer tudo
print("\n")
print("# Exibe se existe determinada palavra 'frase' dentro da string")
print("Frase" in frase) # Exibe se existe determinada palavra dentro da string
print("\n")

print("# Converte a string para maiúscula")
print(frase.upper()) # Converte a string para maiúscula
print("\n")
print("# Converte a string para minúscula")
print(frase.lower()) # Converte a string para minúscula
print("\n")
print("# Converte a string para minúscula e deixa somente a primeira letra em maiuscula")
print(frase.capitalize()) # Converte a string para minúscula e deixa somente a primeira letra em maiuscula
print("\n")
print("# Analisa quantas palavras existem e converte todas as strings para minúscula e deixa somente as primeiras letras em maiusculas")
print(frase.title()) # Analisa quantas palavras existem e converte todas as strings para minúscula e deixa somente as primeiras letras em maiusculas
print("\n")
print("# Remove os espaços em branco do início e do fim da string")
print(frase.strip()) # Remove os espaços em branco do início e do fim da string
print("\n")
print("# Remove os espaços em branco do início da string")
print(frase.lstrip()) # Remove os espaços em branco do início da string
print("\n")
print("# Remove os espaços em branco do fim da string")
print(frase.rstrip()) # Remove os espaços em branco do fim da string
print("\n")
print("# Substitui uma substring por outra")
print(frase.replace("Frase","Substituição")) # Substitui uma substring por outra
print("\n")
print("# Retorna a posição da primeira ocorrência de uma substring #retorna -1 caso não encontrado")
print(frase.find("aleatória")) # Retorna a posição da primeira ocorrência de uma substring #retorna -1 caso não encontrado
print("\n")
print("# Divide a string em uma lista de substrings")
print(frase.split()) # Divide a string em uma lista de substrings
print("\n")
print("# Une uma lista de strings em uma única string")
print(" ".join([frase, "unidas"])) # Une uma lista de strings em uma única string #Adiciona espaço e string ao unir
print("\n")
print("# Retorna o tamanho da string")
print(len(frase)) # Retorna o tamanho da string
print("\n")
print("# Retorna o número de ocorrências de uma substring")
print(frase.count("a")) # Retorna o número de ocorrências de uma substring
print("\n")
print("# Retorna o número de ocorrências de uma substring dentro do range definido ex: 3,9")
print(frase.count("a",3,9)) # Retorna o número de ocorrências de uma substring dentro do range definido ex: 3,9
print("\n")
print("# Exibe o conteúdo da string")
print(frase) # Exibe o conteúdo da string
print("\n")

#Usar aspas 3 vezes serve para um conjunto de strings = texto longo 
#Exemplo
"""Esse é um texto longo que deve ser impresso"""

#Pode concatenar uma função com outra
#Exemplo
#print(frase.upper().replace("ALEATÓRIA","SUBSTITUIÇÃO"))

#Podemos percorrer uma string contando as palavras e letras assim como em linhas e colunas de um vetor
#Exemplo 
#frase = "Curso em Vídeo Python"
#dividido = frase.split()
#print(dividido[2][3]) #Seleciona a terceira palavra, em seguida, seleciona a quarta letra da palavra selecionada anteriormente #OBS: As posições começam em [0]
