dicionario = {'nome': 'alan',
              'sobrnome': 'queiroz'}

#desmpacotamento = {**dicionario}
#print(dicionario)
#print(desmpacotamento)

def funcao(*args, **kwargs):
    print('não nomeados', args)
    #print(kwargs)
    for c, i in kwargs.items():
        print(c, i)

funcao(**dicionario)









''''
lista = ['musica.mp3', 'loniest.mp3', 'broke.mp3']
print(lista)

tamanho = len(lista)
escolha = input(f'escolha sua música acima. Para acessar a música digite o índice começando com 0: ')
if escolha.isalpha():
    print('dado inválido!')
else:   
    int_escolha = int(escolha)


    musica = lista[int_escolha]
    print(musica)

from time import localtime
import pygame
pygame.init()
pygame.mixer.music.load(musica)
pygame.mixer.music.play()
input()

pygame.event.wait() 
'''