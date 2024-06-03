import os

clear = lambda: os.system("cls")
clear()


bill = 0

size = input("What size Pizza do you want 's', 'm' or 'l'?\t")
pepperoni = input("Do you want add pepperoni 'y' or 'n'?\t")
cheese = input("Do you want extra cheese 'y' or 'n' ?\t")

if size == "s":
    bill += 15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill += 20
    if pepperoni == "y":
        bill += 3
elif size == "l":
    bill += 25
    if pepperoni == "y":
        bill += 3

if cheese == "y":
    bill += 1


print("Thanks for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}")