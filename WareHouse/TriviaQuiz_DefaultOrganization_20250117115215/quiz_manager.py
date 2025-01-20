'''
Manages the quiz questions and tracks the user's progress and score.
'''
from question import Question
class QuizManager:
    def __init__(self):
        self.questions = [
            Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2),
            Question("What is 2 + 2?", ["3", "4", "5", "6"], 1),
            Question("What is the largest planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2)
        ]
        self.current_question_index = 0
        self.score = 0
    def get_current_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None
    def check_answer(self, selected_index):
        question = self.get_current_question()
        if question and question.correct_index == selected_index:
            self.score += 1
            return True
        return False
    def next_question(self):
        self.current_question_index += 1
    def get_score(self):
        return self.score
    def total_questions(self):
        return len(self.questions)