from turtle import Turtle

FONT = ("SimSun", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.hideturtle()
        self.score = 0

    def increase_score(self):
        self.score += 1

    def update_score(self):
        return f"Score: {self.score}".rjust(90)

    def game_over(self):
        self.write(f"Game Over", align="center", font=FONT)
        self.sety(self.ycor() - 35)
        self.write(f"Your Final Score: {self.score}", align="center", font=FONT)
