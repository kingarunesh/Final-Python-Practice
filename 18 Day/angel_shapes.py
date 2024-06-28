import os

clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏\n")

################################################################################


from turtle import Turtle, Screen
from random import choice

#SECTION :          Triangle
tom = Turtle()


tom.penup()
tom.goto(x=-50, y=-200)
tom.pendown()

move_number = 3
color_position = 0
colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple", "navy"]


for _ in range(15):
    move_angel = 360 / move_number
    # tom.pencolor(colors[color_position])
    tom.pencolor(choice(colors))
    for _ in range(move_number):
        tom.pensize(3)
        tom.forward(120)
        tom.left(move_angel)
    move_number += 1
    color_position += 1






#SECTION :      screen
screen = Screen()
screen.exitonclick()
