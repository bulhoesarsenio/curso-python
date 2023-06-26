import tkinter as tk


def validar_entrada(char):
    return len(char) <= 5


root = tk.Tk()

entry = tk.Entry(root, show="*", validate="key")
entry["validatecommand"] = (entry.register(validar_entrada), "%S")

entry.pack()
root.mainloop()
