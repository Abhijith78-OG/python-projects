import tkinter as tk
import winsound  # Windows only; use pygame.mixer for cross-platform sound

class PianoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎹 Full Piano Game with Sharps")

        # Frequencies for notes (C4–B4 + C5)
        self.keys = {
            "C": 261,
            "C#": 277,
            "D": 294,
            "D#": 311,
            "E": 329,
            "F": 349,
            "F#": 370,
            "G": 392,
            "G#": 415,
            "A": 440,
            "A#": 466,
            "B": 493,
            "C5": 523
        }

        # Map keyboard input to notes
        self.keymap = {
            "c": "C",
            "d": "D",
            "e": "E",
            "f": "F",
            "g": "G",
            "a": "A",
            "b": "B",
            "c1": "C#",
            "d1": "D#",
            "f1": "F#",
            "g1": "G#",
            "a1": "A#"
        }

        self.create_keys()
        self.root.bind("<KeyPress>", self.key_press)

    def play_sound(self, note):
        freq = self.keys[note]
        winsound.Beep(freq, 300)  # Play note for 300 ms

    def create_keys(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for note in self.keys:
            btn = tk.Button(frame, text=note, width=6, height=10,
                            command=lambda n=note: self.play_sound(n))
            btn.pack(side="left")

    def key_press(self, event):
        # Handle single letters
        char = event.char.lower()
        if char in self.keymap:
            note = self.keymap[char]
            self.play_sound(note)

        # Handle combos like "c1", "d1" etc.
        if event.keysym.lower() in self.keymap:
            note = self.keymap[event.keysym.lower()]
            self.play_sound(note)

def main():
    root = tk.Tk()
    game = PianoGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

