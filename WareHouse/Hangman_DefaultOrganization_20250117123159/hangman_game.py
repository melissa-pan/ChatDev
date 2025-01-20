'''
Contains the HangmanGame class, which manages the game logic for the Hangman game.
'''
import random
class HangmanGame:
    def __init__(self):
        self.words = ["python", "hangman", "challenge", "programming", "developer"]
        self.max_attempts = 6
        self.reset_game()
    def reset_game(self):
        self.selected_word = self.select_random_word()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.attempts_left = self.max_attempts
    def select_random_word(self):
        return random.choice(self.words)
    def make_guess(self, letter):
        if letter in self.selected_word:
            self.correct_guesses.add(letter)
        else:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
    def is_game_over(self):
        return self.attempts_left <= 0 or self.is_word_guessed()
    def is_word_guessed(self):
        return all(letter in self.correct_guesses for letter in self.selected_word)
    def get_display_word(self):
        return " ".join(letter if letter in self.correct_guesses else "_" for letter in self.selected_word)