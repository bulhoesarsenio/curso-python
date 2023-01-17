while True:
   
    numero_1 = input('digite um número: ')
    
    numero_2 = input('digite outro número: ')
    
 
    
    numeros_validos = None

    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Um ou ambos os nomes digitados são inválidos.')
        
        continue
    operador = (input('digite um operador que deseja:-*/+: '))
    operadores_permitidos = '+/*-'
    if operadores_permitidos not in operador:
        if operador == '+':
            print(num_1_float + num_2_float)
        if operador == '*':
            print(num_1_float * num_2_float)
        if operador == '-':
            print(num_1_float -  num_2_float)
        if operador == '/':
            print(num_1_float / num_2_float)
   
    else:
        print('digite só esses operadores -> / + - *')
    
    sair = input('quer continuar(s) ou (n): ')
    
    if sair == 's':
        continue
    
    if sair == 'n':
        break
    else:
        print('algo deu errado')