# Strands Game User Manual

Welcome to the Strands Game, a word-segmentation puzzle designed to challenge your linguistic skills. In this game, you will combine strands of text to form meaningful words or phrases. The game verifies valid strand formations and confirms completion once all strands are correctly merged.

## Main Functions of the Software

- **Strands Loading**: The game loads strands of text from a file or uses default strands if the file is not found.
- **Combination Checking**: Players can input combinations of strands, and the game checks if they form valid words or phrases.
- **Completion Verification**: The game tracks formed combinations and notifies the player upon successful completion of all valid combinations.
- **Graphical User Interface (GUI)**: A user-friendly interface built with Tkinter allows players to interact with the game easily.

## Installation

### Environment Setup

The Strands Game is developed in Python and does not require any external dependencies. However, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository**: Download the game files from the repository or copy them to your local machine.
2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory containing the game files.
3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to launch the game interface.
2. **View Available Strands**: The GUI will display the available strands that you can use to form words or phrases.
3. **Input Combinations**: Enter your strand combinations in the provided text entry field.
4. **Submit Combinations**: Click the "Submit" button to check if your combination is correct.
5. **Receive Feedback**: The game will inform you if your combination is correct or if you need to try again.
6. **Complete the Game**: Once all correct combinations are formed, a congratulatory message will appear, indicating that you have completed the game.

## Troubleshooting

- **Strands File Not Found**: If the strands file is missing, the game will use default strands. Ensure the `strands.txt` file is in the same directory as the game files if you want to use custom strands.
- **Incorrect Combinations**: If your combination is incorrect, try rearranging the strands or using different strands to form valid words or phrases.

Enjoy playing the Strands Game and challenge yourself to form all the correct combinations!