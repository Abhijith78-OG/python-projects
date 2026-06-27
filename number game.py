import random
import time

def play_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("Try to guess the secret number...")

    score = 0
    level = 1

    while True:
        print(f"\n--- Level {level} ---")
        max_number = level * 10
        secret_number = random.randint(1, max_number)
        attempts = 0
        max_attempts = 5

        print(f"Guess a number between 1 and {max_number}. You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"✅ Correct! The secret number was {secret_number}.")
                score += 10 * level
                print(f"Your score: {score}")
                level += 1
                break
            elif guess < secret_number:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

        else:
            print(f"💀 Game Over! The secret number was {secret_number}.")
            print(f"Final Score: {score}")
            break

        time.sleep(1)

if __name__ == "__main__":
    play_game()
