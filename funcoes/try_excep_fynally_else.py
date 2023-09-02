a = 12
b = 3

try:
    divisao = a / b

except ZeroDivisionError:
    print("impossível de dividir")
except NameError:
    print("variável não está definidada")
else:
    print(divisao)
