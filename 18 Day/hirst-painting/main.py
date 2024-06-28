# import colorgram

# photo_colors = colorgram.extract("photo.jpeg", 30)
# colors = []

# for color in photo_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))

# print(colors)


####################################################################################


from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


tom = Turtle()
tom.speed(0)
tom.hideturtle()
colormode(255)

x_pos = -400
y_pos = -300

tom.penup()
tom.setposition(x=x_pos, y=y_pos)


for _ in range(10):
    for _ in range(10):
        tom.dot(20, random_color())
        tom.forward(50)
    y_pos += 50
    tom.setposition(x=x_pos, y=y_pos)


screen = Screen()
screen.exitonclick()