lista = []
x = 0

while True:   
   
    lista_devalores = input('[i]inserir [a]apagar [l]listar: ')
    
    
    if lista_devalores == 'i':
        inserindo = input('insira algo na lista: ')
        if inserindo.isdigit():
            if inserindo.isalnum():
                print('erro digite só letras')
        elif inserindo.isalpha():
            lista.append(inserindo)
            print(lista)
    
    elif lista_devalores == 'l':
        for item in enumerate(lista):       
            print(item)
        if len(lista) == 0:
            print('a lista esta vazia insira algo')     
        
    elif lista_devalores == 'a':
        apagando = input('insira um indíce para deletar: ')
        

        try:

            indice = int(apagando)
            del lista[indice]
            print('oi')
        except:
            print('indice inválido')
    else:
        print('digite l, i ou a')
