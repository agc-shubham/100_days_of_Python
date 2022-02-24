from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Left Score: {self.l_score} | Right Score: {self.r_score}",  align="center",font=('Courier',20,'bold'))
    
    def inc_rscore(self):
        self.r_score += 1
        self.clear()
        self.update_score()
    
    def inc_lscore(self):
        self.l_score += 1
        self.clear()
        self.update_score()