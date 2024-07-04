from turtle import Turtle, Screen
import time



#NOTE :             screen
screen = Screen()

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)



#NOTE :             turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segements = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segements.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segements:
        seg.forward(10)










screen.exitonclick()