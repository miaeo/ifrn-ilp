#Desafio

#Desenvolva um programa que:

#Utilizando a linguagem Python, 
#simule um caixa de supermercado que armazene os produtos comprados pelo cliente, 
#permita a exclusão de qualquer item em uma etapa de conferência 
#e, por fim, apresente um resumo das compras efetuadas.

def titulo(texto, tamanho):
    linha_superior = '=' * tamanho
    linha_inferior = '=' * tamanho
    print(linha_superior)
    print("\t" + texto)
    print(linha_inferior)

def resumo(produtos):
    titulo("Resumo das Compras", 40)
    print("N°\tProduto\t\tValor\tQnt\tTotal")
    total = 0
    for i, produto in enumerate(produtos, start=1):
        total_produto = produto['valor'] * produto['quantidade']
        total += total_produto
        print(f"{i}\t{produto['nome']}\t\t{produto['valor']:.2f}\t{produto['quantidade']}\t{total_produto:.2f}")
    print("\t\t\t\t--> {0:.2f}".format(total).rjust(26))

titulo("Supermercado Tabajara", 40)
produtos = []
contador = 1

while True:
    info_produto = {}
    info_produto['nome'] = input(f"Produto {contador}: ")
    info_produto['valor'] = float(input("Valor: "))
    info_produto['quantidade'] = int(input("Quantidade: "))
    info_produto['numero'] = contador
    info_produto['total'] = info_produto['valor'] * info_produto['quantidade']

    produtos.append(info_produto)
    while True:
        opcao = input("Quer inserir outro produto? S/N: ")
        if opcao.lower() == 's':
            contador += 1
            break
        elif opcao.lower() == 'n':
            break
    if opcao.lower() == 'n':
        break

titulo("Confirmação e exclusão", 40)

while True:
    while True:
        opcao = input("Quer retirar algum produto? S/N: ")
        if opcao.lower() == 's':
            break
        elif opcao.lower() == 'n':
            break

    if opcao.lower() == 'n':
        break

    numero_produto = int(input("Qual o número do produto? "))
    produto_encontrado = False
    for produto in produtos:
        if produto['numero'] == numero_produto:
            produto_encontrado = True
            produtos.remove(produto)
            print(f"Item {produto['nome']} excluído!")
            break

    if not produto_encontrado:
        print("Item não encontrado")

resumo(produtos)
