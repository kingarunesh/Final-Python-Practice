import os

clear = lambda: os.system("cls")
clear()


target_number = int(input("Enter target number:\t"))

total = 0

for i in range(2, target_number + 1):
    if i % 2 == 0:
        total += i
        
print(total)