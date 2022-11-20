from car_manager import CarManager, move_increment
from scoreboard import Scoreboard
from random import randint
from turtle import Screen
from player import Player
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")
scoreboard = Scoreboard()
cars = []


while game_is_on:
    sleep(0.1)
    screen.update()
    if randint(0, 1):
        i = CarManager()
        cars.append(i)
    for i in range(len(cars)):
        cars[i].go()
        if player.distance(cars[i])<=15:
            scoreboard.game_over()
            player.game_over()
            game_is_on = False
            for car in cars:
                car.hideturtle()
            for i in range(21):
                screen.update()
                sleep(0.1)
                scoreboard.goo()
    if player.ycor() >= 280:
        player.new_level()
        scoreboard.level_up()
        move_increment += 2

screen.exitonclick()

