```markdown
# Dou Dizhu Game Application

Welcome to the Dou Dizhu Game Application, a digital version of the popular Chinese card game designed for three players. One player is designated as the 'landlord,' and the objective is to be the first to run out of cards or prevent the landlord from doing so. This manual will guide you through the main functions of the software, how to install it, and how to play the game.

## Main Functions

- **Game Setup**: Automatically deals cards to three players and manages the bidding process to determine the landlord.
- **Bidding Phase**: Players bid to become the landlord. The highest bidder becomes the landlord and receives extra cards.
- **Gameplay**: Players take turns playing valid card combinations. The game checks for winning conditions after each turn.
- **User Interface**: A simple graphical user interface (GUI) built with Tkinter to facilitate interaction with the game.

## Installation

### Environment Setup

The Dou Dizhu Game Application is written in Python and requires Python to be installed on your system. Follow these steps to set up the environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the project repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the project directory:
   ```bash
   cd <project-directory>
   ```

4. **Install Dependencies**: There are no external dependencies required for this project as per the provided code. However, if you plan to extend the functionality, you may need to update the `requirements.txt` file and install additional libraries using:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the main Python script to start the game:
   ```bash
   python main.py
   ```

2. **Bidding Phase**: Each player will be prompted to enter their bid to become the landlord. Enter a bid amount or '0' to pass.

3. **Gameplay**:
   - The game will announce the landlord and distribute the extra cards.
   - Players take turns to play cards. You can play singles, pairs, triples, or straights according to Dou Dizhu rules.
   - The GUI will display whose turn it is and prompt for the next move.

4. **Winning the Game**: The first player to run out of cards wins. If the landlord runs out of cards first, they win. The game will announce the winner.

## Documentation

For more detailed information about the game rules and strategies, please refer to online resources about Dou Dizhu. This manual provides a basic overview to get you started with the application.

Enjoy playing Dou Dizhu!
```
