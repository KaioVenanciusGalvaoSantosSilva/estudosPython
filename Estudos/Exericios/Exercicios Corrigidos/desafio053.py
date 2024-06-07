#Crie um programa que leie uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços.

frase = str(input("Digite uma frase: "))
palindromo = frase.split()
palindromo = ''.join(palindromo)
reverse = palindromo[::-1]
if palindromo == reverse:
    print("Sim, a frase '{}' é um palindromo!".format(frase))
else:
    print("Não, a frase '{}' não é um palindromo!".format(frase))
