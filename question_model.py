question_bank = []


class CreateQuestionObjects:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class CreateQuestionBank:

    def __init__(self, data):
        for question in data:
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = CreateQuestionObjects(question_text, question_answer)
            question_bank.append(new_question)
