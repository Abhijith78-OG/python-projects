import random
import time

def print_field(player_pos, bullets, size=10):
    for i in range(size):
        row = ""
        for j in range(size):
            if (i, j) == player_pos:
                row += "P "
            elif (i, j) in bullets:
                row += "B "
            else:
                row += ". "
        print(row)
    print()

def bullet_survival():
    print("🔫 Welcome to Bullet Survival! 🔫")
    print("Controls: W (up), S (down), A (left), D (right), Q (quit)\n")

    size = 10
    player_pos = (size-1, size//2)  # Start bottom middle
    bullets = []
    score = 0
    lives = 3

    while lives > 0:
        print_field(player_pos, bullets, size)
        print(f"❤️ Lives: {lives} | 🏆 Score: {score}")

        move = input("Move: ").lower()
        x, y = player_pos

        if move == "q":
            print("👋 You quit the game. Final Score:", score)
            break
        elif move == "w" and x > 0:
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

        # Move bullets down
        new_bullets = []
        for bx, by in bullets:
            if bx < size-1:
                new_bullets.append((bx+1, by))
        bullets = new_bullets

        # Spawn new bullets
        if random.random() < 0.4:  # 40% chance each turn
            bullets.append((0, random.randint(0, size-1)))

        # Check collision
        if player_pos in bullets:
            lives -= 1
            print("💀 You got hit by a bullet!")
            bullets.remove(player_pos)

        score += 1
        time.sleep(0.5)

    if lives == 0:
        print("💀 Game Over! Final Score:", score)

if __name__ == "__main__":
    bullet_survival()
