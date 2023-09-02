def generator_1():
    yield 1
    yield 2


def generator_2(gen):
    yield from gen()
    yield 3


gen = generator_2(generator_1)


for x in gen:
    print(x)
