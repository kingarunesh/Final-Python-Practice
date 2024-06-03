import os
import random


clear = lambda: os.system("cls")
clear()


a = random.random()
print(a)

b = random.random()
print(b)

c = random.randint(1,5)
print(c)


print()


#SECTION :      List
items = ["a", "b", "c", "d", "e"]

print(items[0])
print(items[1])

print(items[-1])

print(items)
items[1] = "B"
print(items)

items.append("aa")
print(items)

items.extend(["A", "B", "C"])
print(items)