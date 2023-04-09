lista = [1,4,2,3,6]

lista.sort()
print(lista)

diconario = [{'nome':'arsenio', 'sobrenome': 'neto'},
             {'nome':'slan', 'sobrenome': 'vieira'}]

diconario.sort(key=lambda item: item['sobrenome'])

for item in diconario:
    print(item)
