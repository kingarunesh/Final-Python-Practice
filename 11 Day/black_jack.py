import os
from random import choice


clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏")

print()

print("Welcome to 'Black-Jack' Game.")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(choice(cards))
print(len(cards))
