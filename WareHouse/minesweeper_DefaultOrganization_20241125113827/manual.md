# Minesweeper Game User Manual

Welcome to the Minesweeper Game, a text-based version of the classic game that you can play directly from your Linux Terminal. This manual will guide you through the installation, setup, and gameplay process.

## Introduction

Minesweeper is a puzzle game where the objective is to clear a board containing hidden "mines" without detonating any of them. The game provides two levels of difficulty: easy and hard. Each game starts with a randomly generated board, ensuring a unique experience every time.

## Quick Install

### Prerequisites

- Python 3.x installed on your Linux system.

### Installation

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository.

3. **Install Dependencies:**

   This project does not require any external dependencies. Ensure that Python 3.x is installed on your system.

## How to Play

1. **Start the Game:**

   Run the game by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Select Difficulty:**

   Upon starting the game, you will be prompted to select a difficulty level. Type `easy` or `hard` and press Enter.

3. **Game Board:**

   The game board will be displayed in the terminal. Each cell is initially hidden and represented by a space.

4. **Reveal a Cell:**

   To reveal a cell, enter the coordinates in the format `row col` (e.g., `2 3`) and press Enter. The game will reveal the cell and display the number of adjacent mines.

5. **Game Objective:**

   - Avoid hitting a mine. If you reveal a mine, the game is over.
   - Clear all non-mine cells to win the game.

6. **Winning the Game:**

   If you successfully reveal all non-mine cells, a congratulatory message will be displayed, indicating that you've cleared the minefield.

## Game Features

- **Randomized Board:** Each game starts with a new, randomly generated board.
- **Two Difficulty Levels:** Choose between easy (5x5 board with 5 mines) and hard (10x10 board with 20 mines).
- **Text-Based Interface:** Play directly from the terminal without the need for a graphical interface.

## Troubleshooting

- **Invalid Input:** Ensure that you enter valid coordinates within the board's range.
- **Difficulty Selection:** If an invalid difficulty is selected, the game defaults to easy mode.

## Conclusion

Enjoy playing Minesweeper in your terminal! This game offers a nostalgic experience with a modern twist, allowing you to challenge yourself with different difficulty levels. Happy minesweeping!