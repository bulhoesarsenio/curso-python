lista = []
tupla = ()


def falsy(valor):
    return "falsy" if not valor else "truthy"


print("teste", falsy("teste"))
print(f"{lista=}", falsy(lista))
print(f"{tupla=}", falsy(tupla))

nome = "amei te ver"

print(nome.find(" "))

import tkinter as tk

"""''
def button1_click():
    
    numero1 = int(input("digite um número: "))
    numero2 = int(input("digite um número: "))
    soma = numero1 + numero2
    print(f"a soma entre: {numero1} + {numero2} = {soma}")
    

def button2_click():
    # Obtém o texto inserido na entrada
    print("Texto inserido: ")


# Cria a janela principal
janela = tk.Tk()


# Cria os botões
botao1 = tk.Button(janela, text="soma", command=button1_click)
botao2 = tk.Button(janela, text="multiplicação", command=button2_click)

# Define a posição dos widgets na janela

botao1.pack()
botao2.pack()

# Inicia o loop de eventos da janela
janela.mainloop()



import tkinter as tk


def button1_click():
    print("Botão 1 foi clicado!")


def button2_click():
    print("Botão 2 foi clicado!")


# Cria a janela principal
janela = tk.Tk()

# Cria os botões
botao1 = tk.Button(janela, text="Botão 1", command=button1_click)
botao2 = tk.Button(janela, text="Botão 2", command=button2_click)

# Define a posição dos botões na janela
botao1.pack()
botao2.pack()

# Inicia o loop de eventos da janela
janela.mainloop()



import tkinter as tk

n = int(input("soma: "))
soma = n + n


def btn_click():
    label.config(text=soma)


# Criação da janela
window = tk.Tk()
window.title("Interface Simples")

# Criação de um rótulo
label = tk.Label(window, text="Pressione o botão para exibir uma mensagem.")
label.pack(pady=10)

# Criação de um botão
button = tk.Button(
    window,
    text="soma",
    command=btn_click,
)

button.pack()

# Execução do loop principal da janela
window.mainloop()

import tkinter as tk


def obter_dados():
    # Função para obter os dados inseridos pelo usuário
    nome = entrada_nome.get()

    altura = entrada_altura.get()
    peso = entrada_peso.get()
    peso_int = int(peso)
    altura_int = int(altura)
    peso_int = float(peso)
    altura_int = float(altura)
    imc = peso_int / (altura_int * altura_int)
    print("Nome:", nome)
    print("Altura:", altura)
    print("peso", peso)

    mensagem["text"] = f"Nome: {nome}\n Altura: {altura} \nPeso: {peso} \nIMC: {imc}"


janela = tk.Tk()
janela.title("CALCULO IMC")
janela.geometry("400x300")

# Cria uma entrada de texto para o nome

rotulo_nome = tk.Label(janela, text="Nome:", fg="red")

rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()


rotulo_altura = tk.Label(janela, text="Altura: ", fg="green")
rotulo_altura.pack()

entrada_altura = tk.Entry(janela)
entrada_altura.pack()

rotulo_peso = tk.Label(janela, text="peso:", fg="blue")
rotulo_peso.pack()

entrada_peso = tk.Entry()
entrada_peso.pack()
# Cria um botão para obter os dados
botao = tk.Button(janela, text="Obter Dados", fg="black", command=obter_dados)

mensagem = tk.Label(janela, text="")
mensagem.pack()
botao.pack()

janela.mainloop()
"""
