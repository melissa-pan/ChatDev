'''
This script implements a terminal-based Wordle game. It selects a random 5-letter word and allows the player to guess the word in 6 attempts. Feedback is provided using color codes: green for correct letters in the correct position, yellow for correct letters in the wrong position, and grey for incorrect letters.
'''
import random
# List of 5-letter words
WORDS = ["apple", "grape", "peach", "berry", "melon", "lemon", "mango", "cherry", "plumb", "guava"]
def select_random_word():
    '''
    Selects a random word from the predefined list of words.
    '''
    return random.choice(WORDS)
def get_feedback(guess, target):
    '''
    Compares the guess with the target word and returns feedback.
    Green for correct letter in correct position, yellow for correct letter in wrong position, grey for incorrect letter.
    '''
    feedback = []
    target_letters = list(target)
    guess_letters = list(guess)
    # First pass: Check for correct letters in correct position
    for i in range(5):
        if guess_letters[i] == target_letters[i]:
            feedback.append('\033[92m' + guess_letters[i] + '\033[0m')  # Green
            target_letters[i] = None  # Remove matched letter
        else:
            feedback.append(None)
    # Second pass: Check for correct letters in wrong position
    for i in range(5):
        if feedback[i] is None:
            if guess_letters[i] in target_letters:
                feedback[i] = '\033[93m' + guess_letters[i] + '\033[0m'  # Yellow
                target_letters[target_letters.index(guess_letters[i])] = None
            else:
                feedback[i] = '\033[90m' + guess_letters[i] + '\033[0m'  # Grey
    return ''.join(feedback)
def play_game():
    '''
    Main function to play the Wordle game.
    '''
    target_word = select_random_word()
    attempts = 6
    print("Welcome to Wordle! Guess the 5-letter word.")
    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        feedback = get_feedback(guess, target_word)
        print("Feedback:", feedback)
        if guess == target_word:
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        print(f"Sorry, you've used all attempts. The word was: {target_word}")
if __name__ == "__main__":
    play_game()