nome = str(input('digite um nome: '))
palavra_invertida = nome[::-1]
if nome == palavra_invertida:
    
    print('a palavra ao inverso é igual')
else:
    print(len(nome))