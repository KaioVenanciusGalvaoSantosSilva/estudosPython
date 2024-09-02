# A modularização do código através do uso de funções e procedimentos é uma prática essencial em programação para tornar o código mais organizado,
# reutilizável e fácil de entender. Vou mostrar exemplos de modularização em Python, abordando a passagem de valores por valor, por referência e por resultado.


# 1. Passagem por Valor
# Em Python, a passagem por valor ocorre com tipos imutáveis, como números e strings. Isso significa que a função recebe uma cópia do valor, e não o valor original.

def incrementar_valor(x):
    x += 1
    return x

numero = 5
resultado = incrementar_valor(numero)
print(f"Valor original: {numero}")  # 5
print(f"Valor após a função: {resultado}")  # 6

# Explicação: Aqui, x é uma cópia de numero, então as alterações em x não afetam numero.

# 2. Passagem por Referência
# Python passa objetos mutáveis, como listas ou dicionários, por referência. Isso significa que a função pode modificar o objeto original.

def adicionar_elemento(lista):
    lista.append(4)

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista)
print(f"Lista após a função: {minha_lista}")  # [1, 2, 3, 4]

# Explicação: Aqui, minha_lista é passada por referência, então as alterações feitas dentro da função adicionar_elemento afetam a lista original.


# 3. Passagem por Resultado
# Embora Python não suporte passagem por resultado de forma nativa como algumas outras linguagens, você pode simular esse comportamento retornando o valor modificado.

def quadrado(x):
    return x * x

def cubo(x):
    return x * x * x

numero = 3
quadrado_resultado = quadrado(numero)
cubo_resultado = cubo(numero)

print(f"Quadrado de {numero}: {quadrado_resultado}")  # 9
print(f"Cubo de {numero}: {cubo_resultado}")  # 27


# Explicação: Aqui, cada função retorna um novo valor como resultado da operação realizada.

# 4. Modularização com Funções
# Você pode combinar essas abordagens para criar um programa modularizado, onde cada função realiza uma tarefa específica.

def obter_dados():
    return int(input("Digite um número: "))

def processar_dados(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

def exibir_resultados(quadrado, cubo):
    print(f"O quadrado do número é: {quadrado}")
    print(f"O cubo do número é: {cubo}")

def main():
    numero = obter_dados()
    quadrado, cubo = processar_dados(numero)
    exibir_resultados(quadrado, cubo)

# Executa o programa
main()

# Explicação: Neste exemplo, a função main coordena o fluxo do programa, chamando outras funções para obter dados, processá-los e exibir os resultados. 
# Cada função é responsável por uma parte específica do processo, tornando o código mais modular e fácil de manter.

# Esses exemplos mostram como você pode modularizar seu código em Python, usando funções para manipular dados através de diferentes tipos de passagem de valores.