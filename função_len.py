nome = input('nome: ')
usuario = input('digite outra coisa: ')
qtd_caracteres = len(nome + usuario)
print('quantidades de caracteres: ',qtd_caracteres)

if qtd_caracteres > 7:
    print('é um nome')
else:
    print('não é um nome')