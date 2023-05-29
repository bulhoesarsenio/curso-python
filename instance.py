lista = [2, "a", {0, 1}, "b", 3]


for c in lista:
    if isinstance(c, set):
        c.add(3)
    print(c, isinstance(c, set))
