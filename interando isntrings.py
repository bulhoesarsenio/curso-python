'''
frase = 'olá mundo'
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
'''

frase = 'olá mundo'
indices = range(len(frase))

for indice in indices:
    print(indice, frase[indice])
   