
soma = int(input('digite um número: '))
lista = [n * soma for n in range(10 + 1) if n < 7]


print(*lista , sep='\n')


'''''
def par(*args):
    
    for i in args:
        
        if int(i) % 2 == 0:
            print('par:',i)

        elif int(i) % 2 == 1:
            print('impar:',i)

par(2,3,5,4)
'''