#SECTION :          len function

print(len("Arunesh"))

print(len("12345"))
#! print(len(12345))


print()


#SECTION :          String

first_name = "Arunesh"

print(first_name[0])
print(first_name[1])
print(first_name[-1])
#! print(first_name[-10])

print("123" + "45")


print()


#SECTION :         Integer (number)

print(123 + 45)

print(123456789)
print(123_456_789)


print()


#SECTION :          Float

print(1.1)

print(1.1 + 1.1)

print(1.1 + 2.2)

print(1 + 1.1)

print(1 + 1,1)


print()


#SECTION :      Boolean

print(True)
print(False)

print(True + True)
print(True - True)

print(True + False)
print(True - False)

print(False + True)
print(False - True)

print(False + False)
print(False - False)


print()


#SECTION :      type checking

# a = input("Enter number:\t")
a = "1"
print(a)
print(type(a))

# b = int(input("Enter number:\t"))
b = int("1")
print(b)
print(type(b))


#! print(1 + "1.1")
print(1 + float("1.1"))


print()


#SECTION :      Mathematical Operations

print(1 + 2)
print(2 - 1)
print(2 * 3)
print(3 / 2)
print(3 // 2)
print(2 ** 2)


print()


#SECTION :      Numbers

print(8 / 3)
print(8 // 3)

print(int(8 /3))
print(float(8 / 3))

print(round(8 / 3))
print(round(8 / 3, 2))
print(round(8 / 3, 4))

print(round(2))
print(round(2.1))
print(round(2.12345))
print(round(2.12345, 2))
print(round(2.12345, 8))

print(round(2.2))
print(round(2.4))
print(round(2.5))
print(round(2.6))
print(round(2.8))
print(round(2.11))


a = 2

# a += 1
# a -= 1
# a *= 2
a /= 2

print(a)



print()


#SECTION :      f-string

first_name = input("Enter first name:\t")
last_name = input("Enter last name:\t")
birth_year = input("Enter you'r birth year:\t")

print(f"Hello, {first_name} your surname is '{last_name}' and your age is {2024 - int(birth_year)}")