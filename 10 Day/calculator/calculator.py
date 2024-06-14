import os

from cal_fun import operators


clear = lambda: os.system("cls")
clear()


print("🙏 Sita Ram 🙏")

print("\nWelcome to Py-Calculator.")


def calculator():
    flag = True
    
    num1 = float(input("What's the first number?:\t"))
    
    while flag:
        for operator in operators.keys():
            print(operator)
        operator = input("Pick an operation:\t")

        num2 = float(input("What's the next number?:\t"))

        calculate = operators[operator]
        result = calculate(n1=num1, n2=num2)

        print(f"{num1} {operator} {num2} = {result}")

        user = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or type 'exit' for exit:\t")
                
        if user == "exit":
            flag = False
            clear()
        elif user == "y":
            num1 = result
        elif user == "n":
            flag = False
            clear()
            calculator()
        else:
            print("Invalid Input")

calculator()