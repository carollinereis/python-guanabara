"""
Faça um programa em python que abra e reproduza o áudio 
de um arquivo mp3
necessario baixar pygame no computador e salvar audio mp3 na mesma pasta do exercicio.
"""

import pygame
pygame.init()
pygame.mixer.music.load('canonD.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('O que achou?') # só rodou com esse input 