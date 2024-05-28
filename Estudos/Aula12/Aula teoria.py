# Condições Aninhadas
# estrutura dentro de estrutura #IF dentro de ELSE
#Se     SENÃO SE    SE
#IF     ELIF        ELSE

nome = str(input("Qual é seu nome? "))

if nome == "Kaio":
    print("Seu nome é bonito ;) , tenha um bom dia.")

elif nome == "Maria" or nome == "Pedro" or nome == "Paulo":
    print("Seu nome é comum, tenha um bom dia.")
elif nome in "Ana Cláudioa Jessica Julia":
        print("Belo nome, tenha um bom dia.")
else:
    print("Seu nome é diferente, tenha um bom dia.")
