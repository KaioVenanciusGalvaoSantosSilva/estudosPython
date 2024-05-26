#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria de Souza
#primeiro: Ana
#último: Souza

nome_completo = input("Digite o seu nome completo: ")
nomes = nome_completo.split()
primeiro_nome = nomes[0].capitalize()
ultimo_nome = nomes[-1].capitalize()

print("Primeiro: {} \nÚltimo: {}".format(primeiro_nome, ultimo_nome))
