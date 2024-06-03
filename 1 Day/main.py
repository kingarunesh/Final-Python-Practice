print("Hello, Arunesh")

print("Hello\tArunesh")
print("Hello\nArunesh")

print("Hello" + " " + "Arunesh")

first_name = input("Enter your firstname:\n")
last_name = input("Enter your lastname:\n")
full_name = first_name + " " + last_name
print("Hello, " + full_name)

print()


##################################################################################
#
#SECTION           swap two variables
#
##################################################################################

a = 1
b = 2

print(f"a = {a}")
print(f"b = {b}")

#&      1 - method
# temp = a
# a = b
# b = temp

#&      2 - method
a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

