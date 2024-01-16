from data import question_data
from question_model import CreateQuestionBank, question_bank
from quiz_brain import QuizBrain

CreateQuestionBank(question_data)
quiz_1 = QuizBrain(question_bank)
quiz_1_score = quiz_1.administer_quiz()
