import random

SIZE = 4

def create_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_tile(board)
    add_tile(board)
    return board

def add_tile(board):
    empty = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = random.choice([2, 4])

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" ".join(str(num).rjust(4) if num != 0 else "   ." for num in row))
    print()

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row

def merge(row):
    for i in range(SIZE - 1):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)
        new_board.append(row)
    return new_board

def move_right(board):
    new_board = []
    for row in board:
        row = row[::-1]
        row = compress(row)
        row = merge(row)
        row = compress(row)
        row = row[::-1]
        new_board.append(row)
    return new_board

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board = transpose(board)
    board = move_left(board)
    return transpose(board)

def move_down(board):
    board = transpose(board)
    board = move_right(board)
    return transpose(board)

def can_move(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
            if c < SIZE-1 and board[r][c] == board[r][c+1]:
                return True
            if r < SIZE-1 and board[r][c] == board[r+1][c]:
                return True
    return False

def game():
    board = create_board()
    print("🎯 Welcome to 2048! Use W/A/S/D to move, Q to quit.\n")
    print_board(board)

    while True:
        move = input("Move: ").lower()
        if move == "q":
            print("👋 Thanks for playing!")
            break
        elif move == "w":
            next_board = move_up(board)
        elif move == "s":
            next_board = move_down(board)
        elif move == "a":
            next_board = move_left(board)
        elif move == "d":
            next_board = move_right(board)
        else:
            print("❌ Invalid input. Use W/A/S/D.")
            continue

        if next_board != board:
            board = next_board
            add_tile(board)
            print_board(board)
        else:
            print("⚠️ No move possible in that direction.")

        if any(2048 in row for row in board):
            print("🏆 You win! You reached 2048!")
            break
        if not can_move(board):
            print("💀 Game Over! No moves left.")
            break

if __name__ == "__main__":
    game()
