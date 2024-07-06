import os

clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏")

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#NOTE :         screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


#NOTE :         player
player = Player()


screen.onkey(fun=player.go_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()