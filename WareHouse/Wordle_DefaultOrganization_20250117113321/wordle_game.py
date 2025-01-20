'''
This module contains the WordleGame class which manages the game logic for a terminal-based Wordle game.
'''
import random
class WordleGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.daily_word = random.choice(self.word_list)
        self.max_attempts = 6
    def check_guess(self, guess):
        result = ['grey'] * len(guess)
        daily_word_chars = list(self.daily_word)
        # First pass: check for correct letters in correct positions
        for i in range(len(guess)):
            if guess[i] == self.daily_word[i]:
                result[i] = 'green'
                daily_word_chars[i] = None  # Mark this character as used
        # Second pass: check for correct letters in wrong positions
        for i in range(len(guess)):
            if result[i] == 'grey' and guess[i] in daily_word_chars:
                result[i] = 'yellow'
                daily_word_chars[daily_word_chars.index(guess[i])] = None  # Mark this character as used
        return result
    def is_correct_guess(self, guess):
        return guess == self.daily_word
    def get_daily_word(self):
        return self.daily_word