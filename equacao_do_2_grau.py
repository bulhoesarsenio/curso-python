import math
from fractions import Fraction


def valores(a, b, c):
    potencia = b ** 2
   
    expressao_numerica = -4 * a * c
    subtracao = expressao_numerica  + potencia
       
    
    if subtracao < 0:
        print('IMPOSSÍVEL DE CALCULAR A EQUAÇÃO, POIS NÃO POSSUI RAIZES REAIS ENTÃO A SOLUÇÃO É S = {} ')
    elif a == 0:
       print('O VALOR (A) NÃO PODE RECEBER VALOR 0')
    else:
        print(f'{a}x² {b}x {c} = 0')


        print(f'{a=} |'
          f'{b=} |'
          f'{c=} |')
        soma = potencia + expressao_numerica
        print(f'Δ = (b)² -4.a.c')
        print(f'Δ = {potencia} + {expressao_numerica}')
        print(f'Δ = {soma}')
        print('')
        print('x = -b +- √Δ'
              '\n-----------'
              '\n    2.a')
        regra_de_sinal = -(b)
        print(f'x = -({b}) +- √{soma}'
              '\n------------'
              f'\n    2.{a}')
        divisao = 2 * a
        raiz = float(soma) ** 0.5
        print(f'x = {regra_de_sinal} +- {raiz} '
              '\n------------'
              f'\n    {divisao}')
        print('')
        if b > 0: 

            print(f'x1 = -{b} + {raiz}'
               '\n------------'
               f'\n   {divisao}')
        if b < 0:
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
    
while True:
    
    try:
    
        valores(a=int(input('digite um número para (a): ')),
                b=int(input('digite um número para (b): ')),
                c=int(input('digite um número para (c): ')))

            
        break
    except:
        print('NÚMERO INVÁLIDO')
        continue  
        

            
   
        