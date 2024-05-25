#Faça um programa em python qe abra e reproduza o audio de um arquivo mp3

import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
musica = pygame.mixer.Sound("desafio021trim2.mp3")

# Reproduz o arquivo MP3
musica.play()
pygame.time.delay(10000)#tocar por 10 seg
musica.stop() 

# Mantém o programa em execução até que a música termine
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)
   