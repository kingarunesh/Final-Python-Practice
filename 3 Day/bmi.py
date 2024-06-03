import os


clear = lambda: os.system("cls")
clear()


weight = float(input("Enter your weight:\t"))
height = float(input("Enter your height:\t"))

BMI = weight / (height ** 2)

if BMI < 18:
    print(f"Your BMI is {round(BMI)}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {round(BMI)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")