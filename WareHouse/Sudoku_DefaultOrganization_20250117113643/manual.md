# Sudoku Solver/Creator User Manual

Welcome to the Sudoku Solver/Creator application! This software allows you to solve and create classic Sudoku puzzles using a 9x9 grid. Each row, column, and 3x3 subgrid must contain the digits 1 through 9 exactly once. The program also allows you to input values for specific cells, check for mistakes, and confirm when the puzzle is completed.

## Main Functions

1. **Sudoku Grid Management**: 
   - Input values into the Sudoku grid.
   - Validate the input values according to Sudoku rules.
   - Clear the grid to start a new puzzle.

2. **Sudoku Solver**:
   - Automatically solve the Sudoku puzzle if a solution exists.
   - Provide feedback if no solution is possible.

3. **Puzzle Completion Check**:
   - Check if the puzzle is completed correctly.
   - Receive a congratulatory message upon successful completion.

## Installation

### Environment Setup

This application is built using Python and requires no external dependencies beyond the standard Python library. The graphical user interface is created using Tkinter, which is included in the standard Python library.

### Steps to Install

1. **Ensure Python is Installed**: 
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone the project repository to your local machine.

3. **Navigate to the Project Directory**:
   - Open a terminal or command prompt and navigate to the directory where the project files are located.

4. **Run the Application**:
   - Execute the following command to start the application:
     ```bash
     python main.py
     ```

## How to Use

1. **Launching the Application**:
   - Run the `main.py` script to launch the Sudoku Solver/Creator application.

2. **Inputting Values**:
   - Click on any cell in the 9x9 grid and enter a number between 1 and 9.
   - Ensure the number follows Sudoku rules for rows, columns, and 3x3 subgrids.

3. **Solving the Puzzle**:
   - Click the "Solve" button to automatically solve the puzzle. If a solution exists, the grid will be filled with the correct numbers.

4. **Checking the Solution**:
   - Click the "Check" button to verify if the current grid is completed correctly. A message will inform you if the puzzle is complete or contains errors.

5. **Clearing the Grid**:
   - Click the "Clear" button to reset the grid and start a new puzzle.

6. **Receiving Feedback**:
   - The application will provide feedback messages for invalid inputs, unsolvable puzzles, and successful completions.

Enjoy solving and creating Sudoku puzzles with this intuitive and user-friendly application!