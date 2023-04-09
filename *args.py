
def valor(*args):

    interando = range(len(args))
    soma = 0
    for c in interando:
       soma += args[c]
    
    #print(f'a soma entre {args} é:', soma)
    #return soma

numero = valor(10,23)
numero_2 = valor(3, 2, 4)

print(numero)
print(numero_2)
