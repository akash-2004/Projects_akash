from turtle import Turtle

from numpy import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.cars_list = []
        self.current_move_distance = STARTING_MOVE_DISTANCE
        self.make_car()

    def make_car(self):
        """Makes a car with a probability of 1/6 of rectangular shape, random color, random y-position and fixed x position of 300. The car is added to the cars list."""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(
                (300, random.choice(range(-230, 250, 50))))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars_list.append(new_car)

    def move_cars(self):
        """Moves all the cars in the cars list by the current move distance."""
        for _ in self.cars_list:
            _.forward(self.current_move_distance)

    def increment(self):
        """Increases the current move distance or pace."""
        self.current_move_distance += MOVE_INCREMENT
