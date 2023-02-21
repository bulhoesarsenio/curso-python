''''
def valores(a, b, c):
    print(f'{a}x² {b}x {c} = 0')
         

    print(f'{a=} |' 
          f'{b=} |' 
          f'{c=} |')
    potencia = b ** 2
    
    expressao_numerica = -4 * a * c
    print(f'Δ = ({b}²) - 4.{a}.({c})')
    if c > 0:
        print(f'Δ = {potencia} { expressao_numerica}')
        subtracao = expressao_numerica + potencia 
        print(f'Δ = {subtracao}')
    else:
        soma = potencia + expressao_numerica
        print(f'Δ = {potencia} + {expressao_numerica}')
        print(f'Δ = {soma}')
        print('x = -b +- √Δ'
              '\n-----------'
              '\n    2.a')
        print(f'x = -({b}) +- √{soma}')
    
        
        
while True:
    try:
        valores(a = int(input('digite um número para (a): ')), 
                b= int(input('digite um número para (b): ')),
                c = int(input('digite um número para (c): ')))
        break
    except:
        print('11mNÚMERO INVÁLIDO')
        continue
'''

import math


def valores(a, b, c):
    print(f'{a}x² {b}x {c} = 0')

    print(f'{a=} |'
          f'{b=} |'
          f'{c=} |')
    potencia = b ** 2
    expressao_numerica = -4 * a * c
    subtracao = expressao_numerica + potencia
    print(f'Δ = ({b}²) - 4.{a}.({c})')
    if subtracao < 0:
        print(f'Δ = {potencia} { expressao_numerica}')
        print(f'Δ = {subtracao}')
    else:
        soma = potencia + expressao_numerica
        print(f'Δ = {potencia} + {expressao_numerica}')
        print(f'Δ = {soma}')
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
        print(f'x1 = {b} + {raiz}'
               '\n------------'
               f'\n   {divisao}')
        x_1 = regra_de_sinal + raiz
        print(f'x1 = {x_1}'
               '\n------------'
               f'\n   {divisao}')
        print(f'x1 = {x_1 / divisao}')

        print('=====================================')

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


        print('S = %.4f' % resultado_x1,  resultado_x2)


while True:
    try:
        valores(a=int(input('digite um número para (a): ')),
                b=int(input('digite um número para (b): ')),
                c=int(input('digite um número para (c): ')))
        break
    except:
        print('NÚMERO INVÁLIDO')
        continue