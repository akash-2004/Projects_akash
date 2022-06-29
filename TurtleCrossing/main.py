import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")
cars = CarManager()
score = Scoreboard()


def check_collision(player, obstacles_list):
    global is_game_on
    for obstacle in obstacles_list:
        # half the diagonal length of the car if the breadth is 2 times the length and the length is 20px = 10*(5**(1/2)).
        # if (player.distance((player.xcor(), obstacle.ycor())) == 0) or (player.distance((obstacle.xcor(), player.ycor())) == 0):
        if player.distance(obstacle) <= 20:
            score.game_over()
            is_game_on = False
            return True
    return False


is_game_on = True
while is_game_on:
    score.show_level()
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    check_collision(player=player, obstacles_list=cars.cars_list)
    if player.check_finish_line():
        # Resets pos of turtle when called while also returning a boolean value whether the turtle is at the finish line or not.
        player.check_finish_line()
        cars.increment()
        time.sleep(0.4)
        score.increase_level()
        # for _ in range(5):
        #     cars.make_car()

    cars.make_car()

screen.exitonclick()
