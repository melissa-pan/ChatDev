```markdown
# 2048 Game - 10x10 Grid

Welcome to the 2048 Game with a 10x10 grid! This user manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to play the game.

## 📜 Introduction

The 2048 game is a single-player sliding tile puzzle game. The objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048. This version of the game features a larger 10x10 grid, providing a unique challenge compared to the standard 4x4 grid.

## 🚀 Quick Install

### Prerequisites

Ensure you have Python 3.6 or higher installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**

   Clone the project repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the actual directory name.

3. **Install Dependencies**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will ensure all necessary packages are installed.

## 🎮 How to Play

1. **Run the Game**

   Start the game by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Game Controls**

   Use the arrow keys on your keyboard to move the tiles in the desired direction:
   - **Up Arrow**: Move tiles up
   - **Down Arrow**: Move tiles down
   - **Left Arrow**: Move tiles left
   - **Right Arrow**: Move tiles right

3. **Objective**

   Combine tiles with the same number to create larger numbered tiles. The goal is to reach a tile with the number 2048. The game ends when no more moves are possible.

4. **Game Over**

   If you can no longer make any moves, the game will display "Game Over" on the screen.

## 🛠 Main Functions

- **Game Initialization**: The game initializes with a 10x10 grid and two random tiles placed on the grid.
- **Tile Movement and Merging**: Move tiles in four directions (up, down, left, right) to merge tiles with the same number.
- **Random Tile Addition**: After each move, a new tile (either 2 or 4) is added to a random empty position on the grid.
- **Score Tracking**: The game keeps track of your score, which increases as you merge tiles.

## 📚 Documentation

For further details and documentation, please refer to the source code files:
- `main.py`: Entry point for running the game.
- `game2048.py`: Contains the game logic and mechanics.
- `gamegui.py`: Manages the graphical user interface using tkinter.

Enjoy the challenge of the 2048 game on a larger grid and aim for the highest score possible!

```
