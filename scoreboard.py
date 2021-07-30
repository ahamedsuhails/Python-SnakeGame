from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score  =  {self.count}", align="center", font=("Arial", 12, "normal"))

    def score(self):
        self.count += 1
        self.clear()
        self.write(f"Score  =  {self.count}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align="center", font=("Arial", 20, "normal"))
