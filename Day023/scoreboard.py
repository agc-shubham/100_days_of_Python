FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        #self.color('black')
        self.penup()
        self.goto(-220,250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        global FONT
        self.write(f"Level: {self.level}",  align="center",font=FONT)
    
    def game_over(self):
        global FONT
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)

    def inc_level(self):
        self.level += 1
        self.clear()
        self.update_score()

