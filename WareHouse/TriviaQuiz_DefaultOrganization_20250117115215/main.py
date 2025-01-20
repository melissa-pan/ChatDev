'''
Main application file for the trivia quiz program using tkinter.
'''
import tkinter as tk
from quiz_manager import QuizManager
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.quiz_manager = QuizManager()
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)
        self.option_buttons = []
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
        self.display_question()
    def display_question(self):
        question = self.quiz_manager.get_current_question()
        if question:
            self.question_label.config(text=question.text)
            # Clear existing buttons
            for button in self.option_buttons:
                button.destroy()
            self.option_buttons = []
            # Create buttons based on the number of options
            for i, option in enumerate(question.options):
                button = tk.Button(self.root, text=option, command=lambda i=i: self.check_answer(i))
                button.pack(fill='x', padx=20, pady=5)
                self.option_buttons.append(button)
        else:
            self.show_score()
    def check_answer(self, selected_index):
        correct = self.quiz_manager.check_answer(selected_index)
        if correct:
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Wrong!", fg="red")
    def next_question(self):
        self.result_label.config(text="")
        self.quiz_manager.next_question()
        self.display_question()
    def show_score(self):
        score = self.quiz_manager.get_score()
        self.question_label.config(text=f"Quiz Finished! Your score: {score}/{self.quiz_manager.total_questions()}")
        for button in self.option_buttons:
            button.config(state='disabled')
        self.next_button.config(state='disabled')
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()