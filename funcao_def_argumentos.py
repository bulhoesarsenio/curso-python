
#def soma(x, a, z=None):
def soma(x, a):
    print(x + a)
    print(f'{x=}  {a=} | x + a = {x + a}')
while True:
    try:
        soma(x=int(input('digite para x: ')), a=int(input('digite para a: ')))
        break
    except:
        print('erro')

