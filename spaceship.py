import random
from turtle import Turtle

SPACESHIP_SPEED = 3


class Spaceship:
    def __init__(self):
        self.all_spaceships = []

    def create_spaceship(self):
        if random.randint(1, 20) == 1:
            spaceship = Turtle("spaceship_image.gif")
            spaceship.penup()
            spaceship.goto(random.randint(-280, 280), 300)
            self.all_spaceships.append(spaceship)

    def move(self):
        for spaceship in self.all_spaceships:
            spaceship.sety(spaceship.ycor() - SPACESHIP_SPEED)
