# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation, setup, and gameplay of our terminal-based Wordle game. This game is designed to be simple, fun, and engaging, allowing you to guess a secret 5-letter word within six attempts.

## Introduction

The Wordle Game is a text-based game that you can play directly from your Linux terminal. The objective is to guess a secret 5-letter English word. After each guess, you will receive feedback indicating how close your guess was to the secret word:
- **Green**: Correct letter in the correct position.
- **Yellow**: Correct letter in the wrong position.
- **Grey**: Incorrect letter.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external dependencies, so you can skip this step.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game.
   ```bash
   python main.py
   ```

2. **Gameplay Instructions**:
   - You will be prompted to guess a 5-letter word.
   - Enter your guess and press Enter.
   - You will receive feedback on your guess:
     - Letters in **green** are correct and in the correct position.
     - Letters in **yellow** are correct but in the wrong position.
     - Letters in **grey** are not in the word.
   - You have a total of 6 attempts to guess the word correctly.

3. **Winning the Game**: If you guess the word correctly within 6 attempts, you win! The game will congratulate you.

4. **Losing the Game**: If you fail to guess the word within 6 attempts, the game will reveal the secret word.

## Example

```
Welcome to Wordle! Guess the 5-letter word.
Attempt 1/6: apple
Feedback: a p p l e
Attempt 2/6: grape
Feedback: g r a p e
Attempt 3/6: peach
Feedback: p e a c h
Congratulations! You've guessed the word correctly!
```

## Conclusion

Enjoy playing the Wordle Game and challenge yourself to guess the word in as few attempts as possible! If you have any questions or need further assistance, please feel free to reach out to our support team.

Happy guessing!