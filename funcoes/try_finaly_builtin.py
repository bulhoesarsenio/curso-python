c = 2
d = 0
try:
    print("abrir")
    divisao = c / d

except ZeroDivisionError:
    ...
else:
    print("algo deu errado")
finally:
    print("dividiu por zero")
