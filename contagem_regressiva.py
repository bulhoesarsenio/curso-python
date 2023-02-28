lista = []
nomes = input('digite um nome: ')
lista.append(nomes)

with open('nomes.txt', 'a') as arquivo:
    for val in lista:

        arquivo.write(str(val)+ '\n')
        