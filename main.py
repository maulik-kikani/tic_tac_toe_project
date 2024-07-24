def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(mark == player for mark in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(mark != '_' for row in board for mark in row)

def tic_tac_toe():
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column must be between 1 and 3.")
            continue
        if board[row][col] != '_':
            print("That position is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
