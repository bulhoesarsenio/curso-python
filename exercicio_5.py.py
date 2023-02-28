numero = input('digite um número: ')
numero_1 = input('digite um número: ')


try:
    numero_int = int(numero)
    numero_1_int = int(numero_1)
    calculo = numero_int + numero_1_int
    print(calculo)
except:
    print('algo deu errado')

    

