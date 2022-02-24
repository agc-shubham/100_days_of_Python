from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # segments[0].left(90)
    # Hitting Food
    if snake.segments[0].distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect Collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass
        # elif snake.segments[0].distance(segment)<10:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snake.segments[0].distance(segment)<10:
             game_is_on = False
             scoreboard.game_over()




screen.exitonclick()