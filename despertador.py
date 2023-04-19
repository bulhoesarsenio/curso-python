from time import localtime
import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input()

pygame.event.wait() 
''''

from time import localtime
import pygame
h = input('h: ')
m = input('m: ')
while True:
    if localtime().tm_hour == int(h) and localtime().tm_min == int(m):
'''