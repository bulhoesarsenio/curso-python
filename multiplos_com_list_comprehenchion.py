numero = int(input('digite até quanto quer saber o multiplo: '))
 
#multiplo = int(input('digite qual multiplo deseja'))
lista_1 = [i for i in range(numero + 2)
         if i % 2 == 0
         ]
lista_2 = [i for i in range(numero + 1)
         if i % 2 == 1
         ]
            

print(lista_1)
print(lista_2)

    