import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game (Manual Move)")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(20, 20)]
        self.food = self.place_food()
        self.direction = None
        self.running = True

        self.draw_game()
        self.root.bind("<KeyPress>", self.change_direction)

    def place_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
            self.move_snake()   # move only when key is pressed

    def move_snake(self):
        if not self.direction or not self.running:
            return

        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 20
        elif self.direction == "Down":
            head_y += 20
        elif self.direction == "Left":
            head_x -= 20
        elif self.direction == "Right":
            head_x += 20

        new_head = (head_x, head_y)

        # Check collisions
        if (new_head in self.snake or
            head_x < 0 or head_x >= 400 or
            head_y < 0 or head_y >= 400):
            self.running = False
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 24))
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
        else:
            self.snake.pop()

        self.draw_game()

    def draw_game(self):
        self.canvas.delete("all")

        # Draw food
        self.canvas.create_rectangle(self.food[0], self.food[1],
                                     self.food[0]+20, self.food[1]+20,
                                     fill="red")

        # Draw snake
        for (x, y) in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green")

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
