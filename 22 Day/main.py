from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time



#NOTE :         screen
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


#NOTE :         paddle


r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))


screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

#NOTE :         ball
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()