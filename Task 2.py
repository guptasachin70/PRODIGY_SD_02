import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")

        self.secret_number = random.randint(1, 2)
        self.attempts = 0

        self.label = tk.Label(self.master, text="Enter your guess (between 1 and 50):")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.guessNum)
        self.submit_button.pack()

    def guessNum(self):
        # Generate a random number between 1 and 100
        numInput = self.entry.get()
            
        # Check if the input is a valid integer
        if numInput.isdigit():
            guessedNum = int(numInput)
            self.attempts += 1
                
            # Check if the guess is correct, too high, or too low
            if guessedNum == self.secret_number:
                messagebox.showinfo(f"Congratulations! You guessed the number {self.secret_number} correctly in {self.attempts} attempts.")
                self.master.destroy()
            elif guessedNum < self.secret_number:
                messagebox.showinfo("Try again! A bit higher this time.")
            else:
                messagebox.showinfo("Try again! A bit lower this time.")
        else:
            messagebox.showerror("Invalid input, try again!")

root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()