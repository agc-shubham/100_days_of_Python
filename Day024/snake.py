from turtle import Turtle


MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0,0),(0,-20),(0,-40)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        global STARTING_POSITIONS
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

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




