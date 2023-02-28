lista_frutas = [
    ['mengod', 'manga',],#0

    ['goiaba',],#1

    ['uva', 'jaca',],#2
]

listando_frutas = input('digite  0 para acessar'
     'a primeira lista 1 para a segunda e 2 para ultima lista: ')   
listando_frutas_2 = input('agora digite a posição 0 ou 1, vai depender da lista: ')



numero_lista_1 = 0
numero_lista_2 = 0

try:
    numero_lista_1 = int(listando_frutas)
    numero_lista_2 = int(listando_frutas_2)
    print(lista_frutas[numero_lista_1][numero_lista_2])
except:
    print('indíce invalido')



#print(lista_frutas[0][1])
#print(lista_frutas[2][2][2])

'''
for i in lista_frutas:
    for fruta in i:
        print(fruta)
'''