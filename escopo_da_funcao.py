a = 1
def escopo():
    
    def numero(x):
        print('%.0f'% x, a)
    while True:
        try:  
            numero(x = float(input('digite um número: ')))
            
            break
        except:
            print('digite só números')
        print(a)
escopo()
