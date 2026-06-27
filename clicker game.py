import time

class ClickerGame:
    def __init__(self):
        self.points = 0
        self.click_power = 1
        self.upgrade_cost = 10

    def click(self):
        self.points += self.click_power
        print(f"🖱️ Click! You earned {self.click_power} points. Total: {self.points}")

    def upgrade(self):
        if self.points >= self.upgrade_cost:
            self.points -= self.upgrade_cost
            self.click_power *= 2
            print(f"⚡ Upgrade purchased! Click power is now {self.click_power}.")
            self.upgrade_cost *= 2
        else:
            print(f"❌ Not enough points. Need {self.upgrade_cost}.")

    def show_status(self):
        print(f"Points: {self.points} | Click Power: {self.click_power} | Next Upgrade Cost: {self.upgrade_cost}")

def game():
    print("🎮 Welcome to the Clicker Game!")
    clicker = ClickerGame()

    while True:
        clicker.show_status()
        action = input("Press Enter to click, type 'u' to upgrade, or 'q' to quit: ").lower()

        if action == "":
            clicker.click()
        elif action == "u":
            clicker.upgrade()
        elif action == "q":
            print("👋 Thanks for playing!")
            break
        else:
            print("❌ Invalid input.")

if __name__ == "__main__":
    game()
