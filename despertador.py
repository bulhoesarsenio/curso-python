lista_de_musica = ['loniest.mp3', 'medo.mp3']

from time import localtime
import pygame
pygame.init()
escolha_musica = int(input(f'escolha a música pelo indice: {lista_de_musica}'))
h = input('horas: ')
m = input('minutos: ')

while True:
    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
      
        pygame.mixer.music.load(lista_de_musica[escolha_musica])
        pygame.mixer.music.play()
        input()


''''
from time import localtime
import pygame
pygame.init()
h = input('h: ')
m = input('m: ')
while True:
    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
        pygame.mixer.music.load('loniest.mp3')
        pygame.mixer.music.play()
input()

    
'''

