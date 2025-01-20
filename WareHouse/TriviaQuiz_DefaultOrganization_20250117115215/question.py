'''
Defines the Question class to represent a quiz question.
'''
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index