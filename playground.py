import os

clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏")

print()

print("Welcome to Python-Calculator.")

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": divide
}

first_number = float(input("What's the first number?: "))

for i in operations:
    print(i)

operation = input("Pick an operations: ")
second_number = float(input("What's the next number?: "))

result = operations[f"{operations}"]
# print(result(n1=first_number, n2=second_number))
print(result)

