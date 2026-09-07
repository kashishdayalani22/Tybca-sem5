import tkinter as tk
from tkinter import messagebox


class NumberGame:  #range of number from 1 to  100
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing AI")

        self.low = 1
        self.high = 100
        self.guess = None

        # Title
        tk.Label(  #display the instruction for player to think
            root,
            text="Think of a number from 1 to 100",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # Display guess
        self.display = tk.Label(  #display the number guessed by AI
            root,
            text="",
            font=("Arial", 30)
        )
        self.display.pack(pady=20)

        # Buttons
        frame = tk.Frame(root)  #creates the buttons that allows the player to tell the AI whether the number is lower or higher
        frame.pack()            #or equal

        tk.Button(
            frame,
            text="Higher",
            width=12,
            command=self.higher
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame,
            text="Correct",
            width=12,
            command=self.correct
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            frame,
            text="Lower",
            width=12,
            command=self.lower
        ).grid(row=0, column=2, padx=5)

        # New Game button
        tk.Button(
            root,              #allows the player tp restart the game and reset
                               
            text="New Game",
            command=self.reset
        ).pack(pady=20)

        # Make first guess
        self.make_guess()

    # -----------------------------------
    # Make a guess
    # -----------------------------------
    def make_guess(self):                      # Start the game by making the AI's first guess.
                                               # The AI starts by guessing the middle of 1 and 100.
        if self.low <= self.high:
            self.guess = (self.low + self.high) // 2
            self.display["text"] = str(self.guess)

        else:
            messagebox.showerror(
                "Error",
                "Your answers are inconsistent."
            )

    # -----------------------------------
    # Player says number is higher
    # -----------------------------------
    def higher(self):                    # Higher Method
                                        # Called when the player clicks the "Higher" button.
        self.low = self.guess + 1
        self.make_guess()

    # -----------------------------------
    # Player says number is lower
    # -----------------------------------
    def lower(self):
        self.high = self.guess - 1   # Lower Method
    # Called when the player clicks the "Lower" button.
        self.make_guess()

    # -----------------------------------
    # Player says correct
    # -----------------------------------
    def correct(self):
        messagebox.showinfo(
            "Game",
            f"I found your number: {self.guess}"
        )

        self.reset()

    # -----------------------------------
    # Reset game
    # -----------------------------------
    def reset(self):
        self.low = 1   # Reset Method
                            # Resets the game back to the original range of
                                    # 1 to 100.
        self.high = 100
        self.make_guess()


# ---------------------------------------
# Main program
# ---------------------------------------
root = tk.Tk()
game = NumberGame(root)
root.mainloop()
