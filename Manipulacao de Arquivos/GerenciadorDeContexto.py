#Gerenciador de contexto realiza a abertura e fechamento do arquivo automaticamente sem precisar de usar 'arquivo.close()'
with open(r'C:\Users\Kaio\Git\estudosPython\Manipulacao de Arquivos\arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

