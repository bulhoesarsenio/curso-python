# criando uma função que recebe os números, e os multiplica 
def multiplicacao(*args):
    contador = 1
    for c in args:
        contador*= c
    return contador

valor = multiplicacao(3,2,4,5)
print(valor)    

#criando uma função que recebe um número, e diz se é par ou ímpar

def valor(*args):

    for i in args:
        print(i)
        if i % 2 == 0:
            print(i,'= par' )
        else:
            print(i,'= impar')
    
       
             
        
valor(6,2,3,5)        