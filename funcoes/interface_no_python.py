import tkinter as tk


def obter_dados():
    # Função para obter os dados inseridos pelo usuário
    nome = entrada_nome.get()

    altura = entrada_altura.get()
    peso = entrada_peso.get()

    try:
        peso_int = float(peso)
        altura_int = float(altura)
    except ValueError:
        mensagem["text"] = "erro digite só numeros"
        return
    imc = peso_int / (altura_int * altura_int)
    agua = peso_int * 35
    print("Nome:", nome)
    print("Altura:", altura)
    print("peso", peso)

    mensagem[
        "text"
    ] = f"Nome: {nome}\n Altura: {altura} \nPeso: {peso} \nIMC: {imc} \nvocê deve tomar: {agua} ml de aguá por dia"


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
