lista = []
while True:
   
    
    lista_devalores = input('[i]inserir [a]apagar [l]listar: ')
    if lista_devalores == 'i':
        inserindo = input('insira algo na lista: ')
        lista.append(inserindo)
        print(lista)
    
    try:
       lista_str = str(lista_devalores) 
    except:
        print('digite novamente')
        lista_devalores = None
    if lista_devalores == None:
        print('um ou ambos números estão nomes digitados estão errados, digite novamente')

    