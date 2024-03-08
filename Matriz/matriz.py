def criar_matriz_linha_coluna(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(None)
        matriz.append(linha)
    return matriz

def inserir_dados(matriz, linha, coluna, dados):
    matriz[linha][coluna] = dados

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def excluir_dado(matriz, linha, coluna):
    matriz[linha][coluna] = None

def modificar_dado(matriz, linha, coluna, novo_dado):
    matriz[linha][coluna] = novo_dado

# Criando uma matriz 3x3 para representar o estoque de produtos
estoque = criar_matriz_linha_coluna(3, 3)

# Inserindo dados fictícios no estoque
inserir_dados(estoque, 0, 0, "Produto A")
inserir_dados(estoque, 0, 1, 10)  # Quantidade disponível
inserir_dados(estoque, 0, 2, 5.99)  # Preço

inserir_dados(estoque, 1, 0, "Produto B")
inserir_dados(estoque, 1, 1, 5)
inserir_dados(estoque, 1, 2, 2.49)

inserir_dados(estoque, 2, 0, "Produto C")
inserir_dados(estoque, 2, 1, 20)
inserir_dados(estoque, 2, 2, 8.79)

# Exibindo a lista
print("Lista de estoque:")
exibir_matriz(estoque)

# Excluindo um dado (por exemplo, quantidade do Produto B)
excluir_dado(estoque, 1, 1)

# Modificando um dado (por exemplo, preço do Produto C)
modificar_dado(estoque, 2, 2, 10.99)

# Exibindo a lista atualizada
print("\nLista de estoque após exclusão e modificação:")
exibir_matriz(estoque)


