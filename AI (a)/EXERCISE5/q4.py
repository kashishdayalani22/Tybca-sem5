import random
import tkinter as tk

WIDTH = 600
HEIGHT = 400
STEP = 20


class CatchGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Target")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.player_x = 100
        self.player_y = 200
        self.target_x = 500
        self.target_y = 200
        self.score = 0

        self.player = self.canvas.create_rectangle(
            self.player_x,
            self.player_y,
            self.player_x + 30,
            self.player_y + 30,
            fill="blue",
        )
        self.target = self.canvas.create_oval(
            self.target_x,
            self.target_y,
            self.target_x + 25,
            self.target_y + 25,
            fill="red",
        )

        self.info = tk.Label(
            root,
            text="Use arrow keys to catch the target!",
            font=("Arial", 14),
        )
        self.info.pack()

        # Keyboard controls
        root.bind("<Left>", self.left)
        root.bind("<Right>", self.right)
        root.bind("<Up>", self.up)
        root.bind("<Down>", self.down)

        self.ai_move()

    def left(self, event):
        self.player_x -= STEP
        self.update_player()

    def right(self, event):
        self.player_x += STEP
        self.update_player()

    def up(self, event):
        self.player_y -= STEP
        self.update_player()

    def down(self, event):
        self.player_y += STEP
        self.update_player()

    def update_player(self):
        self.player_x = max(0, min(WIDTH - 30, self.player_x))
        self.player_y = max(0, min(HEIGHT - 30, self.player_y))
        self.canvas.coords(
            self.player,
            self.player_x,
            self.player_y,
            self.player_x + 30,
            self.player_y + 30,
        )
        self.check_collision()

    def ai_move(self):
        # Target flees away from the player
        if self.target_x < self.player_x:
            self.target_x -= STEP
        elif self.target_x > self.player_x:
            self.target_x += STEP

        if self.target_y < self.player_y:
            self.target_y -= STEP
        elif self.target_y > self.player_y:
            self.target_y += STEP

        # Keep target inside screen bounds
        self.target_x = max(0, min(WIDTH - 25, self.target_x))
        self.target_y = max(0, min(HEIGHT - 25, self.target_y))

        self.canvas.coords(
            self.target,
            self.target_x,
            self.target_y,
            self.target_x + 25,
            self.target_y + 25,
        )
        self.check_collision()
        self.root.after(150, self.ai_move)

    def check_collision(self):
        if (
            abs(self.player_x - self.target_x) < 30
            and abs(self.player_y - self.target_y) < 30
        ):
            self.score += 1
            self.info["text"] = f"Target caught! Score: {self.score}"

            # Respawn target at random location
            self.target_x = random.randint(50, WIDTH - 50)
            self.target_y = random.randint(50, HEIGHT - 50)


if __name__ == "__main__":
    root = tk.Tk()
    game = CatchGame(root)
    root.mainloop()