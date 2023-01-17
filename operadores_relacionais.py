#aula 04 operadores relacionais


#se a expressão abaixo estiver correta irá retorna True ou False 
print(2 == 3)
print(3 != 2)
print(4 > 6)
print(2 < 3)
print(4 >= 2)
print(5 <= 6)
#esse é o exemplo usando operadores relacionais
nome = 'Joãozinho'
idade = """40"""
peso = 80.5
e_maior = True
idade = int(idade)
 
if idade > 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} NÃO é maior de idade.')
