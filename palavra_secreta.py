palavra_secreta = 'mengod'

letras_acertadas = ''

x = 0
while True:
    x += 1
    letra = input(f'digite uma letra S para sair:[{x}] ')
    
    tamanho = len(letra)
    if tamanho > 1:
        print('digite só uma letra')
        continue
    if letra in palavra_secreta:
        letras_acertadas += letra
    else: 
        print('*')
    if letra == 's':
        break
    
    print(letras_acertadas)
    
    if letras_acertadas == palavra_secreta:
        print('PARABÉNS! VOCÊ CONCLUIU O PROGRAMA')
    
        break
    
    