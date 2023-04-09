s1 = set()

s1.add('luiz')
s1.add('olá mundo')
s1.update(('olá mundo'))
#s1.clear()
s1.discard('olá mundo')
print(s1)














''''
valor = []
x = 1
while True:
    nomes = input('digite um nome: ')
    if nomes in valor:
        print('aí não papi')
    else:
        valor.append(nomes)
        print(*valor, sep=',')
'''
    