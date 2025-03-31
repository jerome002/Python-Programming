
import time

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice == correct_answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def quiz():
    questions = [
        ("What is the output of print(2 ** 3)?", ["5", "6", "8", "9"], 3),
        ("Who directed the movie 'Inception'?", ["Christopher Nolan", "Steven Spielberg", "James Cameron", "Quentin Tarantino"], 1),
        ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
        ("What keyword is used to define a function in Python?", ["func", "def", "define", "lambda"], 2),
        ("Which animal is known as the 'King of the Jungle'?", ["Tiger", "Elephant", "Lion", "Cheetah"], 3)
    ]
    
    score = 0
    
    print("\nWelcome to the Quiz! 🏆\n")
    time.sleep(1)
    
    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!\n")
        time.sleep(1)
    
    print(f"Your final score: {score}/{len(questions)}\n")
    
    return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

if __name__ == "__main__":
    while quiz():
        print("\nRestarting quiz...\n")
        time.sleep(1)
    print("Thanks for playing! 🎉")
