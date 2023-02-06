numero = input('digite um número: ')
if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('par')
    else:
        print('ímpar')
resultado = 301 * 10
soma = resultado % 11 
print(soma)
