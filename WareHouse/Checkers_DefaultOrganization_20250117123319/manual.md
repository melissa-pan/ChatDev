```markdown
# Checkers Game

Welcome to the Checkers Game developed by ChatDev! This application allows you to play a classic game of Checkers (Draughts) on an 8x8 board with standard capture and kinging rules. The game alternates turns between two players, and you can input your moves using standard notation.

## Main Features

- **Interactive Gameplay**: Play against another player on the same machine.
- **Standard Rules**: Includes standard capture and kinging rules.
- **Graphical Interface**: Utilizes Pygame for a visually appealing board and pieces.
- **Notation Input**: Enter moves using standard notation (e.g., a3-b4).

## Quick Install

To get started with the Checkers Game, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use pip to install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that you have Python and pip installed on your system. The game requires `pygame` version 2.0.0 or higher.

## How to Play

1. **Start the Game**: Run the main Python script to start the game.

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying an 8x8 checkers board. The pieces are colored red and black, representing the two players.

3. **Input Moves**: When it's your turn, input your move in the console using standard notation. For example, to move a piece from position a3 to b4, type:

   ```
   a3-b4
   ```

4. **Alternate Turns**: After a valid move, the turn will switch to the other player. Continue playing until one player wins by capturing all opponent pieces or blocking all possible moves.

5. **Exiting the Game**: To exit the game, close the game window or press the quit button.

## Additional Information

- **Capture Moves**: If a capture is possible, it must be made. The game will automatically enforce this rule.
- **Kinging**: When a piece reaches the opposite end of the board, it becomes a king and can move backward as well as forward.

Enjoy your game of Checkers, and may the best player win!

For any issues or further assistance, please contact our support team at support@chatdev.com.
```
