'''
Contains the MastermindGame class which handles the game logic.
'''
import random
class MastermindGame:
    '''
    Encapsulates the logic for the Mastermind game.
    '''
    def __init__(self):
        self.colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']
        self.secret_code = self.generate_secret_code()
        self.max_attempts = 10
        self.attempts = 0
    def generate_secret_code(self):
        '''
        Generates a random sequence of colors as the secret code, allowing repetitions.
        '''
        return random.choices(self.colors, k=4)
    def check_guess(self, guess):
        '''
        Compares the player's guess to the secret code and returns feedback.
        '''
        correct_position = sum([1 for i in range(4) if guess[i] == self.secret_code[i]])
        correct_color = sum([min(guess.count(c), self.secret_code.count(c)) for c in set(guess)]) - correct_position
        return correct_position, correct_color