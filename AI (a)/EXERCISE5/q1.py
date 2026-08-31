import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")

        self.board = [""] * 9
        self.buttons = []

        self.player = "X"
        self.computer = "O"

        # Title
        title = tk.Label(
            root,
            text="TIC TAC TOE",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        # Game board
        board_frame = tk.Frame(root)
        board_frame.pack()

        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 30, "bold"),
                width=4,
                height=2,
                command=lambda i=i: self.player_move(i)
            )

            button.grid(
                row=i // 3,
                column=i % 3,
                padx=3,
                pady=3
            )

            self.buttons.append(button)

        # Status
        self.status = tk.Label(
            root,
            text="Your turn (X)",
            font=("Arial", 14)
        )
        self.status.pack(pady=15)

        # New Game button
        new_game = tk.Button(
            root,
            text="New Game",
            font=("Arial", 12),
            command=self.reset_game
        )
        new_game.pack()

    # -----------------------------------
    # Player move
    # -----------------------------------
    def player_move(self, position):
        # Ignore occupied cell
        if self.board[position] != "":
            return

        # Put X
        self.board[position] = self.player
        self.buttons[position]["text"] = self.player

        # Check player win
        if self.check_winner(self.player):
            self.status["text"] = "You Win!"
            messagebox.showinfo(
                "Game Over",
                "Congratulations! You Win!"
            )
            self.disable_board()
            return

        # Check draw
        if "" not in self.board:
            self.status["text"] = "Draw!"
            messagebox.showinfo(
                "Game Over",
                "Game Draw!"
            )
            return

        # Computer turn
        self.status["text"] = "Computer thinking..."
        self.root.after(500, self.computer_move)

    # -----------------------------------
    # Computer move
    # -----------------------------------
    def computer_move(self):
        position = self.find_best_move()

        if position is not None:
            self.board[position] = self.computer
            self.buttons[position]["text"] = self.computer

        # Check computer win
        if self.check_winner(self.computer):
            self.status["text"] = "Computer Wins!"
            messagebox.showinfo(
                "Game Over",
                "Computer Wins!"
            )
            self.disable_board()
            return

        # Check draw
        if "" not in self.board:
            self.status["text"] = "Draw!"
            messagebox.showinfo(
                "Game Over",
                "Game Draw!"
            )
            return

        self.status["text"] = "Your turn (X)"

    # -----------------------------------
    # Simple heuristic AI
    # -----------------------------------
    def find_best_move(self):
        # 1. Try to WIN
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.computer

                if self.check_winner(self.computer):
                    self.board[i] = ""
                    return i

                self.board[i] = ""

        # 2. BLOCK player's winning move
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.player

                if self.check_winner(self.player):
                    self.board[i] = ""
                    return i

                self.board[i] = ""

        # 3. Take CENTER
        if self.board[4] == "":
            return 4

        # 4. Take a CORNER
        corners = [0, 2, 6, 8]

        empty_corners = [
            i for i in corners
            if self.board[i] == ""
        ]

        if empty_corners:
            return random.choice(empty_corners)

        # 5. Take any available position
        empty_positions = [
            i for i in range(9)
            if self.board[i] == ""
        ]

        if empty_positions:
            return random.choice(empty_positions)

        return None

    # -----------------------------------
    # Check winner
    # -----------------------------------
    def check_winner(self, player):
        winning_patterns = [
            # Rows
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),

            # Columns
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),

            # Diagonals
            (0, 4, 8),
            (2, 4, 6)
        ]

        for pattern in winning_patterns:
            a, b, c = pattern

            if (
                self.board[a] == player
                and self.board[b] == player
                and self.board[c] == player
            ):
                return True

        return False

    # -----------------------------------
    # Disable board
    # -----------------------------------
    def disable_board(self):
        for button in self.buttons:
            button["state"] = "disabled"

    # -----------------------------------
    # Reset game
    # -----------------------------------
    def reset_game(self):
        self.board = [""] * 9

        for button in self.buttons:
            button["text"] = ""
            button["state"] = "normal"

        self.status["text"] = "Your turn (X)"


# ---------------------------------------
# Main program
# ---------------------------------------
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
