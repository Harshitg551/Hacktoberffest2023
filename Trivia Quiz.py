import random

class TriviaQuiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def display_question(self):
        print("Question", self.current_question + 1)
        print(self.questions[self.current_question]['question'])

        choices = self.questions[self.current_question]['choices']
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

    def get_user_answer(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.questions[self.current_question]['choices']):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_game(self):
        random.shuffle(self.questions)

        for question in self.questions:
            self.current_question += 1
            self.display_question()

            user_answer = self.get_user_answer()
            correct_answer = question['answer']

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}. \n")

        print(f"You answered {self.score} out of {len(self.questions)} questions correctly.")

# Sample questions for the game
questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['Paris', 'London', 'Berlin'],
        'answer': 1
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'choices': ['Mars', 'Venus', 'Jupiter'],
        'answer': 1
    },
    # Add more questions here
]

if __name__ == "__main__":
    quiz = TriviaQuiz(questions)
    quiz.play_game()
