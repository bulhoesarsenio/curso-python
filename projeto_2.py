from datetime import date

while True:
    ativo = input('QUAL É SEU ATIVO: ')

    if len(ativo) == 6 and not ativo.isnumeric() and not ativo.isalpha():

        while True:
            tipo = input('TIPO.DIGITE 5 ELEMENTOS COM TODOS ESSES LETRAS: ')

            if tipo.isdigit():
                continue
            elif len(tipo) == 5 and tipo.isalpha():
                while True:

                    preco_unitario = input('PREÇO UNITÁRIO')
                    if preco_unitario.isalpha():
                        print('DIGITE SÓ NÚMEROS')
                        continue
                    if preco_unitario.isdecimal():
                        preco_unitario_int = float(preco_unitario)

                        while True:
                            quantidade = input('QUANTIDADE: ')
                            if quantidade.isnumeric():
                                quantidade_int = float(quantidade)
                                data_atual = date.today()
                                valor_investido = quantidade_int * preco_unitario_int

                                print(
                                    'TA DO APDAORTE|  ATIVO  |  TIPO  |  PREÇO UNITÁRIO  |  QUANTIDADE  |  VALOR INVESTIDOR   |    ')
                                print(
                                    f'{data_atual}       {ativo} |  {tipo}    r${preco_unitario}                  {quantidade}              r${valor_investido}')
                                break
                        break

                break
        break
    # else:
        # print('DIGITE SÓ NÚMEROS')

    else:
        print('ATIVO INVÁLIDO! O ATIVO DEVE TER NO MÍNIMO 5 ELEMENTOS COM LETRAS E NÚMEROS')
        continue


'''''
tipo = input('TIPO: ')
        if len(tipo) == 5:
            while True:
                preco_unitario = input('PREÇO UNITÁRIO')
                if preco_unitario.isdigit():
                    while True:

                        quantidade = input('QUANTIDADE: ')
                        if quantidade.isnumeric():

                            data_atual = date.today()
                            preco_unitario_int = int(preco_unitario)
                            print(
                                'TA DO APDAORTE|  ATIVO  |  TIPO  |  PREÇO UNITÁRIO  |  QUANTIDADE  |         ')
                            print(
                                f'{data_atual}       {ativo} |  {tipo}    {preco_unitario}                 {quantidade}')
                        
                        else:
                            print('DIGITE SÓ LETRAS')
                            continue
 '''
