
import math
from fractions import Fraction

while True:
    
    try:
    
        a = float(input('digite um número para (a): '))
        b = float(input('digite um número para (b): '))
        c = float(input('digite um número para (c): '))
        

        

        valores_int_a = math.trunc(a)
        valores_int_b = math.trunc(b)
        valores_int_c = math.trunc(c) 
        
        potencia = valores_int_b ** 2
   
        expressao_numerica = -4 * valores_int_a * valores_int_c
        subtracao = expressao_numerica  + potencia
       
    
        if subtracao < 0:
            print('IMPOSSÍVEL DE CALCULAR A EQUAÇÃO, POIS NÃO POSSUI RAIZES REAIS ENTÃO A SOLUÇÃO É S = {} ')
            break
        elif valores_int_a == 0:
            
            print('O VALOR (A) NÃO PODE RECEBER VALOR 0')
            break
        else:
            print(f'{valores_int_a}x² {valores_int_b}x {valores_int_c} = 0')



            soma = potencia + expressao_numerica
            print(f'Δ = (b)² -4.a.c')
            print(f'Δ = {potencia} + {expressao_numerica}')
            print(f'Δ = {soma}')
            print('')
            print('x = -b +- √Δ'
              '\n-----------'
              '\n    2.a')
            regra_de_sinal = -(valores_int_b)
            print(f'x = -({b}) +- √{soma}'
          '\n------------'
              f'\n    2.{valores_int_a}')
            divisao = 2 * valores_int_a
            raiz = float(soma) ** 0.5
            print(f'x = {regra_de_sinal} +- {raiz} '
              '\n------------'
              f'\n    {divisao}')
            print('')
            if valores_int_b > 0: 

                print(f'x1 = -{b} + {raiz}'
               '\n------------'
               f'\n   {divisao}')
            if valores_int_b < 0:
                print(f'x1 = {b} + {raiz}'
               '\n------------'
               f'\n   {divisao}')
            x_1 = regra_de_sinal + raiz
        
            print(f'x1 = {x_1}'
               '\n------------'
               f'\n   {divisao}')
            print(f'x1 = {x_1 / divisao}')
            print('')
            print('====================================')

            x_2 = regra_de_sinal - raiz
            print(f'x2 = {b} - {raiz}'
             '\n-------------'
               f'\n   {divisao}')
            print(f'x2 = {x_2} '
               '\n-------------'
               f'\n   {divisao}')
            resultado_x1 = x_1 /divisao
            resultado_x2 = x_2 /divisao
            print(f'x2 = {x_2 / divisao}')

            print('')
            print('S x1 = %.2f' % resultado_x1)
            
            
            
            
            
            print('S x2 = %.2f' % resultado_x2)            
            print(Fraction(resultado_x2))     
            break
        
    

    except (ValueError, TypeError):
        print('tivemos um problema com os tipos de dados informados. informe um número válido'.upper())
    except NameError:
        print('erro isso não é um número válido'.upper()) 
    except KeyboardInterrupt:
        print('\nvocê não poderá sair do programa, até que você digite um número'.upper())









