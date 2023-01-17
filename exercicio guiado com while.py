nome = 'Maria Helena'  

indício = 0
novo_nome = ''
while indício < len(nome):
    letra = nome[indício]
    novo_nome += f'*{letra}'
    indício += 1

novo_nome += '*'
print(novo_nome)
    