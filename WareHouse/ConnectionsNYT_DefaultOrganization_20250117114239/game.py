'''
Game logic for the NYT Connections-style puzzle game.
'''
class Game:
    def __init__(self):
        # Define words and their categories
        self.words = [
            "apple", "banana", "cherry", "date",
            "carrot", "broccoli", "spinach", "pepper",
            "dog", "cat", "hamster", "rabbit",
            "red", "blue", "green", "yellow"
        ]
        self.categories = {
            "fruits": ["apple", "banana", "cherry", "date"],
            "vegetables": ["carrot", "broccoli", "spinach", "pepper"],
            "animals": ["dog", "cat", "hamster", "rabbit"],
            "colors": ["red", "blue", "green", "yellow"]
        }
        self.tries = 0
        self.max_tries = 10
        self.found_categories = []
    def check_group(self, selected_words):
        # Check if the selected words form a valid category
        for category, words in self.categories.items():
            if set(selected_words) == set(words) and category not in self.found_categories:
                self.found_categories.append(category)
                return True, category
        return False, None
    def is_game_over(self):
        # Determine if the game is over
        return len(self.found_categories) == len(self.categories) or self.tries >= self.max_tries