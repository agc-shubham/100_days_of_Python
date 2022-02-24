# import colorgram


# color_objs = colorgram.extract('image.jpg', 30)

# color_RGB = []
# for color_obj in color_objs:
#     r = color_obj.rgb[0]
#     g = color_obj.rgb[1]
#     b = color_obj.rgb[2]
#     color_RGB.append((r,g,b))

# print(color_RGB)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
# import os

# for file in os.listdir():
#     print(file)
import turtle
import random
turtle.colormode(255)



timmy = turtle.Turtle()

timmy.shape('arrow')
timmy.speed(10)
timmy.penup()
    
timmy.hideturtle()

Y = -250
X = -350
for i in range(11):
    
    timmy.setposition(x=(X,Y),y=None)
    for j in range(11):
        
        timmy.dot(10,random.choice(color_list))
        timmy.forward(60)

    Y += 50

screen = turtle.Screen()
screen.exitonclick()