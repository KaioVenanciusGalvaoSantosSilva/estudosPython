#DICIONARIO DENTRO DE UM DICIONARIO 
#Programa procura o significado da palavra no dicionario

dicionario = {}
dicionarioA ={}


dicionarioA['abacate']= 'fruta tipica de regioes subtropcais e tropicais'
dicionarioA['amor']='palavra que expressa o sentimento do amor, ou a ideia de ser amado.'

dicionarioB = {}

dicionarioB['bater'] ='toque ou atingir com uma bola'
dicionarioB['bola'] ='objeto redondo feito de material elastico, usada em jogos como basquete, futebol, voleibol'

dicionario['A'] = dicionarioA
dicionario['B'] = dicionarioB

#print(dicionario['A']['abacate'])
#print(dicionarioA['abacate'])

palavra = input("Digite a fruta: ")
primeira_letra_palavra= palavra[0].upper()

#print(dicionarioA[palavra])
#print(dicionario['A'][palavra])

print("A palavra que digitou foi: "+ palavra +'\n'
      +"A primeira letra dessa palavra é: "+ primeira_letra_palavra +'\n'
      +"O resultado encontrado foi: "
      +dicionario[primeira_letra_palavra][palavra])

