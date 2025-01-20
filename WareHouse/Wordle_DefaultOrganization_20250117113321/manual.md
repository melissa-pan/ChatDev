# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation and usage of our terminal-based Wordle game, designed to provide a fun and challenging word puzzle experience directly from your Linux terminal.

## Introduction

The Wordle Game is a simple yet engaging word puzzle where players have six attempts to guess a daily 5-letter English word. After each guess, the game provides feedback by coloring each letter of the guessed word:
- **Green**: Correct letter in the correct position.
- **Yellow**: Correct letter in the wrong position.
- **Grey**: Incorrect letter.

## Main Functions

- **Daily Word Selection**: The game randomly selects a 5-letter word from a predefined list each day.
- **Guess Feedback**: Provides color-coded feedback for each letter in the guessed word.
- **Win/Loss Notification**: Notifies the player if they have guessed the word correctly or if they have exhausted all attempts.

## Installation

### Prerequisites

- Ensure you have Python installed on your Linux system. You can verify this by running `python --version` in your terminal.

### Installation Steps

1. **Clone the Repository**: Download the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external dependencies, so you can skip this step.

3. **Run the Game**: Execute the game using the following command:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You will be greeted with a welcome message and instructions.

2. **Make a Guess**: Enter a 5-letter word as your guess. Ensure your input is valid (5 letters and alphabetic).

3. **Receive Feedback**: After each guess, the game will display the word with color-coded feedback:
   - **Green**: Correct letter in the correct position.
   - **Yellow**: Correct letter in the wrong position.
   - **Grey**: Incorrect letter.

4. **Win or Lose**: If you guess the word correctly within six attempts, you win! Otherwise, the game will reveal the correct word after all attempts are used.

5. **Restart**: To play again, simply rerun the `main.py` script.

## Troubleshooting

- **Invalid Input**: Ensure your guesses are exactly 5 letters long and contain only alphabetic characters.
- **Python Errors**: Verify that Python is correctly installed and accessible from your terminal.

## Conclusion

Enjoy playing the Wordle Game and challenge yourself to guess the daily word! If you encounter any issues or have suggestions for improvement, feel free to reach out to our support team.

Happy guessing!