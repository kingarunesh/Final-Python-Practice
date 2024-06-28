from turtle import Turtle, Screen


tom = Turtle()

# tom.forward(10)
# tom.hideturtle()
# tom.forward(10)
# tom.showturtle()
# tom.forward(10)


for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()





screen = Screen()
screen.exitonclick()