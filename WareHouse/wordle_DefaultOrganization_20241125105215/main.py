'''
Wordle Game: A terminal-based implementation of the Wordle game where players guess a 5-letter word.
'''
import random
class WordleGame:
    def __init__(self, secret_word=None):
        '''
        Initialize the Wordle game with a secret word.
        If no word is provided, select a random word from a predefined list.
        '''
        self.word_list = ['apple', 'grape', 'peach', 'berry', 'melon']
        self.secret_word = secret_word or random.choice(self.word_list)
        self.max_attempts = 6
        self.attempts = 0
    def check_guess(self, guess):
        '''
        Check the player's guess against the secret word and return feedback.
        Green for correct letter and position, yellow for correct letter wrong position,
        and grey for incorrect letter.
        '''
        feedback = ['\033[90m{}\033[0m'.format(guess[i]) for i in range(5)]  # Grey
        secret_word_list = list(self.secret_word)
        # First pass: Check for correct letters in the correct position
        for i in range(5):
            if guess[i] == self.secret_word[i]:
                feedback[i] = '\033[92m{}\033[0m'.format(guess[i])  # Green
                secret_word_list[i] = None  # Mark this letter as used
        # Second pass: Check for correct letters in the wrong position
        for i in range(5):
            if feedback[i] == '\033[90m{}\033[0m'.format(guess[i]) and guess[i] in secret_word_list:
                feedback[i] = '\033[93m{}\033[0m'.format(guess[i])  # Yellow
                secret_word_list[secret_word_list.index(guess[i])] = None  # Mark this letter as used
        return feedback
    def play(self):
        '''
        Play the Wordle game, allowing the player to make guesses and receive feedback.
        '''
        print("Welcome to Wordle! Guess the 5-letter word.")
        while self.attempts < self.max_attempts:
            guess = input(f"Attempt {self.attempts + 1}/{self.max_attempts}: ").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Please enter a valid 5-letter word.")
                continue
            self.attempts += 1
            feedback = self.check_guess(guess)
            print("Feedback:", ' '.join(feedback))
            if guess == self.secret_word:
                print("Congratulations! You've guessed the word correctly!")
                return
        print(f"Sorry, you've used all attempts. The word was: {self.secret_word}")
if __name__ == "__main__":
    game = WordleGame()
    game.play()