```markdown
# Monopoly Go! Simplified Version

Welcome to the simplified version of Monopoly Go!, a classic board game reimagined for a digital experience. This version includes basic board mechanics such as rolling dice, moving around properties, buying them, collecting rent, and handling chance events. It also tracks player money and property ownership, displays relevant game information, and prompts each player for decisions.

## Main Features

- **Rolling Dice:** Players roll two six-sided dice to determine their movement on the board.
- **Property Management:** Players can buy properties, collect rent from opponents, and manage their property portfolio.
- **Chance Events:** Players may encounter chance cards that can affect their position or finances.
- **Player Tracking:** The game tracks each player's money and property ownership.
- **Graphical User Interface:** A simple GUI displays game information and prompts players for decisions.

## Quick Install

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   Use the following command to install necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Note: Ensure you have a `requirements.txt` file listing all necessary dependencies. If not, you may need to manually install packages like `tkinter`.

3. **Run the Game:**
   Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Starting the Game:**
   - Launch the game using the command mentioned above.
   - The game window will open, displaying player information and prompting actions.

2. **Taking Turns:**
   - Players take turns rolling the dice by following the on-screen prompts.
   - After rolling, players move their token the number of spaces indicated by the dice roll.

3. **Buying Properties:**
   - If a player lands on an unowned property, they have the option to purchase it.
   - If they choose to buy, the cost is deducted from their money, and the property is added to their portfolio.

4. **Paying Rent:**
   - If a player lands on a property owned by another player, they must pay rent.
   - The rent amount is automatically deducted from the player's money and added to the property owner's balance.

5. **Chance Cards:**
   - Landing on certain spaces may trigger a chance card event, which can have various effects on the player.

6. **Winning the Game:**
   - The game continues until a player is declared the winner based on the rules you define (e.g., last player standing, highest net worth after a set number of turns).

## Documentation

For more detailed information on the game's mechanics and code structure, please refer to the source code files:

- `main.py`: Entry point for the game.
- `game.py`: Manages the overall game state and logic.
- `player.py`: Represents a player in the game.
- `board.py`: Represents the game board and its properties.
- `property.py`: Represents a property on the board.
- `gui.py`: Manages the graphical user interface.

Feel free to explore and modify the code to enhance the game experience!

Enjoy playing Monopoly Go!
```