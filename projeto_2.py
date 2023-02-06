from datetime import date

while True:
    ativo = input('QUAL É SEU ATIVO: ')
    
    if len(ativo) == 6 and not ativo.isnumeric() and not ativo.isalpha():
        tipo = input('TIPO: ') 
        
    else:
        print('ATIVO INVÁLIDO! O ATIVO DEVE TER NO MÍNIMO 5 ELEMENTOS COM LETRAS E NÚMEROS')
        continue
    
    preco_unitario = 0
    quantidade = 0


    data_atual = date.today()


    print('TA DO APDAORTE|  ATIVO  |  TIPO  |  PREÇO UNITÁRIO  |  QUANTIDADE  |         ')
    print(f'{data_atual}       {ativo} |  {ativo}')
