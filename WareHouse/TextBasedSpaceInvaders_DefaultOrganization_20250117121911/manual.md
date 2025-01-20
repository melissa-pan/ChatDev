```markdown
# Space Invaders Game

A simplified version of the classic Space Invaders game, developed using Python and Pygame. The player controls a ship at the bottom of the screen, moving it horizontally and firing shots to destroy descending alien rows. The game ends if aliens reach the bottom or the player defeats all aliens.

## Quick Install

To run the Space Invaders game, you need to have Python and Pygame installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Use pip to install Pygame, a set of Python modules designed for writing video games.
   ```bash
   pip install pygame==2.1.2
   ```

3. **Clone the Repository**: Download the game files from the repository or copy the provided code into your local directory.

4. **Run the Game**: Navigate to the directory containing the game files and execute the main script.
   ```bash
   python main.py
   ```

## 🤔 What is this?

This is a simplified version of the Space Invaders game, where the player controls a ship to shoot down aliens. The game is designed to be easy to understand and play, making it suitable for both beginners and experienced gamers.

## 🎮 How to Play

- **Objective**: Destroy all the aliens before they reach the bottom of the screen.

- **Controls**:
  - Move the ship left: Press the left arrow key.
  - Move the ship right: Press the right arrow key.
  - Fire bullets: Press the spacebar.
  - Quit the game: Press the 'Q' key.

- **Game Over**: The game ends if the aliens reach the bottom of the screen or if all aliens are destroyed.

## 📖 Documentation

### Main Functions

- **Ship Control**: The player's ship can move horizontally and fire bullets to destroy aliens.
- **Alien Movement**: Aliens descend from the top of the screen, and the player must shoot them before they reach the bottom.
- **Bullet Management**: The player can fire a limited number of bullets at a time, which move upwards to hit aliens.

### Code Structure

- **main.py**: The main module to run the game.
- **settings.py**: Contains all the settings for the game, such as screen size and speed factors.
- **ship.py**: Represents the player's ship.
- **alien.py**: Represents the aliens.
- **bullet.py**: Represents the bullets fired by the ship.
- **game_functions.py**: Handles game events and updates, such as key presses and screen updates.

### Requirements

- **requirements.txt**: Lists the required dependencies for the game.
  ```
  pygame==2.1.2
  ```

Enjoy playing Space Invaders and test your skills in defeating the alien invasion!
```