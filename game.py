import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}!")

    def show_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Health: {self.health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}\n")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(5, self.attack_power)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

def battle(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears! ⚔️")
    while player.health > 0 and enemy.health > 0:
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == "a":
            damage = random.randint(10, 20)
            enemy.health -= damage
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!")
                player.add_item("Gold Coin")
                break
            enemy.attack(player)
        elif action == "r":
            print(f"{player.name} runs away safely!")
            break
        else:
            print("Invalid choice! Try again.")
        player.show_status()

def explore(player):
    print("\nYou walk down a dark path...")
    time.sleep(1)
    event = random.choice(["enemy", "treasure", "nothing"])
    if event == "enemy":
        enemy = Enemy("Goblin", 50, 15)
        battle(player, enemy)
    elif event == "treasure":
        treasure = random.choice(["Magic Potion", "Silver Sword", "Shield"])
        player.add_item(treasure)
    else:
        print("Nothing happens... eerie silence surrounds you.")

def main():
    print("🌟 Welcome to the Adventure Game! 🌟")
    name = input("Enter your hero's name: ")
    player = Player(name)

    while player.health > 0:
        print("\nWhat would you like to do?")
        choice = input("(E)xplore, (S)tatus, or (Q)uit: ").lower()
        if choice == "e":
            explore(player)
        elif choice == "s":
            player.show_status()
        elif choice == "q":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

    if player.health <= 0:
        print(f"\n💀 {player.name} has fallen in battle... Game Over 💀")

if __name__ == "__main__":
    main()
