lista = [b for b in range(100000000)]
generator = (c for c in range(1000000000000000000000000000000000))

# print(lista)

print(next(generator))
print(next(generator))

for c in generator:
    print(c)
