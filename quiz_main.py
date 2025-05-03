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
                choice_line = file.readline().strip()
                letter, answer = choice_line.split(".")
                choices[letter.strip] = answer.strip