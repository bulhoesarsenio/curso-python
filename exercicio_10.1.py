cpf = '111444777'
contador_regressivoa = 10
digitos_cpf = cpf[:9]
calculoa = 0
for c in digitos_cpf:
    calculoa += int(c) * contador_regressivoa
    contador_regressivoa -= 1
resultadoa_1 = calculoa *10 % 11
#print(resultadoa)


#cpf = '74682489070'
adicionando = digitos_cpf + str(resultadoa_1)
contador_regessivo = 11

calculo = 0

for con in adicionando:
    calculo += int(con) * contador_regessivo
    contador_regessivo -= 1
resultado_2 = calculo * 10 % 11
cpf_gerado = f'{digitos_cpf}{resultado_2}{resultadoa_1}'
#if resultado <= 9:
print(cpf_gerado)
#else:
print('cpf inválido')