import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def player_move(board, player):
    while True:
        try:
            move = int(input(f"{player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("❌ Spot already taken. Try again.")
        except (ValueError, IndexError):
            print("❌ Invalid input. Enter a number between 1 and 9.")

def ai_move(board):
    print("🤖 AI is thinking...")
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    move = random.choice(empty_spots)
    board[move[0]][move[1]] = "O"

def game():
    print("🎮 Welcome to Tic-Tac-Toe 🎮")
    mode = input("Play against (1) Human or (2) AI? ")

    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    current_player = "X"

    while True:
        if mode == "1" or current_player == "X":
            player_move(board, current_player)
        else:
            ai_move(board)

        print_board(board)

        if check_winner(board, current_player):
            print(f"🏆 {current_player} wins!")
            break
        elif is_full(board):
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    game()
