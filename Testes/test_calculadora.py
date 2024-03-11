# test_calculadora.py
#Os testes são dividido em etapas 'Preparação' 'Ação' e 'Afirmação'

#Preparação#

#Importamos o módulo unittest.
import unittest
#Importamos a função 'adicionar' que queremos testar do arquivo calculadora.py.
from calculadora import adicionar
#importamos a função 'remover' que queremos testar do arquivo calculadora.py.
from calculadora import remover

#Cria a classe de testes, herdando da class unittest.TestCase
class TestCalculadora(unittest.TestCase):       

    def test_adicionar(self):
#Ação e Afirmação
         
        #Asserções de testes -  Testa se a função adicionar retorna o resultado correto
        self.assertEqual(adicionar(3, 5), 8)  # Espera-se que 3 + 5 seja igual a 8
        self.assertEqual(adicionar(-1, 1), 0)  # Espera-se que -1 + 1 seja igual a 0
        self.assertEqual(adicionar(0, 0), 0)   # Espera-se que 0 + 0 seja igual a 0

    def test_remover(self):
        #Testar se a função remover retorna o resultado correto
        self.assertEqual(remover(7,2),5)    #Espera-se que 7 -  2 seja igual a 5
        self.assertEqual(remover(4,2),2)    #Espera-se que 4 -  2 seja igual a 2

# Executa os testes definidos na class TestCalculadora
if __name__ == '__main__':
    unittest.main()

#Para executar o teste, basta rodar o arquivo test_calculadora.py. Se tudo estiver correto, você verá uma saída 'OK' indicando que o teste passou.