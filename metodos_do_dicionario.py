pessoas = {'idade': '14',
           'nome': 'arsenio',
           'altura': '1.23'}
pessoas.setdefault('altura', 0)
print(pessoas['altura'])

print(len(pessoas.keys()))
print(list(pessoas.items()))
print(list(pessoas.values()))
'''''
print(30*'=')
for con in pessoas.values():
    print(con)
'''


