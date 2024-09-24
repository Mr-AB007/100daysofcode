class QuizzBrain:
    def __init__(self,questionList):
        self.questionList = questionList
        self.questionNumber = 0
        self.score = 0

    def still_has_question(self):
        return self.questionNumber < len(self.questionList)


    def ask(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}: {currentQuestion.text}?(True/False) : ").lower()
        self.check_answer(answer,currentQuestion.answer.lower())

        return answer
    def check_answer(self,answer,correct_ans):
        if answer == correct_ans:
            print("That's Correct")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"Correct answer was: {correct_ans}")
        print(f"Your current score is {self.score}/{self.questionNumber}\n")