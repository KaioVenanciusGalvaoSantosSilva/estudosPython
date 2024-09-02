# Usamos o tratamento de exceções em programação para gerenciar erros e situações inesperadas que podem ocorrer durante a execução de um programa. O objetivo principal é evitar que o programa termine de forma abrupta e oferecer uma maneira controlada de lidar com essas situações. Aqui estão alguns motivos específicos para usar o tratamento de exceções:

# Prevenção de Crashes: Sem tratamento de exceções, um erro pode causar a interrupção imediata do programa, resultando em uma má experiência para o usuário. Exceções permitem capturar e lidar com erros, mantendo o programa em execução.

# Manutenção da Lógica de Negócio: Exceções permitem separar a lógica principal do código das rotinas de tratamento de erro. Isso torna o código mais legível e organizado, facilitando a manutenção.

# Diagnóstico de Erros: Exceções podem ser usadas para capturar e registrar informações sobre o erro que ocorreu, ajudando a diagnosticar e corrigir problemas mais tarde.

# Fornecimento de Feedback ao Usuário: Ao capturar exceções, o programa pode fornecer mensagens de erro claras e amigáveis, orientando o usuário sobre como corrigir o problema (por exemplo, inserindo dados corretos).

# Garantia de Liberação de Recursos: Com o uso de blocos finally, você pode garantir que recursos como arquivos, conexões de banco de dados, ou memória sejam liberados corretamente, mesmo que ocorra um erro durante o processamento.

# Resiliência do Programa: Ao lidar com exceções, o programa pode continuar a funcionar mesmo quando encontra condições imprevistas, tornando-o mais robusto e confiável.

# Em resumo, o tratamento de exceções torna os programas mais seguros, confiáveis e fáceis de usar, garantindo que eles possam lidar com erros de forma graciosa e eficiente.

#Esses exemplos cobrem os conceitos fundamentais de tratamento de exceções em Python:
    # Exceção Básica com try-except
    # Tratamento de Múltiplas Exceções
    # Uso do else com try-except
    # Uso do finally
    # Criando Exceções Personalizadas


# 1. Exceção Básica com try-except
#     Devemos usar para resolver exceções simples como:
#         ValueError - ao inserir letras para realizar o calculo em vez de números
    

#SEM TRATAMENTO

# x = int(input("Digite um número: "))
# print(f"O dobro do número é {x * 2}")

#Retornará erro no console-> ValueError: invalid literal for int() with base 10: 'letradigitada'

#COM TRATAMENTO BÁSICO
try:
    x = int(input("Digite um número: "))
    print(f"O dobro do número é {x * 2}")
except ValueError:
    print("Por favor, insira um número válido.")

# Explicação: Aqui, o try tenta converter a entrada do usuário em um número inteiro. 
# Se o usuário inserir algo que não pode ser convertido em um inteiro, o bloco except captura a exceção ValueError e exibe uma mensagem apropriada.

#2. Tratamento de Múltiplas Exceções

#SEM TRATAMENTO

# a = int(input("Digite o dividendo: "))
# b = int(input("Digite o divisor: "))
# resultado = a / b
# print(f"O resultado da divisão é {resultado}")

#Poderá retornar mais de uma exceção para o casos:
#  de valores de divisão não ser inteiros que retornará erro no console -> ValueError: invalid literal for int() with base 10: '2,5'
#  de 0/0 que retorna exception que retornará erro no console -> ZeroDivisionError: division by zero


#COM TRATAMENTO DE MULTIPLAS EXCEPTS
try:
    a = int(input("Digite o dividendo: "))
    b = int(input("Digite o divisor: "))
    resultado = a / b
    print(f"O resultado da divisão é {resultado}")
except ValueError:
    print("Você deve digitar números inteiros.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

# Explicação: Este exemplo mostra como capturar diferentes tipos de exceções: ValueError se a entrada não for um número inteiro, e ZeroDivisionError se o usuário tentar dividir por zero.

#3. Uso do else com try-except

#SEM TRATAMENTO
# x = int(input("Digite um número: "))

# print(f"Você digitou o número {x}")

#No caso acima ainda retornará um erro caso insira dado não valido

#COM TRATAMENTO USANDO ELSE
try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número válido.")
else:
    print(f"Você digitou o número {x}")

#Explicação: O bloco else é executado apenas se nenhuma exceção for levantada no bloco try.


#4. Uso do finally
#SEM TRATAMENTO

# arquivo = open("dados.txt", "r")
# conteudo = arquivo.read()
# print(conteudo)

# arquivo.close()
# print("O arquivo foi fechado.")


#COM TRATAMENTO USANDO FINALLY
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
finally:
    arquivo.close()
    print("O arquivo foi fechado.")

#Explicação: O bloco finally é executado independentemente de uma exceção ter ocorrido ou não. Isso é útil para garantir que recursos como arquivos sejam fechados corretamente.


#5. Criando Exceções Personalizadas
class MinhaExcecao(Exception):
    pass

def verificar_positivo(num):
    if num < 0:
        raise MinhaExcecao("Número negativo não é permitido")
    return num

try:
    x = int(input("Digite um número positivo: "))
    verificar_positivo(x)
except MinhaExcecao as e:
    print(e)

#Explicação: Neste exemplo, uma exceção personalizada é criada e usada para levantar um erro específico caso um número negativo seja inserido.