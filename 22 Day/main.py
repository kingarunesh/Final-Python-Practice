from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard



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


#NOTE :         score board
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    # time.sleep(ball.move_speed)
    time.sleep(0.01)
    screen.update()
    ball.move()
    
    #!      detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #!      detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #!      detect r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
    
    #!      detect l_paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()