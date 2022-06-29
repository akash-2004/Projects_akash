from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset()

    def move(self):
        """If the turtle is not at finish line, the turtle moves forward by move distance when the method is called."""
        if self.check_finish_line() == False:
            self.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        """Checks if the turtle is at the finish line. If yes, returns true and also resets the postion of the turtle, else returns false."""
        if self.ycor() >= FINISH_LINE_Y:
            self.reset()
            return True
        else:
            return False

    def reset(self):
        """Resets the position of the turtle when the method is called."""
        self.setposition(STARTING_POSITION)
