```markdown
# Tower of the Sorcerer: Roguelike Game

Welcome to the Tower of the Sorcerer, a roguelike game inspired by classic dungeon crawlers. Navigate through a maze, battle monsters, collect treasures, and advance to the next level through strategic gameplay.

## Main Features

- **Map Exploration**: Navigate an 80x80 grid map using keyboard controls.
- **Player Movement**: Use W/S/A/D keys to move up, down, left, and right.
- **Combat System**: Engage with monsters, where your HP is compared against theirs.
- **Treasure Collection**: Restore your HP by finding and opening treasure chests.
- **Level Progression**: Reach the door to advance to the next level.
- **Dynamic Map Generation**: Each level is uniquely generated with a guaranteed path to the door.

## Installation

To play the game, you need to set up your environment with the necessary dependencies.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Quick Install

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have `pygame` installed, which is required for the game interface.
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**:
   Run the main game script to start playing.
   ```bash
   python main.py
   ```

2. **Controls**:
   - Use `W` to move up.
   - Use `S` to move down.
   - Use `A` to move left.
   - Use `D` to move right.

3. **Game Objectives**:
   - **Navigate the Map**: Move through the maze-like structure.
   - **Battle Monsters**: Your HP will decrease based on the monster's HP. Survive by managing your health.
   - **Collect Treasures**: Find treasure chests to restore 20-30 HP randomly.
   - **Find the Door**: Reach the door to proceed to the next level.

4. **Game Over**:
   - The game ends if your HP drops to zero after a monster encounter.

## Additional Information

- **Map Generation**: Each level is generated using a randomized depth-first search algorithm, ensuring a unique experience every time.
- **Object Interaction**: The player interacts with monsters, treasures, and doors, each affecting gameplay differently.

Enjoy your adventure in the Tower of the Sorcerer, and may you conquer the challenges that lie ahead!
```
