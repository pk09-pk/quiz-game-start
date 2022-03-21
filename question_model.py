import sqlalchemy


class Question:  # creating a class named Question

    def __init__(self, q_text, q_ansswer):  # constructor with parameters
        self.text = q_text  # giving values to the attributes via parameters
        self.answer = q_ansswer


new_q = Question("Asdfgh", "false")
print(new_q.text)
