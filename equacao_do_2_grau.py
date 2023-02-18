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
        
      