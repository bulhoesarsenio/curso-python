import math


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
        regra_de_sinal = -(b)
        print(f'x = -({b}) +- √{soma}'
              '\n------------'
              f'\n    2.{a}')
        divisao = 2 * a
        raiz = float(soma) ** 0.5
        print(f'x =  {regra_de_sinal} +- {raiz} '
              '\n------------'
              f'\n    {divisao}')


while True:
    try:
        valores(a=int(input('digite um número para (a): ')),
                b=int(input('digite um número para (b): ')),
                c=int(input('digite um número para (c): ')))
        break
    except:
        print('NÚMERO INVÁLIDO')
        continue
