
import random

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

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
        print(f"\n{YELLOW}Question {i + 1}:{RESET} {questiondict['question']}")
        for letter, choice in questiondict['choices'].items():
            print(f"{BLUE}{letter}{RESET}. {choice}")

        while True:
            user_answer = input("Your answer (enter the letter): ").strip().lower()
            if user_answer in questiondict['choices']:
                break
            else:
                print("Invalid input. Please enter the letter corresponding to your choice.")
        if user_answer.lower() == questiondict['correct_answer']:
            print(f"{GREEN}Correct!{RESET}")
            score += 1
        else:
            print(f"{RED}Incorrect.{RESET} The correct answer was {GREEN}{questiondict['correct_answer']}{RESET}.")

    print(f"\n{GREEN}Quiz finished!{RESET} Your final score is {BLUE}{score}/{len(quiz_data)}.{RESET}")

def main():
    quiz_questions = read_quiz("quiz.txt")
    if quiz_questions:
        quiz(quiz_questions)
    else:
        print("Could not load quiz questions from the file.")
        
main()