from random import choice, shuffle
import os

clear = lambda: os.system("cls")
clear()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Python-Password Generator!")

l_numbers = int(input("How many letters would you like in your password?\t"))
s_numbers = int(input("How many symbols would you like?\t"))
n_numbers = int(input("How many numbers would you like?\t"))

password = ""

for i in range(l_numbers):
    password += choice(letters)

for i in range(s_numbers):
    password += choice(symbols)

for i in range(n_numbers):
    password += choice(numbers)

print(password)

password_list = list(password)
shuffle(password_list)

new_password = ""

for i in password_list:
    new_password += i

print(new_password)