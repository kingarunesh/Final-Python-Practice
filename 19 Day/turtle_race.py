from turtle import Turtle, Screen
from random import randint


colors = ["red", "blue", "yellow", "green", "orange", "purple"]
turtle_positions = [150, 90, 30, -30, -90, -150]

turtles = []

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_positions[turtle_index])
    turtles.append(new_turtle)


flag = True

while flag:
    for j in range(len(turtles)):
        t = turtles[j]
        t.forward(randint(1, 10))
    
        if turtles[j].xcor() > 220:
            flag = False



screen.exitonclick()
