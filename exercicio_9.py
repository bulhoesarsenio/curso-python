x = 0
lista = []
resultado = 0
while x < 9:
    x += 1
    
    numero = input(f'digite um númereo: x{x}: ')
    if numero.isdigit():    
        numero_int = int(numero)
        lista.append(numero_int)
        print(lista)
        #resultado += numero_int
        #print(resultado)
    else:
        print('um ou ambos números foram digitados errados ')

soma = sum(lista)
print(soma)
resto = soma * 10
resultado = resto % 11
print(resultado if resultado <= 9 else 0)

#resultado_final = resto_divisao % 11
#print(f'o primeiro digíto do cpf é: {resultado_final}')  
    