import tkinter as tk
from random import sample

def gerar_numeros():
    numeros = sample(range(1, 61), 6)
    numeros.sort() 
    resultado_label.config(text=f"{', '.join(map(str, numeros))}")

janela = tk.Tk()
janela.title("Mega-Sena")
janela.geometry("300x200")

titulo_label = tk.Label(janela, text="Sorteador Mega-Sena", font=("Arial", 14))
titulo_label.pack(pady=10)

instrucoes_label = tk.Label(janela, text="Clique no botão para gerar os números:")
instrucoes_label.pack()

botao_sortear = tk.Button(janela, text="Sortear Números", command=gerar_numeros)
botao_sortear.pack(pady=10)

resultado_label = tk.Label(janela, text="", font=("Arial", 12), fg="green")
resultado_label.pack(pady=10)

janela.mainloop()