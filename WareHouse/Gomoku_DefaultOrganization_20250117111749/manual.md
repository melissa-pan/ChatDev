```markdown
# Gomoku Game

Welcome to the Gomoku Game! This application allows you to play the classic board game Gomoku, also known as Five in a Row, against another player. The game can be played with a graphical user interface (GUI) or in a console mode.

## Main Functions

- **Game Setup**: Initialize a Gomoku game with a standard 15x15 board.
- **Player Management**: Supports two players, each with their own symbol ('X' and 'O').
- **Game Logic**: Automatically checks for a winner after each move.
- **Graphical User Interface**: Provides a visual representation of the board and pieces using Pygame.
- **Console Mode**: Allows playing the game in a text-based console environment.

## Quick Install

To install the necessary environment dependencies, you need to have Python installed on your system. Then, you can install the required package using pip:

```bash
pip install -r requirements.txt
```

This will install Pygame, which is necessary for running the GUI version of the game.

## How to Use/Play

### Running the Game

1. **Clone the Repository**: First, ensure you have all the code files (`main.py`, `gomoku_game.py`, `board.py`, `player.py`, `gui.py`) in the same directory.

2. **Install Dependencies**: As mentioned above, run the following command to install Pygame:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Game**: Run the main script to start the game:
   ```bash
   python main.py
   ```

### Playing the Game

- **GUI Mode**: By default, the game runs in GUI mode. You can click on the board to place your piece. The game will automatically switch turns between Player 1 and Player 2. The first player to get five of their symbols in a row (horizontally, vertically, or diagonally) wins the game.

- **Console Mode**: If you prefer to play in the console, you can modify the `GomokuGame` initialization in `gomoku_game.py` to `use_gui=False`. In console mode, players will be prompted to enter their moves in the format `x y`, where `x` and `y` are the coordinates on the board.

### Game Rules

- The game is played on a 15x15 grid.
- Players take turns placing their symbol ('X' or 'O') on an empty cell.
- The objective is to be the first to form an unbroken chain of five of your pieces horizontally, vertically, or diagonally.
- If the board fills up without any player achieving this, the game is a draw.

Enjoy playing Gomoku and may the best strategist win!
```
