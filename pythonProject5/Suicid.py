import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Суицидщик")

        self.secret_word = "ADOLF"
        self.guess_word = ["_"] * len(self.secret_word)
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.draw_gallows()

        self.word_label = tk.Label(self.master, text=" ".join(self.guess_word), font=("Helvetica", 20))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.master, width=2, font=("Helvetica", 16))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Продолжить", command=self.make_guess, font=("Helvetica", 16))
        self.guess_button.pack()

        self.restart_button = tk.Button(self.master, text="Начать заново", command=self.restart_game, font=("Helvetica", 16))
        self.restart_button.pack()

        self.guess_entry.bind("<KeyPress>", self.validate_input)

    def draw_gallows(self):
        self.canvas.create_line(100, 350, 300, 350, width=5)
        self.canvas.create_line(200, 350, 200, 100, width=5)
        self.canvas.create_line(200, 100, 100, 100, width=5)
        self.canvas.create_line(100, 100, 100, 150, width=5)

    def draw_hangman(self):
        if self.attempts_left == 5:
            # Head
            self.canvas.create_oval(90, 150, 110, 170, width=5)
        elif self.attempts_left == 4:
            # Body
            self.canvas.create_line(100, 170, 100, 250, width=5)
        elif self.attempts_left == 3:
            # Left arm
            self.canvas.create_line(100, 200, 80, 230, width=5)
        elif self.attempts_left == 2:
            # Right arm
            self.canvas.create_line(100, 200, 120, 230, width=5)
        elif self.attempts_left == 1:
            # Left leg
            self.canvas.create_line(100, 250, 80, 290, width=5)
        elif self.attempts_left == 0:
            # Right leg
            self.canvas.create_line(100, 250, 120, 290, width=5)

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        if len(guess) == 1 and guess.isalpha() and guess.isascii():
            if guess in self.secret_word:
                for i in range(len(self.secret_word)):
                    if self.secret_word[i] == guess:
                        self.guess_word[i] = guess
                self.word_label.config(text=" ".join(self.guess_word))
                if "_" not in self.guess_word:
                    messagebox.showinfo("Ура", "Ты отгадал слово и получаешь четверть Польши")
                    self.restart_game()
            else:
                self.attempts_left -= 1
                self.draw_hangman()
                if self.attempts_left == 0:
                    messagebox.showinfo("Ты проиграл", f"Ты не получаешь Польшу. Батя Аркаши и загадоное слово {self.secret_word}.")
                    self.restart_game()
        else:
            messagebox.showwarning("Не верно ввел", "Введи правильные символы иначе не дам балтику")

    def restart_game(self):
        self.secret_word = "ADOLF"
        self.guess_word = ["_"] * len(self.secret_word)
        self.attempts_left = self.max_attempts
        self.word_label.config(text=" ".join(self.guess_word))
        self.canvas.delete("all")
        self.draw_gallows()

    def validate_input(self, event):
        char = event.char
        if char.isalpha() and not char.isascii():
            return "break"

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
