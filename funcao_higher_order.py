def funcao(nome, valor):
    return f'{nome}, {valor}'

def execultando(frase, *arsg):
    return frase(*arsg)

print(execultando(funcao, 'bom dia', 'oi'))