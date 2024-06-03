print("Welcome to the tiup calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

final_tips = (tip * bill) / 100
final_bill = (bill + final_tips) / people

print(f"Each person should pay: ${round(final_bill, 2)}")