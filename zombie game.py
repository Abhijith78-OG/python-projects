import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.ammo = 10
        self.kills = 0
        self.coins = 0
        self.weapon = "Small Sword"
        self.potions = {"regen": 1, "shield": 0, "invisible": 0, "damage": 0}
        self.shield_active = False
        self.invisible_active = False
        self.damage_boost = False

    def shoot(self):
        if self.weapon == "Small Sword":
            return 10

        elif self.weapon == "Diamond Sword":
            damage = 100
            if random.random() < 0.25:
                self.invisible_active = True
                self.health = 100
                print("💎 Diamond Sword ability triggered! Full health + invisibility!")
            return damage

        elif self.weapon == "M119":
            if self.ammo > 0:
                self.ammo -= 1
                damage = 50
                if random.random() < 0.5:
                    self.invisible_active = True
                    self.health = 100
                    print("🔫 M119 ability triggered! Full health + invisibility!")
                return damage
            else:
                print("❌ Out of ammo!")
                return 0

        elif self.weapon == "AK-47":
            if self.ammo > 0:
                self.ammo -= 1
                damage = 75
                if random.random() < 0.75:
                    self.invisible_active = True
                    self.health = 100
                    print("🔫 AK-47 ability triggered! Full health + invisibility!")
                return damage
            else:
                print("❌ Out of ammo!")
                return 0

        elif self.weapon == "GMPG":
            if self.ammo > 0:
                self.ammo -= 1
                damage = 90
                if random.random() < 0.9:
                    self.invisible_active = True
                    self.health = 100
                    print("💥 GMPG ability triggered! Full health + invisibility!")
                return damage
            else:
                print("❌ Out of ammo!")
                return 0

        elif self.weapon == "Minigun":
            if self.ammo > 0:
                self.ammo -= 1
                damage = 150
                self.invisible_active = True
                self.health = 100
                print("🔥 Minigun ability triggered! Full health + invisibility!")
                return damage
            else:
                print("❌ Out of ammo!")
                return 0

        else:
            return 0

    def reload(self):
        if self.weapon not in ["Small Sword", "Diamond Sword"]:
            print("🔄 Reloading...")
            time.sleep(1)
            self.ammo = 10
            print("✅ Ammo refilled!")

    def use_potion(self, potion_type):
        if self.potions[potion_type] > 0:
            self.potions[potion_type] -= 1
            if potion_type == "regen":
                self.health = 100
                print("🧪 Regen potion used! Health fully restored.")
            elif potion_type == "shield":
                self.shield_active = True
                print("🛡️ Shield potion used! Next zombie attack blocked.")
            elif potion_type == "invisible":
                self.invisible_active = True
                print("👻 Invisibility potion used! Zombies miss their next attack.")
            elif potion_type == "damage":
                self.damage_boost = True
                print("🔥 Damage potion used! Your next shot deals double damage.")
        else:
            print(f"❌ No {potion_type} potions left!")

    def show_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"❤️ Health: {self.health}")
        print(f"🔫 Ammo: {self.ammo}")
        print(f"💀 Kills: {self.kills}")
        print(f"🪙 Coins: {self.coins}")
        print(f"🔧 Weapon: {self.weapon}")
        print(f"🧪 Potions: {self.potions}\n")

def store(player):
    print("\n🏪 Welcome to the Store 🏪")
    print("1. Diamond Sword (3 coins)")
    print("2. M119 (50 coins)")
    print("3. AK-47 (80 coins)")
    print("4. GMPG (100 coins)")
    print("5. Minigun (500 coins)")
    print("6. Health Potion (10 coins)")
    print("7. Shield Potion (50 coins)")
    print("8. Damage Potion (70 coins)")
    print("9. Ammo Pack (1 coins for 1000 bullets)")
    print("10. Exit Store")

    choice = input("Choose an item number: ")
    if choice == "1" and player.coins >= 3:
        player.weapon = "Diamond Sword"
        player.coins -= 3
        print("💎 You bought the Diamond Sword!")
    elif choice == "2" and player.coins >= 50:
        player.weapon = "M119"
        player.coins -= 50
        print("🔫 You bought the M119!")
    elif choice == "3" and player.coins >= 80:
        player.weapon = "AK-47"
        player.coins -= 80
        print("🔫 You bought the AK-47!")
    elif choice == "4" and player.coins >= 100:
        player.weapon = "GMPG"
        player.coins -= 100
        print("💥 You bought the GMPG!")
    elif choice == "5" and player.coins >= 500:
        player.weapon = "Minigun"
        player.coins -= 500
        print("🔥 You bought the Minigun!")
    elif choice == "6" and player.coins >= 10:
        player.potions["regen"] += 1
        player.coins -= 10
        print("🧪 Bought a Health Potion!")
    elif choice == "7" and player.coins >= 50:
        player.potions["shield"] += 1
        player.coins -= 50
        print("🛡️ Bought a Shield Potion!")
    elif choice == "8" and player.coins >= 70:
        player.potions["damage"] += 1
        player.coins -= 70
        print("🔥 Bought a Damage Potion!")
    elif choice == "9" and player.coins >= 1:
        player.ammo += 1000
        player.coins -= 1
        print("🔫 Bought 1000 bullets for 1 coins!")
    elif choice == "10":
        print("👋 Leaving the store.")
    else:
        print("❌ Not enough coins or invalid choice.")

def zombie_wave(player, wave):
    print(f"\n🌑 Wave {wave} begins! Zombies are approaching...")
    zombies = [random.randint(20, 40) for _ in range(random.randint(2, 5))]

    while zombies and player.health > 0:
        player.show_status()
        print(f"Zombies left: {len(zombies)}")
        action = input("Choose action: (S)hoot, (L)reload, (P)otion, (R)store, (Q)uit: ").lower()

        skip_attack = False

        if action == "s":
            damage = player.shoot()
            if damage > 0:
                zombies[0] -= damage
                print(f"💥 You hit a zombie for {damage} damage!")
                if zombies[0] <= 0:
                    print("☠️ Zombie killed!")
                    player.kills += 1
                    coin_drop = random.randint(1, 5)
                    player.coins += coin_drop
                    print(f"🪙 You looted {coin_drop} coins!")
                    zombies.pop(0)

        elif action == "l":
            player.reload()

        elif action == "p":
            potion_choice = input("Which potion? (regen/shield/invisible/damage): ").lower()
            if potion_choice in player.potions:
                player.use_potion(potion_choice)
            else:
                print("❌ Invalid potion type.")

        elif action == "r":
            store(player)
            skip_attack = True

        elif action == "q":
            print("👋 You fled the battle!")
            return False
        else:
            print("❌ Invalid choice.")

        if zombies and not skip_attack:
            if player.invisible_active:
                print("👻 Zombies miss you!")
                player.invisible_active = False
            elif player.shield_active:
                print("🛡️ Shield absorbed the attack!")
                player.shield_active = False
            else:
                attack_damage = 3 * len(zombies)
                player.health -= attack_damage
                print(f"🧟 Zombies swarm! You take {attack_damage} damage!")

    return player.health > 0
def game():
    print("🧟 Welcome to Zombie Horde Survival 🧟")
    name = input("Enter your survivor's name: ")
    player = Player(name)

    wave = 1
    while player.health > 0:
        survived = zombie_wave(player, wave)
        if not survived:
            break
        wave += 1
        print(f"🌟 You survived Wave {wave-1}! Prepare for the next...\n")
        time.sleep(2)

    print(f"\n💀 Game Over! {player.name} fell after {wave-1} waves.")
    print(f"Final Kills: {player.kills}")
    print(f"🪙 Coins collected: {player.coins}")
    print(f"🔧 Final Weapon: {player.weapon}")
    print(f"🧪 Potions left: {player.potions}")

if __name__ == "__main__":
    game()
