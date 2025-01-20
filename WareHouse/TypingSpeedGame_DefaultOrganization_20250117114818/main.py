'''
Main application file for the Typing Practice Game.
'''
import tkinter as tk
from word_manager import WordManager
from timer import Timer
import random
class TypingGameApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Practice Game")
        self.word_list = ["example", "practice", "typing", "speed", "accuracy", "python", "programming"]
        self.word_manager = WordManager(self.word_list)
        self.timer = Timer(60)  # 60 seconds for the game
        self.current_word = ""
        self.typed_text = ""
        self.total_typed_chars = 0
        self.total_correct_chars = 0
        self.setup_gui()
    def setup_gui(self):
        self.label = tk.Label(self.root, text="Type the word:", font=("Helvetica", 16))
        self.label.pack(pady=10)
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=10)
        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_input)
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=10)
    def start_game(self):
        self.timer.start()
        self.current_word = self.word_manager.get_random_word()
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.check_time()
    def check_input(self, event):
        self.typed_text = self.entry.get()
        self.total_typed_chars += len(self.typed_text)
        if self.typed_text == self.current_word:
            self.total_correct_chars += len(self.current_word)
            self.current_word = self.word_manager.get_random_word()
            self.word_label.config(text=self.current_word)
            self.entry.delete(0, tk.END)
    def check_time(self):
        if self.timer.get_elapsed_time() >= self.timer.duration:
            self.end_game()
        else:
            self.root.after(1000, self.check_time)  # Check every second
    def end_game(self):
        wpm = self.calculate_wpm(self.timer.get_elapsed_time())
        accuracy = self.calculate_accuracy()
        self.result_label.config(text=f"WPM: {wpm}, Accuracy: {accuracy}%")
    def calculate_wpm(self, elapsed_time):
        words_typed = self.total_typed_chars / 5  # Average word length is 5 characters
        minutes = elapsed_time / 60
        return round(words_typed / minutes)
    def calculate_accuracy(self):
        if self.total_typed_chars == 0:
            return 0.0
        return round((self.total_correct_chars / self.total_typed_chars) * 100, 2)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = TypingGameApp()
    app.run()