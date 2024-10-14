# Função para gravar notas em um arquivo
def escrever_notas(nome_arquivo, nome_aluno, nota):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f'{nome_aluno}: {nota}\n')

# Função para ler o conteúdo do arquivo
def ler_notas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:\n", conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# Exemplo de uso
escrever_notas('notas.txt', 'Maria', 8.5)
escrever_notas('notas.txt', 'João', 7.2)
ler_notas('notas.txt')
