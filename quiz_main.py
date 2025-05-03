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
            if not question:
                break
            choices = {}
            for i in range(4):
                choice_line = file.readline()
                letter, answer = choice_line.split(".")
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
    score = 0
    for i, questiondict in enumerate(quiz_copy):
        print(f"\nQuestion {i + 1}: {questiondict['question']}")
        for letter, choice in questiondict['choices'].items():
            print(f"{letter}. {choice}")
file = "quiz.txt"
quiz(read_quiz(file))
