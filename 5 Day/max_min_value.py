import os


clear = lambda: os.system("cls")
clear()

#SECTION :          max value

"""
student_scores = input("Enter student score's with space:\t").split(" ")

highest_score = 0

for score in student_scores:
    score = int(score)
    if score > highest_score:
        highest_score = score


print(f"The highest score in the class is: {highest_score}")


#!          max value

total_students = int(input("How student's score do you have?\t"))

student_scores = []

for i in range(total_students):
    score = int(input("Enter student score:\t"))
    student_scores.append(score)


highest_score = 0

for i in range(len(student_scores)):
    if student_scores[i] > highest_score:
        highest_score = student_scores[i]


print(f"The highest score in the class is: {highest_score}")




#SECTION :          min value

student_scores = input("Enter student's score:\t").split(" ")

lowest_score = None

for score in student_scores:
    score = int(score)
    
    if lowest_score == None:
        lowest_score = score
        
    if score < lowest_score:
        lowest_score = score


print(lowest_score)


"""

