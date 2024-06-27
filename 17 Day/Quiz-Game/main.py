import os

clear = lambda: os.system("cls")
clear()

#############################################################################

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    data = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(data)


# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)


quiz = QuizBrain(q_list=question_bank)


while quiz.still_has_questions():
    quiz.next_question()


#!      i did in quiz_brain
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{len(question_bank)}")