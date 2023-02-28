nome = 'Maria Helena'  

indicio = 0
novo_nome = ''
while indicio < len(nome):
    letra = nome[indicio]
    novo_nome += f'*{letra}'
    indicio += 1

novo_nome += '*'
print(novo_nome)
    