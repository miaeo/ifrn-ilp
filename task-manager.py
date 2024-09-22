tarefas = []

while True:
  print("\n", "=" * 39)
  print("\u250C", "GERENCIADOR DE TAREFAS".center(38), "\u2510")
  print("\u2502", "1. Adicionar uma nova tarefa".center(38), "\u2502")
  print("\u2502", "2. Visualizar todas as tarefas".center(38), "\u2502")
  print("\u2502", "3. Marcar uma tarefa como concluída".center(38), "\u2502")
  print("\u2502", "4. Remover uma tarefa".center(38), "\u2502")
  print("\u2502", "5. Sair do programa".center(38), "\u2502")
  print("\u2514", "=" * 38, "\u2518")

  opcao = input("\nEscolha uma das opções: ")

  if opcao == "1":
    nova_tarefa = input("\nQual a nova tarefa? ")
    tarefas.append(nova_tarefa)
    print("\nTarefa adicionada!")

  elif opcao == "2":
    if not tarefas:
      print("\nNão há tarefas cadastradas.")
    else:
      print("\nLista de tarefas: ")
      for tarefa in tarefas:
        print("–", tarefa)

  elif opcao == "3":
    if not tarefas:
      print("\nNão há tarefas cadastradas.")
    else:
      print("\nLista de tarefas: ")
      for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
      indice = int(input("\nDigite o número da tarefa: "))
      if 1 <= indice <= len(tarefas):
        print(f"\nTarefa '{tarefas[indice-1]}' concluída!")
        tarefas.pop(indice-1)
      else:
        print("\nTarefa não encontrada...")

  elif opcao == "4":
    if not tarefas:
      print("\nNão há tarefas cadastradas.")
    else:
      print("\nLista de tarefas: ")
      for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")
      indice = int(input("\nDigite o número da tarefa: "))
      if 1 <= indice <= len(tarefas):
        print(f"\nTarefa '{tarefas[indice-1]}' removida!")
        tarefas.pop(indice-1)
      else:
        print("\nTarefa não encontrada...")

  elif opcao == "5":
    print("\nSaindo do programa...")
    break

  else:
    print("\nOpção inválida. Tente novamente.")
