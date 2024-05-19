#Saida de Dados

n = input("Digite um valor: ") #Nesse caso o valor recebido é uma string
print(n)
print(type(n))
print("O resultado para número é: ",n.isnumeric()) # é numero?
print("O resultado para letra é: ", n.isalpha()) # é letra?
print("O resultado para alfanumerico é: ", n.isalnum()) # é alphanumerico (letra + numero)?
print("O resultado para maiuscula é: ", n.isupper()) # é letra maiuscula?
