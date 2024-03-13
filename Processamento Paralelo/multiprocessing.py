#Para tornar uma aplicação paralela é preciso pegar o que esta dentro de um loop -'for' por exemplo e transformar em função passando o parametro
#Em seguida é preciso usar o Parallel para informar o numero de trabalhos a serem feitos ao mesmo tempo, informar a função que sera executada, o parametro e o loop

#Neste exemplo:

#Importamos Parallel e delayed do joblib.
#Definimos uma função calcular_quadrado que calcula o quadrado de um número.
#Criamos uma lista de números de entrada.
#Definimos o número de processos paralelos que queremos usar (nesse caso, 2).
#Usamos a construção de compreensão de lista para gerar uma lista de tarefas, onde cada tarefa é o cálculo do quadrado de um número na lista.
#Usamos Parallel para paralelizar a execução dessas tarefas. O parâmetro n_jobs especifica o número de processos a serem usados.
#Finalmente, imprimimos os resultados.

#Instale joblib 'pip install joblib' em sua maquina se não estiver instalado!
from joblib import Parallel, delayed
import time

tempo_inicial = time.time()

# Função para calcular o quadrado de um número
def calcular_quadrado(numero):
    return numero * numero

if __name__ == "__main__":
    # Lista de números de entrada
    numeros = list(range(1000))

    # Número de processos paralelos a serem usados
    num_processos = 2 # Altere para o número desejado de processos

    # Usando o joblib para paralelizar o cálculo do quadrado para cada número na lista
    resultados = Parallel(n_jobs=num_processos)(delayed(calcular_quadrado)(num) for num in numeros)

    # Imprime os resultados
    print("Números de entrada:", numeros)
    print("Resultados:", resultados)
    tempo = time.time()-(tempo_inicial)
    
    print("Demorou: " + str(tempo))