import random

def create_maze(size):
    maze = [["." for _ in range(size)] for _ in range(size)]
    exit_pos = (random.randint(0, size-1), random.randint(0, size-1))
    maze[exit_pos[0]][exit_pos[1]] = "E"  # Exit
    # Add traps
    for _ in range(size):
        trap_x, trap_y = random.randint(0, size-1), random.randint(0, size-1)
        if maze[trap_x][trap_y] == ".":
            maze[trap_x][trap_y] = "T"
    return maze, exit_pos

def print_maze(maze, player_pos):
    size = len(maze)
    for i in range(size):
        row = ""
        for j in range(size):
            if (i, j) == player_pos:
                row += "P "
            else:
                row += maze[i][j] + " "
        print(row)
    print()

def maze_game():
    print("🌀 Welcome to Maze Escape! 🌀")
    size = 5
    maze, exit_pos = create_maze(size)
    player_pos = (0, 0)
    health = 3

    while True:
        print_maze(maze, player_pos)
        print(f"❤️ Health: {health}")
        move = input("Move (W/A/S/D): ").lower()

        x, y = player_pos
        if move == "w" and x > 0:
            x -= 1
        elif move == "s" and x < size-1:
            x += 1
        elif move == "a" and y > 0:
            y -= 1
        elif move == "d" and y < size-1:
            y += 1
        else:
            print("❌ Invalid move.")
            continue

        player_pos = (x, y)

        if player_pos == exit_pos:
            print("🏆 You found the exit! Escaped the maze!")
            break
        elif maze[x][y] == "T":
            health -= 1
            print("💀 You stepped on a trap! -1 health")
            if health == 0:
                print("Game Over! You lost all health.")
                break

if __name__ == "__main__":
    maze_game()
