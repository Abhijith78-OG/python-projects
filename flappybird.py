import tkinter as tk
import random

class FlappyBird:
    def __init__(self, root):
        self.root = root
        self.root.title("🐦 Flappy Bird")

        self.canvas = tk.Canvas(root, width=400, height=600, bg="skyblue")
        self.canvas.pack()

        self.bird = self.canvas.create_oval(50, 250, 80, 280, fill="yellow")
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.started = False   # <-- start flag

        self.gravity = 3
        self.lift = -10
        self.velocity = 0

        self.score_text = self.canvas.create_text(200, 50, text="Score: 0", font=("Arial", 20), fill="white")
        self.start_text = self.canvas.create_text(200, 300, text="Press SPACE to Start", font=("Arial", 24), fill="white")

        self.root.bind("<space>", self.flap)

    def flap(self, event):
        if not self.started:
            self.started = True
            self.canvas.delete(self.start_text)
            self.update_game()
        elif not self.game_over:
            self.velocity = self.lift

    def create_pipe(self):
        gap = 150
        top_height = random.randint(50, 400)
        bottom_height = 600 - top_height - gap

        top_pipe = self.canvas.create_rectangle(400, 0, 450, top_height, fill="green")
        bottom_pipe = self.canvas.create_rectangle(400, 600-bottom_height, 450, 600, fill="green")

        self.pipes.append((top_pipe, bottom_pipe))

    def move_pipes(self):
        for pipe_pair in self.pipes:
            for pipe in pipe_pair:
                self.canvas.move(pipe, -5, 0)

        # Remove pipes that go off screen
        self.pipes = [(tp, bp) for tp, bp in self.pipes if self.canvas.coords(tp)[2] > 0]

    def check_collision(self):
        bird_coords = self.canvas.coords(self.bird)
        bx1, by1, bx2, by2 = bird_coords

        if by1 < 0 or by2 > 600:
            return True

        for tp, bp in self.pipes:
            if self.overlap(bird_coords, self.canvas.coords(tp)) or self.overlap(bird_coords, self.canvas.coords(bp)):
                return True
        return False

    def overlap(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[3] < rect2[1] or rect1[1] > rect2[3])

    def update_game(self):
        if not self.game_over:
            self.velocity += self.gravity
            self.canvas.move(self.bird, 0, self.velocity)

            if random.randint(1, 100) == 1:
                self.create_pipe()

            self.move_pipes()

            if self.check_collision():
                self.game_over = True
                self.canvas.create_text(200, 300, text="Game Over", font=("Arial", 30), fill="red")
            else:
                self.score += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.root.after(50, self.update_game)

def main():
    root = tk.Tk()
    game = FlappyBird(root)
    root.mainloop()

if __name__ == "__main__":
    main()
