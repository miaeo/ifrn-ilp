import tkinter as tk

agenda = {}

def inserir_registro():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    
    if nome and telefone:
        agenda[nome] = telefone
        print(agenda)  
        entry_nome.delete(0, tk.END) 
        entry_telefone.delete(0, tk.END)

janela = tk.Tk()
janela.title("Agenda")
janela.geometry("300x150")  

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(3, weight=1)

label_instrucao = tk.Label(janela, text="Insira Contatos na Agenda:")
label_instrucao.grid(row=0, column=1, columnspan=2, pady=(10, 10))

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=1, column=1, padx=5, pady=5, sticky="e")
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=2, padx=5, pady=5)

label_telefone = tk.Label(janela, text="Telefone:")
label_telefone.grid(row=2, column=1, padx=5, pady=5, sticky="e")
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=2, column=2, padx=5, pady=5)

botao_inserir = tk.Button(janela, text="Inserir", command=inserir_registro)
botao_inserir.grid(row=3, column=1, columnspan=2, pady=(10, 10))

janela.mainloop()
