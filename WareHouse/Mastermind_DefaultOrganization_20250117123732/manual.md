```markdown
# Mastermind Game

Welcome to the Mastermind Game! This classic code-breaking game challenges you to guess a hidden sequence of colors within a set number of attempts. With a simple graphical user interface, you can enjoy the thrill of deduction and logic.

## Main Functions

- **Secret Code Generation**: The computer randomly selects a sequence of four colors from a predefined list, allowing repetitions.
- **Player Guessing**: You attempt to guess the sequence by entering your guesses through the graphical interface.
- **Feedback System**: After each guess, receive feedback on the number of colors in the correct position and the number of correct colors in the wrong position.
- **Win/Loss Conditions**: Win by guessing the correct sequence within the allowed attempts, or lose if you exhaust all attempts without success.

## Quick Install

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository or download the source code files.
2. Navigate to the project directory in your terminal or command prompt.
3. Install any necessary dependencies (if any are added in the future). Currently, there are no external dependencies required.

```bash
# No external dependencies required for this project as of now.
```

## How to Play

1. **Launch the Game**: Run the `main.py` file to start the game.

   ```bash
   python main.py
   ```

2. **Enter Your Guess**: In the GUI, enter your guess by typing the names of the colors in the provided input fields. The available colors are: Red, Green, Blue, Yellow, Orange, and Purple.

3. **Submit Your Guess**: Click the "Submit Guess" button to see the feedback.

4. **Feedback Interpretation**:
   - **Correct Position**: The number of colors that are in the correct position.
   - **Correct Color**: The number of correct colors that are not in the correct position.

5. **Win the Game**: If you guess all colors in the correct position, a congratulatory message will appear.

6. **Game Over**: If you use all your attempts without guessing the correct sequence, the game will reveal the secret code.

## Documentation

For further details on the game's logic and GUI implementation, refer to the source code files:
- `game_logic.py`: Contains the logic for generating the secret code and checking guesses.
- `gui.py`: Manages the graphical user interface.

Enjoy the challenge and have fun playing the Mastermind Game!
```