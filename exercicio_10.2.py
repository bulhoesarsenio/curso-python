
cpf = '81269401076'

calculando_1 = 0
validando_cpf = cpf[:9]
contador_regressivo = 10
for i in validando_cpf:
    calculando_1 += int(i) * contador_regressivo
    contador_regressivo -= 1
    resultado_1 = calculando_1 * 10 % 11
    print(contador_regressivo)


validando_cpf_2 = validando_cpf + str(resultado_1)

contador_regressivo_2 = 11

calculando_2 = 0
for ite in validando_cpf_2:
    calculando_2 += int(ite) * contador_regressivo_2
    contador_regressivo_2 -= 1
resultado_2 = calculando_2 * 10 % 11
resultado_final = validando_cpf_2 + str(resultado_2)
cpf_gerado = f'{validando_cpf}{resultado_1}{resultado_2}'
if cpf == cpf_gerado:
    print(f'cpf: {cpf} é válido')
else:
    print(f'cpf inválido')
