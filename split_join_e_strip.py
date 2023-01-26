frase = 'olha que,     interessante'

lista_palavras = frase.split()

lista = []
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    lista.append(lista_palavras[i].strip())

print(lista)
frases_unidas = ' '.join(lista_palavras)
print(frases_unidas)