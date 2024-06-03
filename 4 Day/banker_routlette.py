import os
import random


clear = lambda: os.system("cls")
clear()


names = input("Enter names with comma:\t")

print(names)

names_list = names.split(", ")

print(f"{random.choice(names_list)} is going to buy the meal today!")
