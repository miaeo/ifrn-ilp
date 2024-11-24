import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, font

def criar_banco():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS matriculas (matricula TEXT PRIMARY KEY, nome TEXT)''')
    conexao.commit()
    conexao.close()

def incluir_aluno():
    matricula = entry_matricula.get().strip()
    nome = entry_nome.get().strip()

    if not matricula or not nome:
        status.set('Preencha Todos os Campos')
        return

    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM matriculas WHERE matricula = ?', (matricula,))
    if cursor.fetchone():
        status.set('Matrícula já Cadastrada')
    else:
        cursor.execute('INSERT INTO matriculas (matricula, nome) VALUES (?, ?)', (matricula, nome))
        conexao.commit()
        status.set('Aluno Cadastrado com Sucesso!!!')

        cursor.execute('SELECT * FROM matriculas')
        registros = cursor.fetchall()
        print("\nAlunos:")
        for reg in registros:
            print(f"Matrícula: {reg[0]}, Nome: {reg[1]}")

    conexao.close()

root = Tk()
root.title('Inclusão de Alunos')

fonte_padrao = font.Font(family="Arial", size=11, weight="bold")
fonte_titulo = font.Font(family="Arial", size=10, weight="bold")

Label(root, text="Matrícula:", font=fonte_padrao).grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_matricula = Entry(root, font=fonte_padrao)
entry_matricula.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Nome do Aluno:", font=fonte_padrao).grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_nome = Entry(root, font=fonte_padrao)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

Button(root, text="Incluir Aluno no Banco de Dados", command=incluir_aluno, font=fonte_titulo, width=40).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

status = StringVar()
Label(root, textvariable=status, fg="white", bg="gray", width=40, font=fonte_titulo).grid(row=3, column=0, columnspan=2, pady=5)

criar_banco()
root.mainloop()
