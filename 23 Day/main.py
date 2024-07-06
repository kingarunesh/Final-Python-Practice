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


#NOTE :         on key press
screen.onkey(fun=player.go_up, key="Up")


#NOTE :         car
car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #!      detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    
    #!      detect successfull crossing
    if player.is_at_finish_line():
        player.go_to_start()


screen.exitonclick()