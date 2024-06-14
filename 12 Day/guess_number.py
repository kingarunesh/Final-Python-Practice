import os
from random import randint


clear = lambda: os.system("cls")
clear()

print("🙏 Sita Ram 🙏")

print()

print("Welcome to the Number Guessing Game!")
print("I'm thinking between 1 and 100.")


number = randint(1, 100)
attempts = 0

print(f"Testing: {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\t")

if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts remaning to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print("You have 5 attempts remaning to guess the number.")

while attempts > 0:
    attempts -= 1
    
    user_guess = int(input("Make a guess:\t"))
    
    if attempts == 0:
        print("You've run out of guesses, You Lose.")
    elif user_guess > number:
        print("📈 Too high")
        print("Guess again.")
        print(f"You have {attempts} attempts remaning to guess the number.")
    elif user_guess < number:
        print("📉 Too Low")
        print("Guess again.")
        print(f"You have {attempts} attempts remaning to guess the number.")
    elif user_guess == number:
        print(f"🥇 You got it! The answer was {number}.")
        attempts = 0
        