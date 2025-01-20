# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation and usage of the Wordle game, which is a terminal-based word guessing game. The game challenges you to guess a random 5-letter word within six attempts, providing feedback on each guess using color codes.

## Main Functions of the Software

- **Random Word Selection**: The game selects a random 5-letter word from a predefined list of words.
- **User Interaction**: Players can input their guesses directly into the terminal.
- **Feedback Mechanism**: After each guess, the game provides feedback using color codes:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Grey**: Incorrect letter.
- **Attempts**: Players have six attempts to guess the correct word.

## Installation

### Requirements

The Wordle game does not require any external dependencies. It is implemented in Python and can be run directly in a terminal environment.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Download the Game Script**: Save the provided `main.py` script to your local machine.

3. **Run the Game**: Open a terminal and navigate to the directory where `main.py` is located. Run the game using the following command:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script in your terminal. The game will welcome you and prompt you to guess a 5-letter word.

2. **Enter Your Guess**: Type a 5-letter word and press Enter. The game will provide feedback on your guess using color codes:
   - **Green**: The letter is in the correct position.
   - **Yellow**: The letter is in the word but in the wrong position.
   - **Grey**: The letter is not in the word.

3. **Continue Guessing**: You have a total of six attempts to guess the correct word. Use the feedback to refine your guesses.

4. **Win or Lose**: If you guess the word correctly within six attempts, you win! If not, the game will reveal the correct word after your sixth attempt.

5. **Play Again**: To play another round, simply run the `main.py` script again.

Enjoy the challenge and have fun playing Wordle! If you have any questions or need further assistance, feel free to reach out.