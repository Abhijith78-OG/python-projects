import random

def choose_word():
    words = ["python", "adventure", "hangman", "terminal", "keyboard", "programming", "challenge", "mystery"]
    return random.choice(words)

def display(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("🎮 Welcome to Hangman! 🎮")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\n🏆 Congratulations! You guessed the word: {word}")
                break
        else:
            print("❌ Wrong guess!")
            attempts -= 1

    else:
        print(f"\n💀 Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
