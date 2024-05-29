#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem ao final, de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média do aluno é {:.2f}'.format(media))
if media < 5.0 :
    print('Reprovado')
elif media >= 5.0 or media <= 6.9 :
    print('Recuperação')
elif media >= 7.0 : #Não tem necessidade do elif pode ser usado o else nessa situação #até o elif acima ele valida todas as notas <= 6.9 acima disso é aprovado.
    print('Aprovado')
    