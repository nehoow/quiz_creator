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

        while True:
            user_answer = input("Your answer (enter the letter): ").strip().lower()
            if user_answer in questiondict['choices']:
                break
            else:
                print("Invalid input. Please enter the letter corresponding to your choice.")
        if user_answer == questiondict['correct_answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {questiondict['correct_answer']}.")

    print(f"\nQuiz finished! Your final score is {score}/{len(quiz_data)}.")

def main():
    quiz_questions = read_quiz("quiz.txt")
    if quiz_questions:
        quiz(quiz_questions)
    else:
        print("Could not load quiz questions from the file.")
        
main()