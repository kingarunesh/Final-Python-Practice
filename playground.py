from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()






# from turtle import Turtle, Screen, colormode
# from random import randint


# def random_color():
#     return (randint(0, 255), randint(0, 255), randint(0, 255))


# tom = Turtle()
# tom.speed(0)
# colormode(255)

# x_pos = -400
# y_pos = -300

# tom.penup()
# tom.hideturtle()
# tom.setposition(x=x_pos, y=y_pos)


# for _ in range(15):
#     for _ in range(15):
#         tom.dot(20, random_color())
#         tom.forward(50)
#     y_pos += 50
#     tom.setposition(x=x_pos, y=y_pos)


# screen = Screen()
# screen.exitonclick()


