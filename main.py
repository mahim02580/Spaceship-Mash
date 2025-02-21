import time
import turtle
from player import Player
from gun import Gun
from spaceship import Spaceship
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkSlateGray1")
screen.addshape("spaceship_image.gif")
screen.tracer(0)

player = Player()
gun = Gun(player)
spaceship = Spaceship()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=gun.fire, key="Up")

game_is_on = True
while game_is_on:
    screen.title(scoreboard.update_score())
    screen.update()
    time.sleep(0.1)
    spaceship.create_spaceship()
    spaceship.move()
    gun.move()
    for c_spaceship in spaceship.all_spaceships:
        if c_spaceship.ycor() < -280:
            scoreboard.game_over()
            game_is_on = False
        for c_fire in gun.fires:
            if c_spaceship.distance(c_fire) < 20:
                c_spaceship.hideturtle()
                spaceship.all_spaceships.remove(c_spaceship)
                c_fire.hideturtle()
                gun.fires.remove(c_fire)
                scoreboard.increase_score()

turtle.mainloop()
