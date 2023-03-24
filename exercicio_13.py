acerto = 0
erro = 0
dicionario = [{'pergunta_1': 'quanto é 3*5?',
               'opcoes_1': [2,4,3,15],
                'resposta_1': '15',
                
                'pergunta_2': 'quanto é 4/2?',
                'opcoes_2': [4,2,3,5],
                'resposta_2': '2',
                
                'pergunta_3': 'quanto é 80-4?',
                'opcoes_3': [4,76,54,2],
                'resposta_3': '76'}]


print(dicionario[0]['pergunta_1'])
for c in dicionario[0]['opcoes_1']:
    
    print(f'{c}')

perguntando = input('qual número está correto? ')


if perguntando == dicionario[0]['resposta_1']:
    acerto +=1
    print('acertou')
else:
    erro += 1

print('=============================================')
print(dicionario[0]['pergunta_2'])
for c in dicionario[0]['opcoes_2']:
    
    print(f'{c}')

perguntando = input('qual número está correto? ')


if perguntando == dicionario[0]['resposta_2']:
    acerto +=1
    print('acertou')
else:
    erro += 1
print('=============================================')

print(dicionario[0]['pergunta_3'])
for c in dicionario[0]['opcoes_3']:
    
    print(f'{c}')

perguntando = input('qual número está correto? ')


if perguntando == dicionario[0]['resposta_3']:
    acerto +=1
    print('acertou')
else:
    erro += 1
    
print(f'você acertou {acerto} de 3')