nome = "arsenio"
valor = input("digite um método para usar: ")

metodo = valor
if hasattr(nome, metodo):
    print(getattr(nome, metodo)())
else:
    print(f"não podemos unir o metodo {metodo}")
