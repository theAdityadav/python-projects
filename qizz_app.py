class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        answer = input("Your answer: ")
        if answer.lower() == question["answer"].lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Sorry, the correct answer is {question['answer']}")

    def play(self):
        for question in self.questions:
            self.ask_question(question)
        print(f"Your final score is {self.score} out of {len(self.questions)}")

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"}
]

quiz = Quiz(questions)
quiz.play()