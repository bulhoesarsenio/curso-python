import decimal
numero_flloat_1 = decimal.Decimal('0.1')
numero_flloat_2 = decimal.Decimal('0.3')

numero_3 = numero_flloat_1 + numero_flloat_2
print(f'{numero_3:.10f}')
print(round(numero_3, 2))