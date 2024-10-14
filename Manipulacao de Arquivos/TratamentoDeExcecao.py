try:
    with open(r'C:\Users\Kaio\Git\estudosPython\Manipulacao de Arquivos\arquivo.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        #Comandos
        arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado.")
except IOError:
    print("Ocorreu um erro ao acessar o arquivo.")
