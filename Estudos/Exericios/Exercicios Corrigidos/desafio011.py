# Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

print("Largura: {}".format(largura))
print("Altura: {}".format(altura))
print("Área da parede: {}m²".format(area))

litros = (area/2)
print("É necessário {} litros para pintar a parede".format(litros))
