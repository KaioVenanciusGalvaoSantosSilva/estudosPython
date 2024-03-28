#FUNCAO == SUB-ROTINA
#Funcao para Somar 2 valores
#inicio
def soma (x,y):
    #DOCUMENTAÇÃO
    """
    Função soma que recebe dois valores  x e y como parametros e retorna a soma deles.
    
    Parâmetros:
        - x: Recebe o primeiro valor do operador da adição.
        - y: Recebe o segundo valor do operador da adição.
        
    Retorno:
        A função retorna a soma de x e y.
    
    """
    soma = x + y
    print("O valor da soma pela função do lado de dentro  é: "+ str(soma))
    return soma #POSSUI RETORNO
#fim

valor1 = 2
valor2 = 3
#chamada da função com os valores passados como parâmetros

print("O valor da soma pela função do lado de fora é: "+ str(soma(valor1, valor2)))#passando os parametros direto para a função soma
   
   