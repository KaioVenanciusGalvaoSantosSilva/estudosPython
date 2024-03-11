# Definindo a matriz de estoque de produtos como uma lista de listas
estoque = [
    ["Produto A", 10, 5.99],
    ["Produto B", 5, 2.49],
    ["Produto C", 20, 8.79]
]

# Imprimir o estoque
for item in estoque:
    print(f"Produto: {item[0]}, Quantidade: {item[1]}, Preço: R${item[2]:.2f}")
