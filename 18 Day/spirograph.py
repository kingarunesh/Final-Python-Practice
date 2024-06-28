from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


tom = Turtle()
tom.speed(0)
colormode(255)
tom.pensize(2)


#!      my solution
# for _ in range(75):
#     tom.pencolor(random_color())
#     tom.circle(200)
#     tom.left(5)


def draw(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.pencolor(random_color())
        tom.circle(150)
        tom.setheading(tom.heading() + size_of_gap)


draw(size_of_gap=5)
draw(size_of_gap=10)



screen = Screen()
screen.exitonclick()