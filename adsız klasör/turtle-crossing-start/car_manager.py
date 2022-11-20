from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
move_increment = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.goto(x=280, y=randint(-230, 240))
        self.car_on_the_line = False
        self.speed("slowest")
        self.go()

    def go(self):
        self.forward(move_increment)
        self.car_on_the_linee()

    def car_on_the_linee(self):
        if self.xcor() <= -290:
            self.car_on_the_line = True
            self.hideturtle()




