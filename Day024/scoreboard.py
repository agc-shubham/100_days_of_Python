from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        #self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",  align="center",font=('Courier',20,'bold'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",align="center",font=('Courier',22,'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            score = f'{self.high_score}'
            with open('data.txt','w') as f:
                f.write(score)

        self.score = 0
        self.update_score()
         
          
    def increase_score(self):
        self.score +=1
        self.update_score()

        