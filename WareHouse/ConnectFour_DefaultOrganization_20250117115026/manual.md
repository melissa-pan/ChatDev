```markdown
# Connect Four Game

Welcome to the Connect Four Game! This application allows two players to engage in a classic game of Connect Four using a graphical user interface (GUI) built with Python's Tkinter library.

## Main Functions

- **Two-Player Game**: The game supports two players, alternating turns to drop discs into a seven-column, six-row grid.
- **Win Detection**: The game automatically detects when a player forms a horizontal, vertical, or diagonal line of four discs, declaring them the winner.
- **Draw Detection**: If the board fills up without any player winning, the game declares a draw.
- **Graphical Interface**: The game features a simple and intuitive GUI where players can click buttons to make their moves.
- **Game Reset**: After a win or draw, the game can be reset to start a new match.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Download the source code from the repository or copy the provided `main.py` file to your local machine.

2. **Install Tkinter**: Tkinter is included with Python's standard library. If you encounter any issues, you can install it using your package manager. For example:
   - On Ubuntu: `sudo apt-get install python3-tk`
   - On macOS: Tkinter is included with Python from python.org.
   - On Windows: Tkinter is included with Python from python.org.

3. **Requirements**: No additional external dependencies are required for this project.

## How to Play

1. **Run the Game**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the following command:
   ```bash
   python main.py
   ```

2. **Game Interface**: A window will open displaying the Connect Four board and buttons labeled "Column 1" to "Column 7".

3. **Make a Move**: Players take turns clicking on the column buttons to drop their discs into the desired column. The current player is indicated by the color of the discs (Red or Yellow).

4. **Winning the Game**: The game will automatically detect and announce a winner when a player forms a line of four discs.

5. **Draw**: If the board fills up without a winner, the game will declare a draw.

6. **Restarting the Game**: After a win or draw, the game will reset, allowing players to start a new match.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided with the game.

Enjoy playing Connect Four!
```