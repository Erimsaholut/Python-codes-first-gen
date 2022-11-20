from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setpos(STARTING_POSITION)
        self.level = 0

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)


