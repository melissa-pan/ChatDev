# Minesweeper Game User Manual

Welcome to the Minesweeper Game! This classic puzzle game challenges you to uncover all the cells on a grid without hitting a mine. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to play the game.

## Quick Install

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Run the following command to clone the repository:
     ```
     git clone <repository-url>
     ```
   - Navigate into the cloned directory:
     ```
     cd <repository-directory>
     ```

2. **Install Dependencies:**
   - This project does not require any external dependencies. All necessary modules are included in Python's standard library.

## Main Functions of the Software

The Minesweeper Game consists of two main components:

1. **MinesweeperGame Class:**
   - Handles the game logic, including mine placement, uncovering cells, and checking win conditions.
   - Initializes a 9x9 grid with 10 hidden mines.
   - Provides methods to uncover cells and calculate adjacent mines.

2. **MinesweeperGUI Class:**
   - Manages the graphical user interface using the Tkinter library.
   - Displays the game board and updates it based on user interactions.
   - Handles user input and game end conditions.

## How to Play

1. **Start the Game:**
   - Run the `main.py` script to launch the game:
     ```
     python main.py
     ```
   - A window will open displaying a 9x9 grid of buttons.

2. **Uncover Cells:**
   - Click on any cell to uncover it.
   - If the cell contains a mine, the game ends, and the cell will be marked with a red '*'.
   - If the cell does not contain a mine, it will display a number indicating how many adjacent cells contain mines.

3. **Winning the Game:**
   - Successfully uncover all cells that do not contain mines to win the game.
   - A message box will appear congratulating you on your victory.

4. **Game Over:**
   - If you uncover a mine, the game will end, and a message box will inform you that you hit a mine.

## Additional Information

- The game automatically updates the display after each move.
- You can restart the game by closing the window and running the `main.py` script again.

Enjoy playing Minesweeper, and good luck avoiding those mines!