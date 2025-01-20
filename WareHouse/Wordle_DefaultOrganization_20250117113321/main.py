'''
This script runs the terminal-based Wordle game, allowing the user to guess the daily word within a limited number of attempts.
'''
from wordle_game import WordleGame
def colorize_output(guess, result):
    colored_output = []
    for char, color in zip(guess, result):
        if color == 'green':
            colored_output.append(f"\033[92m{char}\033[0m")  # Green
        elif color == 'yellow':
            colored_output.append(f"\033[93m{char}\033[0m")  # Yellow
        else:
            colored_output.append(f"\033[90m{char}\033[0m")  # Grey
    return ''.join(colored_output)
def main():
    word_list = ['apple', 'berry', 'cherry', 'grape', 'lemon']  # Example word list
    game = WordleGame(word_list)
    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")
    attempts = 0
    while attempts < game.max_attempts:
        guess = input(f"Attempt {attempts + 1}: ").strip().lower()
        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a 5-letter word.")
            continue
        result = game.check_guess(guess)
        print(colorize_output(guess, result))
        if game.is_correct_guess(guess):
            print("Congratulations! You've guessed the word!")
            break
        attempts += 1
    if attempts == game.max_attempts:
        print(f"Sorry, you've used all attempts. The word was: {game.get_daily_word()}")
if __name__ == "__main__":
    main()