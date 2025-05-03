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

    correct_answer = input("Enter the correct answer using (a,b,c, or d): ").lower()
    while correct_answer not in ['a','b','c','d']:
        print("Invalid input! Enter the correct answer (a,b,c, or d)")
        correct_answer = input("Enter the correct answer using (a,b,c, or d): ").lower()

    return {'question':question_input, 'answer':answers, 'correct_answer':correct_answer}

def write_file(quiz_data):
    with open("quiz.txt", "a") as file:
        file.write(f"Question: {quiz_data['question']}\n")
        for choice, answers in quiz_data['answer'].items():
            file.write(f"{choice}. {answers}\n")
        file.write(f"correct answer: {quiz_data['correct_answer']}\n")

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