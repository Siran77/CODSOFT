import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors Game")

        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12)).grid(row=0, column=0, columnspan=3)

        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set("")

        choices = ["Rock", "Paper", "Scissors"]
        for i, choice in enumerate(choices):
            tk.Radiobutton(self.main_frame, text=choice, variable=self.user_choice_var, value=choice.lower(), font=("Arial", 10)).grid(row=1, column=i, padx=5, pady=5)

        self.play_button = tk.Button(self.main_frame, text="Play", command=self.play, font=("Arial", 12))
        self.play_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

        self.result_label = tk.Label(self.main_frame, text="", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.score_label = tk.Label(self.main_frame, text="", font=("Arial", 12))
        self.score_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.play_again_button = tk.Button(self.main_frame, text="Play Again", command=self.play_again, font=("Arial", 12))
        self.play_again_button.grid(row=5, column=0, columnspan=3, padx=5, pady=10)
        self.play_again_button.config(state="disabled")

        self.root.mainloop()

    def play(self):
        user_choice = self.user_choice_var.get().lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            messagebox.showerror("Error", "Invalid choice. Please choose Rock, Paper, or Scissors.")
            return

        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        self.result_label.config(text=f"Result: {result}", fg="blue")
        self.score_label.config(text=f"Score - You: {self.user_score}  Computer: {self.computer_score}", fg="green")
        self.play_again_button.config(state="normal")

    def play_again(self):
        self.user_choice_var.set("")
        self.result_label.config(text="")
        self.play_again_button.config(state="disabled")

if __name__ == "__main__":
    RockPaperScissorsGame()
