import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()
resp = input('deseja iniciar a musica [s/n] = ')
if resp == 's':
    print('tocando 100 bad days 8bits')
    pygame.mixer.music.load('an.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('tchau')

