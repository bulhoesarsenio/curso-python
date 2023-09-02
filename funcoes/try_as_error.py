a = 2
c = 0


try:
    v = a / c

    print(c[9])

except (TypeError, NameError, ZeroDivisionError) as erro:
    print("erro:", erro.__class__.__name__)

