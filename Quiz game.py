class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

# Create quiz questions
quiz_questions = [
    QuizQuestion(
        "What is the capital of France?",
        ["a) London", "b) Paris", "c) Rome", "d) Madrid"],
        "b"
    ),
    QuizQuestion(
        "Which planet is known as the Red Planet?",
        ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "b"
    ),
    QuizQuestion(
        "Who painted the Mona Lisa?",
        ["a) Leonardo da Vinci", "b) Vincent van Gogh", "c) Pablo Picasso", "d) Michelangelo"],
        "a"
    ),
    QuizQuestion(
        "Which natural wonder is located in Arizona, USA, and is known for its colorful rock formations?",
        ["a) Grand Canyon", "b) Great Barrier Reef", "c) Mount Everest", "d) Niagara Falls"],
        "a"
    ),
    QuizQuestion(
        "What is the largest mammal in the world?",
        ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Lion"],
        "b"
    ),
    QuizQuestion(
        "What is the chemical symbol for the element gold?",
        ["a) Ag", "b) Au", "c) Go", "d) Gd"],
        "b"
    ),
    QuizQuestion(
        "Which famous scientist developed the theory of general relativity?",
        ["a) Isaac Newton", "b) Albert Einstein", "c) Galileo Galilei", "d) Marie Curie"],
        "b"
    ),
    QuizQuestion(
        "In which year did World War I begin?",
        ["a) 1905", "b) 1914", "c) 1939", "d) 1918"],
        "b"
    ),
    QuizQuestion(
        "What is the smallest prime number?",
        ["a) 1", "b) 2", "c) 3", "d) 4"],
        "b"
    ),
    QuizQuestion(
        "Which famous playwright wrote Romeo and Juliet?",
        ["a) Mark Twain", "b) William Shakespeare", "c) Charles Dickens", "d) Jane Austen"],
        "b"
    ),
    QuizQuestion(
        "Which country is known as the Land of the Rising Sun?",
        ["a) China", "b) Japan", "c) South Korea", "d) Thailand"],
        "b"
    ),
    QuizQuestion(
        "What is the largest ocean on Earth?",
        ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
        "d"
    ),
    QuizQuestion(
        "Which famous scientist is known for his theory of evolution by natural selection?",
        ["a) Galileo Galilei", "b) Isaac Newton", "c) Charles Darwin", "d) Albert Einstein"],
        "c"
    ),
    QuizQuestion(
        "Which gas do plants use for photosynthesis?",
        ["a) Oxygen", "b) Carbon Dioxide", "c) Nitrogen", "d) Hydrogen"],
        "b"
    ),
    QuizQuestion(
        "What is the largest organ in the human body?",
        ["a) Heart", "b) Liver", "c) Brain", "d) Skin"],
        "d"
    ),
]

def display_question(question):
    print(question.question)
    for option in question.options:
        print(option)
    return input("Your answer: ").strip().lower()

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def main():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice questions.")
    print("Enter the letter corresponding to your answer.")
    
    total_questions = len(quiz_questions)
    correct_answers = 0

    for index, question in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {index}/{total_questions}:")
        user_answer = display_question(question)
        if evaluate_answer(user_answer, question.correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {question.correct_answer.upper()}")

    final_score = (correct_answers / total_questions) * 100
    print(f"\nQuiz completed!\nYour final score: {final_score:.2f}%")

if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":
        main()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thank you for playing!")
