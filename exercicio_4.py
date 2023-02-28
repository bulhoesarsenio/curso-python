indice = 0
nome = 'mengo'
while indice < len(nome):
    qtd_letras = nome[indice]
    lettras = nome.count(qtd_letras)

    print(qtd_letras,lettras)
    indice += 1