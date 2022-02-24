from turtle import Screen
import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()

timmy.shape('turtle')
timmy.color('navy')
timmy.pensize(1)
timmy.speed('fastest')
colors = ['gray','dark blue','dark sea green','green yellow','red','medium purple','orchid','seashell','orange']
# # Challenge #1
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # Challenge #2
# for i in range(10):
    
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# Challenge 3
# def draw(no_of_sides):
#     angle = int(360/no_of_sides)
#     timmy.color(random.choice(colors))
#     for i in range(no_of_sides):
#         timmy.forward(80)
#         timmy.right(angle)

# for i in range(3,11):
#     draw(i)

# # Challenge 4
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

# direction = [0,90,180,270]
# while True:
#     timmy.setheading(random.choice(direction))
#     timmy.color(random_color())
# #   timmy.color(random.choice(colors))
#     timmy.forward(20)

# Challenge 5

angle = 0
while angle <= 360:
    timmy.color(random_color())
    # timmy.color(random.choice(colors))
    timmy.circle(50)
    angle += 10
    timmy.setheading(angle)


screen = Screen()
screen.exitonclick()