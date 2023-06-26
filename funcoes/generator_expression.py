lista = [c for c in range(100)]
generator = (c for c in range(100000))


print(next(generator))
print(next(generator))

for c in generator:
    print(c)
