from turtle import Turtle

MOVE_PLAYER = 25


class Player(Turtle):
    def __init__(self):
        ##shape: triangle
        super().__init__(shape="triangle")
        self.penup()
        ##fillcolor: red
        ##outline: black
        self.color("black", "red")
        self.setheading(90)
        self.goto(0, -280)

    def move_right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + MOVE_PLAYER)

    def move_left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - MOVE_PLAYER)
