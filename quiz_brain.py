class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.current_score = 0
        self.still_has_questions = True

    def administer_quiz(self):
        while self.still_has_questions:
            question = self.question_list[self.question_number]
            self.question_number += 1
            user_input = input(f"Q.{self.question_number}: {question.text} (True/False):\n").capitalize()
            self.is_user_correct(user_input, question.answer)
        final_score = int((self.current_score / self.question_number) * 100)
        return final_score

    def is_user_correct(self, user_answer, answer):
        right_answer = False
        if user_answer == answer:
            self.current_score += 1
            right_answer = True
        self.display_answer(right_answer, answer)

    def display_answer(self, result, answer):
        if result:
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        self.display_score()

    def display_score(self):
        if self.question_number < len(self.question_list):
            print(f"Your current score is: {self.current_score}/{self.question_number}")
            print("\n")
        else:
            print("You completed the quiz!")
            print(f"Your final score is: {self.current_score}/{self.question_number}")
            self.still_has_questions = False
