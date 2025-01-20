```markdown
# Spelling Bee Puzzle Game

Welcome to the Spelling Bee Puzzle Game! This application challenges users to form words using a central letter and six surrounding letters. The game is designed to enhance your vocabulary and spelling skills while providing an engaging and fun experience.

## Main Functions

- **Central and Surrounding Letters**: The game provides one central letter and six surrounding letters. All words formed must include the central letter.
- **Word Submission**: Users can submit words they form using the provided letters.
- **Scoring System**: Points are awarded based on the length of the words. Longer words yield higher scores.
- **Feedback Mechanism**: The game provides feedback on the validity of submitted words, informing users if a word is valid, invalid, or already found.

## Installation Guide

### Environment Setup

To run the Spelling Bee Puzzle Game, you need to set up your Python environment with the necessary dependencies. Follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Install the required Python packages using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**: Ensure that the NLTK 'words' corpus is downloaded for the game logic.

   ```bash
   python nltk_setup.py
   ```

## How to Play

1. **Launch the Game**: Run the main application file to start the game.

   ```bash
   python main.py
   ```

2. **Game Interface**: The game interface will display the central letter and surrounding letters. Use these letters to form words.

3. **Submit Words**: Enter your word in the input field and click the "Submit" button. The game will provide feedback on the validity of your word.

4. **Scoring**: Your score will be updated based on the length of valid words you submit. Aim to find as many valid words as possible to maximize your score.

5. **Feedback**: The game will inform you if a word is valid, invalid, or has already been found.

Enjoy the challenge and improve your spelling skills with the Spelling Bee Puzzle Game!

## Additional Information

For any issues or questions, please contact our support team. We are here to help you have the best experience with our game.

Happy spelling!
```
