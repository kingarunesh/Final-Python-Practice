from turtle import Turtle, Screen, colormode
from random import choice, randint



# colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple", "navy"]
directions = [0, 90, 180, 270]

tom = Turtle()
tom.pensize(8)
tom.speed("fastest")
colormode(255)

def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


for _ in range(500):
    tom.pencolor(random_color())
    tom.forward(30)
    tom.setheading(choice(directions))



screen = Screen()
screen.exitonclick()