import os

clear = lambda: os.system("cls")
clear()


number = int(input("Enter number:\t"))

if number % 2 == 0:
    print(f"{number} is EVEN number.")
else:
    print(f"{number} is ODD number.")


