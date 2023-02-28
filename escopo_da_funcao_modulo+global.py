valor = 1

def escopo():
    global valor
    valor_2 = 13
    valor = 3
    print(valor_2, valor)
    def escopo_2():
        nome = 'mengo'
        print(nome)
    escopo_2()

escopo()

