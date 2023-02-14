
from datetime import date
preco_unitario = 0
preco_unitario_int = 0
quantidade_int = 0
data_atual = date.today()
quantidade = 0
while True:
    ativo = input('QUAL É SEU ATIVO, COM 6 ELEMENTOS CONTENDO LETRAS E NÚMEROS: ')

    
    
    if len(ativo) == 6 and not ativo.isnumeric() and not ativo.isalpha():
        
        while True:
                tipo = input('TIPO.DIGITE 5 ELEMENTOS COM TODOS ESSES LETRAS: ')
                
                if tipo.isdigit():
                    continue
                elif len(tipo) == 5 and tipo.isalpha():   
                    while True:
                        try:
                            preco_unitario = float(input('PREÇO UNITÁRIO: '))                     
                            break
                            
                                
                        except:
                             print('ERROR DIGITE SÓ NÚMEROS')
                             continue
                    preco_unitario_int = float(preco_unitario)    
                    while True:
                                try:
                                    quantidade = (input('QUANTIDADE: '))
                                    quantidade_int = float(quantidade)
                                    data_atual = date.today()

                                    break
                                    

                                except:
                                        print('ERRO, DIGITE SÓ NÚMEROS')
                                        continue
                                    
                    
                                    
                    print(
                        'TA DO APDAORTE|  ATIVO  |  TIPO  |  PREÇO UNITÁRIO  |  QUANTIDADE  |  VALOR INVESTIDOR   |    ')
                    print(
                        f'{data_atual}       {ativo} |  {tipo}    r${preco_unitario}                  {quantidade}              r${quantidade_int * preco_unitario_int}')
                    break
                #break

            #break
        break
    #else:
        #print('DIGITE SÓ NÚMEROS')

    else:
        print('ATIVO INVÁLIDO! O ATIVO DEVE TER NO MÍNIMO 5 ELEMENTOS COM LETRAS E NÚMEROS')
        continue
    
