```markdown
# Reversi (Othello) Game

Welcome to the Reversi (Othello) Game! This application allows two players to enjoy the classic board game of Reversi, where strategy and skill determine the victor. This user manual will guide you through the installation process, introduce the main features of the game, and provide instructions on how to play.

## Quick Install

To get started with the Reversi game, you need to install the required dependencies. The game is developed using Python and the Pygame library. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Once Python is installed, you can install Pygame using pip. Open your terminal or command prompt and run the following command:

```bash
pip install pygame==2.1.2
```

This command will install the Pygame library, which is necessary to run the game.

## Main Functions of the Software

The Reversi (Othello) Game application includes the following main functions:

- **Game Board**: An 8x8 grid where players place their discs.
- **Player Turns**: Two players alternate turns, placing discs on the board.
- **Disc Flipping**: Discs of the opponent that lie between the newly placed disc and existing discs of the same color are flipped.
- **Game End**: The game ends when the board is full or no valid moves remain for both players.
- **Graphical Interface**: A user-friendly graphical interface using Pygame to display the board and discs.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You can do this by navigating to the directory containing the game files and executing the following command:

   ```bash
   python main.py
   ```

2. **Game Interface**: The game window will open, displaying the 8x8 board. The initial setup includes two black and two white discs placed in the center.

3. **Taking Turns**: Players take turns clicking on the board to place their discs. The current player is indicated by the color of the disc they are placing.

4. **Valid Moves**: A move is valid if it results in at least one of the opponent's discs being flipped. If a player has no valid moves, the turn automatically passes to the opponent.

5. **Flipping Discs**: When a valid move is made, all opponent discs lying in a straight line between the new disc and another disc of the same color are flipped.

6. **Game Over**: The game ends when the board is full or neither player has a valid move. The player with the most discs of their color on the board wins.

## Additional Information

- **Reset Game**: The game can be reset by restarting the application.
- **Quit Game**: To exit the game, close the game window or press the close button.

Enjoy playing Reversi and may the best strategist win!
```
