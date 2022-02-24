from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter a color:")
colors = ['','red','orange','yellow','blue','green','purple']
turtles = []
move_y = -125
for i in range(1,7):
    timmy = Turtle(shape='turtle')
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(-230,move_y)
    turtles.append(timmy)
    move_y += 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color ==  user_bet:
                print(f'You have Won! The {winning_color} turtle is winner')
            else:
                print(f'You have Lost! The {winning_color} turtle is winner')
                
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)



screen.exitonclick()