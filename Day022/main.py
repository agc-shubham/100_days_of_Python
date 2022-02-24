from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Creating Screen and its attributes
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

# Creating Paddles and Ball
# Right Paddle
r_paddle = Paddle((350,0))
# Left Paddle
l_paddle = Paddle((-350,0))
# Ball
ball = Ball()
scoreboard = Scoreboard()
# Event Listners
screen.listen()
# Event Listener for right paddle
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
# Event Listener for left paddle
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detect Collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 350 :
        ball.reset()
        scoreboard.inc_lscore()

    if ball.xcor() < -350 :
        ball.reset()
        scoreboard.inc_rscore()

screen.exitonclick()