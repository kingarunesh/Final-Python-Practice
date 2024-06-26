import os

from turtle import Turtle, Screen

clear = lambda: os.system("cls")
clear()


print("🙏 Sita Ram 🙏")
print()


timmy = Turtle()
# print(timmy)
timmy.shape("turtle")
timmy.shapesize(2)

# timmy.fillcolor("red")
timmy.color("red")
# timmy.pencolor("red")

timmy.forward(100)



my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()


# tom = Turtle()
# print(tom)