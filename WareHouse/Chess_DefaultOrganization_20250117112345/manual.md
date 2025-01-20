```markdown
# Chess Game User Manual

Welcome to the Chess Game application, a simple yet engaging chess game designed to be played directly from the Linux Terminal. This manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to play the game.

## Quick Install

This chess game is implemented in Python and does not require any external dependencies. To get started, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step-by-Step Installation

1. **Clone the Repository:**
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the cloned directory.

3. **Run the Game:**
   Execute the main script to start the game:
   ```bash
   python main.py
   ```

## 🤔 What is this?

This application is a terminal-based chess game that allows two players to take turns and determine the winner. The game is designed to be simple and intuitive, providing a classic chess experience without the need for a graphical user interface.

### Main Functions

- **Display Board:** The game displays the current state of the chessboard after each move.
- **Player Turns:** Players take turns to make moves using formal chess notation (e.g., Ke8).
- **Move Validation:** The game checks the validity of each move.
- **Checkmate and Stalemate Detection:** The game detects checkmate and stalemate conditions to determine the winner or declare a draw.

## 📖 How to Play

1. **Start the Game:**
   Run the `main.py` script as described in the installation section. The game will initialize and display the starting position of the chessboard.

2. **Enter Moves:**
   - The game prompts the current player to enter their move using standard chess notation (e.g., `Ke8` for moving the King to e8).
   - The board updates after each valid move.

3. **Game End:**
   - The game continues until a checkmate or stalemate is detected.
   - The game announces the winner or declares a draw.

4. **Invalid Moves:**
   - If an invalid move is entered, the game will prompt the player to try again.

Enjoy playing chess directly from your terminal and challenge your friends to a classic game of strategy and skill!

For any issues or questions, please contact our support team.

Happy Playing!
```