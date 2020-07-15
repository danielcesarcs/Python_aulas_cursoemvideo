"""Abrindo MP3"""

# Importação de bibliotecas de reprodução

import pygame
pygame.init()
pygame.mixer.music.load('../usando_modulos_py-mundo_1/rap.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('Reprodução de Música')
