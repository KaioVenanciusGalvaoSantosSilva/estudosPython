#Módulos Python
#https://docs.python.org/3.12/library/index.html
#https://pypi.org/ #biblioteca de programadores  

#Biblioteca emoji
#https://pypi.org/project/emoji/#description
#EMOJI LIST 
#https://carpedm20.github.io/emoji/all.html?enableList=enable_list_pt

#Utilizando módulos
#Use o 'import nome_da_biblioteca' para importar bibliotecas
#Ao importar a biblioteca irá importar tudo que tem dentro dela

#Exemplo:
#import math

#Importação única use 'from nome_da_biblioteca import função'
#Ao importar a função de dentro da biblioteca será realizado um import especifico
#Usamos import especificos para otimizar o código

#Exemplo:
#from math import factorial
#ou
#from math import factorial, sqrt

#Biblioteca math - utilizada para calculos matemáticos
#ceil       - arredonda para cima
#floor      - arredonda para baixo
#trunc      - remove a parte fracionária do número
#pow        - potencia == **
#sqrt       - raiz quadrada
#factorial  - fatorial

#Exemplo prático
# import math
import emoji
from math import sqrt
num = int(input("Digit um número: "))
# raiz = math.sqrt(num)
raiz = sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num,raiz))

#Biblioteca random - utilizado para dados randomicos
import random
num0 = random.random() #Números randomicos decimais entre 0 e 1
num1 = random.randint(1,10) # Números randomicos inteiros no range definido
print(emoji.emojize("Python é :medalha_de_ouro:", language='pt'))
