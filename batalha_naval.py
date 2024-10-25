from random import randint

board = [["O"] * 5 for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))

ship_row, ship_col = randint(0, 4), randint(0, 4)

print("BATALHA NAVAL")
print("Tente adivinhar a localização do navio!")
print("Você tem 4 tentativas.")
print()

for turn in range(4):
    print("==========")
    print(f"Rodada {turn + 1}")
    print_board(board)
    guess_row = int(input("Qual linha? (0-4) "))
    guess_col = int(input("Qual coluna? (0-4) "))
    print()

    if guess_row == ship_row and guess_col == ship_col:
        print("Parabéns! Você venceu!")
        break
    else:
        if not (0 <= guess_row < 5 and 0 <= guess_col < 5):
            print("Oops, longe demais")
        elif board[guess_row][guess_col] == "X":
            print("Você já tentou essa!")
        else:
            print("Não foi dessa vez!")
            board[guess_row][guess_col] = "X"

        if turn == 3:
            print("Fim de Jogo!")

board[ship_row][ship_col] = "H"
print("==========")
print("O navio estava na posição: ")
print_board(board)
