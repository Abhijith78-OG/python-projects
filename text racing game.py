import random
import time

def race_game():
    print("🏁 Welcome to Text Racing! 🏁")
    print("You vs Computer. First to 100 points wins!")
    print("Controls: Press ENTER to accelerate each turn.\n")

    player_score = 0
    computer_score = 0

    while player_score < 100 and computer_score < 100:
        input("Press ENTER to accelerate...")
        player_boost = random.randint(5, 15)
        computer_boost = random.randint(5, 15)

        # Random events
        if random.random() < 0.2:
            print("⚠️ You hit an obstacle! -5 points")
            player_boost -= 5
        if random.random() < 0.2:
            print("⚠️ Computer hit an obstacle! -5 points")
            computer_boost -= 5

        player_score += max(0, player_boost)
        computer_score += max(0, computer_boost)

        print(f"You gained {player_boost} points! Total: {player_score}")
        print(f"Computer gained {computer_boost} points! Total: {computer_score}\n")

        time.sleep(1)

    if player_score >= 100 and computer_score >= 100:
        print("🤝 It's a tie!")
    elif player_score >= 100:
        print("🏆 You win the race!")
    else:
        print("💀 Computer wins the race!")

if __name__ == "__main__":
    race_game()
