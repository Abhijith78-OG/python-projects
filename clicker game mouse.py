import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.points = 0
        self.click_power = 1
        self.upgrade_cost = 10

        self.root = root
        self.root.title("Mouse Clicker Game")

        self.label = tk.Label(root, text="Points: 0 | Power: 1 | Upgrade Cost: 10")
        self.label.pack(pady=10)

        self.click_button = tk.Button(root, text="🖱️ Click Me!", command=self.click, width=20, height=2)
        self.click_button.pack(pady=10)

        self.upgrade_button = tk.Button(root, text="⚡ Upgrade", command=self.upgrade, width=20, height=2)
        self.upgrade_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, width=20, height=2)
        self.quit_button.pack(pady=10)

    def click(self):
        self.points += self.click_power
        self.update_label()

    def upgrade(self):
        if self.points >= self.upgrade_cost:
            self.points -= self.upgrade_cost
            self.click_power *= 2
            self.upgrade_cost *= 2
            self.update_label()
        else:
            self.label.config(text=f"Not enough points! Need {self.upgrade_cost}")

    def update_label(self):
        self.label.config(text=f"Points: {self.points} | Power: {self.click_power} | Upgrade Cost: {self.upgrade_cost}")

def main():
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
