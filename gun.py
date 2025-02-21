from turtle import Turtle

GUN_SPEED = 20


class Gun:
    def __init__(self, player):
        self.fires = []
        self.player = player

    def fire(self):
        fire = Turtle(shape="circle")
        fire.penup()
        fire.shapesize(stretch_wid=0.5, stretch_len=0.5)
        fire.color("firebrick")
        fire.goto(self.player.position())
        self.fires.append(fire)

    def move(self):
        for fire in self.fires:
            fire.sety(fire.ycor() + GUN_SPEED)
            if fire.ycor() > 300:
                fire.hideturtle()
                self.fires.remove(fire)
