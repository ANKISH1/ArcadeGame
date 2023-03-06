from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect Collision With Wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Detect Collision with right paddle or left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <  -320:
        ball.bounce_x()
        ball.speed("fastest")

    # If Right Paddle misses the ball
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # If Left Paddle Misses the ball
    if ball.xcor()< -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

