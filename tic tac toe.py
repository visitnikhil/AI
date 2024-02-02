def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        row, col = map(int, input(f"Player {player}, enter row and column (e.g., 1 2): ").split())

        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
            print("Invalid move. Try again.")
            continue
        board[row - 1][col - 1] = player
        print_board(board)
        if check_win(board, player):
            print(f"Player {player} wins! Congratulations!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"
if __name__ == "__main__":
    main()
