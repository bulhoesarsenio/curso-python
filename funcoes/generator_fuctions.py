def generator(n=0, m=10):
    while True:
        yield n
        n += 1

        if n > m:
            return -1


gen = generator(n=0)
for c in gen:
    print(c)
