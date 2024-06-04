import os

clear = lambda: os.system("cls")
clear()


heights = input("Enter height with space:\t")

height_list = heights.split(" ")

sum_of_height = 0
total_height = 0

for i in height_list:
    sum_of_height += int(i)
    total_height += 1


average_height = sum_of_height / total_height

print(f"Average Height = {round(average_height)}")