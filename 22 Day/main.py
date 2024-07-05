from turtle import Turtle, Screen



#NOTE :         screen
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


#NOTE :         paddle

def go_up():
    right_paddle.goto(x=right_paddle.xcor(), y=right_paddle.ycor() + 20)

def go_down():
    right_paddle.goto(x=right_paddle.xcor(), y=right_paddle.ycor() - 20)

right_paddle = Turtle(shape="square")
right_paddle.shapesize(stretch_len=1, stretch_wid=5)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(x=350, y=0)


screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()