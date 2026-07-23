import tkinter as tk
import random

# --- Game Variables ---
zombie_health = 10
player_attack = 1
coins = 0

# --- Functions ---
def attack_zombie():
    global zombie_health, coins
    zombie_health -= player_attack
    if zombie_health <= 0:
        coins += 5
        result_label.config(text="Zombie defeated! +5 coins")
        spawn_zombie()
    else:
        result_label.config(text=f"Zombie hit! HP left: {zombie_health}")
    update_stats()

def spawn_zombie():
    global zombie_health
    zombie_health = random.randint(8, 15)
    zombie_label.config(text=f"Zombie HP: {zombie_health}")

def buy_upgrade():
    global coins, player_attack
    if coins >= 10:
        coins -= 10
        player_attack += 1
        result_label.config(text="Bought upgrade! Attack +1")
    else:
        result_label.config(text="Not enough coins!")
    update_stats()

def update_stats():
    stats_label.config(text=f"Attack: {player_attack} | Coins: {coins}")

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Zombie Game with Store")
root.geometry("400x300")

# Labels
zombie_label = tk.Label(root, text=f"Zombie HP: {zombie_health}", font=("Arial", 14))
zombie_label.pack(pady=10)

stats_label = tk.Label(root, text=f"Attack: {player_attack} | Coins: {coins}", font=("Arial", 12))
stats_label.pack(pady=5)

result_label = tk.Label(root, text="Fight the zombie!", font=("Arial", 12))
result_label.pack(pady=5)

# Buttons
attack_button = tk.Button(root, text="Attack Zombie", command=attack_zombie, font=("Arial", 12))
attack_button.pack(pady=10)

store_button = tk.Button(root, text="Buy Upgrade (10 coins)", command=buy_upgrade, font=("Arial", 12))
store_button.pack(pady=10)

# Start with a zombie
spawn_zombie()

root.mainloop()
