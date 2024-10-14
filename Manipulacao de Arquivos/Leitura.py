arquivo = open(r'C:\Users\Kaio\Git\estudosPython\Manipulacao de Arquivos\arquivo.txt', 'r')
#conteudo = arquivo.read()
#linha = arquivo.readline()
linhas = arquivo.readlines()
for linha in linhas:
    print(linha)
arquivo.close()