import tkinter as tk
from tkinter import messagebox
import requests

def consultar():
    cnpj = entrada_cnpj.get().strip()
    
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            entrada_razao.config(state="normal")
            entrada_fantasia.config(state="normal")
            entrada_municipio.config(state="normal")
            entrada_uf.config(state="normal")
            
            entrada_razao.delete(0, tk.END)
            entrada_razao.insert(0, dados.get("razao_social", "N/A"))
            
            entrada_fantasia.delete(0, tk.END)
            entrada_fantasia.insert(0, dados.get("nome_fantasia", "N/A"))
            
            entrada_municipio.delete(0, tk.END)
            entrada_municipio.insert(0, dados.get("municipio", "N/A"))
            
            entrada_uf.delete(0, tk.END)
            entrada_uf.insert(0, dados.get("uf", "N/A"))
            
            entrada_razao.config(state="readonly")
            entrada_fantasia.config(state="readonly")
            entrada_municipio.config(state="readonly")
            entrada_uf.config(state="readonly")
            
            situacao.config(text="Situação: CNPJ OK", bg="green")
        
        else:
            situacao.config(text="Situação: CNPJ Inválido", bg="red")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar o CNPJ: {e}")

janela = tk.Tk()
janela.title("Unidade 07 - Questão Aleatória 01")
janela.geometry("400x270")
janela.resizable(width=0, height=0)

titulo = tk.Label(janela, text="Consulta Informações de Pessoa Jurídica CNPJ", font=("Arial", 11, "bold"), bg="white")
titulo.pack(pady=5, fill="x")

frame_cnpj = tk.Frame(janela)
frame_cnpj.pack(pady=5, padx=10, fill="x")

label_cnpj = tk.Label(frame_cnpj, text="Informe CNPJ a consultar:", font=("Arial", 10, "bold"))
label_cnpj.pack(side="left", padx=5)

entrada_cnpj = tk.Entry(frame_cnpj, width=20)
entrada_cnpj.pack(side="left", padx=5)

botao_consultar = tk.Button(janela, text="Consultar CNPJ", bg="blue", fg="white", font=("Arial", 12, "bold"), command=consultar, width=20)
botao_consultar.pack(pady=10, fill="x", padx=10)

frame_resultados = tk.Frame(janela)
frame_resultados.pack(pady=5, padx=10, fill="x")

label_razao = tk.Label(frame_resultados, text="Razão Social:", anchor="w", width=15)
label_razao.grid(row=0, column=0, sticky="w", padx=5, pady=2)

entrada_razao = tk.Entry(frame_resultados, width=30, state="readonly")
entrada_razao.grid(row=0, column=1, pady=2)

label_fantasia = tk.Label(frame_resultados, text="Nome Fantasia:", anchor="w", width=15)
label_fantasia.grid(row=1, column=0, sticky="w", padx=5, pady=2)

entrada_fantasia = tk.Entry(frame_resultados, width=30, state="readonly")
entrada_fantasia.grid(row=1, column=1, pady=2)

label_municipio = tk.Label(frame_resultados, text="Município:", anchor="w", width=15)
label_municipio.grid(row=2, column=0, sticky="w", padx=5, pady=2)

entrada_municipio = tk.Entry(frame_resultados, width=30, state="readonly")
entrada_municipio.grid(row=2, column=1, pady=2)

label_uf = tk.Label(frame_resultados, text="Estado UF:", anchor="w", width=15)
label_uf.grid(row=3, column=0, sticky="w", padx=5, pady=2)

entrada_uf = tk.Entry(frame_resultados, width=30, state="readonly")
entrada_uf.grid(row=3, column=1, pady=2)

situacao = tk.Label(janela, text="Situação:", bg="black", fg="white", font=("Arial", 10, "bold"), anchor="w")
situacao.pack(fill="x", padx=10, pady=10)

janela.mainloop()