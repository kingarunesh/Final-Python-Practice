from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


tom = Turtle()
tom.speed(0)
colormode(255)

x_pos = -400
y_pos = -300

tom.penup()
tom.hideturtle()
tom.setposition(x=x_pos, y=y_pos)


for _ in range(15):
    for _ in range(15):
        tom.dot(20, random_color())
        tom.forward(50)
    y_pos += 50
    tom.setposition(x=x_pos, y=y_pos)


screen = Screen()
screen.exitonclick()