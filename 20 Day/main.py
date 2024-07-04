from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard


#NOTE :             screen
screen = Screen()

screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


#!          snake class
snake = Snake()

#!          food
food = Food()

#!          score board
scoreboard = ScoreBoard()



#!          keyboard listen
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")



#NOTE :             turtle





game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    
    #!      move snake
    snake.move()
    
    #!      detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increment_score()
    
    #!      delect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    #!      detect snake tail touch
    for segment in snake.segements[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()