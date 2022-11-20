from turtle import Turtle
FONT = ("Courier", 20, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-280, 260)
        self.level = 1
        self.write(f"Level {self.level} ",font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level} ", font=FONT)

    def game_over(self):
        self.goto(300, 0)

    def goo(self):
        self.clear()
        self.write(f"Game over\n Your score is : {self.level} ", font=FONT)
        self.forward(-20)







