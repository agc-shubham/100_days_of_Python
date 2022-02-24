from turtle import Turtle, Screen

angle = 0

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_counterclock():
    global angle
    angle -= 2
    timmy.left(angle)

def turn_clock():
    global angle
    angle += 2
    timmy.right(angle)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=turn_counterclock)
screen.onkey(key='d',fun=turn_clock)
screen.onkey(key='c',fun=clear)

screen.exitonclick()