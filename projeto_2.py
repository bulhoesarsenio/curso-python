from datetime import date
while True:
    ativo = input('QUAL É SEU ATIVO: ')
    if  ativo.isalnum():
        print(ativo)
    if ativo.isdigit():
        ativo = input('digite SEU ATIVO EXEMPLO: TAEE11: ')
    tipo = 0  
    preco_unitario = 0
    quantidade = 0


    data_atual = date.today()


    print(f'DATA DO APORTE|  ATIVO  |  TIPO  |  PREÇO UNITÁRIO  |  QUANTIDADE  |\n{data_atual}    |  {ativo}   |  {tipo} |  {preco_unitario}               |  {quantidade}           |')

