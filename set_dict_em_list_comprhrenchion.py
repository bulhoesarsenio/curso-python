dictt = {"nome": "arsenio", "idade": 14}

lista = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in dictt.items()
}

print(lista)


sets_comprenchion = {c for c in range(10)}


print(sets_comprenchion)

"""''
for c, i in dictt.items():
    
    print(f'{c}: {i}')
"""
