valor = {'idade': '12'}
valor['nome'] = 'arsenio'

print(len(valor))
del valor['idade'] #deletando a chave da função
#valor_int = int(valor['idade'])

#print(type(valor_int))
#print(valor_int)
if valor.get('idade') is None:
    print('não existe')
else:
    print(valor)
#soma = valor_int + 2

#print(soma)