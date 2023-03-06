from turtle import Turtle
import random

ANGLES = [45, 135, 225, 315]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.setheading(random.choice(ANGLES))


    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        #We are simply reversing the value of y_move so it moves opposite of how it was moving initially
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
