import os

clear = lambda: os.system("cls")
clear()


items = ["a", "b", "c"]

for item in items:
    print(item)

print()

for i in range(len(items)):
    print(items[i])

print()

for i in range(5):
    print(i)
    
print()

for i in range(0, 5):
    print(i)

print()

for i in range(1, 5):
    print(i)

print()

for i in range(1, 5, 1):
    print(i)

print()

for i in range(1, 10, 3):
    print(i)

print()

even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
print(even_sum)