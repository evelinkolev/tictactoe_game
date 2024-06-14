def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 5)


def check_winner(board, player):
    return any(
        all(cell == player for cell in row) for row in board
    ) or any(
        all(row[col] == player for row in board) for col in range(3)
    ) or all(
        board[i][i] == player for i in range(3)
    ) or all(
        board[i][2 - i] == player for i in range(3)
    )


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player):
    return int(input(f"Player {player}, enter the row (0, 1, or 2): ")), \
        int(input(f"Player {player}, enter the column (0, 1, or 2): "))


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell is already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
