import os


clear = lambda: os.system("cls")
clear()


print("Welcome to 'Bling Auction'.")


flag = True
bids = {}

while flag:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    there = input("Are there any other bidders? Type 'y' or 'n'. ")
    
    bids[name] = amount
    
    if there == "n":
        flag = False

print(bids)

winner_name = ""
winner_amount = 0

for name, amount in bids.items():
    if winner_name == "" and winner_amount == 0:
        winner_name = name
        winner_amount = amount
    
    if winner_name != name:
        if winner_amount < amount:
            winner_name = name
            winner_amount = amount


winner = {}
winner[winner_name] = winner_amount
print(winner)