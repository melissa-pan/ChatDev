'''
Game logic for the Spelling Bee puzzle game.
'''
import random
import string
import nltk
from nltk.corpus import words
# Ensure the 'words' corpus is downloaded
try:
    words.words()
except LookupError:
    nltk.download('words')
class SpellingBeeGame:
    def __init__(self, central_letter=None, surrounding_letters=None):
        if central_letter is None or surrounding_letters is None:
            letters = random.sample(string.ascii_lowercase, 7)
            self.central_letter = letters[0]
            self.surrounding_letters = letters[1:]
        else:
            self.central_letter = central_letter
            self.surrounding_letters = surrounding_letters
        self.valid_words = self.load_valid_words()
        self.found_words = set()
        self.score = 0
    def load_valid_words(self):
        # Load a comprehensive dictionary of valid words
        return set(words.words())
    def is_valid_word(self, word):
        # Check if the word is valid
        if len(word) < 4:
            return False
        if self.central_letter not in word:
            return False
        if not all(letter in self.surrounding_letters + [self.central_letter] for letter in word):
            return False
        return word in self.valid_words
    def submit_word(self, word):
        if word in self.found_words:
            return "Word already found!"
        if self.is_valid_word(word):
            self.found_words.add(word)
            self.score += len(word)  # Example scoring: 1 point per letter
            return "Valid word!"
        else:
            return "Invalid word!"