''''''
dicionario = {'nome': 'mengo'}
print(dicionario)
print(type(dicionario))
'''

def funcao(a):
    return a * a
    return a + a

print(funcao(a = int(input('digite um número: '))))
'''''


verbo = input('digite um verbo: ')

lista = verbo


iterando = verbo[-1]
if iterando == 'r':
    print('é um verbo')
else:
    print('não é um verbo')