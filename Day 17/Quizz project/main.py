from data import question_data
from question_model import Question
from quizzBrain import QuizzBrain

questionBank = []

for question in question_data:
    questionBank.append(Question(question["text"],question["answer"]))

quiz = QuizzBrain(questionBank)
questionNumber = quiz.questionNumber

while quiz.still_has_question():
    answer = quiz.ask()

print("\nQuiz Completed")
print(f"Your Final score is: {quiz.score}/{quiz.questionNumber}")

