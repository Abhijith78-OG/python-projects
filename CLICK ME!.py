import tkinter as tk
import random
import time

# Game settings
GAME_TIME = 100  # seconds

def move_button():
    # Random position inside the window
    x = random.randint(50, 250)
    y = random.randint(50, 150)
    button.place(x=x, y=y)

def click_button():
    global score
    score += 10
    score_label.config(text=f"Score: {score}")
    move_button()

def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.config(text=f"Time: {remaining_time}")
        root.after(1000, update_timer)
    else:
        button.config(state="disabled")
        timer_label.config(text="Game Over!")
        button.place_forget()

# Main window
root = tk.Tk()
root.title("Catch the Button Game")
root.geometry("400x300")

score = 0
remaining_time = GAME_TIME

# Labels
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 14))
score_label.pack()

timer_label = tk.Label(root, text=f"Time: {remaining_time}", font=("Arial", 14))
timer_label.pack()

# Button
button = tk.Button(root, text="Catch Me!", command=click_button, font=("Arial", 12))
button.place(x=150, y=100)

# Start timer
update_timer()

root.mainloop()

