weight = float(input("Enter weight:\t"))
height = float(input("Enter height(m):\t"))

BMI = weight / (height ** 2)

print(f"BMI: {int(BMI)}")
print(f"BMI: {round(BMI)}")
print(f"BMI: {round(BMI, 2)}")
