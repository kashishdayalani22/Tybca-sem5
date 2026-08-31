import tkinter as tk
import random
from collections import Counter


class RPS:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.history = []
        self.player_score = 0
        self.computer_score = 0

        # Title
        tk.Label(
            root,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        # Result
        self.result = tk.Label(
            root,
            text="Choose your move",
            font=("Arial", 15)
        )
        self.result.pack(pady=10)

        # Buttons
        frame = tk.Frame(root)
        frame.pack()

        for move in ["Rock", "Paper", "Scissors"]:
            tk.Button(
                frame,
                text=move,
                width=12,
                command=lambda m=move: self.play(m)
            ).pack(side="left", padx=5)

        # Score
        self.score = tk.Label(
            root,
            text="You: 0    Computer: 0",
            font=("Arial", 14)
        )
        self.score.pack(pady=20)

    # -----------------------------------
    # Play game
    # -----------------------------------
    def play(self, player):
        self.history.append(player)

        computer = self.predict_move()
        winner = self.get_winner(player, computer)

        if winner == "player":
            self.player_score += 1
            text = "You Win!"

        elif winner == "computer":
            self.computer_score += 1
            text = "Computer Wins!"

        else:
            text = "Draw!"

        self.result["text"] = (
            f"You: {player}\n"
            f"Computer: {computer}\n\n"
            f"{text}"
        )

        self.score["text"] = (
            f"You: {self.player_score}    "
            f"Computer: {self.computer_score}"
        )

    # -----------------------------------
    # Predict player's next move
    # -----------------------------------
    def predict_move(self):
        # Not enough history
        if len(self.history) < 3:
            return random.choice(
                ["Rock", "Paper", "Scissors"]
            )

        counts = Counter(self.history)

        predicted = counts.most_common(1)[0][0]

        # Counter move
        if predicted == "Rock":
            return "Paper"

        if predicted == "Paper":
            return "Scissors"

        return "Rock"

    # -----------------------------------
    # Determine winner
    # -----------------------------------
    def get_winner(self, p, c):
        if p == c:
            return "draw"

        if (
            (p == "Rock" and c == "Scissors")
            or
            (p == "Paper" and c == "Rock")
            or
            (p == "Scissors" and c == "Paper")
        ):
            return "player"

        return "computer"


# ---------------------------------------
# Main program
# ---------------------------------------
root = tk.Tk()
game = RPS(root)
root.mainloop()
