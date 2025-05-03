#Question: what is 4+4
#a. 4
#b. 8
#d. 20
#c. 16
#correct answer: b
import random

def read_quiz(quiz_file):
    with open(quiz_file ,"r") as file:
        questions = []
        while True:
            question = file.readline().strip().removeprefix("Question: ")
            choices = {}
            for i in range(4):
                letter, answer = file.readline().strip().split(".")
                choices[letter.strip()] = answer.strip()
            correctanswer = file.readline().strip().removeprefix("correct answer: ")
            questions.append({
                                "question": question,
                                "choices": choices,
                                "correct_answer": correctanswer
                            })
    return questions
def quiz(quiz_data):
    quiz_copy = list(quiz_data)
    random.shuffle(quiz_copy)
    for i in range(quiz_copy):