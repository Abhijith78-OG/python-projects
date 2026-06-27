import random
import time

def space_invaders():
    print("👾 Welcome to Text Space Invaders 👾")
    print("Defend Earth by shooting down alien ships!")
    print("Controls: Type 's' to shoot, 'q' to quit.\n")

    score = 0
    lives = 3

    while lives > 0:
        # Alien appears
        alien_position = random.randint(1, 5)
        print(f"🚀 Alien ship spotted at position {alien_position}!")
        time.sleep(1)

        shot = input("Enter position to shoot (1-5): ")

        if shot == "q":
            print("👋 You retreated from battle. Final Score:", score)
            break

        try:
            shot_position = int(shot)
        except ValueError:
            print("❌ Invalid input! You missed your chance.")
            lives -= 1
            continue

        if shot_position == alien_position:
            print("💥 Direct hit! Alien destroyed!")
            score += 10
        else:
            print("😱 Missed! The alien attacks your base!")
            lives -= 1

        print(f"Score: {score} | Lives left: {lives}\n")
        time.sleep(1)

    if lives == 0:
        print("💀 Game Over! Earth has fallen...")
        print("Final Score:", score)

if __name__ == "__main__":
    space_invaders()
