import random

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def word_scramble():
    words = ["python", "adventure", "hangman", "keyboard", "challenge", "mystery", "terminal", "programming" , "artifical intllegence","gammer","teacher","movie","words","wrong","import","random","explore","search","lower","attempts","IDLE= Intrgrated Devlopment and Learning Enviroment","subject","kill","scramble","run","pencil"]
    score = 0

    print("🔤 Welcome to Word Scramble! 🔤")
    print("Unscramble the letters to form the correct word.")

    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)
        attempts = 3
        print(f"\nScrambled word: {scrambled}")

        while attempts > 0:
            guess = input("Your guess: ").lower()
            if guess == word:
                print("✅ Correct!")
                score += 10
                print(f"Your score: {score}")
                break
            else:
                attempts -= 1
                print(f"❌ Wrong! Attempts left: {attempts}")

        if attempts == 0:
            print(f"💀 Out of attempts! The word was: {word}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(f"🏆 Final Score: {score}")
            print("Thanks for playing Word Scramble!")
            break

if __name__ == "__main__":
    word_scramble()
