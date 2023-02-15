cpf = '74682489070'
contador_regressivo = 10
digitos_cpf = cpf[:9]
calculo = 0
for c in digitos_cpf:
    calculo += int(c) * contador_regressivo
    contador_regressivo -= 1
resultado = calculo *10 % 11
print(resultado)
