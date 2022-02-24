from turtle import Turtle

X_COR = 0
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        global X_COR
        for _ in range(3):
            seg = Turtle(shape='square')
            seg.color('white')
            seg.penup()
            seg.goto(X_COR,0)
            X_COR -= 20
            self.segments.append(seg)

    def move(self):
        global MOVE
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE)

    def up(self):
        global UP, DOWN
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        

    def down(self):
        global DOWN, UP
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        

    def right(self):
        global RIGHT, LEFT
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        global LEFT, RIGHT
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)




