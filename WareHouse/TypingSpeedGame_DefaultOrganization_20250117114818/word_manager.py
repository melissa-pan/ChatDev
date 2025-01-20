'''
WordManager class for managing words or phrases in the Typing Practice Game.
'''
import random
class WordManager:
    def __init__(self, word_list):
        self.word_list = word_list
    def get_random_word(self):
        return random.choice(self.word_list)