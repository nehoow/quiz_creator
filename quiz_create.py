##For Assignment 9: Quiz Creator
#
##Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.
#
#Hint: 
#On the next assignment, you will create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.
#Format the data written on the text file so it is easier the read on the next assignment.
#Use your creativity, dapat maangas.
#Feel free to use any library
#
#
#Important Note:
#Bawal ng mangopya. Matindi ang kaparusahan.
#Give descriptive caption s mga commit. Match dapat s last code changes.
#Kaylangan ko masundan kng paano nabuo ung program using your commits.
#Pag di ko masundan matic magtatanong ako. Umamin kyo kagad.
#Create a demo, send the link of your demo to my messenger before April 12.
#Upload the source code to your github account using gitbash.
import os

def create_item():
    question_input = input("Enter your question or type 'exit' to finish: ")
    if question_input == "exit":
        return None
    answers = {}
    answers['a'] = input("Enter answer a: ")
    answers['b'] = input("Enter answer b: ")
    answers['c'] = input("Enter answer c: ")
    answers['d'] = input("Enter answer d: ")

    correct_answer = input("Enter the correct answer using (a,b,c, or d): ").lower
    while correct_answer not in ['a','b','c','d']:
        print("Invalid input! Enter the correct answer (a,b,c, or d)")
        correct_answer = input("Enter the correct answer using (a,b,c, or d): ").lower

    return {'question':question_input, 'answer':answers, 'correct_answer':correct_answer}

def write_file(quiz_data):
    with open("quiz.txt", "a") as file:
        file.write(f"Question: {quiz_data['question']}\n")
        for choice, answers in quiz_data['answer'].items():
            file.write(f"{choice}. {answers}\n")
        file.write(f"correct answer: {quiz_data['correct_answer']}\n-\n")

def main():
    filename = "quiz.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Existing file '{filename}' deleted.")

    while True:
        quiz_data = create_item()
        if quiz_data is None:
            break
        write_file(quiz_data)
main()