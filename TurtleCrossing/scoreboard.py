from turtle import Turtle


FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.currentlevel = 1

    def show_level(self):
        """Shows the current level of the player at position of (-295, 270) which is top left."""
        self.clear()
        self.goto(-295, 270)
        self.write(arg=f"Level: {self.currentlevel}", font=FONT)

    def increase_level(self):
        """Increases the level."""
        self.currentlevel += 1

    def game_over(self):
        self.goto(-50, 0)
        self.write(arg="GAME OVER", font=FONT)
